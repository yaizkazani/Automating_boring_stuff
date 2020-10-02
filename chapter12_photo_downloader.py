# Image Site Downloader
#
# Write a program that goes to a photo-sharing site like Flickr or Imgur, searches for a category of photos,
# and then downloads all the resulting images.
# You could write a program that works with any photo site that has a search feature.


# Input search request somehow (Input will be OK i think)
# Create a search request address
# Download html using that search request address
# Sent html to bs4
# Get all photo objects from bs4 object
# Create a folder
# Download all objects to folder one-by-one
# Report on completion

import requests, bs4, os, pyinputplus, logging

logging.basicConfig(level=logging.DEBUG, format='%(levelname)s %(message)s')

search_request = pyinputplus.inputStr('Please enter your search request\n', default='nature', allowRegexes=['a-zA-Z'])
html = requests.get(f"https://imgur.com/search/score?q={search_request}")
try:
	html.raise_for_status()
	logging.info("HTML was successfully downloaded and put into html variable")
except Exception as err:
	logging.error(f"Error occurred during HTML download: {err}")

mySoup = bs4.BeautifulSoup(html.text, "html.parser")
images = mySoup.select("img")  # <img alt="" src="//i.imgur.com/Balxh6qb.jpg" original-title="">
folder_path = os.path.abspath(f".\\{search_request}")
os.makedirs(folder_path, exist_ok=True)

for image in images:
	image_src = image.get("src")
	tmp_image = requests.get(f"http:{image_src}")
	try:
		tmp_image.raise_for_status()
		logging.info(f"Image {str(tmp_image)} was downloaded")
	except Exception as err_2:
		logging.error(f"Image {str(tmp_image)} download error {err_2}")
	with open(f"{os.path.join(folder_path, str(image_src).rpartition('/')[2])}", "wb") as image_file:
		for chunk in tmp_image.iter_content():
			image_file.write(chunk)

print("Done")
