
from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import database


####webdriver
driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com')
print('<<<<<SISTEMA DE ENVIO AUTOMÁTICO>>>>>>')
input('Connect Whatsapp web and press Enter ')
for i in range(1,4):
    print('.'*i)
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
    driver.find_element(By.CSS_SELECTOR, "span[data-icon='clip']").click()
    attach = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
    sleep(2)
    attach.send_keys(product.loc)
    sleep(4)
    sfield = driver.find_elements(By.XPATH, '//div[contains(@class,"copyable-text selectable-text")]')
    sfield[0].click()
    sfield[0].send_keys(product.description)
    sleep(2)
    send = driver.find_element(By.CSS_SELECTOR, "span[data-icon='send']")
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
            sleep(2)
            print(f'ENVIANDO PARA O GROUP {list_of_contacts[i]}')
            for item in database.set_of_products:
                sleep(1)
                print(f'ENVIANDO {item.name}')
                try:
                    send_message(item)
                    print('ENVIO REALIZADO COM SUCESSO')
                    print('------------------------')
                    sleep(6)
                except:
                    print('ERRO AO ENVIAR')
        except:
            print('Erro ao enviar')

