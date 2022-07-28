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
    sleep(3)
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
    contact_name = str(input('Contato para enviar: \n> ')).strip()
    sleep(1)
    try:
        find_contact(contact_name)
    except:
        print('Houve um erro, tente novamente')
    start = input('Enter para começar o envio')
    for item in database.set_of_products:
        try:
            print(f'ENVIANDO {item.name}')
            send_message(item)
            print('ENVIO REALIZADO COM SUCESSO')
            sleep(6)
        except:
            print('Houve um erro no envio deste arquivo')

