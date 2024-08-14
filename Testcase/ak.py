import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to your chromedriver executable
chromedriver_path = r"C:\Users\ajay\OneDrive\Desktop\chromedriver.exe"
os.environ["PATH"] += os.pathsep + os.path.dirname(chromedriver_path)

# Create Chrome options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

# Initialize the WebDriver
driver = webdriver.Chrome(options=chrome_options)


driver.get("https://www.instagram.com/guviofficial/")
time.sleep(10)  # Add a delay to allow page content to load

# Use WebDriverWait to wait for elements to be present
wait = WebDriverWait(driver, 10)
followers_element = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="mount_0_0_Jf"]/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section/div[2]/ul/li[2]/div/button')))
following_element = wait.until(EC.presence_of_element_located((By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button")))

# Extract the follower and following counts
followers_count = followers_element.get_attribute("title")
following_count = following_element.text

print(f"Followers: {followers_count}")
print(f"Following:{following_count}")

# Quit the WebDriver
driver.quit()