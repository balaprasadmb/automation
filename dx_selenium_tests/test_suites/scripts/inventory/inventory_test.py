from dx_test.dx_test import DXTest
from lib.gui_tests import test_case
import time
from lib.dx_date import DXDate
from selenium.webdriver.common.keys import Keys

class InventoryTest(DXTest):

    @test_case()
    def login_as_campaign_manager(self):
        self.setup(self.dx_constant.user_by_role['campaign_manager'])

    def click_inventory_tab(self):
        self.pages.search_page.click_inventory_link()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.guaranteed_inventory_list_table)

    @test_case()
    def guaranteed_inventory_list_page_contents(self):
        for page_contents in self.pages.inventory_list_page.guaranteed_inventory_list_page_contents:
            self.pages.inventory_list_page.page_should_contain(page_contents)
        for elements in self.pages.inventory_list_page.guaranteed_inventory_list_page_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, elements))
    
    @test_case()
    def verify_guaranteed_inventory_list_page_contents(self):
        self.login_as_campaign_manager()
        self.click_inventory_tab()
        self.guaranteed_inventory_list_page_contents()

    @test_case()
    def functionality_of_advertiser_dropdown(self):
        self.pages.inventory_list_page.click_on_organization_dropdown()
        self.pages.inventory_list_page.fill_organization_text_box(self.dx_constant.advertiser_name)
        self.pages.inventory_list_page.fill_field(self.pages.inventory_list_page.advertiser_input, Keys.ENTER)
        time.sleep(5)

    @test_case()
    def creation_of_guaranteed_inventory(self, media_type = 'Online'):
        inventory_media_type =  self.dx_constant.inventory_names_with_media_type
        self.click_inventory_tab()
        self.pages.inventory_list_page.click_on_new_guaranteed_media_button()
        self.inventory_name = inventory_media_type[media_type] + self.pages.guaranteed_inventory_edit_page.get_random_string(6)
        self.pages.guaranteed_inventory_edit_page.wait_till_visible(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_form)
        functions_dict = {'enter_guaranteed_inventory_publisher_name': self.inventory_name, 'enter_guaranteed_inventory_placement_name': self.inventory_name,
                            'click_on_guaranteed_inventory_available_checkbox': '', 'click_on_guaranteed_inventory_secure_checkbox': '',
                            'select_guaranteed_inventory_media_type': media_type}
        for key, value in functions_dict.iteritems():
            if value:
                getattr(self.pages.guaranteed_inventory_edit_page, key)(value)
            else:
                getattr(self.pages.guaranteed_inventory_edit_page, key)()
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_save_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.guaranteed_inventory_list_table)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.guaranteed_inventory_success_message.format(self.inventory_name))

    @test_case()
    def creation_of_mobile_guaranteed_inventory(self):
        self.creation_of_guaranteed_inventory('Mobile')

    @test_case()
    def creation_of_video_guaranteed_inventory(self):
        self.creation_of_guaranteed_inventory('Video')

    @test_case()
    def guaranteed_inventory_gear_icon_contents(self):
        self.pages.inventory_list_page.click_on_guaranteed_inventory_gear_icon()
        for elements in self.pages.inventory_list_page.guaranteed_inventory_gear_icon_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, elements))

    @test_case()
    def guaranteed_inventory_functionality_of_edit_link(self):
        self.pages.inventory_list_page.click_on_guaranteed_inventory_edit_link()
        self.pages.guaranteed_inventory_edit_page.wait_till_visible(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_save_button)
        self.pages.guaranteed_inventory_edit_page.page_should_contain(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_edit_page_title)

    @test_case()
    def guaranteed_inventory_publisher_name_textbox_max_limit(self):
        assert self.pages.guaranteed_inventory_edit_page.get_attribute_value(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_publisher_name, 'size') == '255'

    @test_case()
    def guaranteed_inventory_placement_name_textbox_max_limit(self):
        assert self.pages.guaranteed_inventory_edit_page.get_attribute_value(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_placement_name, 'size') == '255'

    @test_case()
    def guaranteed_inventory_update_functionality(self):
        self.updated_inventory_name = self.dx_constant.updated_gm_inventory_name + self.pages.guaranteed_inventory_edit_page.get_random_string(6)
        update_dict = {'enter_guaranteed_inventory_publisher_name':self.updated_inventory_name, 'enter_guaranteed_inventory_placement_name':self.updated_inventory_name,
                       'click_on_guaranteed_inventory_available_checkbox':'', 'click_on_guaranteed_inventory_secure_checkbox':'', 'select_guaranteed_inventory_media_type': 'Mobile'}
        for key, value in update_dict.iteritems():
            if value:
                getattr(self.pages.guaranteed_inventory_edit_page, key)(value)
            else:
                getattr(self.pages.guaranteed_inventory_edit_page, key)()                
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_save_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.guaranteed_inventory_list_table)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.guaranteed_inventory_update_message.format(self.updated_inventory_name))

    @test_case()
    def guaranteed_inventory_functionality_of_publisher_or_placement_name_link(self):
        self.click_inventory_tab()
        self.pages.inventory_list_page.click_on_guaranteed_inventory_publisher_name_link()
        self.guaranteed_inventory_functionality_of_placement_name_link_helper()
        self.click_inventory_tab()
        self.pages.inventory_list_page.click_on_guaranteed_inventory_placement_name_link()
        self.guaranteed_inventory_functionality_of_placement_name_link_helper()

    def guaranteed_inventory_functionality_of_placement_name_link_helper(self):
        self.pages.guaranteed_inventory_show_page.wait_till_visible(self.pages.guaranteed_inventory_show_page.edit_guaranteed_media_button)
        for page_contents in self.pages.guaranteed_inventory_show_page.guaranteed_inventory_show_page_contents:
            self.pages.guaranteed_inventory_show_page.page_should_contain(page_contents)
        self.pages.guaranteed_inventory_show_page.page_should_not_contain("Price")
        for elements in self.pages.guaranteed_inventory_show_page.guaranteed_inventory_show_page_elements:
            assert self.pages.guaranteed_inventory_show_page.is_element_present(getattr(self.pages.guaranteed_inventory_show_page, elements))

    @test_case()
    def functionality_of_new_guaranteed_media_button(self):
        self.click_inventory_tab()
        self.pages.inventory_list_page.click_on_new_guaranteed_media_button()
        self.pages.guaranteed_inventory_edit_page.wait_till_visible(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_form)
        self.pages.guaranteed_inventory_edit_page.page_should_contain(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_create_page_title)

    @test_case()
    def guaranteed_inventory_click_on_budget_section(self):
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_budget_section_header()
        for elements in self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_budget_section_elements:
            assert self.pages.guaranteed_inventory_edit_page.is_element_present(getattr(self.pages.guaranteed_inventory_edit_page, elements))
        
    @test_case()
    def guaranteed_inventory_edit_page_contents(self):
        for page_contents in self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_edit_page_contents:
            self.pages.guaranteed_inventory_edit_page.page_should_contain(page_contents)
        self.pages.guaranteed_inventory_edit_page.page_should_not_contain("Price")
        for elements in self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_edit_page_elements:
            assert self.pages.guaranteed_inventory_edit_page.is_element_present(getattr(self.pages.guaranteed_inventory_edit_page, elements))

    @test_case()
    def guaranteed_inventory_tag_section_for_linear_video_media_type(self):
        self.pages.guaranteed_inventory_edit_page.select_guaranteed_inventory_media_type('Video')
        self.pages.guaranteed_inventory_edit_page.page_should_contain('Maximum Duration')
        self.pages.guaranteed_inventory_edit_page.check_dropdown_options(self.pages.guaranteed_inventory_edit_page.maximum_duration_dropdown,
                                                                         self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_tag_size_dropdown01)

    @test_case()
    def guaranteed_inventory_add_another_size_button_functionality(self):
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_add_another_size_button()
        for elements in self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_another_size_element:
            assert self.pages.guaranteed_inventory_edit_page.is_element_present(getattr(self.pages.guaranteed_inventory_edit_page, elements))
        
    @test_case()
    def guaranteed_inventory_functionality_of_none_assigned_link(self):
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_none_assigned_link()
        self.pages.guaranteed_inventory_edit_page.wait_till_visible(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_creative_popup_assign_creative_button)
        self.pages.guaranteed_inventory_edit_page.page_should_contain('Assign Creative')

    @test_case()
    def guaranteed_inventory_assign_creative_popup_contents(self):
        for elements in self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_assign_creative_popup_elements:
            assert self.pages.guaranteed_inventory_edit_page.is_element_present(getattr(self.pages.guaranteed_inventory_edit_page, elements))

    @test_case()
    def guaranteed_inventory_functionality_of_assign_creative_popup_close_button(self):
        self.pages.guaranteed_inventory_edit_page.click_on_close_button_from_assign_creative_popup()
        assert not self.pages.guaranteed_inventory_edit_page.find_element(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_creative_popup_assign_creative_button).is_displayed()

    @test_case()
    def guaranteed_inventory_functionality_of_creative_size_remove_button(self):
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_remove_creative_size_button()
        assert not self.pages.guaranteed_inventory_edit_page.is_element_present(self.pages.guaranteed_inventory_edit_page.guaranteed_inventory_not_assigned_link01)

    @test_case()
    def guaranteed_inventory_functionality_of_cancel_button(self):
        self.pages.guaranteed_inventory_edit_page.click_on_guaranteed_inventory_cancel_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.guaranteed_inventory_list_table)
        self.guaranteed_inventory_list_page_contents()

    @test_case()
    def deal_tab_access_to_permission_user(self):
        self.pages.inventory_list_page.is_element_present(self.pages.inventory_list_page.deal_inventory_tab)

    @test_case()
    def deal_inventory_list_page_contents(self):
        self.pages.inventory_list_page.click_on_deals_tab()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.deal_inventory_list_table)
        for page_contents in self.pages.inventory_list_page.deals_inventory_list_page_contents:
            self.pages.inventory_list_page.page_should_contain(page_contents)
        for elements in self.pages.inventory_list_page.deals_inventory_list_page_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, elements))

    @test_case()
    def creation_of_deal_inventory(self):
        self.pages.inventory_list_page.click_on_new_deal_button()
        self.pages.deal_inventory_edit_page.wait_till_visible(self.pages.deal_inventory_edit_page.deal_inventory_form)
        self.deal_inventory_name = 'test-deal-' + self.pages.deal_inventory_edit_page.get_random_string(6)
        self.pages.deal_inventory_edit_page.enter_deal_name(self.deal_inventory_name)
        self.pages.deal_inventory_edit_page.select_deal_inventory_exchange('Admeta')
        self.pages.deal_inventory_edit_page.enter_deal_id(self.pages.deal_inventory_edit_page.get_random_string())
        self.pages.deal_inventory_edit_page.select_deal_type(1)
        self.pages.deal_inventory_edit_page.enter_cost_cpm_value(self.dx_constant.deal_cpm)
        self.pages.deal_inventory_edit_page.enter_start_date(DXDate().todays_date())
        self.pages.deal_inventory_edit_page.enter_deal_description(self.dx_constant.deal_description)
        self.pages.deal_inventory_edit_page.enter_deal_permissioned_advertiser_name(self.dx_constant.advertiser_name)
        self.pages.deal_inventory_edit_page.fill_field(self.pages.deal_inventory_edit_page.deal_permissioned_advertiser_name, Keys.ENTER)
        self.pages.deal_inventory_edit_page.enter_end_date(DXDate().last_date_of_current_month())
        self.pages.deal_inventory_edit_page.click_on_save_deal_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.deal_inventory_list_table)
        self.pages.inventory_list_page.page_should_contain(self.pages.inventory_list_page.deal_success_message.format(self.deal_inventory_name))

    @test_case()
    def deal_inventory_gear_icon_contents(self):
        self.pages.inventory_list_page.click_on_deal_inventory_gear_icon()
        assert self.pages.inventory_list_page.is_element_present(self.pages.inventory_list_page.deal_inventory_edit_link)

    @test_case()
    def functionality_of_new_deal_button(self):
        self.pages.inventory_list_page.click_on_new_deal_button()
        self.pages.deal_inventory_edit_page.wait_till_visible(self.pages.deal_inventory_edit_page.deal_inventory_form)
        self.pages.deal_inventory_edit_page.page_should_contain(self.pages.deal_inventory_edit_page.deal_create_page_title)

    @test_case()
    def deal_inventory_edit_page_contents(self):
        for page_contents in self.pages.deal_inventory_edit_page.deal_inventory_edit_page_contents:
            self.pages.deal_inventory_edit_page.page_should_contain(page_contents)
        for elements in self.pages.deal_inventory_edit_page.deal_inventory_edit_page_elements:
            assert self.pages.deal_inventory_edit_page.is_element_present(getattr(self.pages.deal_inventory_edit_page, elements))

    @test_case()
    def deal_inventory_functionality_of_cancel_button(self):
        self.pages.deal_inventory_edit_page.click_on_deal_cancel_button()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.deal_inventory_list_table)
        for page_contents in self.pages.inventory_list_page.deals_inventory_list_page_contents:
            self.pages.inventory_list_page.page_should_contain(page_contents)
        for elements in self.pages.inventory_list_page.deals_inventory_list_page_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, elements))

    @test_case()
    def custom_inventory_tab_access_to_permission_user(self):
        self.pages.inventory_list_page.is_element_present(self.pages.inventory_list_page.custom_inventory_tab)

    @test_case()
    def custom_inventory_list_page_contents(self):
        self.pages.inventory_list_page.click_on_custom_inventory_tab()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.custom_inventory_table)
        for page_contents in self.pages.inventory_list_page.custom_inventory_list_page_contents:
            self.pages.inventory_list_page.page_should_contain(page_contents)
        for elements in self.pages.inventory_list_page.custom_inventory_list_page_elements:
            assert self.pages.inventory_list_page.is_element_present(getattr(self.pages.inventory_list_page, elements))

    @test_case()
    def custom_inventory_gear_icon_contents(self):
        self.pages.inventory_list_page.click_on_custom_inventory_gear_icon()
        assert self.pages.inventory_list_page.is_element_present(self.pages.inventory_list_page.custom_inventory_edit_link)

    @test_case()
    def custom_inventory_export_tag_link_not_available(self):
        assert not self.pages.inventory_list_page.is_element_present(self.pages.inventory_list_page.custom_inventory_export_tag_link)

    @test_case()
    def custom_inventory_functionality_of_edit_link(self):
        self.pages.inventory_list_page.click_on_custom_inventory_edit_link()
        self.pages.custom_inventory_edit_page.wait_till_visible(self.pages.custom_inventory_edit_page.save_custom_inventory_button)
        self.pages.custom_inventory_edit_page.page_should_contain(self.pages.custom_inventory_edit_page.custom_inventory_edit_page_title)

    @test_case()
    def custom_inventory_functionality_of_publisher_or_placement_name_link(self):
        self.click_inventory_tab()
        self.pages.inventory_list_page.click_on_custom_inventory_tab()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.custom_inventory_table)
        self.pages.inventory_list_page.click_on_custom_inventory_publisher_name_link()
        self.custom_inventory_functionality_of_placement_name_link_helper()
        self.pages.inventory_list_page.click_on_custom_inventory_placement_name_link()
        self.custom_inventory_functionality_of_placement_name_link_helper()

    @test_case()
    def custom_inventory_functionality_of_placement_name_link_helper(self):
        self.pages.custom_inventory_show_page.wait_till_visible(self.pages.custom_inventory_show_page.edit_custom_inventory_button)
        for page_contents in self.pages.custom_inventory_show_page.custom_inventory_show_page_contents:
            self.pages.custom_inventory_show_page.page_should_contain(page_contents)
        for elements in self.pages.custom_inventory_show_page.custom_inventory_show_page_elements:
            assert self.pages.custom_inventory_show_page.is_element_present(getattr(self.pages.custom_inventory_show_page, elements))
        self.pages.custom_inventory_show_page.click_on_custom_inventory_link()
        self.pages.inventory_list_page.wait_till_visible(self.pages.inventory_list_page.custom_inventory_table)

    @test_case()
    def functionality_of_new_custom_inventory_button(self):
        self.pages.inventory_list_page.click_on_new_custom_inventory_button()
        self.pages.custom_inventory_edit_page.wait_till_visible(self.pages.custom_inventory_edit_page.save_custom_inventory_button)
        self.pages.custom_inventory_edit_page.page_should_contain(self.pages.custom_inventory_edit_page.custom_inventory_create_page_title)
