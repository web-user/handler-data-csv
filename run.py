import argparse

import pandas as pd

# create dataframe from csv
task_data = pd.read_csv("test_task_data.csv")

# create dict from dataframe
studentDict = task_data.to_dict('list')
parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('--fields', '--list', nargs='+', help='fields help')
args = parser.parse_args()

# getting arguments 
data_parse_args = [value for _, value in parser.parse_args()._get_kwargs()][0]

data = {value: '' for value in data_parse_args}

try:
	for item in data_parse_args:
		data[item] = task_data[item]
	print(data)
except Exception as e:
	print(f'Error: {repr(e)}')
