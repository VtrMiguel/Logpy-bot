from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

#abrindo o navegador desejado
navegador = webdriver.Firefox()

#abrindo o site desejado
navegador.get("https://accounts.mlabs.io/accounts/sign_in?access_token=true")

#selecionando o id do input para colocar a 'conta'
time.sleep(7)
navegador.find_element(By.XPATH, ('//*[@id="email"]')).send_keys("conta")

#selecionando o id do input para colocar a 'senha'
time.sleep(5)
navegador.find_element(By.XPATH, ('//*[@id="password"]')).send_keys("senha123")

#selecionando o id do botão para clicar
time.sleep(5)
navegador.find_element(By.XPATH, ('//*[@id="btnSubmit"]/p/div')).click()

#só pra ter certeza que tudo deu certo!
time.sleep(5)
print("sucesso!")