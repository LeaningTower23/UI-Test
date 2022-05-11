from Rely.Rely_Element import *
from Rely.Rely_ExecuteMethod import change_time_zone
from Rely.Rely_ExecuteMethod import *


class CommonNewLoad(object):
    def __init__(self):
        self.pickup_start = get_time_format(60)
        self.pickup_end = get_time_format(61)
        self.delivery_start = get_time_format(65)
        self.delivery_end = get_time_format(66)

    def common_new_load(self, driver, load_data, load_number):
        for i in range(0, len(load_data)):
            button = load_data[i]['button']
            if button == 'pickup start':
                load_data[i]['remark'] = str(self.pickup_start)
                continue
            elif button == 'pickup end':
                load_data[i]['remark'] = str(self.pickup_end)
                continue
            elif button == 'delivery start':
                load_data[i]['remark'] = str(self.delivery_start)
                continue
            elif button == 'delivery end':
                load_data[i]['remark'] = str(self.delivery_end)
                continue

        execute_method(driver, load_data)
        if check_element(driver, 'xpath', '//span[contains(text(), "' + load_number + '")]'):
            print('Create load "' + load_number + '" Success!')
            logger.info('Create load "' + load_number + '" Success!')
            return True
        else:
            print('Not seen the created load, create load failed!')
            logger.error('Not seen the created load, create load failed!')
            return False

    def check_load_list(self, driver, load_list, load_number):
        for i in range(0, len(load_list)):
            if load_list[i]['button'] == 'load number':
                load_list[i]['value'] = '//span[contains(text(), "' + load_number + '")]'
            elif load_list[i]['button'] == 'pickup date':
                load_list[i]['remark'] = str(self.pickup_end)
                load_list[i]['value'] = load_list[0]['value'] + '/../../../../../' + load_list[i]['value']
            elif load_list[i]['button'] == 'delivery date':
                load_list[i]['remark'] = str(self.delivery_end)
                load_list[i]['value'] = load_list[0]['value'] + '/../../../../../' + load_list[i]['value']
            else:
                load_list[i]['value'] = load_list[0]['value'] + '/../../../../../' + load_list[i]['value']

        if execute_method(driver, load_list) is not False:
            return True
        else:
            return False

    @staticmethod
    def common_edit_load(driver, load_data, load_number):
        print(load_data)
        for i in range(0, len(load_data)):
            button = load_data[i]['button']
            if button == 'pickup start':
                load_data[i]['remark'] = str(get_time_format(63))
                continue
            elif button == 'pickup end':
                load_data[i]['remark'] = str(get_time_format(63))
                continue
            elif button == 'delivery start':
                load_data[i]['remark'] = str(get_time_format(64))
                continue
            elif button == 'delivery end':
                load_data[i]['remark'] = str(get_time_format(64))
                continue
            elif load_data[i]['button'] == "load number":
                load_data[i]['value'] = '//span[contains(text(), "' + load_number + '")]'
                continue

        execute_method(driver, load_data)
        if check_element(driver, 'xpath', '//span[contains(text(), "' + load_number + '")]'):
            print('Edit load "' + load_number + '" Success!')
            logger.info('Edit load "' + load_number + '" Success!')
            return True
        else:
            print('Not seen the edited load, edit load failed!')
            logger.error('Not seen the edited load, edit load failed!')
            return False
