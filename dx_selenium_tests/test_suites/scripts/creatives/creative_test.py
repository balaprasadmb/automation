from dx_test.dx_test import DXTest
from lib.dx_date import DXDate
from lib.gui_tests import test_case
import os
import time

class CreativeTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(self.dx_constant.user_by_role['campaign_manager'])

    def navigate_to_creative_list(self):
        self.pages.search_page.click_creative_link()
        self.pages.search_page.accept_alert()
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.asset_list_table)
        self.pages.creative_list_page.click_element(self.pages.creative_list_page.filters)
        self.pages.creative_list_page.select_advertiser(self.dx_constant.advertiser_name)
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.asset_list_table)

    @test_case()
    def working_of_advertiser_dropdown(self):
        self.navigate_to_creative_list()
        self.pages.creative_list_page.page_should_contain(self.dx_constant.advertiser_name)

    def wait_for_spinner(self):
        self.pages.creative_list_page.wait_till_visible(self.pages.creative_list_page.creative_tag_spinner)
        self.pages.creative_list_page.wait_till_invisible(self.pages.creative_list_page.creative_tag_spinner)

    @test_case()
    def offer_type_should_not_present(self):
        self.pages.creative_list_page.page_should_not_contain('Offer Type')

    @test_case()
    def working_of_filter_creatives(self):
        try:
            self.pages.creative_list_page.search_creative(self.pages.creative_list_page.search)
            self.pages.creative_list_page.wait_for_spinner()
            assert self.pages.creative_list_page.search in self.pages.creative_list_page.get_first_creative()
            self.pages.creative_list_page.search_creative('Dns#3Bpd')
            self.pages.creative_list_page.wait_for_spinner()
            self.pages.creative_list_page.page_should_contain(self.pages.creative_list_page.creatives_not_found_message)
            self.pages.creative_list_page.search_creative('')
        except Exception as e:
            self.pages.creative_list_page.search_creative('')
            raise e

    @test_case()
    def working_of_master_checkbox(self):
        self.navigate_to_creative_list()
        self.pages.creative_list_page.click_select_all()
        assert self.pages.creative_list_page.find_element(self.pages.creative_list_page.first_creative_checkbox).is_selected()
        self.pages.creative_list_page.click_select_all()
        assert not self.pages.creative_list_page.find_element(self.pages.creative_list_page.first_creative_checkbox).is_selected()

    @test_case()
    def working_of_creative_link(self):
        contents = self.pages.detailed_edit_creatives.creative_show_page_contents
        contents.append(self.pages.creative_list_page.get_first_creative())
        self.pages.creative_list_page.click_first_creative()
        self.pages.detailed_edit_creatives.wait_for_details_view()
        for content in contents:
            self.pages.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def go_to_detailed_edit(self):
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.pages.creative_list_page.go_to_link('Detailed Edit')
        self.pages.detailed_edit_creatives.wait_for_detailed_form()

    @test_case()
    def working_of_cancel_button(self):
        self.navigate_to_creative_list()
        self.pages.creative_list_page.click_new_creatives()
        self.go_to_detailed_edit()
        self.pages.detailed_edit_creatives.click_cancel_first()
        self.pages.detailed_edit_creatives.accept_alert()
        self.pages.creative_list_page.wait_for_creatives_list()
        self.pages.creative_list_page.page_should_contain('Creative tags')

    @test_case()
    def working_of_new_creatives_button(self):
        self.pages.creative_list_page.click_new_creatives()
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.pages.bulk_edit_creative_page.page_should_contain('Set Up Creatives')

    @test_case()
    def verify_contents_of_bulk_edit(self):
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        for element in self.pages.bulk_edit_creative_page.page_contents:
            assert self.pages.bulk_edit_creative_page.is_element_present(getattr(self.pages.bulk_edit_creative_page, element))

    @test_case()
    def working_of_add_creatives_button(self):
        self.pages.bulk_edit_creative_page.click_add_creative()
        time.sleep(5)
        for element in self.pages.bulk_edit_creative_page.new_creative_contents:
            assert self.pages.bulk_edit_creative_page.is_element_present(getattr(self.pages.bulk_edit_creative_page, element))

    @test_case()
    def working_of_cancel_bulk_edit(self):
        self.pages.bulk_edit_creative_page.click_cancel()
        self.pages.bulk_edit_creative_page.accept_alert()
        self.pages.creative_list_page.wait_for_creatives_list()
        self.pages.creative_list_page.page_should_contain('Creative tags')

    @test_case()
    def get_creative_tags(self):
        tag_file = open(os.path.dirname(__file__) + '/../../../data/bulk_upload_creative_files/creative_tags.txt')
        tags =  tag_file.read()
        tag_file.close()
        return tags

    @test_case()
    def fill_bulk_edit_creative_details(self):
        creative = self.dx_constant.creative_name + self.pages.bulk_edit_creative_page.get_random_string()
        self.pages.bulk_edit_creative_page.input_first_creative_name(creative)
        concept = self.dx_constant.creative_concept_name + self.pages.bulk_edit_creative_page.get_random_string()
        self.pages.bulk_edit_creative_page.input_first_concept(concept)
        self.pages.bulk_edit_creative_page.input_first_tag(self.get_creative_tags())
        time.sleep(10)
        self.pages.bulk_edit_creative_page.click_save_creatives()

    @test_case()
    def working_of_save_creatives(self):
        self.navigate_to_creative_list()
        self.pages.creative_list_page.click_new_creatives()
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.fill_bulk_edit_creative_details()
        self.pages.creative_list_page.wait_for_creatives_list()
        self.pages.creative_list_page.page_should_contain(self.pages.bulk_edit_creative_page.success_message)

    @test_case()
    def working_of_detailed_edit_link(self):
        self.navigate_to_creative_list()
        self.pages.creative_list_page.click_new_creatives()
        self.go_to_detailed_edit()
        self.pages.detailed_edit_creatives.page_should_contain('Creatives List')

    @test_case()
    def verify_contents_of_detailed_edit(self):
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        for element in self.pages.detailed_edit_creatives.page_elements:
            assert self.pages.detailed_edit_creatives.is_element_present(getattr(self.pages.detailed_edit_creatives, element))
        for index in range(1,10):
            self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.page_contents[index])

    @test_case()
    def verify_options_in_size(self):
        assert self.pages.detailed_edit_creatives.get_dropdown_selected_value(self.pages.detailed_edit_creatives.first_size) == '- Select One -'
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.creative_sizes, self.pages.detailed_edit_creatives.first_size)

    @test_case()
    def verify_custom_size_fields(self):
        self.pages.detailed_edit_creatives.select_first_size('Custom Size...')
        time.sleep(5)
        for element in ['first_size_width', 'first_size_height']:
            assert self.pages.detailed_edit_creatives.is_element_present(getattr(self.pages.detailed_edit_creatives, element))

    @test_case()
    def verify_ad_type(self):
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.ad_type, self.pages.detailed_edit_creatives.first_ad_type)

    @test_case()
    def verify_ad_features_for_banner(self):
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.banner_features, self.pages.detailed_edit_creatives.first_ad_feature)

    @test_case()
    def verify_ad_features_for_linear_video(self):
        self.pages.detailed_edit_creatives.select_first_ad_type(self.pages.detailed_edit_creatives.ad_type[1])
        time.sleep(10)
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.video_features, self.pages.detailed_edit_creatives.first_ad_feature)

    @test_case()
    def verify_ad_features_for_rich_media(self):
        self.pages.detailed_edit_creatives.select_first_ad_type(self.pages.detailed_edit_creatives.ad_type[2])
        time.sleep(10)
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.rich_media_features, self.pages.detailed_edit_creatives.first_ad_feature)

    @test_case()
    def verify_additional_url_not_mandatory(self):
        assert self.pages.detailed_edit_creatives.find_element(self.pages.detailed_edit_creatives.first_additional).text == ''

    @test_case()
    def verify_lang_targeting(self):
        assert self.pages.detailed_edit_creatives.get_dropdown_selected_value(self.pages.detailed_edit_creatives.first_lang_targeting) == 'None'
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.languages, self.pages.detailed_edit_creatives.first_lang_targeting)

    @test_case()
    def verify_creative_attributes(self):
        assert self.pages.detailed_edit_creatives.get_dropdown_selected_value(self.pages.detailed_edit_creatives.first_is_flash) == 'Flashless'
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.creative_attributes, self.pages.detailed_edit_creatives.first_is_flash)

    @test_case()
    def verify_oba_icon_placement(self):
        assert self.pages.detailed_edit_creatives.get_dropdown_selected_value(self.pages.detailed_edit_creatives.first_placement) == '- Select One -'
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.placements, self.pages.detailed_edit_creatives.first_placement)

    @test_case()
    def verify_ad_tag_section(self):
        for element in self.pages.detailed_edit_creatives.ad_tag_section:
            assert self.pages.detailed_edit_creatives.is_element_present(getattr(self.pages.detailed_edit_creatives, element))
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.ad_tag_types, self.pages.detailed_edit_creatives.first_tag_type)

    @test_case()
    def verify_external_id_section(self):
        self.pages.detailed_edit_creatives.click_first_external_id()
        self.pages.detailed_edit_creatives.wait_for_external_id_source()
        for element in self.pages.detailed_edit_creatives.external_id_row_elements:
            assert self.pages.detailed_edit_creatives.is_element_present(getattr(self.pages.detailed_edit_creatives, element))
        assert self.pages.detailed_edit_creatives.get_dropdown_selected_value(self.pages.detailed_edit_creatives.first_external_id_source) == 'RMX'
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.external_id_sources,
                                                                  self.pages.detailed_edit_creatives.first_external_id_source)

    @test_case()
    def verify_vendors_section(self):
        self.pages.detailed_edit_creatives.click_add_first_vendor()
        self.pages.detailed_edit_creatives.check_dropdown_options(self.pages.detailed_edit_creatives.vendors, self.pages.detailed_edit_creatives.first_select_vendor)

    @test_case()
    def working_of_remove_button_with_cancel(self):
        self.pages.detailed_edit_creatives.click_remove_first_vendor()
        time.sleep(3)
        self.pages.detailed_edit_creatives.dismiss_alert()
        assert self.pages.detailed_edit_creatives.is_element_present(self.pages.detailed_edit_creatives.first_select_vendor)

    @test_case()
    def working_of_remove_button_with_ok(self):
        self.pages.detailed_edit_creatives.click_remove_first_vendor()
        time.sleep(3)
        self.pages.detailed_edit_creatives.accept_alert()
        time.sleep(2)
        assert not self.pages.detailed_edit_creatives.is_element_present(self.pages.detailed_edit_creatives.first_select_vendor)

    def fill_creative_details_with_blank(self):
        self.working_of_detailed_edit_link()
        self.pages.detailed_edit_creatives.wait_for_detailed_form()
        self.pages.detailed_edit_creatives.input_first_url('')
        self.pages.detailed_edit_creatives.select_first_is_flash('- Select One -')
        self.pages.detailed_edit_creatives.click_validate_first()
        self.pages.detailed_edit_creatives.wait_for_errors()

    def blank_message_validation(self, key):
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.blank_messages[key])

    @test_case()
    def blank_creative_name(self):
        self.blank_message_validation('name')

    @test_case()
    def blank_concept_name(self):
        self.blank_message_validation('concept')

    @test_case()
    def size_should_not_selected(self):
        for key in ['height', 'width']:
            self.blank_message_validation(key)

    @test_case()
    def creative_attributes_kept_blank(self):
        self.blank_message_validation('flash')

    @test_case()
    def blank_ad_tag(self):
        for key in ['tags', 'ad_tag']:
            self.blank_message_validation(key)

    @test_case()
    def blank_advertiser_url(self):
        self.blank_message_validation('url')

    def fill_creative_details_with_special_chars(self):
        self.working_of_detailed_edit_link()
        time.sleep(5)
        self.pages.detailed_edit_creatives.input_first_url(self.dx_constant.special_char)
        time.sleep(5)
        self.pages.detailed_edit_creatives.input_first_add_url(self.dx_constant.special_char)
        self.pages.detailed_edit_creatives.select_first_placement('Top Right')
        time.sleep(5)
        self.pages.detailed_edit_creatives.input_first_z_index(self.dx_constant.special_char)
        self.pages.detailed_edit_creatives.click_validate_first()
        self.pages.detailed_edit_creatives.wait_for_errors()

    def special_chars_validation(self, key):
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.special_chars[key])

    @test_case()
    def special_chars_urls(self):
        self.special_chars_validation('url')

    @test_case()
    def special_chars_z_index(self):
        self.special_chars_validation('z_index')

    def fill_creative_details_with_256_chars(self):
        self.pages.detailed_edit_creatives.input_first_creative_name(self.pages.detailed_edit_creatives.get_random_string(256))
        self.pages.detailed_edit_creatives.input_first_concept(self.pages.detailed_edit_creatives.get_random_string(201))
        self.pages.detailed_edit_creatives.click_validate_first()
        time.sleep(10)

    def over_limit_validation(self, key):
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.over_limit[key])

    @test_case()
    def over_limit_name(self):
        self.over_limit_validation('name')

    @test_case()
    def over_limit_concept(self):
        self.over_limit_validation('concept')

    @test_case()
    def fill_creative_details(self):
        if self.creative_details.has_key('lang'):
            self.pages.detailed_edit_creatives.select_first_lang_targeting(self.creative_details['lang'])
        self.pages.detailed_edit_creatives.input_first_creative_name(self.creative_details['name'])
        self.pages.detailed_edit_creatives.input_first_concept(self.creative_details['concept'])
        if self.creative_details.has_key('advertiser_url'):
            self.pages.detailed_edit_creatives.input_first_url(self.creative_details['advertiser_url'])
        if self.creative_details.has_key('first_url'):
            self.pages.detailed_edit_creatives.input_first_add_url(self.creative_details['first_url'])
        if self.creative_details.has_key('second_url'):
            self.pages.detailed_edit_creatives.update_first_add_url(self.creative_details['second_url'])
        if self.creative_details.has_key('size'):
            self.pages.detailed_edit_creatives.select_first_size(self.creative_details['size'])
            if self.creative_details['size'] == 'Custom Size...':
                self.pages.detailed_edit_creatives.input_first_width(self.creative_details['width'])
                self.pages.detailed_edit_creatives.input_first_height(self.creative_details['height'])
        if self.creative_details.has_key('first_source'):
            self.pages.detailed_edit_creatives.click_first_external_id()
            time.sleep(5)
            self.pages.detailed_edit_creatives.select_first_external_id_source(self.creative_details['first_source'])
            self.pages.detailed_edit_creatives.input_first_external_id_value(self.creative_details['first_external_id'])
        if self.creative_details.has_key('second_source'):
            self.pages.detailed_edit_creatives.click_first_external_id()
            time.sleep(5)
            self.pages.detailed_edit_creatives.select_second_source(self.creative_details['second_source'])
            self.pages.detailed_edit_creatives.input_second_value(self.creative_details['second_external_id'])
        if self.creative_details.has_key('z_index'):
            self.pages.detailed_edit_creatives.input_first_z_index(self.creative_details['z_index'])
        self.pages.detailed_edit_creatives.input_first_tags(self.get_creative_tags())

    @test_case()
    def fill_creative_details_with_valid_special_chars(self):
        self.working_of_detailed_edit_link()
        payload = self.dx_constant.special_char + self.pages.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = self.dx_constant.creative_name + payload
        self.creative_details['concept'] = self.dx_constant.creative_concept_name + payload
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['size'] = '300x250'
        self.creative_details['lang'] = 'English'
        self.creative_details['first_source'] = 'RMX'
        self.creative_details['first_external_id'] = '3'
        self.creative_details['second_source'] = 'RMX'
        self.creative_details['second_external_id'] = '9'
        self.fill_creative_details()
        self.pages.detailed_edit_creatives.click_validate_first()

    @test_case()
    def working_of_validate_creative(self):
        time.sleep(5)
        creative_name = self.pages.detailed_edit_creatives.get_attribute_value(self.pages.detailed_edit_creatives.first_creative_name, 'value')
        if creative_name != self.creative_details['name']:
            self.pages.detailed_edit_creatives.input_first_creative_name(self.creative_details['name'])
            self.pages.detailed_edit_creatives.click_validate_first()
            time.sleep(5)
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['name'])
        assert not self.pages.detailed_edit_creatives.is_element_present(self.pages.detailed_edit_creatives.errors)

    @test_case()
    def working_of_save_creative(self):
        self.pages.detailed_edit_creatives.save_creative()
        self.pages.creative_list_page.wait_for_creatives_list()
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.success_message)

    @test_case()
    def go_to_show_creative(self):
        self.pages.creative_list_page.go_to_link(self.creative_details['name'])
        self.pages.detailed_edit_creatives.wait_for_details_view()

    @test_case()
    def assert_creative_name(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['name'])

    @test_case()
    def assert_creative_concept(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['concept'])

    @test_case()
    def assert_creative_size(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['size'])

    @test_case()
    def assert_additional_url(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['first_url'])

    @test_case()
    def assert_creative_attributes(self):
        self.pages.detailed_edit_creatives.page_should_contain('Flashless')

    @test_case()
    def assert_oba_placement(self):
        self.pages.detailed_edit_creatives.page_should_contain('top-right')

    @test_case()
    def assert_lang_targeting(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['lang'])

    @test_case()
    def assert_external_ids(self):
        for content in self.pages.detailed_edit_creatives.external_ids_values:
            self.pages.detailed_edit_creatives.page_should_contain(self.creative_details[content])

    @test_case()
    def creative_name_should_not_accept_script(self):
        self.working_of_detailed_edit_link()
        time.sleep(5)
        self.creative_details = {}
        self.creative_details['name'] = self.dx_constant.html_tag
        self.creative_details['concept'] = self.dx_constant.html_tag
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['size'] = '300x250'
        self.creative_details['lang'] = 'English'
        self.creative_details['z_index'] = self.dx_constant.strings
        self.creative_details['first_source'] = 'BlueKai'
        self.creative_details['first_external_id'] = '9'
        self.creative_details['second_source'] = 'BlueKai'
        self.creative_details['second_external_id'] = '9'
        self.fill_creative_details()
        self.pages.detailed_edit_creatives.input_first_tags(self.pages.detailed_edit_creatives.get_random_string())
        self.pages.detailed_edit_creatives.click_validate_first()
        self.pages.detailed_edit_creatives.wait_for_errors()
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.blank_messages['name'])

    @test_case()
    def assert_concept_not_accepts_script(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.validation['concept'])

    @test_case()
    def assert_invalid_ad_tag(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.validation['ad_tag'])

    def validation_of_custom_size(self, width, height, messages):
        self.pages.detailed_edit_creatives.input_first_width(getattr(self.dx_constant, width))
        self.pages.detailed_edit_creatives.input_first_height(getattr(self.dx_constant, height))
        self.pages.detailed_edit_creatives.click_validate_first()
        time.sleep(5)
        for message in messages:
            self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.validation[message])

    @test_case()
    def validation_of_custom_size_number_name(self):
        self.working_of_detailed_edit_link()
        self.pages.detailed_edit_creatives.select_first_size('Custom Size...')
        for value in [['strings', 'value', ['width']], ['value','strings', ['height']],
                      ['strings', 'strings', ['width','height']]]:
            self.validation_of_custom_size(value[0], value[1], value[2])
        self.creative_details = {}
        self.creative_details['name'] = self.pages.detailed_edit_creatives.get_random_digits()
        self.creative_details['concept'] = self.dx_constant.creative_concept_name + self.pages.detailed_edit_creatives.get_random_digits(5)
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['second_url'] = 'www.xyz.com'
        self.creative_details['size'] = 'Custom Size...'
        self.creative_details['width'] = self.dx_constant.value
        self.creative_details['height'] = self.dx_constant.value
        self.creative_details['lang'] = 'French'
        self.creative_details['z_index'] = '39'
        self.creative_details['first_source'] = 'Atlas'
        self.creative_details['first_external_id'] = '19'
        self.creative_details['second_source'] = 'DFA'
        self.creative_details['second_external_id'] = '19'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_custom_size(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['width'] + 'x' + self.creative_details['height'])

    @test_case()
    def assert_proper_url_accepted(self):
        self.pages.detailed_edit_creatives.page_should_contain('http://www.someurl.com')

    @test_case()
    def assert_oba_placement_with_entered_index(self):
        for content in ['top-right', '39']:
            self.pages.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def assert_additional_url_accepts_more_than_one(self):
        for content in [self.creative_details['first_url'], self.creative_details['second_url']]:
            self.pages.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def validation_for_limit(self):
        self.working_of_detailed_edit_link()
        self.creative_details = {}
        self.creative_details['name'] = str(self.pages.detailed_edit_creatives.get_random_string(255)).lower()
        self.creative_details['concept'] = str(self.pages.detailed_edit_creatives.get_random_string(200)).lower()
        self.creative_details['size'] = '300x250'
        self.creative_details['advertiser_url'] = str('www.' + self.pages.detailed_edit_creatives.get_random_characters(247) + '.com').lower()
        self.creative_details['first_url'] = str('www.' + self.pages.detailed_edit_creatives.get_random_characters(247) + '.com').lower()
        self.creative_details['lang'] = 'German'
        self.creative_details['first_source'] = 'MediaMind'
        self.creative_details['first_external_id'] = '11'
        self.creative_details['second_source'] = 'MediaMind'
        self.creative_details['second_external_id'] = '19'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_url_with_255_chars(self):
        self.pages.detailed_edit_creatives.page_should_contain('http://' + self.creative_details['advertiser_url'])

    @test_case()
    def assert_additional_url_with_255_chars(self):
        self.pages.detailed_edit_creatives.page_should_contain('http://' + self.creative_details['first_url'])

    @test_case()
    def creatives_with_valid_details(self):
        self.working_of_detailed_edit_link()
        payload = self.pages.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = self.dx_constant.creative_name + payload
        self.creative_details['concept'] = self.dx_constant.creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Italian'
        self.creative_details['first_source'] = 'WURFL'
        self.creative_details['first_external_id'] = '19'
        self.creative_details['second_source'] = 'SalesForce'
        self.creative_details['second_external_id'] = '19'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_salesforce_external_id(self):
        self.pages.detailed_edit_creatives.page_should_contain('SalesForce')

    @test_case()
    def creatives_with_validation_of_external_ids(self):
        self.working_of_detailed_edit_link()
        payload = self.pages.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = self.dx_constant.creative_name + payload
        self.creative_details['concept'] = self.dx_constant.creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Polish'
        self.creative_details['first_source'] = 'RMX'
        self.creative_details['first_external_id'] = '1903'
        self.creative_details['second_source'] = 'Facebook'
        self.creative_details['second_external_id'] = 'mshskn'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_external_ids_with_numbers(self):
        for content in ['RMX', '1903']:
            self.pages.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def assert_external_ids_with_chars(self):
        for content in ['Facebook', 'mshskn']:
            self.pages.detailed_edit_creatives.page_should_contain(content)

    @test_case()
    def creatives_with_multiple_external_ids(self):
        self.working_of_detailed_edit_link()
        payload = self.pages.detailed_edit_creatives.get_random_string()
        self.creative_details = {}
        self.creative_details['name'] = self.dx_constant.creative_name + payload
        self.creative_details['concept'] = self.dx_constant.creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Portuguese'
        self.creative_details['first_source'] = 'BlueKai'
        self.creative_details['first_external_id'] = '19msh03'
        self.creative_details['second_source'] = 'MediaMind'
        self.creative_details['second_external_id'] = 'skn3919'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_click_tracking(self, click_tracking = True):
        status = self.pages.detailed_edit_creatives.get_attribute_value(self.pages.detailed_edit_creatives.click_tracking_status, 'innerHTML')
        if click_tracking:
            assert 'Enabled' in status
        else:
            assert 'Disabled' in status

    @test_case()
    def valid_tags_entered(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.creative_details['name'])

    def go_to_creative_edit(self):
        self.navigate_to_creative_list()
        self.pages.creative_list_page.go_to_link(self.creative_details['name'])
        self.pages.detailed_edit_creatives.wait_for_details_view()
        self.pages.detailed_edit_creatives.go_to_link('Edit')
        self.pages.creative_edit_page.wait_for_update_form()

    @test_case()
    def validation_while_updating_creatives(self):
        self.go_to_creative_edit()
        self.pages.creative_edit_page.input_creative_name('')
        self.pages.creative_edit_page.input_creative_concept('')
        self.pages.creative_edit_page.click_save_creatives()
        self.pages.creative_edit_page.wait_for_errors()

    @test_case()
    def update_details_with_limit_values(self):
        self.pages.creative_edit_page.select_size('120x90')
        self.creative_name = str(self.pages.detailed_edit_creatives.get_random_string(255)).lower()
        self.concept = str(self.pages.detailed_edit_creatives.get_random_string(200)).lower()
        self.pages.creative_edit_page.input_creative_name(self.creative_name)
        self.pages.creative_edit_page.input_creative_concept(self.concept)
        self.pages.creative_edit_page.select_second_source('DFA')
        self.pages.creative_edit_page.input_external_id('190391')
        self.pages.creative_edit_page.click_save_creatives()
        self.pages.detailed_edit_creatives.wait_for_details_view()

    @test_case()
    def assert_updated_name(self):
        self.pages.creative_edit_page.page_should_contain(self.creative_name)

    @test_case()
    def assert_updated_concept(self):
        self.pages.creative_edit_page.page_should_contain(self.concept)

    @test_case()
    def assert_updated_size(self):
        self.pages.creative_edit_page.page_should_contain('120x90')

    @test_case()
    def assert_updated_external_ids(self):
        for content in ['DFA', '190391']:
            self.pages.creative_edit_page.page_should_contain(content)

    @test_case()
    def creatives_with_spanish_lang_targeting(self):
        self.working_of_detailed_edit_link()
        payload = self.pages.detailed_edit_creatives.get_random_string()
        self.pages.detailed_edit_creatives.click_first_click_tracking()
        self.pages.detailed_edit_creatives.click_first_original_link()
        time.sleep(5)
        self.creative_details = {}
        self.creative_details['name'] = self.dx_constant.creative_name + payload
        self.creative_details['concept'] = self.dx_constant.creative_concept_name + payload
        self.creative_details['size'] = '300x250'
        self.creative_details['first_url'] = 'www.example.com'
        self.creative_details['lang'] = 'Spanish'
        self.creative_details['first_source'] = 'BlueKai'
        self.creative_details['first_external_id'] = '3bpd9dns'
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()

    @test_case()
    def assert_click_tracking_disabled(self):
        self.assert_click_tracking(False)

    @test_case()
    def update_creatives_with_special_chars(self):
        self.go_to_creative_edit()
        payload = self.pages.detailed_edit_creatives.get_random_string(5) + self.dx_constant.special_char
        self.creative_name = self.dx_constant.creative_name + payload
        self.concept = self.dx_constant.creative_concept_name + payload
        self.pages.creative_edit_page.click_add_external_ids()
        time.sleep(5)
        self.pages.creative_edit_page.select_second_source('WURFL')
        self.pages.creative_edit_page.input_second_external_id('b1p9d3')
        self.pages.creative_edit_page.input_creative_name(self.creative_name)
        self.pages.creative_edit_page.input_creative_concept(self.concept)
        self.pages.creative_edit_page.click_save_creatives()
        self.pages.creative_edit_page.click_save_creatives()
        self.pages.detailed_edit_creatives.wait_for_details_view()

    @test_case()
    def assert_updated_multiple_external_ids(self):
        for content in ['BlueKai', '3bpd9dns', 'WURFL', 'b1p9d3']:
            self.pages.creative_edit_page.page_should_contain(content)

    @test_case()
    def creatives_with_vendors(self):
        self.working_of_detailed_edit_link()
        payload = self.pages.detailed_edit_creatives.get_random_string()
        self.creative_details= {}
        self.creative_details['name'] = self.dx_constant.creative_name + payload
        self.creative_details['concept'] = self.dx_constant.creative_concept_name + payload
        self.pages.detailed_edit_creatives.click_add_first_vendor()
        time.sleep(3)
        self.pages.detailed_edit_creatives.select_first_vendor('DFA')
        self.pages.detailed_edit_creatives.click_add_first_vendor()
        time.sleep(3)
        self.pages.detailed_edit_creatives.select_first_vendor('OpenX')
        self.fill_creative_details()
        self.working_of_save_creative()
        self.go_to_show_creative()
        for vendors in ['DFA', 'OpenX']:
            self.pages.detailed_edit_creatives.page_should_contain(vendors)

    @test_case()
    def go_to_bulk_upload_creative_page(self):
        self.navigate_to_creative_list()
        self.pages.creative_list_page.click_new_creatives()
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.pages.bulk_edit_creative_page.click_bulk_upload_new_creative()
        self.pages.bulk_upload_new_creative.accept_alert()
        self.pages.bulk_upload_new_creative.wait_for_bulk_upload_creatives()

    @test_case()
    def working_of_bulk_upload_creative_button(self):
        self.go_to_bulk_upload_creative_page()
        self.pages.bulk_upload_new_creative.page_should_contain('Upload creatives for ' + self.dx_constant.advertiser_name)

    @test_case()
    def verify_bulk_upload_creatives_page(self):
        for content in self.pages.bulk_upload_new_creative.page_contents:
            assert self.pages.bulk_upload_new_creative.is_element_present(getattr(self.pages.bulk_upload_new_creative, content))

    @test_case()
    def verify_upload_assets_link(self):
        self.pages.bulk_upload_new_creative.click_use_assets_link()
        self.pages.upload_assets_page.wait_till_visible(self.pages.upload_assets_page.upload_assets_button)
        self.pages.upload_assets_page.page_should_contain('Generating creatives for ' + self.dx_constant.advertiser_name)

    @test_case()
    def verify_set_up_creatives_link(self):
        self.go_to_bulk_upload_creative_page()
        self.pages.bulk_upload_new_creative.click_setup_creatives_link()
        self.pages.bulk_edit_creative_page.wait_for_creative_forms()
        self.pages.bulk_edit_creative_page.page_should_contain('Set Up Creatives')

    @test_case()
    def upload_creative_file(self, filename, is_flash = None):
        filepath = '/../../../data/bulk_upload_creative_files/' + filename
        self.pages.bulk_upload_new_creative.click_upload(os.path.dirname(__file__) + filepath)
        self.pages.bulk_upload_new_creative.input_concept('Creative-Concept')
        if is_flash:
            self.pages.bulk_upload_new_creative.select_is_flash(is_flash)
        self.pages.bulk_upload_new_creative.click_submit()

    @test_case()
    def file_not_uploaded_without_creative_attributes(self):
        self.go_to_bulk_upload_creative_page()
        self.upload_creative_file('mock_creative_data.xls')
        self.pages.bulk_upload_new_creative.wait_till_visible(self.pages.bulk_upload_new_creative.errors)
        self.pages.bulk_upload_new_creative.page_should_contain('Please select Flash or Flashless')

    @test_case()
    def upload_invalid_file(self):
        self.upload_creative_file('creative_tags.txt')
        time.sleep(5)
        self.pages.bulk_upload_new_creative.page_should_contain('No creatives could be parsed from upload.')

    @test_case()
    def assert_details(self, attribute, element):
        assert attribute == self.pages.detailed_edit_creatives.get_dropdown_selected_value(getattr(self.pages.detailed_edit_creatives, element))

    @test_case()
    def bulk_upload_creatives_file(self, filename, is_flash, attribute, element):
        self.go_to_bulk_upload_creative_page()
        self.upload_creative_file(filename, is_flash)
        self.go_to_detailed_edit()
        self.assert_details(attribute, element)

    @test_case()
    def file_upload_with_flash(self):
        self.bulk_upload_creatives_file('mock_creative_data.xls', 'Flash', 'Flash', 'first_is_flash')

    @test_case()
    def dfa_tagsheet_with_flash(self):
        self.pages.detailed_edit_creatives.input_first_creative_name(self.dx_constant.creative_name + self.pages.detailed_edit_creatives.get_random_string())
        self.working_of_save_creative()

    @test_case()
    def file_upload_with_flashless(self):
        self.bulk_upload_creatives_file('test_creative_data.xls', 'Flashless', 'Flashless', 'first_is_flash')

    @test_case()
    def verify_uploaded_creative_concept(self):
        assert 'Creative-Concept' == self.pages.detailed_edit_creatives.get_attribute_value(self.pages.detailed_edit_creatives.first_concept, 'value')
        self.pages.detailed_edit_creatives.click_second_creative()
        time.sleep(5)
        assert 'Creative-Concept' == self.pages.detailed_edit_creatives.get_attribute_value(self.pages.detailed_edit_creatives.second_concept, 'value')

    @test_case()
    def verify_iframe_creative_type(self):
        self.pages.detailed_edit_creatives.click_first_creative()
        self.assert_details('iFrame', 'first_tag_type')

    @test_case()
    def dfa_tagsheet_with_flashless(self):
        payload = self.pages.detailed_edit_creatives.get_random_string()
        self.pages.detailed_edit_creatives.input_first_creative_name('test-creative-1' + payload)
        self.pages.detailed_edit_creatives.click_second_creative()
        time.sleep(5)
        self.pages.detailed_edit_creatives.input_second_creative_name('test-creative-2' + payload)
        self.pages.detailed_edit_creatives.click_first_creative()
        self.working_of_save_creative()

    @test_case()
    def dfa_tagsheet_uploaded_properly(self):
        self.pages.detailed_edit_creatives.page_should_contain(self.pages.detailed_edit_creatives.success_message)

    @test_case()
    def javascript_file_upload(self):
        self.bulk_upload_creatives_file('js_creative.xls', 'Flash', 'Javascript', 'first_tag_type')

    @test_case()
    def vast_creatives_uploaded_with_flash(self):
        self.bulk_upload_creatives_file('mock_vast_creative_data.xml', 'Flash', 'Flash', 'first_is_flash')

    @test_case()
    def verify_vast_creative_type(self):
        self.assert_details('VAST 2.0.1', 'first_tag_type')

    @test_case()
    def vast_creatives_uploaded_properly(self):
        self.pages.detailed_edit_creatives.input_first_creative_name(self.dx_constant.creative_name + self.pages.detailed_edit_creatives.get_random_string())
        self.pages.detailed_edit_creatives.input_first_concept(self.dx_constant.creative_concept_name)
        self.working_of_save_creative()

    @test_case()
    def vast_creatives_uploaded_with_flashless(self):
        self.bulk_upload_creatives_file('mock_vast_creative_data.xml', 'Flashless', 'Flashless', 'first_is_flash')
        self.vast_creatives_uploaded_properly()

    @test_case()
    def image_creative_file_upload(self):
        self.bulk_upload_creatives_file('image_creative.xls', 'Flash', 'Image', 'first_tag_type')
