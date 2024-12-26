import time
from selenium import webdriver

# Initialize the Chrome driver
driver = webdriver.Chrome()  # Update with the correct path to chromedriver

# Open Google
driver.get('http://www.google.com/')
time.sleep(5)  # Allow the page to load

# Locate the search box by its name attribute
search_box = driver.find_element("name", "q")  # Updated to use modern Selenium syntax
search_box.send_keys('Korea')  # Enter the search term "Korea"
search_box.submit()  # Submit the search query

time.sleep(5)  # Allow time to see the results

# Close the browser
driver.quit()
