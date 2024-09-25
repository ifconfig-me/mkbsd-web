import os
import asyncio
from flask import Flask, render_template, Response
from aiohttp import ClientSession
from urllib.parse import urlparse

app = Flask(__name__)
downloading = False 

url = 'https://storage.googleapis.com/panels-api/data/20240916/media-1a-i-p~s'

async def download_image(session, image_url, file_path):
    async with session.get(image_url) as response:
        if response.status == 200:
            content = await response.read()
            with open(file_path, 'wb') as f:
                f.write(content)
            file_size = len(content)
            return file_size 

def download_images_sync():
    global downloading

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    async def fetch_data():
        async with ClientSession() as session:
            async with session.get(url) as response:
                if response.status != 200:
                    yield f"data: Failed to fetch JSON file.\n\n"
                    return

                json_data = await response.json()
                data = json_data.get('data', None)
                if not data:
                    yield f"data: No 'data' field in the JSON.\n\n"
                    return

                total_images = sum(1 for subproperty in data.values() if subproperty and subproperty.get('dhd'))
                download_dir = os.path.join(os.getcwd(), 'static', 'downloads')
                os.makedirs(download_dir, exist_ok=True)

                file_index = 1
                downloaded_images = 0
                total_size = 0

                for key, subproperty in data.items():
                    if not downloading:
                        break 

                    if subproperty and subproperty.get('dhd'):
                        image_url = subproperty['dhd']
                        parsed_url = urlparse(image_url)
                        ext = os.path.splitext(parsed_url.path)[-1] or '.jpg'
                        filename = f"{file_index}{ext}"
                        file_path = os.path.join(download_dir, filename)

                        file_size = await download_image(session, image_url, file_path)
                        total_size += file_size
                        downloaded_images += 1

                        yield {
                            "image": f"downloads/{filename}",
                            "downloaded": downloaded_images,
                            "total": total_images,
                            "size": file_size,
                            "total_size": total_size
                        }
                        file_index += 1
                        await asyncio.sleep(0.25)

    async_gen = fetch_data()

    while True:
        try:
            data = loop.run_until_complete(async_gen.__anext__())
            yield f"data: {data}\n\n"
        except StopAsyncIteration:
            break

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start', methods=['GET'])
def start():
    global downloading
    downloading = True
    return Response(download_images_sync(), content_type='text/event-stream')

@app.route('/stop', methods=['POST'])
def stop():
    global downloading
    downloading = False
    return {"status": "stopped"}

if __name__ == "__main__":
    app.run(debug=True)
