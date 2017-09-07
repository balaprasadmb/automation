from base.dx import Dx

class CampaignDashboardPage(Dx):
    def click_on_reports_button(self):
        self.click_element(self.reports_button)

    def click_on_report_builder_link(self):
        self.click_element(self.report_builder_link)

    def click_on_report_audience_link(self):
        self.click_element(self.report_audience_link)

    def click_on_report_advanced_insights_link(self):
        self.click_element(self.report_advanced_insights_link)

    def click_on_report_intelligence_link(self):
        self.click_element(self.report_intelligence_link)

    def click_on_report_custom_query_link(self):
        self.click_element(self.report_custom_query_link)

    def click_on_flights_button(self):
        self.click_element(self.flights_button)

    def click_on_edit_flights_link(self):
        self.click_element(self.edit_flights_link)

    def click_on_assign_creatives_link(self):
        self.click_element(self.assign_creatives_link)

    def click_on_flight_creatives_link(self):
        self.click_element(self.flight_creatives_link)

    def click_on_flight_domains_link(self):
        self.click_element(self.flight_domains_link)

    def click_on_add_flights_link(self):
        self.click_element(self.add_flights_link)

    def click_on_bulk_upload_flights_link(self):
        self.click_element(self.bulk_upload_flights_link)

    def click_on_bulk_edit_via_csv_link(self):
        self.click_element(self.bulk_edit_via_csv_link)

    def click_on_export_flights_link(self):
        self.click_element(self.export_flights_link)

    def click_on_flight_domain_list_management_link(self):
        self.click_element(self.flight_domain_list_management_link)

    def click_on_campaign_button(self):
        self.click_element(self.campaign_button)

    def click_on_edit_campaign_link(self):
        self.click_element(self.edit_campaign_link)

    def click_on_campaign_domains_link(self):
        self.click_element(self.campaign_domains_link)

    def click_on_cruise_control_link(self):
        self.click_element(self.cruise_control_link)

    def click_on_campaign_domain_list_management_link(self):
        self.click_element(self.campaign_domain_list_management_link)
