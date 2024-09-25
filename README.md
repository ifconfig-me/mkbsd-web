# Browser based verion of MKBSD 
Forked from: https://github.com/nadimkobeissi/mkbsd

# 🌐 Browser based verion of MKBSD 

[![License](https://img.shields.io/badge/license-WTFPL-brightgreen.svg)](http://www.wtfpl.net/about/)  

Download wallpapers from your favorite sellout grifter's app, with a sleek Web3-inspired UI, real-time previews, and dynamic image fetching!

## 🚀 Features

- **Real-time Image Preview**: See the images as they are downloaded. (Does this works?)
- **Progress Tracking**: Displays current download status, including the number of images, file size, and total downloaded size.
- **Start/Stop Control**: Start or stop the download process whenever you want.
- **Responsive UI**: Built with Bootstrap for a clean, modern look and great performance on all devices.
- **Server-Sent Events (SSE)**: Real-time updates on downloads using SSE, ensuring the UI is always in sync with the backend.

## 🎯 Technologies Used

- **Flask**: Lightweight Python web framework.
- **aiohttp**: Asynchronous HTTP requests for downloading images efficiently.
- **Bootstrap**: CSS framework for a modern, responsive UI.
- **JavaScript (EventSource)**: Handles real-time data from the server using Server-Sent Events (SSE).

## 🛠️ Setup & Installation

### Prerequisites

- Python 3.7+
- `pip` (Python package installer)

### Clone the repository

```bash
git clone https://github.com/ifconfig-me/mkbsd-web
cd mkbsd-web
```

### Install dependencies

Install the required Python packages by running:

```bash
pip install flask aiohttp
```

### Run the application

1. Start the Flask server:

    ```bash
    python mkbsd_web.py
    ```

2. Open your web browser and go to `http://127.0.0.1:5000`.

## 🖥️ Usage

1. **Start the download**: Click the **Start Download** button, and the images will begin downloading. As each image downloads, it will appear in the preview area.
2. **Stop the download**: Click the **Stop Download** button to halt the download process at any time.
3. **Real-time updates**: Watch the progress of the download, including the size of each image and the total amount downloaded so far.

## 📁 Project Structure

```bash
.
├── static
│   └── downloads       # Directory where downloaded images are stored
├── templates
│   └── index.html      # HTML file for the web interface
├── mkbsd_web.py        # Main Python script (Flask app)
└── README.md           # This README file
```

## 🔥 Example Output

### Real-time Image Preview*

*WIP 

As you download, the images will appear dynamically on your screen:

![Preview](https://via.placeholder.com/200) ![Preview](https://via.placeholder.com/200) ![Preview](https://via.placeholder.com/200)

## 📝 License

This project is licensed under the **WTFPL** License. See the [LICENSE](http://www.wtfpl.net/about/) file for details.

## 💬 Acknowledgments

Special thanks to https://github.com/nadimkobeissi/mkbsd 
