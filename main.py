import requests
import os
from dotenv import load_dotenv
import ctypes  # For Windows wallpaper change
from PIL import Image  # For image conversion

# Load environment variables from .env file
load_dotenv()

# Get API Key
ACCESS_KEY = os.getenv("UNSPLASH_API_KEY")

if not ACCESS_KEY:
    print("Error: API key not found. Make sure you have a .env file.")
    exit(1)

UNSPLASH_URL = "https://api.unsplash.com/photos/random"


def download_image(query="nature", directory="wallpapers"):
    """Downloads a random image from Unsplash and converts it to BMP."""
    print("Starting image download process...")

    headers = {"Authorization": f"Client-ID {ACCESS_KEY}"}
    params = {"query": query, "orientation": "landscape"}

    print(f"Sending request to Unsplash API with query: {query}")
    response = requests.get(UNSPLASH_URL, headers=headers, params=params)

    if response.status_code == 200:
        print("Successfully connected to Unsplash API.")
        data = response.json()

        if "urls" in data and "full" in data["urls"]:
            image_url = data["urls"]["full"]
            print(f"Image URL retrieved: {image_url}")
        else:
            print("Error: No valid image URL found in response.")
            return None

        # Download the image
        print("Downloading image...")
        img_data = requests.get(image_url).content

        if not os.path.exists(directory):
            print(f"Creating directory: {directory}")
            os.makedirs(directory)

        jpg_path = os.path.join(directory, "wallpaper.jpg")
        bmp_path = os.path.join(directory, "wallpaper.bmp")

        with open(jpg_path, "wb") as img_file:
            img_file.write(img_data)

        print(f"Image successfully downloaded as: {jpg_path}")

        # Convert to BMP (Windows requirement)
        try:
            print("Converting image to BMP format...")
            with Image.open(jpg_path) as img:
                img = img.convert("RGB")  # Ensure compatibility
                img.save(bmp_path, "BMP")

            print(f"Image converted to BMP: {bmp_path}")
            return bmp_path
        except Exception as e:
            print(f"Error converting image to BMP: {e}")
            return None
    else:
        print(f"Failed to fetch image. Status Code: {response.status_code}")
        print(f"Response Message: {response.text}")
        return None


def set_wallpaper(file_path):
    """Sets the downloaded image as the desktop wallpaper."""
    print("Attempting to set wallpaper...")

    try:
        abs_path = os.path.abspath(file_path)  # Ensure absolute path
        print(f"Setting wallpaper using file: {abs_path}")

        ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_path, 3)
        print("Wallpaper successfully set.")
    except Exception as e:
        print(f"Error setting wallpaper: {e}")


# Run the wallpaper update
print("Starting Wallpaper Update Process...")

wallpaper_path = download_image()

if wallpaper_path:
    print("Downloaded image successfully, now setting it as wallpaper...")
    set_wallpaper(wallpaper_path)
else:
    print("Failed to download image. Exiting process.")
