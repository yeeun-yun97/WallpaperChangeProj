from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random 
import os 
import ctypes 

print("--starting wallpaper program--")
ROOT_PATH = os.path.dirname(__file__).replace('\\','/')
driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())








