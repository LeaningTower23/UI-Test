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
table = 'process-edit'
new_load_data = case_data.get_data(table, 'create load')
load_list_data = case_data.get_data(table, 'view load list')
assign_data = case_data.get_data(table, 'assign load')
edit_data = case_data.get_data(table, 'edit1 load')

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
        load_number = 'PROCESSEDIT' + str(count)

# driver deal load data, accept load/pickup/delivery/upload_pod
accept_load = case_data.get_data(table, 'accept load')
pickup_data = case_data.get_data(table, 'pickup')
delivery_data = case_data.get_data(table, 'delivery')
upload_data = case_data.get_data(table, 'upload pod')
driver_paid_data = case_data.get_data(table, 'check paid')


class TestEditProcess(unittest.TestCase):
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

    def test2_edit_load(self):
        saas_driver = start_saas()
        print('***********Login App by driver************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('****************case3. Edit load******************')
        deal = CommonNewLoad().common_edit_load(saas_driver, edit_data, load_number)
        assert deal, 'Edit load failed!'
        saas_driver.quit()


if __name__ == '__main__':
    Dispatch = TestEditProcess()
