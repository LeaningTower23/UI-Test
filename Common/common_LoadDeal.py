from Rely.Rely_Element import *
from Rely.Rely_ExecuteMethod import execute_method
from selenium.webdriver.common.action_chains import ActionChains


class CommonLoadDeal(object):
    def __init__(self):
        pass

    @staticmethod
    def deal_load(driver, confirm_data, load_number, execute):
        for i in range(0, len(confirm_data)):
            if confirm_data[i]['button'] == "load number":
                confirm_data[i]['value'] = '//span[contains(text(), "' + load_number + '")]'
            elif confirm_data[i]['button'] == "status value":
                confirm_data[i]['value'] = '//span[contains(text(), "' + load_number + '")]/../../../../../' \
                                           + confirm_data[i]['value']
            else:
                continue

        result = execute_method(driver, confirm_data)
        if result is not False:
            print(execute + " success!")
            return True
        else:
            return False
