from Rely.Rely_Element import *


class CommonDriver(object):

    @staticmethod
    def common_driver(driver, test_data):
        res = execute_method(driver, test_data)
        if res is True:
            return True
        else:
            print('Testcase false!')
            return False
