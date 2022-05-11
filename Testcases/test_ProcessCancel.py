from Common.common_NewLoad import *
from Common.common_LoadDeal import *
from Common.common_DriverDealLoad import *
from Common.common_Login import login_by
from Rely.Rely_ExecuteMethod import change_href
from Rely.Rely_Count import *
from Rely.Rely_StartApplication import start_app
from Rely.Rely_StartApplication import start_saas
import unittest


# Get cases from excel
case_data = GetTestCase()

# login data
saas_login = case_data.get_data('login', 'saas login')
driver_login = case_data.get_data('login', 'driver login')

# load data
table = "process-cancel"
new_load_data = case_data.get_data(table, 'create load')
load_list_data = case_data.get_data(table, 'view load list')
assign_data = case_data.get_data(table, 'assign load')
check_status_data = case_data.get_data(table, 'check load status')
reject_load = case_data.get_data(table, 'reject load')

assign2_data = case_data.get_data(table, 'assign2 load')
assign3_data = case_data.get_data(table, 'assign3 load')
assign4_data = case_data.get_data(table, 'assign4 load')
accept_load = case_data.get_data(table, 'accept load')
rate_confirm_data = case_data.get_data(table, 'rate confirm')
haulistix_cancel_data = case_data.get_data(table, 'haulistix cancel')
check_haulistix_cancel = case_data.get_data(table, 'check haulistix cancel')
driver_cancel_data = case_data.get_data(table, 'driver cancel')
check_driver_cancel = case_data.get_data(table, 'check driver cancel')
shipper_cancel_data = case_data.get_data(table, 'shipper cancel')
check_shipper_cancel = case_data.get_data(table, 'check shipper cancel')

pickup_data = case_data.get_data(table, 'pickup')
delivery_data = case_data.get_data(table, 'delivery')
upload_data = case_data.get_data(table, 'upload pod')
pod_approval_data = case_data.get_data(table, 'pod approval')
paid_data = case_data.get_data(table, 'paid')
driver_paid_data = case_data.get_data(table, 'check paid')

# defined the load number by count
count = ExecuteCount.count()
for i in range(0, len(new_load_data)):
    if new_load_data[i]['button'] == 'load number':
        new_load_data[i]['remark'] = new_load_data[i]['remark'] + str(count)
        load_number = new_load_data[i]['remark']
    else:
        load_number = 'PROCESSTEST' + str(count)


class TestProcess(unittest.TestCase):
    def test10_new_load(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, no execute test cases!"

        print('***********case1. Create new load************')
        logger.info('***********case1. Create new load************')
        change_href(saas_driver, "dispatch")
        load = CommonNewLoad()
        create_load = load.common_new_load(saas_driver, new_load_data, load_number)
        assert create_load, 'Create load failed!'

        print('***********Check load list information************')
        logger.info('***********Check load list information************')
        load_list = load.check_load_list(saas_driver, load_list_data, load_number)
        assert load_list, 'Check load list failed!'

        print('***********case2. Assign load to driver************')
        logger.info('***********case2. Assign load to driver************')
        assign_load = CommonLoadDeal().assign_load(saas_driver, assign_data, load_number)
        assert assign_load, 'Assign load Failed!'
        saas_driver.quit()

    def test11_deal_upcoming(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_admin = login_by(app_driver, driver_login)
        assert login_admin, "Login failed!"

        print('****************case3. Driver reject load******************')
        change_title(app_driver, "upcoming")
        driver_upcoming = DealLoad(app_driver)
        deal = driver_upcoming.deal_load(reject_load, 'reject')
        assert deal, 'Driver accept load failed!'
        print('****************Logout******************')
        logout_data = case_data.get_data('login', 'logout')
        logout = driver_upcoming.logout(logout_data)
        assert logout, 'Driver logout failed!'
        app_driver.quit()

    def test12_reassign(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, no execute test cases!"

        print('***********case4. Assign load to driver************')
        logger.info('***********case4. Assign load to driver************')
        change_href(saas_driver, "dispatch")
        assign_load = CommonLoadDeal().assign_load(saas_driver, assign2_data, load_number)
        assert assign_load, 'Assign load Failed!'
        saas_driver.quit()

    def test13_deal_upcoming(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_admin = login_by(app_driver, driver_login)
        assert login_admin, "Login failed!"

        print('****************case5. Driver Accept load******************')
        change_title(app_driver, "upcoming")
        driver_upcoming = DealLoad(app_driver)
        deal = driver_upcoming.deal_load(accept_load, 'accept')
        assert deal, 'Driver accept load failed!'
        print('****************Logout******************')
        logout_data = case_data.get_data('login', 'logout')
        logout = driver_upcoming.logout(logout_data)
        assert logout, 'Driver logout failed!'
        app_driver.quit()

    def test14_rate_confirm(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('****************case6. Rate confirmation******************')
        change_href(saas_driver, "dispatch")
        rate = CommonLoadDeal().deal_load(saas_driver, rate_confirm_data, load_number, 'Rate confirm')
        assert rate is not False, "Rate confirm load failed!"
        saas_driver.quit()

    def test15_haulistix_cancel(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('****************case7. Haulistix cancel load******************')
        change_href(saas_driver, "dispatch")
        rate = CommonLoadDeal().deal_load(saas_driver, haulistix_cancel_data, load_number, 'Haulistix cancel load')
        assert rate is not False, "Haulistix cancel load failed!"
        saas_driver.quit()

    def test16_check_cancel(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_admin = login_by(app_driver, driver_login)
        assert login_admin, "Login failed!"

        print('****************case8. Check haulistix cancel result******************')
        change_title(app_driver, 'canceled')
        driver_cancel = DealLoad(app_driver)
        rate = driver_cancel.deal_load(check_haulistix_cancel, 'Check canceled result')
        assert rate is not False, "Haulistix cancel load result failed!"
        app_driver.quit()

    def test17_reassign(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, no execute test cases!"

        print('***********case4. Assign load to driver************')
        change_href(saas_driver, "dispatch")
        logger.info('***********case9. Assign load to driver************')
        assign_load = CommonLoadDeal().assign_load(saas_driver, assign3_data, load_number)
        assert assign_load, 'Assign load Failed!'
        saas_driver.quit()

    def test18_driver_cancel(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('****************case10. Driver cancel load******************')
        change_href(saas_driver, "dispatch")
        rate = CommonLoadDeal().deal_load(saas_driver, driver_cancel_data, load_number, 'Driver cancel load')
        assert rate is not False, "Driver cancel load failed!"
        saas_driver.quit()

    def test19_check_cancel(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_admin = login_by(app_driver, driver_login)
        assert login_admin, "Login failed!"

        print('****************case11. Check driver cancel result******************')
        change_title(app_driver, 'canceled')
        rate = DealLoad.deal_load(app_driver, check_driver_cancel, 'Check canceled result')
        assert rate is not False, "Driver cancel load result failed!"

    def test20_reassign(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, no execute test cases!"

        print('***********case12. Assign load to driver************')
        logger.info('***********case12. Assign load to driver************')
        change_href(saas_driver, "dispatch")
        assign_load = CommonLoadDeal().assign_load(saas_driver, assign4_data, load_number)
        assert assign_load, 'Assign load Failed!'
        saas_driver.quit()

    def test21_shipper_cancel(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('****************case13. Shipper cancel load******************')
        change_href(saas_driver, "dispatch")
        rate = CommonLoadDeal().deal_load(saas_driver, shipper_cancel_data, load_number, 'Shipper cancel load')
        assert rate is not False, "Shipper cancel load failed!"
        saas_driver.quit()

    def test22_check_cancel(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('****************case11. Check driver cancel result******************')
        change_href(saas_driver, 'payment')
        rate = CommonLoadDeal().deal_load(saas_driver, check_shipper_cancel, load_number, 'Check canceled result')
        assert rate is not False, "Driver cancel load result failed!"


if __name__ == '__main__':
    process = TestProcess()

