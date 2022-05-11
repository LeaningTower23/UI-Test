from Common.common_Login import login_by
from Rely.Rely_ExecuteMethod import change_href
from Rely.Rely_ExecuteMethod import case_common
from Rely.Rely_StartApplication import start_saas
from Rely.Rely_AnalysisCases import GetTestCase
import unittest


# Get cases from excel
case_data = GetTestCase()

# login data
saas_login = case_data.get_data('login', 'saas login')

# 获取测试数据：driver tab
table = 'driver'
new_driver_data = case_data.get_data(table, 'new driver')
check_new_driver_data = case_data.get_data(table, 'check new driver')
edit_driver_data = case_data.get_data(table, 'edit driver')

saas_driver = start_saas()


class TestDriver(unittest.TestCase):

    def test1_new_driver(self):
        print('***********Login Saas by admin************')
        login_admin = login_by(saas_driver, saas_login)
        assert login_admin, "Login failed, can't execute test cases!"

        print('***********case1. Create new driver************')
        change_href(saas_driver, "drivers")
        create_driver = case_common(saas_driver, new_driver_data)
        assert create_driver, 'Case1: Create driver failed!'

        print('***********case1. Check create driver data************')
        change_href(saas_driver, "drivers")
        check_new = case_common(saas_driver, check_new_driver_data)
        assert check_new, 'Case1: Check create driver failed!'

    def test2_edit_driver(self):
        print('***********case2. Edit driver************')
        change_href(saas_driver, "drivers")
        edit_driver = case_common(saas_driver, edit_driver_data)
        assert edit_driver, 'Case2: Edit driver failed!'

        saas_driver.quit()
