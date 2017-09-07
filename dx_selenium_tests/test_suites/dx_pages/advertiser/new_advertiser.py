import time
from selenium.webdriver.common.by import By
from base.dx import Dx
from configs.dx_constant import DXConstant


class NewAdvertiser(Dx):
    def fill_fields(self, attribute):
        self.type_organization_name(attribute["organization_name"])
        self.type_email(attribute["email"])
        self.type_contact_name(attribute["contact_name"])
        self.type_advertiser_domain(attribute["primary_domain"])
        self.check_select_all_currencies()
        self.click_new_add_on_cost_button()
        self.type_add_on_cost_name(attribute["add_on_cost_name"])
        self.type_add_on_cost_rate(attribute["add_on_cost_value"])
        self.upload_rate_card(attribute["rate_card"])
        self.click_create_advetiser_button()

    def select_agency_group(self, agency_group, method='label'):
        self.select_option(self.agency_group, agency_group, method)

    def select_agency(self, agency, method='label'):
        self.select_option(self.agency, agency, method)

    def type_organization_name(self, organization):
        self.clear_and_send_value(organization, self.organization_name)

    def type_advertiser_domain(self, domain):
        self.clear_and_send_value(domain, self.primary_domain)

    def click_create_advetiser_button(self):
        self.click_element(self.create_advertiser)

    def type_contact_name(self, contact_name):
        self.clear_and_send_value(contact_name, self.contact_name)

    def select_currency_from_listbox(self, currency='United States Dollar (USD)', method='label'):
        self.select_option(self.currency, currency, method)

    def check_select_all_currencies(self):
        self.click_element(self.select_all_currency)

    def select_currency_using_checkbox(self, currencies):
        currency_code_dict = DXConstant().agency_currency_code
        if type(currencies) is list:
            for currency in currencies:
                self.click_element((By.ID, 'agency_organization_attributes_currency_ids_{0}'.format(currency_code_dict[currency])))
        if type(currencies) is str:
            self.click_element((By.ID, 'agency_organization_attributes_currency_ids_{0}'.format(currency_code_dict[currencies])))

    def check_limit_one_impression_per_page_view(self):
        self.click_element(self.one_impression_per_page)

    def click_cogs_inherited_value_checkbox(self):
        self.click_element(self.cogs_inherited_checkbox)

    def click_margin_inherited_value_checkbox(self):
        self.click_element(self.margin_inherited_checkbox)

    def type_cogs_value(self, value):
        self.clear_and_send_value(value, self.cogs_textbox)

    def type_margin_value(self, value):
        self.clear_and_send_value(value, self.margin_textbox)

    def click_new_add_on_cost_button(self):
        self.click_element(self.new_add_on_cost)

    def type_add_on_cost_name(self, name):
        self.clear_and_send_value(name, self.get_last_element(self.add_on_cost_name))

    def type_add_on_cost_rate(self, rate):
        self.clear_and_send_value(rate, self.get_last_element(self.add_on_cost_value))

    def select_add_on_cost_fee_type(self, fee_type, method='label'):
        self.select_option(self.get_last_element(self.add_on_cost_fee_type), fee_type, method)

    def click_add_on_cost_billable_checkbox(self):
        self.get_last_element(self.add_on_cost_billable_checkbox).click()

    def click_marketlace_checkbox(self):
        self.get_last_element(self.add_on_cost_marketplace_checkbox).click()

    def click_dataxu_controlled_checkbox(self):
        self.get_last_element(self.add_on_cost_dataxu_controlled_checkbox).click()

    def click_add_on_cost_channel(self, channel, method='label'):
        self.select_option(self.get_last_element(self.add_on_cost_channel), channel, method)

    def remove_add_on_cost_functionality(self):
        self.get_last_element(self.remove_add_on_cost).click()

    def upload_rate_card(self, file_path):
        self.upload_file(file_path, self.rate_card)

    def click_inherit_licenses_checkbox(self):
        self.click_element(self.inherit_licensing_checkbox)

    def click_media_type_checkbox(self, media_type='Mobile'):
        self.click_element(self.online_media_type_checkbox[media_type.lower()].values())

    def select_all_inventory(self):
        self.click_element(self.select_all_inventories)

    def select_inventories(self, inventories):
        if type(inventories) is list:
            for inventory in inventories:
                self.click_element((By.CSS_SELECTOR, "input[data-inventory_supplier_name='{0}']".format(inventory)))
        if type(inventories) is str:
            self.click_element((By.CSS_SELECTOR, "input[data-inventory_supplier_name='{0}']".format(inventories)))

    def click_targeting_checkbox(self):
        self.click_element(self.geo_targeting_checkbox)

    def click_cost_model_type(self, cost_model):
        if cost_model == 'CPA':
            self.click_element(self.cost_model_type)

    def select_insights(self, insight='Frequency Impact Report'):
        insight_dict = {
            'Frequency Impact Report': 'frequency',
            'Consideration Period Report': 'consideration',
            'Retargeting Effectiveness Report': 'retargeting',
            'Index of Best Metrocodes': 'index'
        }
        while not self.find_element(self.insights[insight_dict[insight]].values()).is_selected():
            self.click_element(self.insights[insight_dict[insight]].values())

    def click_create_agency_button(self):
        self.click_element(self.submit_button)

    def click_cancel_button(self):
        self.click_element(self.cancel_button)

    def accept_add_on_cost_pop_up(self):
        if self.is_element_present(self.add_on_cost_modified_pop_up['pop_up'].values()):
            self.click_element(self.add_on_cost_modified_pop_up['accept'].values())

    def decline_add_on_cost_pop_up(self):
        if self.is_element_present(self.add_on_cost_modified_pop_up['pop_up'].values()):
            self.click_element(self.add_on_cost_modified_pop_up['cancel'].values())

    def click_seats_edit_icon(self):
        self.click_element(self.edit_configure_seat)

    def click_on_google_adx_seat_edit_icon(self):
        self.click_element(self.google_adx_seat_edit_icon)

    def click_seats_cancel_button(self):
        self.click_element(self.configure_seats_pop_up['cancel_button'].values())

    def click_seats_ok_button(self):
        self.click_element(self.configure_seats_pop_up['ok_button'].values())

    def type_seat_name(self, value):
        self.clear_and_send_value(value, self.configure_seats_pop_up['seat_name'].values())

    def type_seat_id(self, value):
        self.clear_and_send_value(value, self.configure_seats_pop_up['seat_id'].values())

    def click_seats_billable_checkbox(self):
        self.click_element(self.configure_seats_pop_up['seat_billable'].values())

    def add_seats(self):
        self.click_element(self.configure_seats_pop_up['add_seat'].values())

    def remove_seats(self):
        self.click_element(self.configure_seats_pop_up['remove_seat'].values())

    def click_seats_inherit_radio_button(self):
        self.click_element(self.configure_seats_pop_up['inherit_checkbox'].values())

    def click_seats_override_radio_button(self):
        self.click_element(self.configure_seats_pop_up['override_checkbox'].values())

    def select_offer_type(self, offer, method='label'):
        self.select_option(self.offer_type, offer, method)

    def select_platform_type(self, platform, method='label'):
        self.select_option(self.platform_type, platform, method)

    def click_high_precision_policy_checkbox(self):
        self.click_element(self.one_view_section['high_precision_policy_checkbox'].values())

    def click_broad_reach_policy_checkbox(self):
        self.click_element(self.one_view_section['broad_reach_policy_checkbox'].values())

    def click_lock_policy_checkbox(self):
        self.click_element(self.one_view_section['lock_policy_checkbox'].values())

    def click_on_oba_checkbox(self):
        self.click_element(self.oba_checkbox)

    def click_on_oba_popup_accept_button(self):
        self.click_element(self.oba_popup_accept_button)
