
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import database


####webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
wait = WebDriverWait(driver,10)
print('<<<<<SISTEMA DE ENVIO AUTOMÁTICO>>>>>>')
input('Connect Whatsapp web and press Enter ')
print('Carregando sistema...')
sleep(3)

list_of_contacts = ['OLX ZONA SUL','VENDAS PIEDADE/CANDEIAS','COND.PRAIA PIEDADE COMERC','FEIRINHA E SERVIÇOS 2',
                    'BOA VIAGEM COMPRAS','PRAIA PIEDADE COMERCIAL2','Praia Piedade Comercial']
##encontrar contato
def find_contact(name):
    sfield = driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    sfield[0].click()
    sfield[0].send_keys(name)
    sfield[0].send_keys(Keys.ENTER)

###enviar mensagem
def send_message(product):
    clip = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, "span[data-icon='clip']"))
    clip.click()
    attachimage = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, "input[type='file']"))
    sleep(3)
    attachimage.send_keys(product.loc)
    sleep(4)
    descriptionfield = driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    descriptionfield[0].click()
    descriptionfield[0].send_keys(product.description)
    sleep(3)
    send = wait.until(EC.element_to_be_clickable(By.CSS_SELECTOR, "span[data-icon='send']"))
    send.click()

#####automatização
while True:
    print('...................................')
    sleep(0.5)
    input('Continuar?')
    sleep(1)    
    for i in range(0,len(list_of_contacts)):
        try:
            find_contact(list_of_contacts[i])
            sleep(3)
            print(f'ENVIANDO PARA O GROUP {list_of_contacts[i]}')
            for item in database.set_of_products:
                sleep(2)
                print(f'ENVIANDO {item.name}')
                try:
                    send_message(item)
                    print('ENVIO REALIZADO COM SUCESSO')
                    print('------------------------')
                    sleep(8)
                except:
                    print('ERRO AO ENVIAR')
                    sleep(3)
        except:
            print('Erro')
            sleep(3)

