import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium import webdriver



driver = Chrome()

driver.get("https://bugbank.netlify.app/")
driver.maximize_window()

time.sleep(2)
#Registrar uma conta
driver.find_element(By.XPATH,'//*[@id="btnRegister"]').click()
time.sleep(1)
#Preencher campo email
driver.find_element(By.XPATH,'//*[@id="inputEmail"]').send_keys('registro2@bugbank.com')
time.sleep(1)
#Preencher campo nome
driver.find_element(By.XPATH,'//*[@id="inputName"]').send_keys('aroldo jose')
time.sleep(1)
#Preencher campo senha e confirmação de senha
driver.find_element(By.XPATH,'//*[@id="inputPassword"]').send_keys('aroljose')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="inputPasswordConfirmation"]').send_keys('aroljose')

time.sleep(1)
#Criar conta com saldo?
driver.find_element(By.XPATH,'//*[@id="toggleAddBalance"]').click()
time.sleep(2)
#Clicar em cadastrar
driver.find_element(By.XPATH,'//*[@id="btnRegister"]').click()
time.sleep(1)

#A conta foi criada com sucesso?
driver.find_element(By.XPATH,'//*[@id="modalText"]')
time.sleep(3)
#Caso sim, fechar
botao_fechar = driver.find_element(By.XPATH, '//*[@id="btnCloseModal"]').click()


driver.refresh()

#Fazendo login com usuário válido
driver.find_element(By.XPATH,'//*[@id="inputEmail"]').send_keys('registro2@bugbank.com')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="inputPassword"]').send_keys('aroljose')
driver.find_element(By.XPATH,'//*[@id="btnAccess"]').click()




#Fazer uma transferência
time.sleep(2)
botao_transferencia = driver.find_element(By.XPATH,'//*[@id="btn-TRANSFERÊNCIA"]').click()
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="inputAccountNumber"]').send_keys('100')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="inputAccountDigit"]').send_keys('7')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="inputTransferValue"]').send_keys('100')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="inputDescription"]').send_keys('Infelizmente, ainda em desenvolvimento')
time.sleep(1)
driver.find_element(By.XPATH,'//*[@id="btnTransferNow"]').click()
time.sleep(1)
botao_fechar = driver.find_element(By.XPATH,'//*[@id="btnCloseModal"]').click()
botao_voltar = driver.find_element(By.XPATH, '//*[@id="btnBack"]').click()
time.sleep(1)
clique_sair = driver.find_element(By.XPATH,'//*[@id="__next"]/div/div[1]/div').click()
driver.find_element(By.XPATH,'//*[@id="inputEmail"]').send_keys('Adeus!')
time.sleep(2)

driver.close()