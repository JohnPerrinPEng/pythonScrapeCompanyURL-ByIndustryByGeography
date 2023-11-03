from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# Set up the driver (assuming chromedriver is in PATH)
driver = webdriver.Chrome()
# Navigate to Google
driver.get("https://www.google.com")
# Find the search box using its name attribute
# search_box = driver.find_element_by_name("q")
# search_box = driver.find_element(name("q"))
search_box = driver.find_element.name("q")
# Input a query into the search box
search_box.send_keys("Hello, World!")
# Submit the search form
search_box.send_keys(Keys.RETURN)
# Wait for a few seconds to see the results (for demonstration purposes)
import time
time.sleep(5)
# Close the browser
driver.quit()