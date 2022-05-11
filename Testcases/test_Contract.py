from Common.common_NewLoad import *
from Common.common_Contract import *
from Common.common_Login import login_by
from Rely.Rely_ExecuteMethod import change_href
from Rely.Rely_Count import *
from Rely.Rely_StartApplication import start_saas
import unittest


# Get cases from excel
case_data = GetTestCase()

# login data
saas_login = case_data.get_data('login', 'saas login')
driver_login = case_data.get_data('login', 'driver login')

# load data in saas, new load/assign load/rate confirm/pod approval/paid
table = 'contract'
new_contract_data = case_data.get_data(table, 'create contract')
contract_list_data = case_data.get_data(table, 'view contract list')
assign_contract_data = case_data.get_data(table, 'assign contract')
new_load_data = case_data.get_data(table, 'create load')
load_list_data = case_data.get_data(table, 'view load list')
assign_load_data = case_data.get_data(table, 'assign load')

# defined the load number by count
count = ExecuteCount.count()
for i in range(0, len(new_contract_data)):
    if new_contract_data[i]['button'] == 'contract number':
        new_contract_data[i]['remark'] = new_contract_data[i]['remark'] + str(count)
        contract_number = new_contract_data[i]['remark']
    else:
        contract_number = 'AUTOCONTRACTNO' + str(count)
for i in range(0, len(new_load_data)):
    if new_load_data[i]['button'] == 'load number':
        new_load_data[i]['remark'] = new_load_data[i]['remark'] + str(count)
        load_number = new_load_data[i]['remark']
    else:
        load_number = 'TESTCONTRACTLOAD' + str(count)


class TestContract(unittest.TestCase):
    def test1_new_contract(self):
        saas_driver = start_saas()
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, no execute test cases!"

        print('***********case1. Create new contract************')
        change_href(saas_driver, "contract")
        contract = CommonContract()
        create_contract = contract.common_contract(saas_driver, new_contract_data, contract_number)
        assert create_contract, 'Create contract failed!'

        print('***********Check contract list information************')
        contract_list = contract.check_contract_list(saas_driver, contract_list_data, contract_number)
        assert contract_list, 'Check contract list failed!'

        print('***********case2. Assign contract to driver************')
        assign_contract = contract.assign_contract(saas_driver, assign_contract_data, contract_number)
        assert assign_contract, 'Assign contract Failed!'
        saas_driver.quit()

    def test2_create_load_by_contract(self):
        saas_driver = start_saas()
        print('***********Login App by driver************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed!"

        print('***********case3. Create new load************')
        change_href(saas_driver, "dispatch")
        load = CommonNewLoad()
        create_load = load.common_new_load(saas_driver, new_load_data, load_number)
        assert create_load, 'Create load failed!'

        saas_driver.quit()


if __name__ == "__main__":
    test = TestContract()
