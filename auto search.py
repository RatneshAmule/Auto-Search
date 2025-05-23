import random
import string
import time
import pyautogui
import webbrowser

# Function to generate a random three-letter string
def random_three_letters():
    return ''.join(random.choices(string.ascii_lowercase, k=3))

# Open the browser to the first tab
webbrowser.open("https://www.bing.com")
time.sleep(3)  # Wait for the browser to open

# Loop to perform 30 searches
for _ in range(40):
    # Generate a new random three-letter search term
    search_term = random_three_letters()
    
    # Type the search term and press Enter
    pyautogui.write(search_term)
    pyautogui.press("enter")
    
    # Wait briefly for the search to complete
    time.sleep(2)
    
    # Open a new tab
    pyautogui.hotkey("ctrl", "t")
    time.sleep(1.5)  # Reduced time delay
    
    # Focus on the address bar and go to Bing again
    pyautogui.hotkey("ctrl", "l")  # Shortcut to select the address bar
    time.sleep(0.5)  # Faster transition
    pyautogui.write("https://www.bing.com")
    pyautogui.press("enter")
    time.sleep(2.5)  # Wait for Bing to load

# Close the browser manually after all searches
