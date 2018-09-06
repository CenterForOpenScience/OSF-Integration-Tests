import settings

from api import osf_api
from selenium.webdriver.common.by import By

from base.locators import Locator, GroupLocator, ComponentLocator
from pages.base import GuidBasePage, OSFBasePage
from components.user import SettingsSideNavigation


class UserProfilePage(GuidBasePage):
    user = osf_api.current_user()

    def __init__(self, driver, verify=False, guid=user.id):
        super().__init__(driver, verify, guid)

    #TODO: Reconsider using a component here (and using component locators correctly)
    identity = Locator(By.CLASS_NAME, 'profile-fullname', settings.LONG_TIMEOUT)
    no_public_projects_text = Locator(By.CSS_SELECTOR, '#publicProjects .help-block')
    no_public_components_text = Locator(By.CSS_SELECTOR, '#publicComponents .help-block')
    edit_profile_link = Locator(By.CSS_SELECTOR, '#edit-profile-settings')

    #TODO: Seperate out by component if it becomes necessary
    loading_indicator = Locator(By.CSS_SELECTOR, '.ball-pulse')

    # Group locators
    public_projects = GroupLocator(By.CSS_SELECTOR, '#publicProjects .list-group-item')
    public_components = GroupLocator(By.CSS_SELECTOR, '#publicComponents .list-group-item')
    quickfiles = GroupLocator(By.CSS_SELECTOR, '#quickFiles .list-group-item')


class BaseUserSettingsPage(OSFBasePage):
    url = settings.OSF_HOME + '/settings/'

    identity = Locator(By.ID, 'profileSettings')

    # Components
    side_navigation = ComponentLocator(SettingsSideNavigation)

class ProfileInformationPage(BaseUserSettingsPage):
    url = settings.OSF_HOME + '/settings/'

    identity = Locator(By.CSS_SELECTOR, '#profileSettings')
    middle_name_input = Locator(By.CSS_SELECTOR, '#names > div > form > div:nth-child(5) > input')
    save_button = Locator(By.CSS_SELECTOR, '#names > div > form > div.p-t-lg.p-b-lg > button.btn.btn-success')
    update_success = Locator(By.CSS_SELECTOR, '.text-success')

class AccountSettingsPage(BaseUserSettingsPage):
    url = settings.OSF_HOME + '/settings/account/'

    identity = Locator(By.CSS_SELECTOR, '#connectedEmails')

class ConfigureAddonsPage(BaseUserSettingsPage):
    url = settings.OSF_HOME + '/settings/addons/'

    identity = Locator(By.CSS_SELECTOR, '#configureAddons')

class NotificationsPage(BaseUserSettingsPage):
    url = settings.OSF_HOME + '/settings/notifications/'

    identity = Locator(By.CSS_SELECTOR, '#notificationSettings')

class DeveloperAppsPage(BaseUserSettingsPage):
    url = settings.OSF_HOME + '/settings/applications/'

    identity = Locator(By.CSS_SELECTOR, '#applicationListPage')

class PersonalAccessTokenPage(BaseUserSettingsPage):
    url = settings.OSF_HOME + '/settings/tokens/'

    identity = Locator(By.CSS_SELECTOR, '#personalTokenListPage')
