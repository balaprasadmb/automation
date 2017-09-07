import random
import string
from dx_test_helper.dx_test_helper import DXTestHelper
from configs.dx_constant import DXConstant
from lib.dx_date import DXDate

class CampaignTestHelper(DXTestHelper):
    def get_campaign_with_distribution(self, campaign_attributes):
        random_string = ''.join(random.choice(string.lowercase + string.digits) for _ in range(8))
        return {
        'campaign_name': DXConstant().test_campaign_name + random_string,
        'start_date': DXDate().todays_date(),
        'end_date': DXDate().date_after_two_days(),
        'value': campaign_attributes['value_ten'],
        'budget': campaign_attributes['budget'],
        'cogs':  campaign_attributes['cogs'],
        'margin':  campaign_attributes['margin'],
        'objective':  campaign_attributes['objective_distribution'],
        'custom':  campaign_attributes['custom_value'],
        'tactics': campaign_attributes['custom_value'],
        'tactics_value':  DXConstant().tactics_name + random_string,
        'tactics_budget':  campaign_attributes['tactics_budget'],
        'aoc_custom':  DXConstant().activity_name + random_string,
        'aoc_rate': campaign_attributes['value_ten'],
        'true_val':  campaign_attributes['true_val'],
        'source':  campaign_attributes['first_source'],
        'source_value':  campaign_attributes['first_source_value'],
        'lang_target':  campaign_attributes['first_lang_target'],
        'geo_target':  campaign_attributes['first_geo_target'],
        'brand_safety_level':  campaign_attributes['brand_safety_four'],
        'brand_safety': campaign_attributes['brand_safety_four']
        }

    def set_campaign_attributes(self, campaign, new_campaign_attributes):
        campaign.campaign_attributes.update(new_campaign_attributes)
        campaign.campaign_attributes['cpa'] = new_campaign_attributes['value']
        campaign.campaign_attributes['cpm'] = new_campaign_attributes['value']
        campaign.campaign_attributes['icaps'] = new_campaign_attributes['value']
        campaign.campaign_attributes['aoc_name'] = new_campaign_attributes['custom']
        campaign.campaign_attributes['is_billable'] = new_campaign_attributes['true_val']
        campaign.campaign_attributes['is_marketpalce'] = new_campaign_attributes['true_val']
        return campaign

    def get_campaign_with_ctr(self, campaign_attributes):
        ctr_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        ctr_campaign_attributes['start_date'] = DXDate().date_before_three_days()
        ctr_campaign_attributes['end_date'] = DXDate().date_before_two_days()
        ctr_campaign_attributes['objective'] = campaign_attributes['objective_ctr']
        ctr_campaign_attributes['ctr_goal'] = campaign_attributes['ctr_goal']
        ctr_campaign_attributes['tactics_value'] = DXConstant().number_name + str(random.randint(1,10)) + str(random.randint(1,10))
        ctr_campaign_attributes['aoc_custom'] = DXConstant().number_name + str(random.randint(1,10)) + str(random.randint(1,10))
        ctr_campaign_attributes['source'] = campaign_attributes['sec_source']
        ctr_campaign_attributes['source_value'] = campaign_attributes['sec_source_value']
        ctr_campaign_attributes['lang_target'] = campaign_attributes['sec_lang_target']
        ctr_campaign_attributes['geo_target'] = campaign_attributes['sec_geo_target']
        return ctr_campaign_attributes

    def get_campaign_with_future_date(self, campaign_attributes):
        future_date_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        future_date_campaign_attributes['start_date'] = DXDate().date_after_two_days()
        future_date_campaign_attributes['end_date'] =  DXDate().last_date_of_current_month()
        future_date_campaign_attributes['tactic_value'] = DXConstant().special_char + str(random.randint(1,10))
        future_date_campaign_attributes['aoc_custom'] = DXConstant().number_name + str(random.randint(1,10)) + str(random.randint(1,10))
        future_date_campaign_attributes['source'] = campaign_attributes['third_source']
        future_date_campaign_attributes['source_value'] = campaign_attributes['third_source_value']
        return future_date_campaign_attributes

    def get_campaign_with_retargeting(self, campaign_attributes):
        campaign_with_retargeting = self.get_campaign_with_distribution(campaign_attributes)
        campaign_with_retargeting['end_date'] = DXDate().last_date_of_current_month()
        campaign_with_retargeting['tactics'] = campaign_attributes['retargeting_tactic']
        campaign_with_retargeting['aoc_custom'] = DXConstant().number_name + str(random.randint(1,10)) + str(random.randint(1,10))
        campaign_with_retargeting['source'] = campaign_attributes['four_source']
        campaign_with_retargeting['source_value'] = campaign_attributes['four_source_value']
        return campaign_with_retargeting

    def get_campaign_with_optimized(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_retargeting(campaign_attributes)
        new_campaign_attributes['tactics'] = campaign_attributes['optimized_tactics']
        new_campaign_attributes['source'] = campaign_attributes['six_source']
        return new_campaign_attributes

    def get_campaign_with_channel(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_optimized(campaign_attributes)
        new_campaign_attributes['tactics'] = campaign_attributes['channel_tactics']
        new_campaign_attributes['source'] = campaign_attributes['seven_source']
        new_campaign_attributes['source_value'] = campaign_attributes['seven_source_value']
        return new_campaign_attributes

    def get_campaign_with_ad_views(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['objective'] = campaign_attributes['objective_views']
        return new_campaign_attributes

    def get_campaign_max_limit(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        activity = 'test-activity-9'
        for i in range(1,25):
            activity += '0123456789'
        new_campaign_attributes['aoc_custom'] = activity
        new_campaign_attributes['brand_safety_level'] = None
        return new_campaign_attributes

    def fill_cpm_max_limit(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        cpm = DXConstant().number_name + '931'
        for i in range(1,50):
            cpm += '13579'
        new_campaign_attributes['aoc_rate'] = cpm
        new_campaign_attributes['brand_safety_level'] = None
        return new_campaign_attributes

    def fill_fields_with_tactics(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['tactics'] = 'Custom...'
        tactics = DXConstant().tactics_name + '19'
        for i in range(1,50):
            tactics += '13579'
        new_campaign_attributes['tactics_value'] = tactics
        new_campaign_attributes['brand_safety_level'] = None
        return new_campaign_attributes

    def fill_fields_with_facebook_campaign(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['source'] =  campaign_attributes['eight_source']
        new_campaign_attributes['source_value'] =  campaign_attributes['eight_source_value']
        new_campaign_attributes['brand_safety_level'] = None
        return new_campaign_attributes

    def fill_fields_with_brand_safety_one(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['source'] =  campaign_attributes['nine_source']
        new_campaign_attributes['source_value'] =  campaign_attributes['nine_source_value']
        new_campaign_attributes['brand_safety_level'] = '1'
        return new_campaign_attributes

    def get_campaign_with_objective_performance(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['objective'] = campaign_attributes['objective_performance']
        new_campaign_attributes['brand_safety_level'] =  None
        return new_campaign_attributes

    def get_campaign_with_blank_external_value(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['source_value'] = ''
        new_campaign_attributes['brand_safety_level'] =  None
        return new_campaign_attributes

    def get_campaign_with_brand_safety_three(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['brand_safety_level'] =  '3'
        return new_campaign_attributes

    def get_campaign_with_lang_targeting(self, campaign_attributes, base_type):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['lang_target'] = campaign_attributes['sec_lang_target']
        new_campaign_attributes['brand_safety_level'] = '1'
        return new_campaign_attributes

    def get_campaign_without_geo_target(self, campaign_attributes):
        new_campaign_attributes = self.get_campaign_with_distribution(campaign_attributes)
        new_campaign_attributes['geo_target'] = None
        return new_campaign_attributes
