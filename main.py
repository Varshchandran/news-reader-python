"""
Author: Varsha Chandran

This Python script downloads news from BBC and using a Text to Speech Engine , it reads it ou

Requirements:
- Selenium: You can install it using 'pip install selenium'.
- Firefox: You should have Firefox installed on your system.

Usage:
1. Set the 'profile_directory' variable to the location of your Firefox profile directory.

"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pyttsx3
engine = pyttsx3.init()

def get_headlines():
    # Your main code goes here
    # Create a Firefox WebDriver instance
    driver = webdriver.Firefox()

    # Open the BBC News website
    driver.get('https://www.bbc.com/news')
    try:
        # Wait for the headlines to load (adjust the timeout as needed)
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'gel-pica-bold'))
        )

        # Find the headlines by their CSS class
        headlines = driver.find_elements(By.CLASS_NAME, 'gel-pica-bold')
        # Initialize the text-to-speech engine        
        unique_headlines = set()

        #Remove duplicates if any
        for headline in headlines:
            news_headline = headline.text
            if news_headline not in unique_headlines: 
                unique_headlines.add(news_headline)
    finally:
        # Close the WebDriver
        driver.quit()
    return unique_headlines

def read_news(newsentry):
    print(newsentry)  # Print the headline to the console
    engine.say(newsentry)  # Convert headline to speech
    engine.runAndWait()  # Play the speech

if __name__ == "__main__":
    news_entries=get_headlines()
    for entry in news_entries:
        read_news(entry)