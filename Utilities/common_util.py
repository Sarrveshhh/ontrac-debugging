import os
import time
from functools import reduce
from operator import getitem
import requests
from requests_ntlm import HttpNtlmAuth
import json
import random
import string
import logging
from datetime import datetime, timedelta
from appium.webdriver.webdriver import WebDriver
import pytz
from Utilities.read_properties import read_json_file, read_config_data


CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(CURRENT_DIR, '..', 'Configurations', 'config.ini')
LOGIN_PATH = os.path.join(CURRENT_DIR, '..', 'Data', 'login.json')

def generate_random_string(length):
    characters = string.ascii_lowercase + string.digits
    return "".join(random.choice(characters) for _ in range(length))


def generate_random_number(length):
    characters = string.digits
    return "".join(random.choice(characters) for _ in range(length))


def current_date(date_format="%Y-%m-%d"):
    new_date = (datetime.now()).strftime(date_format)
    return new_date


def customer_order_number():
    time_stamp = current_date("%S%M%Y%m%d")
    return "1T" + time_stamp
def update_nested_key_delivery(data, nested_key, value):
    current = data
    for key in nested_key[:-1]:
        current = current[key]
    current[nested_key[-1]] = value
    return data


def update_service_code(data, new_service_code):
    data["ServiceCode"] = new_service_code
    return data

def current_date_time(days=0, hours=0, minutes=0, date_format="%Y-%m-%dT%H:%M:%S"):
    delta = timedelta(days=days, hours=hours, minutes=minutes)
    utc_now = datetime.now(pytz.UTC)
    new_date_time = (utc_now + delta).strftime(date_format)
    return new_date_time


def generate_barcode():
    gen_barcode = "1LSCYEY" + current_date(date_format="%m%d%Y") + generate_random_number(5).upper()
    return gen_barcode


def update_json(file_name, key=None, value=None):
    with open(file_name, 'r') as file:
        data_list = json.load(file)
        if key is not None:
            data_list[key] = value
        json.dumps(data_list)
    return data_list


def update_nested_key_delivery(data, nested_key, value):
    current = data
    for key in nested_key[:-1]:
        current = current[key]
    current[nested_key[-1]] = value
    return data


def update_service_code(data, new_service_code):
    data["ServiceCode"] = new_service_code
    return data


def update_json_data(data, key, value):
    if isinstance(data, dict):
        for k, v in data.items():
            if k == key:
                data[k] = value
            elif isinstance(v, dict) or isinstance(v, list):
                update_json_data(v, key, value)
    elif isinstance(data, list):
        for item in data:
            update_json_data(item, key, value)
    json.dumps(data)
    return data


def update_json_data_nested_key(data, nested_key, value):
    reduce(getitem, nested_key[:-1], data)[nested_key[-1]] = value
    return data
