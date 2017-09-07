from new_advertiser import NewAdvertiser
import time


class EditAdvertiser(NewAdvertiser):
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

    def click_on_existing_acc_id_radio_button(self):
        self.click_element(self.existing_acc_id_radio_button)
        time.sleep(1)

    def enter_acc_id(self, account_id):
        self.clear_and_send_value(account_id, self.acc_id_textbox)

    def click_on_authenticate_button(self):
        self.click_element(self.authenticate_button)
        time.sleep(2)

    def click_on_facebook_authentication_save_button(self):
        self.click_element(self.facebook_authentication_save_button)

    def click_on_save_advertiser_button(self):
        self.click_element(self.save_advertiser_button)

    def click_facebook_popup_close_button(self):
        self.click_element(self.facebook_popup_close_button)

    def enter_facebook_page_id_textbox(self, facebook_page_id):
        self.clear_and_send_value(facebook_page_id, self.facebook_page_id_textbox)

    def click_facebook_add_page_button(self):
        self.click_element(self.facebook_add_page_button)

    def click_on_facebook_resync_link(self):
        self.click_element(self.facebook_resync_link)

    def click_on_cancel_button(self):
        self.click_element(self.cancel_button)
