from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep

chrome_options = Options()
chrome_options.add_argument("--window-size=1,1")
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://repl.it/github/YOUR_GITHUB_USERNAME/REPO_NAME')

errorpass = 75
loadtext = 1
clonetext = 1

while True:
    try:
        browser.find_element_by_xpath("//*[text()='Loading files...']")
        if loadtext == 1:
            print('Repl loading')
            loadtext = 0
    except:
        try:
            browser.find_element_by_css_selector('div.spinner-modal-container')
            if clonetext == 1:
                print('Cloning github')
                clonetext = 0
        except:
            if errorpass != 0:
                errorpass = errorpass - 1
                pass
            else:
                break

print('Running')
browser.execute_script("document.getElementsByClassName('ws-header-cta')[0].click()")
