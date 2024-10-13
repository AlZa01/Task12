import requests
import re
url = "https://gsom.spbu.ru/en/"
response = requests.get(url)
content = response.text
png_links = content.count('.png')
print("Number of .png images found: "+str(png_links))

match = re.search(r'href=[\'"]?(\/[^\'" >]+\.png)', content)
if match:
    png_link = match.group(1)
    print(png_link)
else:
    print("No .png link found.")

base_url = "https://gsom.spbu.ru"
full_link = base_url + png_link
print(full_link)
response = requests.get(full_link)
if response.status_code == 200:
    with open('image.png', 'wb') as file:
        file.write(response.content)
    print("The image is saved as 'image.png'")
else:
    print("Failed to retrieve the image.")