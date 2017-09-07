from base.dx import Dx

class MediaPlanShowPage(Dx):

    def click_on_media_plans_and_campaigns_link(self):
        self.click_element(self.media_plans_and_campaigns_link)

    def click_on_edit_media_plan_button(self):
        self.click_element(self.edit_media_plan_button)
