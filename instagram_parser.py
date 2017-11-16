import os
from selenium import webdriver
import bs4 as BeautifulSoup
import time
import random


# THIS SCRIPT PARSES THE INSTAGRAM WEBSITE HTML FOR A GIVEN TAG.
villes = ['paris', 'lyon', 'marseille', 'bordeaux','lille', 'loisir']
liens = ['https://www.instagram.com/explore/locations/6889842/paris-france/', 'https://www.instagram.com/explore/locations/213168722/lyon-france/', 'https://www.instagram.com/explore/locations/101977618/marseille-france/', 'https://www.instagram.com/explore/locations/213097372/bordeaux-france/', 'https://www.instagram.com/explore/locations/215780716/lille-france/', 'https://www.instagram.com/explore/tags/loisir/']

iteration = 1

# create new Edge session
dir = os.path.dirname("C:\Users\Lolo\Desktop\MicrosoftWebDriver")
edge_path = dir + "\MicrosoftWebDriver.exe"
driver = webdriver.Edge(edge_path)

# access instagram tag search page
driver.get(liens[iteration])
driver.set_window_size(600, 6000) # set window size

time.sleep(5) # necessary time to click the 'Charger la suite' button


# scroll parameters
scroll_counter = 0 
scroll_limit = 11
time_between_scrolls = 1 # to load instagram photos
iteration = str(2)

# parsing
while scroll_counter <= scroll_limit:
    
    #r = random.randint(0, 100)

    # scroll
    time.sleep(float(time_between_scrolls)) # + (float(r) / 100.0))
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") # execute scroll
    
    # retrieve html data
    soup = BeautifulSoup.BeautifulSoup(driver.page_source)

    # save data
    if scroll_counter == (scroll_limit - 1):
        text_file = open('data_insta/html/instagram_html.txt', "w")
        text_file.write(str(soup))
        text_file.close()
    
    scroll_counter += 1 # add 1 to counter
    print scroll_counter

        
driver.close()