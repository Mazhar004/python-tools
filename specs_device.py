import os
import sys
import re
import json
from datetime import datetime
from collections import defaultdict


global date_index
date_index = [[365, 'year'], [30, 'month'], [1, 'day']]


def convert_date(val, d_format="%m/%d/%Y", r_format="%d %b, %Y"):
    # Convert date string to datetime object or vice versa
    try:
        date_time_obj = datetime.strptime(val, d_format)
    except:
        val = re.search(r'[\d]{1,}/[\d]{1,}/[\d]{4}', val).group()
        date_time_obj = datetime.strptime(val, d_format)
    date_time_str = date_time_obj.strftime(r_format)
    return date_time_obj, date_time_str


def process_data(cmd_data):
    # Process the command data
    all_lines = cmd_data.splitlines()
    data = defaultdict(list)
    for line in all_lines:
        if ':' in line:
            key, val = map(str.strip, line.split(':', 1))
            data[key.lower()].append(val)
    return data


def date_format(val, index=0, str_val=''):
    # Convert dat time object to string
    if index < 3:
        divisor, name = date_index[index]
        quotient = val//divisor
        if quotient:
            str_val += f" {quotient} {name}"
        str_val = date_format(val % divisor, index+1, str_val)
    return str_val


def age_calculate(date_time_obj):
    # Calculate the age
    age = datetime.now()-date_time_obj
    return date_format(age.days)


def format_data(data, keys):
    # Format the data based on keys
    dict_data = {}
    for key, vals in keys.items():
        dict_data[vals[0]] = data[key][0]
        if len(vals) == 2:
            date_time_obj, dict_data[vals[0]] = convert_date(
                dict_data[vals[0]])
            dict_data[vals[1]] = age_calculate(date_time_obj)

    return dict_data


def get_command_data():
    # Get the command data based on different OS
    platform = (sys.platform).lower()
    command = ''
    if 'win' in platform:
        command = "systeminfo.exe"
        keys = {'system model': ['Model Name'],
                'system manufacturer': ['Brand Name'],
                'original install date': ['OS Install Date', 'OS Age'],
                'bios version': ['Manufacture Date', 'Device Age']}

    elif platform == 'linux':
        command = "dmidecode"
        keys = {'release date': ['Manufacture Date', 'Device Age'],
                'manufacturer': ['Brand Name'],
                'product name': ['Model Number'],
                'family': ['Model Family'],
                'maximum capacity': ['RAM Size']}
    cmd_data = os.popen(command).read()
    return cmd_data, keys


def show(json_data, save=False):
    # Show the data & save based on save flag
    str_json_data = json.dumps(json_data, indent=2)
    print(str_json_data)
    if save:
        with open("pc_specification.txt", "w") as fh:
            fh.write(str_json_data)


if __name__ == "__main__":
    cmd_data, keys = get_command_data()
    data = process_data(cmd_data)
    json_data = format_data(data, keys)
    show(json_data)
