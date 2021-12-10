from time import sleep 
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import random 
import os 
import ctypes 
#driver=webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=webdriver.ChromeOptions())
WALLPAPER_DIR_NAME = os.path.dirname(__file__).replace('\\','/')+"/wallPapers"
CURRENT_INDEX=0;

def changeWallPaper():
	print("--starting wallpaper program--")
	WALLPAPER_LIST=os.listdir(WALLPAPER_DIR_NAME)
	WALLPAPER_COUNT=len(WALLPAPER_LIST)
	print("wallpapers loaded: total "+str(WALLPAPER_COUNT))

	currentWallpaperName = random.choice(WALLPAPER_LIST)
	imagePath = WALLPAPER_DIR_NAME+"/"+currentWallpaperName;
	print("selected wallpaper name: "+imagePath)
	ctypes.windll.user32.SystemParametersInfoW(20, 0, imagePath, 0)
	CURRENT_INDEX+=1;

changeWallPaper()





