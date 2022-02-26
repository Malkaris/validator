import json
import re


def read_json(filename) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        filename = json.load(file)
        return filename


def is_valid_name(func) -> bool:
    a = func.get('fullname')
    return all([len(a.split()) == 2, len(a) <= 50,
                a.split()[0].isalpha(), a.split()[1].isalpha()])


def is_valid_email(func) -> bool:
    a = func.get('email')
    pattern = r"[a-zA-Z0-9]{1,100}[@][a-z]{2,6}\.[a-z]{2,4}"
    number_re = re.compile(pattern)
    if number_re.findall(a):
        return True
    else:
        return False


def is_valid_phonenumber(func) -> bool:
    a = func.get('phonenumber')
    code = ('25', '29', '33', '44')
    return a.startswith('+375') and a[4:6] in code and len(a[6:]) == 7


def is_valid_message(func) -> bool:
    a = func.get('message')
    return len(a) <= 140


def main(filename):
    data = read_json(filename)
    valid = {
        'fullname': is_valid_name(data),
        'phonenumber': is_valid_phonenumber(data),
        'email': is_valid_email(data),
        'message': is_valid_message(data),
    }
    return valid


if __name__ == '__main__':
    print(main('input.json'))
