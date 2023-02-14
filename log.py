from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

#abrindo o navegador desejado
navegador = webdriver.Firefox()

#abrindo o site desejado
navegador.get("https://accounts.mlabs.io/accounts/sign_in?access_token=true")
