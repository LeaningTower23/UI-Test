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

# load data in saas, new load/assign load/rate confirm/pod approval/paid
table = 'dispatch'
new_load_data = case_data.get_data(table, 'create load')
load_list_data = case_data.get_data(table, 'view load list')
assign_data = case_data.get_data(table, 'assign load')
check_status_data = case_data.get_data(table, 'check load status')
rate_confirm_data = case_data.get_data(table, 'rate confirm')
pod_approval_data = case_data.get_data(table, 'pod approval')
paid_data = case_data.get_data(table, 'paid')

# defined the load number by count
count = ExecuteCount.count()
for i in range(0, len(new_load_data)):
    if new_load_data[i]['button'] == 'load number':
        new_load_data[i]['remark'] = new_load_data[i]['remark'] + str(count)
        load_number = new_load_data[i]['remark']
    else:
        load_number = 'TESTGWAUTO' + str(count)

# driver deal load data, accept load/pickup/delivery/upload_pod
accept_load = case_data.get_data(table, 'accept load')
pickup_data = case_data.get_data(table, 'pickup')
delivery_data = case_data.get_data(table, 'delivery')
upload_data = case_data.get_data(table, 'upload pod')
driver_paid_data = case_data.get_data(table, 'check paid')


class TestDispatch(unittest.TestCase):
    def test1_new_load(self):
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

    def test2_deal_upcoming(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_driver = login_by(app_driver, driver_login)
        assert login_driver, "Login failed!"

        print('****************case3. Driver Accept load******************')
        change_title(app_driver, "upcoming")
        driver_upcoming = DealLoad(app_driver)
        deal = driver_upcoming.deal_load(accept_load, 'accept')
        assert deal, 'Driver accept load failed!'
        print('****************Logout******************')
        logout_data = case_data.get_data('dispatch', 'logout')
        logout = driver_upcoming.logout(logout_data)
        assert logout, 'Driver logout failed!'
        app_driver.quit()

    def test3_rate_confirm(self):
        saas_driver = start_saas()
        print('***********Login App by driver************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('****************case4. Rate confirmation******************')
        rate = CommonLoadDeal().deal_load(saas_driver, rate_confirm_data, load_number, 'Rate confirm')
        assert rate is not False, "Rate confirm load failed!"
        saas_driver.quit()

    def test4_pick_delivery(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_driver = login_by(app_driver, driver_login)
        assert login_driver, "Login failed!"
        print('****************case5. Pickup load******************')
        change_title(app_driver, "upcoming")
        driver_pickup = DealLoad(app_driver)
        pickup = driver_pickup.deal_load(pickup_data, 'Pickup')
        assert pickup, "Driver pickup failed!"
        print('****************case6. Delivery load******************')
        delivery = driver_pickup.deal_load(delivery_data, 'Delivery')
        assert delivery, "Driver delivery failed!"
        print('****************Logout******************')
        logout_data = case_data.get_data('dispatch', 'logout')
        logout = driver_pickup.logout(logout_data)
        assert logout, 'Driver logout failed!'
        app_driver.quit()

    def test5_upload_pod(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_driver = login_by(app_driver, driver_login)
        assert login_driver, "Login failed!"
        print('****************case7. Upload POD******************')
        change_title(app_driver, "my money")
        driver_upload = DealLoad(app_driver)
        upload = driver_upload.deal_load(upload_data, 'Upload POD')
        assert upload, "Driver pickup failed!"
        print('****************Logout******************')
        logout_data = case_data.get_data('dispatch', 'logout')
        logout = driver_upload.logout(logout_data)
        assert logout, 'Driver logout failed!'
        app_driver.quit()

    def test6_payment_deal(self):
        saas_driver = start_saas()
        print('***********Login App by driver************')
        login_driver = login_by(saas_driver, saas_login)
        assert login_driver, "Login failed!"

        print('****************case8. POD approval******************')
        change_href(saas_driver, "payment")
        approval = CommonLoadDeal().deal_load(saas_driver, pod_approval_data, load_number, 'POD approval')
        assert approval is not False, "POD approval failed!"
        print('****************case9. Load Paid******************')
        change_href(saas_driver, "payment")
        approval = CommonLoadDeal().deal_load(saas_driver, paid_data, load_number, 'POD paid')
        assert approval is not False, "POD paid failed!"
        saas_driver.quit()

    def test7_check_paid(self):
        app_driver = start_app()
        print('***********Login App by driver************')
        login_driver = login_by(app_driver, driver_login)
        assert login_driver, "Login failed!"
        print('****************case10. Check load paid******************')
        change_title(app_driver, "my money")
        driver_upload = DealLoad(app_driver)
        paid = driver_upload.check_paid(driver_paid_data, load_number)
        assert paid, "Driver check paid failed!"
        print('****************Logout******************')
        logout_data = case_data.get_data('dispatch', 'logout')
        logout = driver_upload.logout(logout_data)
        assert logout, 'Driver logout failed!'
        app_driver.quit()


if __name__ == "__main__":
    test = TestDispatch()
    # test.test1_new_load()
    # test.test2_deal_upcoming()
    # test.test3_rate_confirm()
    # test.test4_pick_delivery()
    # test.test5_upload_pod()
    # test.test6_payment_deal()
    # test.test7_check_paid()
