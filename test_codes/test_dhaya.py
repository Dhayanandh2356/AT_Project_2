from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from test_locators.test_locators import dhaya_locators
from test_data.test_data import dhaya_data
from selenium.webdriver.common.action_chains import ActionChains
import pytest

class Test_dhaya_project:

    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        yield
        self.driver.close() 
    

    def test_tc_pim_01(self, boot):
        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(10)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('ADMIN')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().admin_locator).click()
        admin_check1       = self.driver.find_element(by=By.XPATH,value=dhaya_locators().admin_check)
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('admin')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().admin_locator).click()
        admin_check2       = self.driver.find_element(by=By.XPATH,value=dhaya_locators().admin_check)
       
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('PIM')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().pim_locator).click()
        pim_check1         = self.driver.find_element(by=By.XPATH,value=dhaya_locators().pim_check)
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('pim')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().pim_locator).click()
        pim_check2         = self.driver.find_element(by=By.XPATH,value=dhaya_locators().pim_check)
        
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('LEAVE')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().leave_locator).click()
        leave_check1       = self.driver.find_element(by=By.XPATH,value=dhaya_locators().leave_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('leave')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().leave_locator).click()
        leave_check2       = self.driver.find_element(by=By.XPATH,value=dhaya_locators().leave_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('TIME')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().time_locator).click()
        time_check1        = self.driver.find_element(by=By.XPATH,value=dhaya_locators().time_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('time')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().time_locator).click()
        time_check2        = self.driver.find_element(by=By.XPATH,value=dhaya_locators().time_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('RECRUITMENT')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().recruitment_locator).click()
        recruitment_check1 = self.driver.find_element(by=By.XPATH,value=dhaya_locators().recruitment_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('recruitment')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().recruitment_locator).click()
        recruitment_check2 = self.driver.find_element(by=By.XPATH,value=dhaya_locators().recruitment_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('MY INFO')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().myinfo_locator).click()
        myinfo_check1      = self.driver.find_element(by=By.XPATH,value=dhaya_locators().myinfo_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('my info')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().myinfo_locator).click()
        myinfo_check2      = self.driver.find_element(by=By.XPATH,value=dhaya_locators().myinfo_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('PERFORMANCE')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().performance_locator).click()
        performance_check1 = self.driver.find_element(by=By.XPATH,value=dhaya_locators().performance_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('performance')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().performance_locator).click()
        performance_check2 = self.driver.find_element(by=By.XPATH,value=dhaya_locators().performance_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('DASHBOARD')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().dashboard_locator).click()
        dashboard_check1   = self.driver.find_element(by=By.XPATH,value=dhaya_locators().dashboard_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('dashboard')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().dashboard_locator).click()
        dashboard_check2   = self.driver.find_element(by=By.XPATH,value=dhaya_locators().dashboard_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('DIRECTORY')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().directory_locator).click()
        directory_check1   = self.driver.find_element(by=By.XPATH,value=dhaya_locators().directory_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('directory')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().directory_locator).click()
        directory_check2   = self.driver.find_element(by=By.XPATH,value=dhaya_locators().directory_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('MAINTENANCE')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().maintenance_locator).click()
        maintenance_check1 = self.driver.find_element(by=By.XPATH,value=dhaya_locators().cancel_button)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().cancel_button).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('maintenance')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().maintenance_locator).click()
        maintenance_check2 = self.driver.find_element(by=By.XPATH,value=dhaya_locators().cancel_button)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().cancel_button).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('BUZZ')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().buzz_locator).click()
        buzz_check1        = self.driver.find_element(by=By.XPATH,value=dhaya_locators().buzz_check)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().searchbox_locator).send_keys('buzz')
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().buzz_locator).click()
        buzz_check2        = self.driver.find_element(by=By.XPATH,value=dhaya_locators().buzz_check)

        assert admin_check1 and admin_check2 and pim_check1 and pim_check2 and leave_check1 and leave_check2 and time_check1 and time_check2 and recruitment_check1 and recruitment_check2 and myinfo_check1 and myinfo_check2 and performance_check1 and performance_check2 and dashboard_check1 and dashboard_check2 and directory_check1 and directory_check2 and maintenance_check1 and maintenance_check2 and buzz_check1 and buzz_check2
        

    def test_tc_pim_02(self, boot):
        
        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(10)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().admin).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().usermanagement).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().users).click()

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().userrole)).perform()
        ur_admin   = self.driver.find_element(by=By.XPATH,value=dhaya_data().ur_admin)
        ur_ess     = self.driver.find_element(by=By.XPATH,value=dhaya_data().ur_ess)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().status)).perform()
        enable  = self.driver.find_element(by=By.XPATH,value=dhaya_data().enable)
        disable = self.driver.find_element(by=By.XPATH,value=dhaya_data().disable)

        assert ur_admin and ur_ess and enable and disable
        
    def test_tc_pim_03(self, boot):
        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('demo567')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('Demo980')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().login_details).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().username_details).send_keys('kong4646')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().password_details).send_keys('Demo@123')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().confirm_password).send_keys('Demo@123')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()
        employee_list_check    = self.driver.find_element(by=By.XPATH,value=dhaya_data().PersonalDetails_locator)

        assert employee_list_check   
    

    def test_tc_pim_04(self, boot):
        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('demo357')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('Demo753')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()
        
        personal_details   = self.driver.find_element(by=By.XPATH,value=dhaya_data().PersonalDetails_locator)
        contact_details    = self.driver.find_element(by=By.XPATH,value=dhaya_data().ContactDetails_locator)
        emergency_contacts = self.driver.find_element(by=By.XPATH,value=dhaya_data().EmergencyContacts_locator)
        dependents         = self.driver.find_element(by=By.XPATH,value=dhaya_data().dependents_locator)
        immigration        = self.driver.find_element(by=By.XPATH,value=dhaya_data().immigration_locator)
        job                = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_locator)
        salary             = self.driver.find_element(by=By.XPATH,value=dhaya_data().salary_locator)
        tax_exemptions     = self.driver.find_element(by=By.XPATH,value=dhaya_data().TaxExemptions_locator)
        report             = self.driver.find_element(by=By.XPATH,value=dhaya_data().report_locator)
        qualifications     = self.driver.find_element(by=By.XPATH,value=dhaya_data().qualifications_locator)
        memberships        = self.driver.find_element(by=By.XPATH,value=dhaya_data().memberships_locator)

        assert personal_details and contact_details and emergency_contacts and dependents and immigration and job and salary and tax_exemptions and report and qualifications and memberships
    
    def test_tc_pim_05(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('autodemo')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('demo')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().nick_name_locator).send_keys('kong')
        
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().other_id_locator).send_keys('1234567890')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().license_no_locator).send_keys('1234567890')
        
        action.click(on_element= self.driver.find_element(by=By.XPATH,value=dhaya_data().expiry_date_locator)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().expiry_date).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().ssn_no_locator).send_keys('1234567890')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().sin_no_locator).send_keys('1234567890')

        action.click(on_element= self.driver.find_element(by=By.XPATH,value=dhaya_data().nationality_locator)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().nationality).click()

        action.click(on_element= self.driver.find_element(by=By.XPATH,value=dhaya_data().marital_status_locator)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().marital_status).click()  

        action.click(on_element= self.driver.find_element(by=By.XPATH,value=dhaya_data().DoB_locator)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().PD_DoB).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().gender_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().military_service).send_keys('No')
         
        self.driver.find_element(by=By.XPATH,value=dhaya_data().PD_save_button).click()

        nickname         = self.driver.find_element(by=By.XPATH,value=dhaya_data().nick_name_locator) 
        other_id         = self.driver.find_element(by=By.XPATH,value=dhaya_data().other_id_locator)
        license          = self.driver.find_element(by=By.XPATH,value=dhaya_data().license_no_locator)
        expiry_date      = self.driver.find_element(by=By.XPATH,value=dhaya_data().expiry_date_locator)
        ssn_no           = self.driver.find_element(by=By.XPATH,value=dhaya_data().ssn_no_locator)
        sin_no           = self.driver.find_element(by=By.XPATH,value=dhaya_data().sin_no_locator)
        nationlity       = self.driver.find_element(by=By.XPATH,value=dhaya_data().nationality_locator)
        marital_status   = self.driver.find_element(by=By.XPATH,value=dhaya_data().marital_status_locator)
        DoB              = self.driver.find_element(by=By.XPATH,value=dhaya_data().DoB_locator)
        gender           = self.driver.find_element(by=By.XPATH,value=dhaya_data().gender_locator)
        military_service =self.driver.find_element(by=By.XPATH,value=dhaya_data().military_service)
        

        assert dhaya_data().nick_name_locator != nickname and dhaya_data().other_id_locator != other_id and dhaya_data().nationality_locator != nationlity and dhaya_data().license_no_locator != license and dhaya_data().expiry_date_locator != expiry_date and dhaya_data().ssn_no_locator != ssn_no and dhaya_data().sin_no_locator != sin_no and dhaya_data().expiry_date_locator != expiry_date and dhaya_data().marital_status_locator != marital_status and dhaya_data().DoB_locator != DoB and dhaya_data().gender_locator != gender and dhaya_data().military_service != military_service

    def test_tc_pim_06(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('demoauto123')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('autodemo432')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().ContactDetails_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().street_locator).send_keys('101')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().city_locator).send_keys('Chennai')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().state_locator).send_keys('Tamilnadu')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().zip_code_locator).send_keys('600456')
        action.click(on_element= self.driver.find_element(by=By.XPATH,value=dhaya_data().country_locator)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().country).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().home_no_locator).send_keys('9234567890')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().mobile_no_locator).send_keys('8234567890')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().office_no_locator).send_keys('7234567899')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().office_email_locator).send_keys('xyz@email.com')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().other_email_locator).send_keys('abc@email.com')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().CD_save_button).click()

        street       = self.driver.find_element(by=By.XPATH,value=dhaya_data().street_locator)
        city         = self.driver.find_element(by=By.XPATH,value=dhaya_data().city_locator)
        state        = self.driver.find_element(by=By.XPATH,value=dhaya_data().state_locator)
        zip_code     = self.driver.find_element(by=By.XPATH,value=dhaya_data().zip_code_locator)
        country      = self.driver.find_element(by=By.XPATH,value=dhaya_data().country_locator)
        home_no      = self.driver.find_element(by=By.XPATH,value=dhaya_data().home_no_locator)
        mobile_no    = self.driver.find_element(by=By.XPATH,value=dhaya_data().mobile_no_locator)
        office_no    = self.driver.find_element(by=By.XPATH,value=dhaya_data().office_no_locator)
        office_email = self.driver.find_element(by=By.XPATH,value=dhaya_data().office_email_locator)
        other_email  = self.driver.find_element(by=By.XPATH,value=dhaya_data().other_email_locator)

        assert dhaya_data().street_locator != street and dhaya_data().city_locator != city and dhaya_data().state_locator != state and dhaya_data().zip_code_locator != zip_code and dhaya_data().country_locator != country and dhaya_data().home_no_locator != home_no and dhaya_data().mobile_no_locator != mobile_no and dhaya_data().office_no_locator != office_no and dhaya_data().office_email_locator != office_email and dhaya_data().other_email_locator != other_email

    def test_tc_pim_07(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('autodemo098')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('auto732')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().EmergencyContacts_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_add).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_name).send_keys('xyz')
        name = self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_name)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_realtionship).send_keys('friend')
        relationship = self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_realtionship)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_home_no).send_keys('8989600456')
        HomeNo = self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_home_no)
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_mobile_no).send_keys('9234567890')
        MobileNo = self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_mobile_no)
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_office_no).send_keys('8234567890')
        OfficeNo = self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_office_no)
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_save).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().emc_edit).click()


        assert dhaya_data().emc_name != name and dhaya_data().emc_realtionship != relationship and dhaya_data().emc_home_no != HomeNo and dhaya_data().emc_mobile_no != MobileNo and dhaya_data().emc_office_no != OfficeNo

    def test_tc_pim_08(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('kong123')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('autokong')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().dependents_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_add).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_name).send_keys('DemoDemo')
        name = self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_name)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_relationship)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().realtion).click()
        relationship = self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_relationship)
        
        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_DoB)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().Dob_dep).click()
        DoB = self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_DoB)
                                 
        self.driver.find_element(by=By.XPATH,value=dhaya_data().dep_save).click()
        
        assert dhaya_data().dep_name != name and dhaya_data().dep_relationship != relationship and dhaya_data().dep_DoB != DoB
        

    def test_tc_pim_09(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('godzila')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('kong')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_joindate).send_keys('2022-01-02')

        title_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().job_title)
        action.click(on_element=title_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().title).click()

        category_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().job_category)
        action.click(on_element=category_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().category).click()

        subunit_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().job_subunit)
        action.click(on_element=subunit_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().subunit).click()

        location_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().job_location)
        action.click(on_element=location_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().location).click()
        
        employement_status_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().job_employement_status)
        action.click(on_element=employement_status_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().employement_status).click()

        toggle=self.driver.find_element(by=By.XPATH,value=dhaya_data().job_toggle)
        action.click(on_element=toggle).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_contract_start).send_keys('2022-03-04')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_contract_end).send_keys('2022-12-30')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_save).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_locator).click()

        joindate           = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_joindate)
        title              = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_title)
        category           = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_category)
        SubUnit            = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_subunit)
        Location           = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_location)
        employement_status = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_employement_status)
        
        toggle=self.driver.find_element(by=By.XPATH,value=dhaya_data().job_toggle)
        action.click(on_element=toggle).perform()

        contract_start     = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_contract_start)
        contract_end       = self.driver.find_element(by=By.XPATH,value=dhaya_data().job_contract_end)
        
        assert dhaya_data().job_joindate != joindate and dhaya_data().job_title != title and dhaya_data().job_category != category and dhaya_data().job_subunit != SubUnit and dhaya_data().job_location != Location and dhaya_data().job_employement_status != employement_status and dhaya_data().job_contract_start != contract_start and dhaya_data().job_contract_end != contract_end

    def test_tc_pim_10(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('supra')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('gtr')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_terminate_employment).click()
        date_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().termination_date_locator)
        action.click(on_element=date_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().date).click()
        reason_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().termination_reason_locator)
        action.click(on_element=reason_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().reason).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().termination_save).click()
        success=self.driver.find_element(by=By.XPATH,value=dhaya_data().sucess_termination)
        activate_button=self.driver.find_element(by=By.XPATH,value=dhaya_data().activate_employment)

        assert success and activate_button
    
    def test_tc_pim_11(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('charger123')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('hellcat123')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().job_terminate_employment).click()
        date_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().termination_date_locator)
        action.click(on_element=date_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().date).click()
        reason_dropdown=self.driver.find_element(by=By.XPATH,value=dhaya_data().termination_reason_locator)
        action.click(on_element=reason_dropdown).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().reason).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().termination_save).click()
        
        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().activate_employment)).perform()

        success=self.driver.find_element(by=By.XPATH,value=dhaya_locators().sucess_locator)
        assert success

    def test_tc_pim_12(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('interceptor')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('classic')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().salary_locator).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().salary_add).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().salary_component).send_keys('demodemo')
        component=self.driver.find_element(by=By.XPATH,value=dhaya_data().salary_component)


        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().pay_grade)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().grade).click()
        grade=self.driver.find_element(by=By.XPATH,value=dhaya_data().pay_grade)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().pay_frequency)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().frequency).click()
        frequnecy=self.driver.find_element(by=By.XPATH,value=dhaya_data().pay_frequency)
        
        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().currency)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().usd).click()
        currency=self.driver.find_element(by=By.XPATH,value=dhaya_data().currency)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().amount).send_keys('50500')
        amount=self.driver.find_element(by=By.XPATH,value=dhaya_data().amount)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().salary_toggle)).perform()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().ac_no).send_keys('10101010101010')
        ac_no=self.driver.find_element(by=By.XPATH,value=dhaya_data().ac_no)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().ac_type)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().type).click()
        ac_type=self.driver.find_element(by=By.XPATH,value=dhaya_data().ac_type)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().routing_no).send_keys('1010101010')
        routing_no=self.driver.find_element(by=By.XPATH,value=dhaya_data().routing_no)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().DD_amount).send_keys('50100')
        DD_amount=self.driver.find_element(by=By.XPATH,value=dhaya_data().DD_amount)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().salary_save).click()

        assert dhaya_data().salary_component != component and dhaya_data().pay_grade != grade and dhaya_data().pay_frequency != frequnecy and dhaya_data().currency != currency and dhaya_data().amount != amount and dhaya_data().ac_no != ac_no and dhaya_data().ac_type != ac_type and dhaya_data().routing_no != routing_no and dhaya_data().DD_amount != DD_amount

    def test_tc_pim_13(self,boot):

        self.driver.maximize_window()
        self.driver.get(dhaya_data().url)
        self.driver.implicitly_wait(100)
        action = ActionChains(self.driver)

        self.driver.find_element(by=By.XPATH,value=dhaya_locators().username_inputbox).send_keys(dhaya_data().username)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().password_inputbox).send_keys(dhaya_data().password)
        self.driver.find_element(by=By.XPATH,value=dhaya_locators().submitbutton).click()

        self.driver.find_element(by=By.XPATH,value=dhaya_data().pim).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().add_employee).click()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().firstname).send_keys('metor5656')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().lastname).send_keys('shotgun3636')
        self.driver.find_element(by=By.XPATH,value=dhaya_data().save_button).click()
        
        self.driver.find_element(by=By.XPATH,value=dhaya_data().TaxExemptions_locator).click()
        
        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().tax_fi_status)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().fi_status).click()
        fi_status=self.driver.find_element(by=By.XPATH,value=dhaya_data().tax_fi_status)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().fi_exemptions).send_keys('22')
        fi_exemptions=self.driver.find_element(by=By.XPATH,value=dhaya_data().fi_exemptions)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().tax_si_state)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().si_state).click()
        si_state=self.driver.find_element(by=By.XPATH,value=dhaya_data().tax_si_state)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().tax_si_status)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().si_status).click()
        si_status=self.driver.find_element(by=By.XPATH,value=dhaya_data().tax_si_status)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().si_exemptions).send_keys('33')
        si_exemptions=self.driver.find_element(by=By.XPATH,value=dhaya_data().si_exemptions)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().unemployment_state)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().up_state).click()
        unemployment=self.driver.find_element(by=By.XPATH,value=dhaya_data().unemployment_state)

        action.click(on_element=self.driver.find_element(by=By.XPATH,value=dhaya_data().work_state)).perform()
        self.driver.find_element(by=By.XPATH,value=dhaya_data().wk_state).click()
        work=self.driver.find_element(by=By.XPATH,value=dhaya_data().work_state)

        self.driver.find_element(by=By.XPATH,value=dhaya_data().tax_save).click()

        assert dhaya_data().tax_fi_status != fi_status and dhaya_data().fi_exemptions != fi_exemptions and dhaya_data().tax_si_state != si_state and dhaya_data().tax_si_status != si_status and dhaya_data().si_exemptions != si_exemptions and dhaya_data().unemployment_state != unemployment and dhaya_data().work_state != work        