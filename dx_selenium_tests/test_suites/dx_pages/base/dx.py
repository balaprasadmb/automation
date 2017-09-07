import re
import random, string
from configs.dx_config import DXConfig
from configs.dx_locator import DXLocator
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.action_chains import ActionChains

class Dx(DXConfig):
    """
    Base class that all page models can inherit from
    """
    def __init__(self, selenium_driver, parent=None):
        self.by_dict = {
            'id': By.ID,
            'css': By.CSS_SELECTOR,
            'css selector': By.CSS_SELECTOR,
            'link text': By.LINK_TEXT,
            'class': By.CLASS_NAME,
            'xpath': By.XPATH,
            'tag_name': By.TAG_NAME
        }
        self.base_url = DXConfig().URL
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent
        self.tabs = {}
        class_name = self.convert_to_lower(self.__class__.__name__)
        existing_locators = getattr(DXLocator(class_name), class_name)
        inherited_locators = existing_locators['common'] if existing_locators.has_key('common') else None
        new_combined_locators = dict(inherited_locators.items() + existing_locators.items()) if inherited_locators != None else existing_locators
        if new_combined_locators.has_key('common'):
            del new_combined_locators['common']
        for key, locator in new_combined_locators.iteritems():
            if isinstance(locator, dict):
                if locator.has_key('by') != 1:
                    locator['by'] = 'id'
                if locator.has_key('by') and locator.has_key('value'):
                    setattr(self, key, locator.values())
                else:
                    setattr(self, key, locator)
            else:
                setattr(self, key, locator)

    def _open(self, url):
        self.driver.get(self.base_url + url)

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def find_element(self, loc):
        loc = tuple(loc)
        return self.driver.find_element(*loc)

    def find_elements(self, loc):
        loc = tuple(loc)
        return self.driver.find_elements(*loc)

    def script(self, src):
        return self.driver.execute_script(src)

    def send_keys(self, loc, value, clear_first=True, click_first=True):
        try:
            if click_first:
                self.find_element(loc).click()
            if clear_first:
                self.find_element(loc).clear()
            self.find_element(loc).send_keys(value)
        except AttributeError:
            print '%s page does not have "%s" locator' % (self, loc)

    def fill_field(self, loc, value):
        element = self.find_element(loc) if type(loc) is not WebElement else loc
        element.send_keys(value)

    def convert_to_lower(self, name):
        s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
        return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()

    def type_email(self, email):
        self.clear_and_send_value(email, self.email)

    def type_search_string(self, search_string):
        self.fill_field(self.search_box, search_string)

    def click_element(self, loc):
        element = self.find_element(loc) if type(loc) is not WebElement else loc
        element.click()

    def click_and_hold(self, element):
        loc = self.find_element(element)
        ActionChains(self.driver).click_and_hold(loc).perform()
        ActionChains(self.driver).release(loc).perform()

    def select_option(self, select_field, option_to_select, select_method='label'):
        select = Select(select_field) if type(select_field) is WebElement else Select(self.find_element(select_field))
        attribute_dict = { 'label':'select_by_visible_text', 'value':'select_by_value',
                          'index':'select_by_index' }
        getattr(select, attribute_dict[select_method])(option_to_select)

    def check_success_message(self, message=None):
        if message is not None:
            self.success_message = message 
        assert self.success_message in self.driver.page_source

    def check_failure_message(self, message=None):
        if message is not None:
            self.failure_message = message 
        assert self.failure_message in self.driver.page_source, message

    def page_should_contain(self, string):
        assert string in self.driver.page_source, "Content doesn't match. Obtained message is {0}".format(string)

    def page_should_not_contain(self, string):
        assert string not in self.driver.page_source, "Content doesn't match. Obtained message is {0}".format(string)

    def get_id_from_link(self, link):
        loc = (By.LINK_TEXT, link)
        href = self.find_element(loc).get_attribute('href')
        split_list = href.split('?locale=en')
        split_list_first_element = split_list[1]
        first_element_split_list = split_list_first_element.split("/")
        return first_element_split_list[-1]

    def get_last_element(self, loc):
        return self.find_elements(loc)[-1]

    def get_element_by_index(self, index, loc):
        return self.find_elements(loc)[index - 1]

    def go_to_link(self, link_name):
        self.click_element((By.LINK_TEXT, link_name))

    def submit_form(self,loc):
        self.find_element(loc).submit()

    def wait_till_visible(self, loc, wait_time = 30):
        WebDriverWait(self.driver, wait_time).until(EC.visibility_of_element_located((self.by_dict[loc[0]], loc[1])))

    def wait_till_invisible(self, loc, wait_time = 30):
        WebDriverWait(self.driver, wait_time).until(EC.invisibility_of_element_located((self.by_dict[loc[0]], loc[1])))

    def wait_till_element_clickable(self, locator, wait_time = 30):
        WebDriverWait(self.driver, wait_time).until(EC.element_to_be_clickable((self.by_dict[locator[0]], locator[1])))

    def accept_alert(self):
        try:
            WebDriverWait(self.driver, 10).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')
            alert = self.driver.switch_to_alert()
            alert.accept()
        except TimeoutException:
            print 'No alert accepted'

    def upload_file(self, file_path, loc):
        element = self.find_element(loc) if type(loc) is not WebElement else loc
        element.send_keys(file_path)

    def press_enter_key(self, loc):
        if type(loc) is WebElement:
            loc.send_keys(Keys.ENTER)
        else:
            self.find_element(loc).send_keys(Keys.ENTER)

    def clear_and_send_value(self, value, loc):
        element = self.find_element(loc) if type(loc) is not WebElement else loc
        element.click()
        element.clear()
        element.send_keys(value)

    def close_message_popup(self):
        if self.is_element_present(self.system_message_dialog):
            self.click_element(self.system_message_dialog)
            self.click_element(self.system_message_dialog_close_link)

    def is_element_present(self, loc):
        try: self.find_element(loc)
        except NoSuchElementException: return False
        return True

    def link_not_exists(self, link):
        assert self.is_element_present(link) == False

    def link_exists(self, link):
        assert self.is_element_present(link)

    def switch_to_view(self, view='Classic'):
        view_dict = {
            'Dashboard': 'Switch to Campaign Dashboard',
            'Classic': 'Switch to Classic Campaign View'
        }
        self.driver.find_element_by_link_text("Admin").click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Agency Groups")))
        self.driver.find_element_by_link_text(view_dict[view]).click()
        WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.LINK_TEXT, view_dict[view])))

    def get_random_string(self, len=10):
        return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(len))

    def get_random_characters(self, len=10):
        return ''.join(random.choice(string.ascii_uppercase) for _ in range(len))

    def get_random_digits(self, len=10):
        return ''.join(random.choice(string.digits) for _ in range(len))

    def get_content_value(self, loc):
        element = self.find_element(loc) if type(loc) is not WebElement else loc
        return element.get_attribute('value')

    def get_content_text(self, loc):
        element = self.find_element(loc) if type(loc) is not WebElement else loc
        return element.text

    def check_dropdown_options(self, option_list, loc):
        select = Select(self.find_element(loc))
        options_text = []
        for opt in select.options:
            options_text.append(opt.text.encode())
        for option in option_list:
            assert option in options_text, "Actaul/Obtained list :- {0}/{1}".format(option, options_text)

    def get_content_text_list(self, loc):
        elements = self.find_elements(loc)
        text_list = []
        for element in elements:
            text_list.append(element.text)
        return text_list

    def go_back(self):
        self.driver.back()

    def assert_options(self):
        widget=self.find_element(self.geo_target_area_type)
        select = Select(widget)
        for option in select.options:
            if option.text == 'Metrocodes':
                raise AssertionError

    def assert_geographic_selected_country(self, locator, country=None, countries=None):
        select = Select(self.find_element(locator))
        selected = []
        for option in select.options:
            selected.append(option.text)
        if country:
            if country not in selected:
                raise AssertionError
        elif countries:
            for country in countries:
                if country not in selected:
                    raise AssertionError

    def get_dropdown_options(self, loc):
        select = Select(self.find_element(loc))
        options_text = []
        for opt in select.options:
            options_text.append(opt.text.encode())
        return options_text

    def dismiss_alert(self):
        try:
            WebDriverWait(self.driver, 3).until(EC.alert_is_present(),
                                   'Timed out waiting for PA creation ' +
                                   'confirmation popup to appear.')

            alert = self.driver.switch_to_alert()
            alert.dismiss()
        except TimeoutException:
            print 'No alert accepted'

    def clear(self , loc):
        self.find_element(loc).clear()

    def page_refresh(self):
        self.driver.refresh()

    def get_attribute_value(self, locator, attribute='innerHTML'):
        return self.find_element(locator).get_attribute(attribute)

    def get_attribute_value_with_strip(self, locator, attribute='innerHTML'):
        attribute_value = self.get_attribute_value(locator, attribute)
        return attribute_value.strip()

    def get_dropdown_selected_value(self, locator):
        select = Select(self.find_element(locator))
        option = select.first_selected_option
        return option.text

    def wait_till_enabled(self, web_element=None, wait_time = 30):
        element = self.find_element(web_element) if type(web_element) is not WebElement else web_element
        WebDriverWait(self.driver, wait_time).until(lambda driver : element.is_enabled())

    def generate_and_accept_javascript_alert(self):
        self.script("alert('Keeping to Front')")
        self.accept_alert()

    def wait_till_element_visible_and_invisible(self, locator):
        self.wait_till_visible(locator)
        self.wait_till_invisible(locator)
