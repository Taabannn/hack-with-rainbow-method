import hashlib
import csv
from collections import OrderedDict

def hash_password_hack(input_file_name, output_file_name):
    username_hashcode_dict = read_username_hashed_passwords(input_file_name)
    start = 1000
    end = 10000
    hash_password_dict = find_hash_pass_dict_in_range(start, end)
    username_password_dict = find_username_raw_pass(username_hashcode_dict, hash_password_dict)
    write_pass_in_csv_file(output_file_name, username_password_dict)


def read_username_hashed_passwords(input_file_name):
    username_hashcode_dict = OrderedDict()
    hash_password_dict = OrderedDict()
    with open(input_file_name) as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            username = row[0]
            username_hashcode_dict[username] = row[1]
    return username_hashcode_dict


def find_hash_pass_dict_in_range(start, end):
    hash_password_dict = OrderedDict()
    for i in range(start, end):
        hashcode = hashlib.sha256(str(i).encode('utf-8')).hexdigest()
        hash_password_dict[hashcode] = str(i)
    return hash_password_dict


def find_username_raw_pass(username_hashcode_dict, hash_password_dict):
    username_password_dict = OrderedDict()
    for key in username_hashcode_dict.keys():
        hash = username_hashcode_dict[key]
        password = hash_password_dict[hash]
        username_password_dict[key] = password
    return username_password_dict


def write_pass_in_csv_file(output_file_name, username_password_dict):
    file = open(output_file_name, "w")
    for key in username_password_dict.keys():
        file.write("%s,%s\n" % (key, username_password_dict[key]))


hash_password_hack("input.csv", "output.csv")