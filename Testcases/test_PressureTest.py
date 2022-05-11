from Common.common_PressureTest import *
from Rely.Rely_AnalysisCases import GetTestCase
from Common.common_Login import *
from Rely.Rely_StartApplication import start_app

driver = start_app()

print('***********Login App by driver************')
login_data = GetTestCase().get_login()
driver_login = GetTestCase().get_cases('driver登录', login_data)
login_admin = Login().login_by(driver, driver_login)
assert login_admin, "Login failed!"

pressure_data = GetTestCase().get_pressure_data()


class TestUpcoming(object):
    def test_pressure(self):
        print('***********Pressure Test**************')
        PressureTest(driver).pressure_test(pressure_data, 20)


if __name__ == '__main__':
    TestUpcoming().test_pressure()
