from Rely.Rely_ExecuteMethod import *


class CommonContract(object):
    def __init__(self):
        self.start = get_time_format(1)
        self.end = get_time_format(31)

    def common_contract(self, driver, contract_data, contract_number):
        for i in range(0, len(contract_data)):
            button = contract_data[i]['button']
            if button == 'start time':
                contract_data[i]['remark'] = str(self.start)
                continue
            elif button == 'end time':
                contract_data[i]['remark'] = str(self.end)
                continue

        execute_method(driver, contract_data)
        if check_element(driver, 'xpath', '//span[contains(text(), "' + contract_number + '")]'):
            print('Create contract "' + contract_number + '" Success!')
            return True
        else:
            print('Not seen the created contract, create contract failed!')
            return False

    @staticmethod
    def check_contract_list(driver, contract_list, contract_number):
        for i in range(0, len(contract_list)):
            if contract_list[i]['button'] == 'contract number':
                contract_list[i]['value'] = '//span[contains(text(), "' + contract_number + '")]'
            else:
                contract_list[i]['value'] = contract_list[0]['value'] + '/../../../../../' + contract_list[i]['value']

        if execute_method(driver, contract_list) is not False:
            return True
        else:
            return False

    @staticmethod
    def common_edit_contract(driver, contract_data, load_number):
        for i in range(0, len(contract_data)):
            button = contract_data[i]['button']
            if button == 'pickup start':
                contract_data[i]['remark'] = str(get_time_format(63))
                continue
            elif button == 'pickup end':
                contract_data[i]['remark'] = str(get_time_format(63))
                continue
            elif button == 'delivery start':
                contract_data[i]['remark'] = str(get_time_format(64))
                continue
            elif button == 'delivery end':
                contract_data[i]['remark'] = str(get_time_format(64))
                continue
            elif contract_data[i]['button'] == "load number":
                contract_data[i]['value'] = '//span[contains(text(), "' + load_number + '")]'
                continue

        execute_method(driver, contract_data)
        if check_element(driver, 'xpath', '//span[contains(text(), "' + load_number + '")]'):
            print('Edit load "' + load_number + '" Success!')
            return True
        else:
            print('Not seen the edited load, edit load failed!')
            return False

    @staticmethod
    def assign_contract(driver, assign_data, contract_number):
        for i in range(0, len(assign_data)):
            if assign_data[i]['button'] == "contract number":
                assign_data[i]['value'] = '//span[contains(text(), "' + contract_number + '")]'
                continue

        for j in range(0, len(assign_data)):
            if assign_data[j]['button'] == "driver":
                find_element_retry(driver, assign_data[j]['by'], assign_data[j]['value'], assign_data[j + 1]['value'])
            elif assign_data[j]['button'] == "next":
                pass
            else:
                assign = execute_method(driver, assign_data)
                if assign is not False:
                    return True
                else:
                    return False
