# from selenium import webdriver

# # URL to open in both windows
# url = 'http://127.0.0.1:8000/'

# # First Chrome window
# # driver1 = webdriver.Chrome()
# # driver1.get(url)
# driver1 = webdriver.Remote(command_executor=url)
# import time
# time.sleep(1)
# # Perform automation with driver1

# # Second Chrome window
# driver2 = webdriver.Chrome()
# driver2.get(url)
# # Perform automation with driver2

# # Close the browser windows
# driver1.quit()
# driver2.quit()

import webbrowser
webbrowser.open_new("http://127.0.0.1:8000/")