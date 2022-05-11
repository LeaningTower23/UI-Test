from Rely.Rely_Element import *


class DealLoad:
    def __init__(self, driver):
        self.driver = driver

    def deal_load(self, load_data, deal):
        for case in load_data:
            if case['button'] in ('setup', 'allow'):
                if is_element_exist(self.driver, case['by'], case['value']):
                    check_and_click(self.driver, case['by'], case['value'])
                else:
                    continue
            else:
                result = execute_unit(self.driver, case)
                if result:
                    print(deal + ' load success!')
                    return True
                else:
                    continue

    def check_paid(self, load_data, load_number):
        for i in range(0, len(load_data)):
            if load_data[i]['remark'] == 'load number':
                load_data[i]['remark'] = str(load_number)
                break

        for case in load_data:
            result = execute_unit(self.driver, case)
            if result:
                print("Check load paid success!")
                return True
            else:
                continue

    def logout(self, logout_data):
        for i in range(0, len(logout_data)):
            if logout_data[i]['button'] == 'profile':
                find_element_retry(self.driver, logout_data[i]['by'], logout_data[i]['value'], logout_data[i+1]['value'])
                break

        del logout_data[0:2]
        for case in logout_data:
            # print(case['button'])
            result = execute_unit(self.driver, case)
            if result:
                print('Logout success!')
                return True
            else:
                continue
