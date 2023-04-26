import requests
import hashlib


class Yandex():

    main_search_field = '.search3__input'  # поле поиска на главной ya.ru
    main_search_button = '.search3__button'  # кнопка поиска на главной ya.ru
    search_category = '.search2__input input'  # поле поиска в категориях
    suggest_list = '.mini-suggest__popup-content li'  # подсказки в поиске
    search_page = '.navigation__item_name_www'  # вкладка "поиск"
    search_results = '[id="search-result"] > li a'  # ссылки результатов поиска
    search_group_photos = '.serp-item_group_search'  # фото результатов поиска
    preview_photo = '.MMImageContainer > img'  # окно просмотра изображений
    btn_next_photo = '.MediaViewer_theme_fiji-ButtonNext'  # кнопка вперед в просмотре
    btn_prev_photo = '.MediaViewer_theme_fiji-ButtonPrev'  # кнопка назад в просмотре
    services_suggest = '.services-suggest__list > li'  # всплывающее окно сервисов на главной ya.ru
    all_services = '.services-more-popup__item > a'  # все сервисы на главной
    category_image_list = '.PopularRequestList-Item img'  # категории изображений

    def check_url(self, input_url, reference_url):
        """Сверяет переданные url
        input_url: проверяем url
        reference_url: эталонный url
        """
        assert input_url == reference_url, f'ссылка {input_url} не соответствует эталону'

    def visible_element(self, element):
        """Проверяет видимость элемента страницы"""
        assert element, f'элемент {element} страницы не доступен'

    def move_to_serivice(self, list_services, serivce_name):
        """Кликает по элементу из списка сервисов
        list_services: список
        service_name: название сервиса
        """
        for i in list_services:
            if i.get_attribute('aria-label') == serivce_name:
                i.click()

    def check_categories(self, first_category, second_category):
        """Сверяет переданные названия категорий."""
        assert first_category == second_category, f'Категория списка изображений {first_category} не соответствует категории в поиске {second_category}'

    def get_image(self, url):
        """Возвращает хэш переданного изображения."""
        try:
            response = requests.get(url)
            return self.get_hash(response.content)

        except Exception as e:
            return "Image didn't load"

    def get_hash(self, content):
        """Вычисляет хэш переданного контента в бинарном виде."""
        hash_object = hashlib.md5(content)
        return hash_object.hexdigest()




