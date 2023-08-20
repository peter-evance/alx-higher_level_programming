#!/usr/bin/python3
"""
Script that adds all arguments to a Python list, and then saves them to a file.
"""


import sys
save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file

try:
    item_list = load_from_json_file('add_item.json')
except Exception:
    item_list = []

for item in sys.argv[1:]:
    item_list.append(item)

save_to_json_file(item_list, 'add_item.json')
