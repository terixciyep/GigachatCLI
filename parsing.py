from selenium import webdriver
from bs4 import BeautifulSoup


def pars_cases(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    page_content = driver.page_source
    soup = BeautifulSoup(page_content, 'html.parser')
    driver.quit()

    data = []
    if soup:
        content = soup.find('div', id='allrecords').find('div', id='rec570167622').find('div', class_='t786').find('div', class_='t-store').find('div',class_="js-store-grid-cont t-store__grid-cont t-store__grid-cont_col-width_stretch t-container_100 t-store__grid-cont_mobile-grid")
        for div in content.find_all('div', class_='js-product'):
            product = div.find('a')
            href = product.get('href')
            if 'https://eora.ru/' not in href:
                href = 'https://eora.ru/' + href
            name = product.find('div', class_="t-store__card__textwrapper").find('div', class_="js-store-prod-name js-product-name t-store__card__title t-typography__title t-name t-name_md").text
            data.append((href, name))

    return data

