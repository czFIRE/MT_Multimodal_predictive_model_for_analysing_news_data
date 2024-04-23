import os
import json
import requests
from concurrent.futures import ThreadPoolExecutor

def download_image(item):
    if 'images' in item:
        images = item['images']
        for i, image_url in enumerate(images):
            try:
                response = requests.get(image_url)
                response.raise_for_status()
                file_extension = ".jpg"
                if i == 0:
                    filename = f"{item['id']}{file_extension}"
                else:
                    filename = f"{item['id']}-{i}{file_extension}"
                with open("images/"+filename, 'wb') as f:
                    f.write(response.content)
            except:
                print(f"Failed to download image from {image_url}, id: {item['id']}")

def main():
    data_original = None

    with open('exported_articles.json', encoding="utf8") as json_file:
        data_original = json.load(json_file, )

        if data_original:
            # Parallelize image downloads
            with ThreadPoolExecutor() as executor:
                executor.map(download_image, data_original)
        else:
            print("No data loaded from the JSON file.")

if __name__ == "__main__":
    main()