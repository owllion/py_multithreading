from datetime import datetime

meat_types = ["雞肉", "豬肉", "牛肉"]
workers = ["A", "B", "C", "D", "E"]


def get_dateTime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def get_process_time(meat_type):
    if meat_type == "牛肉":
        return 1
    if meat_type == "豬肉":
        return 2
    if meat_type == "雞肉":
        return 3


def get_number_of_meat(meat_type):
    if meat_type == "牛肉":
        return 10
    if meat_type == "豬肉":
        return 7
    if meat_type == "雞肉":
        return 5
