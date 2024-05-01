from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from time import sleep

def test_sale():
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    browser.get('https://magento.softwaretestingboard.com/sale.html')
    sleep(1)
    sale_link = browser.find_element(By.ID, value= 'ui-id-8')
    sale_link.click()
    title = browser.find_element(By.TAG_NAME, value= 'h1')
    assert title.text == 'Sale'
    print('Sale присутствует на странице')

    training_link = browser.find_element(By.ID, value= 'ui-id-7')
    training_link.click()
    sleep(1)
    title = browser.find_element(By.TAG_NAME, value= 'h1')
    assert title.text == 'Training'
    print('Training присутствует на странице')

    Gear_link = browser.find_element(By.ID, value='ui-id-6')
    Gear_link.click()
    sleep(1)
    title = browser.find_element(By.TAG_NAME, value='h1')
    assert title.text == 'Gear'
    print('Gear присутствует на странице')

    # Найти элемент, на который нужно навести мышь
    element = browser.find_element(By.ID, value='ui-id-6')
    # Создать экземпляр класса ActionChains
    actions = ActionChains(browser)
    # Навести мышь на элемент
    actions.move_to_element(element).perform()

    Bags_link = browser.find_element(By.ID, value= 'ui-id-25')
    Bags_link.click()
    sleep(1)
    title = browser.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Bags'
    print('Bags присутствует на странице')

    # Найти элемент, на который нужно навести мышь
    element = browser.find_element(By.ID, value='ui-id-6')
    # Создать экземпляр класса ActionChains
    actions = ActionChains(browser)
    # Навести мышь на элемент
    actions.move_to_element(element).perform()

    Fitness_Equipment_link = browser.find_element(By.ID, value= 'ui-id-26')
    Fitness_Equipment_link .click()
    sleep(1)
    title = browser.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Fitness Equipment'
    print('Fitness Equipment присутствует на странице')

    # Найти элемент, на который нужно навести мышь
    element = browser.find_element(By.ID, value='ui-id-6')
    # Создать экземпляр класса ActionChains
    actions = ActionChains(browser)
    # Навести мышь на элемент
    actions.move_to_element(element).perform()

    Watches_link = browser.find_element(By.ID, value= 'ui-id-27')
    Watches_link .click()
    sleep(1)
    title = browser.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Watches'
    print('Watches присутствует на странице')

    # Найти элемент, на который нужно навести мышь
    element = browser.find_element(By.ID, value='ui-id-5')
    # Создать экземпляр класса ActionChains
    actions = ActionChains(browser)
    # Навести мышь на элемент
    actions.move_to_element(element).perform()

    # Найти элемент, на который нужно навести мышь
    element = browser.find_element(By.ID, value='ui-id-17')
    # Создать экземпляр класса ActionChains
    actions = ActionChains(browser)
    # Навести мышь на элемент
    actions.move_to_element(element).perform()

    jackets_link = browser.find_element(By.ID, value= 'ui-id-19')
    jackets_link.click()
    sleep(1)
    title = browser.find_element(By.TAG_NAME, 'h1')
    assert title.text == 'Jackets'
    print('Jackets присутствует на странице')
