import allure
from selene import browser, be, by, have


class TherapistsPage:
    def __init__(self):
        self.therapists_cards ='.ysn-grid-without-outer-padding > div'
        self.short_filters = '[data-id="therapist-catalog-short-filters"] div._overflow-auto span._whitespace-nowrap'
        self.answers_to_questions = '._border-grey-500'
        self.price_of_therapists_in_card = '._items-center ._t-body-accent'
        self.show_more = 'button._btn-base-secondary'
        self.symptoms = 'Симптомы'
        self.approach = 'Подход'
        self.price = 'Цена'
        self.gender = 'Пол'
        self.all_filters = 'Все фильтры'
        self.sort_short_filters = '[data-id="therapist-catalog-short-filters"] ._s-select._ml-auto ._inline-flex > div'
        self.apply_filter_in_search_modal = '._s-popup_controls ._btn-base-primary'
        self.cancel_filter_in_search_modal = '.._s-popup_controls ._btn-base-secondary'
        self.clear_filter_in_search_modal = '._s-popup_controls ._btn-base-thetriary'

    @allure.step("Открытие страницы каталога терапевтов")
    def open(self):
        browser.open("/therapists")

