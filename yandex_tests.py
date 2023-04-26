from driver import Driver
from yandex_page import Yandex
from time import sleep


url = "https://ya.ru"


def test_01():
    """Тест1. Проверка соответсвия ссылки в результате поиска.
    1)	Зайти на https://ya.ru/
    2)	Проверить наличия поля поиска
    3)	Ввести в поиск Тензор
    4)	Проверить, что появилась таблица с подсказками (suggest)
    5)	Нажать enter
    6)	Проверить, что появилась страница результатов поиска
    7)	Проверить 1 ссылка ведет на сайт tensor.ru
    """
    page = Driver(url)
    element = Yandex()
    page.get_element(element.main_search_field).send_keys("Тензор")
    sleep(1)
    suggest = page.get_elements(element.suggest_list)
    element.visible_element(suggest)
    page.get_element(element.main_search_button).click()
    sleep(1)
    search_page = page.get_element(element.search_page)
    element.visible_element(search_page)
    search_url = page.get_elements(element.search_results)[0].get_attribute('href')
    element.check_url(search_url, "https://tensor.ru/")


def test_02():
    """Тест 2.
    1)	Зайти на ya.ru
    2)	Проверить, что кнопка меню присутствует на странице
    3)	Открыть меню, выбрать “Картинки”
    4)	Проверить, что перешли на url https://yandex.ru/images/
    5)	Открыть первую категорию
    6)	Проверить, что название категории отображается в поле поиска
    7)	Открыть 1 картинку
    8)	Проверить, что картинка открылась
    9)	Нажать кнопку вперед
    10)	Проверить, что картинка сменилась
    11)	Нажать назад
    12)	Проверить, что картинка осталась из шага 8
    """
    page = Driver(url)
    element = Yandex()
    page.get_element(element.main_search_field).click()
    page.get_elements(element.services_suggest)[-1].click()
    sleep(1)
    all_services = page.get_elements(element.all_services)
    element.move_to_serivice(all_services, 'Картинки')
    sleep(2)
    page.select_tab(1)
    category_list = page.get_elements(element.category_image_list)
    first_category = category_list[0].get_attribute('alt')
    sleep(1)
    page.hover_on_element(category_list[0]).click().perform()
    sleep(2)
    search = page.get_element(element.search_category).get_attribute('value')
    element.check_categories(first_category, search)
    page.get_elements(element.search_group_photos)[0].click()
    sleep(2)
    preview_window = page.get_element(element.preview_photo)
    reference_image = element.get_image(preview_window.get_attribute('src'))
    page.hover_on_element(preview_window).perform()
    sleep(1)
    page.get_element(element.btn_next_photo).click()
    assert reference_image != element.get_image(page.get_element(element.preview_photo).get_attribute('src')), 'изображение не изменилось'
    page.get_element(element.btn_prev_photo).click()
    assert reference_image == element.get_image(page.get_element(element.preview_photo).get_attribute('src')), 'изображение не соответствует эталону'


def test_head():
    test_01()
    test_02()