import time

from selenium.webdriver.common.by import By

from first_t import setup, tear_down


def test_empty_search(driver):
    # поиск поля для поиска
    search_button_locator = By.CLASS_NAME, 'tm-header-user-menu__search'
    search_button = driver.find_element(*search_button_locator)
    search_button.click()
    time.sleep(1)

    # вбить текст
    search_input_locator = By.CLASS_NAME, 'tm-input-text-decorated__input'
    search_input = driver.find_element(*search_input_locator)
    text_to_search = 'dthfjgnf'
    search_input.send_keys(text_to_search)

    # нажать на кнопку поиска
    search_icon_locator = By.CSS_SELECTOR, 'span.tm-search__icon'
    search_icon = driver.find_element(*search_icon_locator)
    search_icon.click()
    time.sleep(1)

    # посчитать количество записей
    article_locator = By.TAG_NAME, 'article'
    articles = driver.find_elements(*article_locator)
    print(f'Number of articles is {len(articles)}')
    time.sleep(1)

    # проверяем текст
    empty_res_locator = By.CLASS_NAME, 'tm-empty-placeholder__text'
    empty_results = driver.find_element(*empty_res_locator)
    print(f'Text on page: {empty_results.text}')


if __name__ == '__main__':
    driver = setup()

    test_empty_search(driver)

    tear_down(driver)
