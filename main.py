from selenium import webdriver
from flask import Flask, request
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import os

app = Flask(__name__)

def download_selenium():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1280x1696')
    options.add_argument('--user-data-dir=/tmp/user-data')
    options.add_argument('--data-path=/tmp/data-path')
    options.add_argument('--homedir=/tmp')
    options.add_argument('--disk-cache-dir=/tmp/cache-dir')
    options.add_argument('--single-process')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-software-rasterizer')
    options.binary_location = '/usr/local/bin/google-chrome'
    driver = webdriver.Chrome(executable_path="/usr/local/bin/chromedriver", options=options)
    driver.get("https://google.com")
    title = driver.title
    language = driver.find_element(By.XPATH, "//div[@id='SIvCob']").text
    data = {'Page Title': title, 'Language': language}
    return data


@app.route('/', methods = ['GET','POST'])
def home():
    if (request.method == 'GET'):
        return download_selenium()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(debug=True, host='0.0.0.0', port=port)
    
