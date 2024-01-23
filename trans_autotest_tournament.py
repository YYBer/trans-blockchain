import subprocess
import pkg_resources
import sys
import getpass
from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
# from selenium.common.exceptions import TimeoutException, NoSuchElementException

def install(library_name):
    subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])

def is_library_installed(library_name):
    try:
        pkg_resources.get_distribution(library_name)
        return True
    except pkg_resources.DistributionNotFound:
        return False
def install_check(library_name):
    if is_library_installed(library_name):
        print(f"{library_name} is already installed.")
    else:
        print(f"{library_name} is not installed. Installing now...")
        install(library_name)
        print(f"{library_name} installed successfully.")

def open_chrome_and_start_game(url, player_name):
    driver = webdriver.Chrome()
    driver.get(url)
    button_id = 'Start Remote Game'
    # Wait for the button to be present on the page
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, button_id)))
    
    # Find the start_game button using its id and click it
    start_game_button = driver.find_element(By.ID, button_id)
    start_game_button.click()
    print("Clicked the start_game button.")

    # Enter the player name
    player_name_input = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'Emter your name')))
    player_name_input.send_keys(player_name)

    # Choice the game type
    match_selection = driver.find_element(By.ID, 'Match')
    match_selection.click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, "//select[@id='Match']/option[2]")))
    match_dropdown = Select(driver.find_element(By.ID, 'Match'))
    match_dropdown.select_by_index(1)

    # Click the submit 
    submit_button = driver.find_element(By.ID, 'Submit')
    submit_button.click()


if __name__ == "__main__":
    install_check("selenium")
    install_check("pyautogui")
    open_chrome_and_start_game('http://127.0.0.1:8000/', "p1")
    open_chrome_and_start_game('http://127.0.0.1:8000/', "p2")
    open_chrome_and_start_game('http://127.0.0.1:8000/', "p3")
    open_chrome_and_start_game('http://127.0.0.1:8000/', "p4")
