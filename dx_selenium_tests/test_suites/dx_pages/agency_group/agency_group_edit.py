from new_agency_group import NewAgencyGroup
import time

class AgencyGroupEdit(NewAgencyGroup):
    def sort_segment_name(self):
        self.click_element(self.segment_name)

    def sort_external_id(self):
        self.click_element(self.external_id)

    def sort_cost(self):
        self.click_element(self.cost)

    def sort_price(self):
        self.click_element(self.price)

    def sort_inherited(self):
        self.click_element(self.inherited)

    def click_on_facebook_rtb_edit_icon(self):
        self.click_element(self.facebook_rtb_edit_icon)

    def click_on_own_facebook_seat_radio_button(self):
        self.click_element(self.own_facebook_seat_radio_button)

    def enter_bussiness_id(self, bussiness_id):
        self.clear_and_send_value(bussiness_id, self.bussiness_id_textbox)

    def enter_access_token(self, access_token):
        self.clear_and_send_value(access_token, self.access_token_textbox)

    def click_on_authenticate_button(self):
        self.click_element(self.facebook_authenticate_button)
        time.sleep(3)

    def click_on_facebook_authentication_save_button(self):
        self.click_element(self.facebook_authentication_save_button)

    def click_on_save_agency_group_button(self):
        self.click_element(self.submit_button)

    def click_facebook_popup_close_button(self):
        self.click_element(self.facebook_popup_close_button)

    def click_on_cancel_button(self):
        self.click_element(self.cancel_button)
