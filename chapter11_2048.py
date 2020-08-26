# 2048
#
# 2048 is a simple game where you combine tiles by sliding them up, down, left, or right with the arrow keys.
# You can actually get a fairly high score by repeatedly sliding in an up, right, down, and left pattern over
# and over again. Write a program that will open the game at https://gabrielecirulli.github.io/2048/
# and keep sending up, right, down, and left keystrokes to automatically play the game.

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()
browser.get("https://gabrielecirulli.github.io/2048/")
webpage = browser.find_element_by_tag_name("html")
while True:
	webpage.send_keys(Keys.UP)
	time.sleep(0.5)
	webpage.send_keys(Keys.RIGHT)
	time.sleep(0.5)
	webpage.send_keys(Keys.DOWN)
	time.sleep(0.5)
	webpage.send_keys(Keys.LEFT)
	time.sleep(0.5)
