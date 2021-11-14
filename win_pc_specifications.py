import os
from datetime import datetime
import json

global date_index
date_index = [[365, 'year'], [30, 'month'], [1, 'day']]


def process_data(val):
    """Process cmd prompt data"""
    all_data = {}
    val = val.strip().split('\n')
    key = ""
    for item in val:
        sub_item = item.split(': ')
        if len(sub_item) == 2:
            sub_item1, sub_item2 = sub_item[0].strip(
            ).lower(), sub_item[1].strip().lower()
            if sub_item1:
                key = sub_item1
                all_data[key] = []
            all_data[key].append(sub_item2)
    return all_data


def get_command_data():
    """cmd propmt data get & process pipeline"""
    command = "systeminfo.exe"
    val = os.popen(command).read()
    return process_data(val)


def date_format(val, index=0, str_val=''):
    """Date time format to build datetime object"""
    if index < 3:
        divisor, name = date_index[index]
        quotient = val//divisor
        if quotient:
            str_val += f" {quotient} {name}"
        str_val = date_format(val % divisor, index+1, str_val)
    return str_val


def age_calculate(date_time_obj):
    """Calculate age"""
    age = datetime.now()-date_time_obj
    return date_format(age.days)


def format_data(all_data):
    """Build JSON data"""
    json_data = {}
    json_data['model_name'] = all_data['system model'][-1]
    json_data['brand_name'] = all_data['system manufacturer'][-1]

    os_install_date = all_data['original install date'][0]
    json_data['os_install_date'] = datetime.strptime(
        os_install_date, "%m/%d/%Y, %I:%M:%S %p")
    json_data['os_age'] = age_calculate(json_data['os_install_date'])
    json_data['os_install_date'] = json_data['os_install_date'].strftime(
        "%a, %d %b %Y")

    manufacture_date = all_data['bios version'][-1].split(',')[-1].strip()
    json_data['manufacture_date'] = datetime.strptime(
        manufacture_date, "%m/%d/%Y")
    json_data['device_age'] = age_calculate(json_data['manufacture_date'])
    json_data['manufacture_date'] = json_data['manufacture_date'].strftime(
        "%a, %d %b %Y")
    return json_data


def get_command_data():
    """Run cmd for system info"""
    command = "systeminfo.exe"
    val = os.popen(command).read()
    return process_data(val)


if __name__ == "__main__":
    """Full pipeline for system specification"""
    all_data = get_command_data()
    json_data = format_data(all_data)
    str_json_data = json.dumps(json_data, indent=2)
    print(str_json_data)
    with open("pc_specification.txt", "w") as fh:
        fh.write(str_json_data)
