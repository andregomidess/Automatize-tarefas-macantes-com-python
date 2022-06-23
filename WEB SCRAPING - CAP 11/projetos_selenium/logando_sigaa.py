from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
browser.get('https://sigaa.unifei.edu.br/sigaa/verTelaLogin.do')
email_input = browser.find_element(By.NAME, 'user.login')
email_input.send_keys('15797911663')
senha_input = browser.find_element(By.NAME, 'user.senha')
senha_input.send_keys('Cocafora007*')
senha_input.send_keys(Keys.ENTER)
