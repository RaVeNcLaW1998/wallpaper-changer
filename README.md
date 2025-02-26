# Wallpaper Updater with Unsplash API

This Python script allows you to automatically download a random image from Unsplash and set it as your desktop wallpaper. The script is designed to work on Windows and uses the Unsplash API to fetch images.

## Features

- **Random Image Download**: Fetches a random image from Unsplash based on a search query.
- **Image Conversion**: Converts the downloaded image to BMP format, which is required for setting wallpapers on Windows.
- **Wallpaper Setting**: Automatically sets the downloaded image as the desktop wallpaper.

## Prerequisites

Before running the script, ensure you have the following:

1. **Python 3.x**: The script is written in Python 3. Make sure Python is installed on your system.
2. **Unsplash API Key**: You need an API key from Unsplash. You can get one by creating a developer account at [Unsplash Developer](https://unsplash.com/developers).
3. **Required Python Libraries**: Install the required libraries using pip:
   ```bash
   pip install requests python-dotenv pillow
   ```

## Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/wallpaper-updater.git
   cd wallpaper-updater
   ```

2. **Create a `.env` File**:
   Create a `.env` file in the root directory of the project and add your Unsplash API key:
   ```
   UNSPLASH_API_KEY=your_api_key_here
   ```

3. **Run the Script**:
   Execute the script using Python:
   ```bash
   python main.py
   ```

## How It Works

1. **API Request**: The script sends a request to the Unsplash API with a search query (default is "cars") and retrieves a random image URL.
2. **Image Download**: The image is downloaded and saved as `wallpaper.jpg` in the `wallpapers` directory.
3. **Image Conversion**: The image is converted to BMP format and saved as `wallpaper.bmp`.
4. **Wallpaper Setting**: The script sets the downloaded BMP image as the desktop wallpaper using Windows API.

## Customization

- **Change Search Query**: Modify the `query` parameter in the `download_image()` function to download images of different categories.
  ```python
  wallpaper_path = download_image(query="nature")
  ```

- **Change Save Directory**: You can change the directory where images are saved by modifying the `directory` parameter in the `download_image()` function.
  ```python
  wallpaper_path = download_image(directory="my_wallpapers")
  ```

## Troubleshooting

- **API Key Not Found**: Ensure that the `.env` file is correctly set up and contains the `UNSPLASH_API_KEY`.
- **Image Conversion Errors**: If the script fails to convert the image, ensure that the `Pillow` library is installed correctly.
- **Wallpaper Not Setting**: Ensure that the script is running on a Windows system and that the image path is correct.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Unsplash](https://unsplash.com/) for providing the API and images.
- [Pillow](https://python-pillow.org/) for image processing.

---

Enjoy your new wallpaper! If you have any issues or suggestions, feel free to open an issue or contribute to the project.
```

### Steps to Use:
1. Save the above content as `README.md` in your project directory.
2. Ensure your `main.py` script and `.env` file are in the same directory.
3. Follow the instructions in the `README.md` to set up and run the script.