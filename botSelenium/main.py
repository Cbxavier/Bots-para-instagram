#chrome -> chromedriver
#firefox -> geckodriver
from selenium import webdriver
import time

#abrir navegador 
navegador = webdriver.Chrome()

#Acessa a página desejada
navegador.get("https://www.instagram.com/")

#Espera 15s antes de executar o próximo passo
time.sleep(15)

#AQUI INCIA O LOGIN 

#NOME DE USUARIO
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("user")
time.sleep(6)

#SENHA
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("senha")
time.sleep(6)

#CLICAR NO LOGIN
navegador.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div').click()
time.sleep(15)

navegador.get("https://www.instagram.com/direct/inbox/")






