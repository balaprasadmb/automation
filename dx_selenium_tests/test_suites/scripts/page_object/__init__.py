from login.login import Login
from login.sso_login_page import SsoLoginPage

from search.search import SearchPage

from admin_page import AdminPage

from activity_list_page import ActivityListPage
from activity_create_new_page import ActivityCreateNewPage
from activity_edit_page import ActivityEditPage
from activity_show_page import ActivityShowPage

from agency_group.agency_group_details import AgencyGroupDetails
from agency_group.new_agency_group import NewAgencyGroup
from agency_group.agency_group_list import AgencyGroupList
from agency_group.agency_group_edit import AgencyGroupEdit

from agencies.agency_details import AgencyDetailsPage
from agencies.new_agency import NewAgency
from agencies.agency_edit import AgencyEdit
from agencies.agencies_list_page import AgenciesListPage

from new_advertiser import NewAdvertiser
from advertiser_list import AdvertiserListPage
from edit_advertiser import EditAdvertiser
from advertiser_details import AdvertiserDetailsPage

from creatives.new_creatives import NewCreatives
from creatives.detailed_edit_creatives import DetailedEditCreatives
from creatives.bulk_upload_creatives import BulkUploadCreatives
from creatives.creative_list_page import CreativeList
from creatives.bulk_edit_creatives import BulkEditCreatives
from creatives.bulk_upload_assets import BulkUploadAssets
from creative_show_page import CreativeShowPage
from edit_creatives import EditCreatives
from generate_creative_page import GenerateCreativePage
from asset_edit_page import AssetEditPage

from audiences_segments.audiences_list_page import AudiencesListPage
from audiences_segments.create_audience import CreateAudience
from audiences_segments.create_segment import CreateSegment
from audiences_segments.audiences_show_page import AudiencesShowPage
from audiences_segments.segment_show_page import SegmentShowPage

from custom_inventory_edit_page import CustomInventoryEditPage
from custom_inventory_show_page import CustomInventoryShowPage
from deal_inventory_edit_page import DealInventoryEditPage
from deal_inventory_show_page import DealInventoryShowPage
from inventory_list_page import InventoryListPage
from guaranteed_inventory_edit_page import GuaranteedInventoryEditPage
from guaranteed_inventory_show_page import GuaranteedInventoryShowPage

from new_system_message import NewSystemMessage
from system_notices_list import SystemNoticesList
from edit_system_notices import EditSystemNotices

from users.user_list_page import UserListPage
from users.user_edit_page import UserEditPage
from users.user_show_page import UserShowPage
from users.new_user import NewUser

from login_slides_list_page import LoginSlidesListPage
from login_slides_edit_page import LoginSlidesEditPage
from login_slides_show_page import LoginSlidesShowPage

from campaigns.new_campaign import NewCampaign
from campaigns.create_campaign import CreateCampaign
from campaigns.edit_campaign import EditCampaign
from campaigns.campaign_show_page import CampaignShowPage
from campaigns.campaign_list import CampaignList
from campaigns.campaign_dashboard_page import CampaignDashboardPage
from campaigns.domain_list_management_page import DomainListManagementPage
from campaigns.creative_assign_dashboard_page import CreativeAssignDashboardPage
from campaigns.create_media_plan import CreateMediaPlan
from campaigns.edit_media_plan import EditMediaPlan
from campaigns.media_plan_show_page import MediaPlanShowPage

from flights.flight_budget_scheduling import FBSPage
from flights.flights_show_page import FlightsShowPage
from flights.create_flight import CreateFlight
from flights.upload_flights import UploadFlights
from flights.edit_flight import EditFlight

from bi_report_list_page import BiReportListPage
from bi_report_create_page import BiReportCreatePage
from bi_reports_pack_create_page import BiReportsPackCreatePage

from ci_datasets_list_page import CiDatasetsListPage
from create_new_dataset_page import CreateNewDatasetPage

from product_features_list_page import ProductFeaturesListPage
from product_feature_edit_page import ProductFeatureEditPage

class PageObjects(object):

    """ Provides access to all page objects"""

    def __init__(self, driver):
        #activity page objects
        self.activity_list_page = ActivityListPage(driver)
        self.activity_create_new_page = ActivityCreateNewPage(driver)
        self.activity_edit_page = ActivityEditPage(driver)
        self.activity_show_page = ActivityShowPage(driver)
        #search page objects
        self.search_page = SearchPage(driver)
        #login page objects
        self.login_page = Login(driver)
        self.sso_login_page = SsoLoginPage(driver)
        #admin page objects
        self.admin_page = AdminPage(driver)
        #agency group page objects
        self.new_agency_group_page = NewAgencyGroup(driver)
        self.agency_group_details_page = AgencyGroupDetails(driver)
        self.agency_group_list_page = AgencyGroupList(driver)
        self.agency_group_edit_page = AgencyGroupEdit(driver)
        #agency page objects
        self.agency_details_page = AgencyDetailsPage(driver)
        self.new_agency_page = NewAgency(driver)
        self.agency_list_page = AgenciesListPage(driver)
        self.agency_edit_page = AgencyEdit(driver)
        #advertiser page objects
        self.new_advertiser_page = NewAdvertiser(driver)
        self.advertiser_list_page = AdvertiserListPage(driver)
        self.advertiser_details_page = AdvertiserDetailsPage(driver)
        self.advertiser_edit_page = EditAdvertiser(driver)
        #creative page objects
        self.new_creative_page = NewCreatives(driver)
        self.detailed_edit_creatives = DetailedEditCreatives(driver)
        self.bulk_upload_new_creative = BulkUploadCreatives(driver)
        self.creative_list_page = CreativeList(driver)
        self.bulk_edit_creative_page = BulkEditCreatives(driver)
        self.upload_assets_page = BulkUploadAssets(driver)
        self.creative_show_page = CreativeShowPage(driver)
        self.creative_edit_page = EditCreatives(driver)
        self.generate_creative_page = GenerateCreativePage(driver)
        self.asset_edit_page = AssetEditPage(driver)
        #audiences and segments page objects
        self.audience_segment_list_page = AudiencesListPage(driver)
        self.audience_create_page = CreateAudience(driver)
        self.segment_create_page = CreateSegment(driver)
        self.audience_show_page = AudiencesShowPage(driver)
        self.segment_show_page = SegmentShowPage(driver)
        #user page objects
        self.user_list_page = UserListPage(driver)
        self.user_edit_page = UserEditPage(driver)
        self.user_show_page = UserShowPage(driver)
        self.new_user_page = NewUser(driver)
        #inventory page objects
        self.deal_inventory_edit_page = DealInventoryEditPage(driver)
        self.inventory_list_page = InventoryListPage(driver)
        self.guaranteed_inventory_edit_page = GuaranteedInventoryEditPage(driver)
        self.guaranteed_inventory_show_page = GuaranteedInventoryShowPage(driver)
        self.deal_inventory_show_page = DealInventoryShowPage(driver)
        self.custom_inventory_edit_page = CustomInventoryEditPage(driver)
        self.custom_inventory_show_page = CustomInventoryShowPage(driver)
        #system messages page objects
        self.new_system_message_page = NewSystemMessage(driver)
        self.edit_system_notices_page = EditSystemNotices(driver)
        self.system_notices_list_page = SystemNoticesList(driver)
        #login slides page object
        self.login_slides_list_page = LoginSlidesListPage(driver)
        self.login_slides_edit_page = LoginSlidesEditPage(driver)
        self.login_slides_show_page = LoginSlidesShowPage(driver)
        #campaign page objects
        self.new_campaign_pop_up = NewCampaign(driver)
        self.create_campaign_page = CreateCampaign(driver)
        self.campaign_edit_page = EditCampaign(driver)
        self.campaign_show_page = CampaignShowPage(driver)
        self.campaign_list_page = CampaignList(driver)
        self.campaign_dashboard_page = CampaignDashboardPage(driver)
        self.domain_list_management_page = DomainListManagementPage(driver)
        self.creative_assign_dashboard_page = CreativeAssignDashboardPage(driver)
        self.create_media_plan_page = CreateMediaPlan(driver)
        self.edit_media_plan_page = EditMediaPlan(driver)
        self.media_plan_show_page = MediaPlanShowPage(driver)
        #flight page objects
        self.flight_show_page = FlightsShowPage(driver)
        self.create_flight_page = CreateFlight(driver)
        self.flight_edit_page = EditFlight(driver)
        self.fbs_page = FBSPage(driver)
        self.upload_flights_page = UploadFlights(driver)
        #BI report page object
        self.bi_reports_list_page = BiReportListPage(driver)
        self.bi_report_create_page = BiReportCreatePage(driver)
        self.bi_report_pack_create_page = BiReportsPackCreatePage(driver)
        #CI Dataset objects
        self.ci_datasets_list_page = CiDatasetsListPage(driver)
        self.create_new_dataset_page = CreateNewDatasetPage(driver)
        #Product features objects
        self.product_feature_list_page = ProductFeaturesListPage(driver)
        self.product_feature_edit_page = ProductFeatureEditPage(driver)
