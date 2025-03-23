from model.pages.therapists_page import therapists


class TestTherapistsPage:
    def test_filters_should_has_short_filters(self):
        (therapists
         .open()
         .filters_should_be_not_selected())

    def test_header_links_should_be_clickable(self):
        (therapists.open()
         .links_should_be_clickable_header())

    def test_psychologist_cards_should_increase(self):
        (therapists.open()
         .therapists_cards_should_increase())
    def test_sorting_for_max_price(self):
        (therapists.open()
         .choose_max_filter()
         .check_max_price_in_card())

    def test_compare_price_popup_and_card(self):
        (therapists.open()
         .click_info_icon_in_card()
         .check_price_in_info_popup())

    def test_choose_couple_therapy(self):
        (therapists.open()
         .choose_couple_therapy()
         .check_couple_symptoms_in_popup()
         .check_couple_therapy_short_filters())

    def test_footer_should_have_links(self):
        (therapists.open()
         .check_footer_page_for_links())