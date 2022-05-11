excel_data = []


def get_excel(excel):
    first_line = excel.row_values(0)
    values_merge_cell = merge_cell(excel)
    for i in range(1, excel.nrows):
        other_line = excel.row_values(i)
        for key in values_merge_cell.keys():
            if key[0] == i:
                other_line[key[1]] = values_merge_cell[key]
        dic = list_dic(first_line, other_line)
        excel_data.append(dic)
    return excel_data


def list_dic(list1, list2):
    '''
    two lists merge a dict,a list as key,other list as value
    :param list1:key
    :param list2:value
    :return:dict
    '''
    dic = dict(map(lambda x, y: [x, y], list1, list2))
    return dic


def merge_cell(sheet_info):
    '''
    #handle Merge transverse cells and handle Merge Vertical Cells, assign empty cells,
    :param sheet_info:object of sheet
    :return:dic contain all of empty cells value
    '''
    merge = {}
    merge_cells = sheet_info.merged_cells
    for (rlow, rhigh, clow, chigh) in merge_cells:
        value_mg_cell = sheet_info.cell_value(rlow, clow)
        if rhigh - rlow == 1:
            for n in range(chigh - clow - 1):
                merge[(rlow, clow + n + 1)] = value_mg_cell
        elif chigh - clow == 1:
            for n in range(rhigh - rlow - 1):
                merge[(rlow + n + 1, clow)] = value_mg_cell
    return merge
