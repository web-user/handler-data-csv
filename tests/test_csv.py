# content of test_csv.py

import pandas as pd


def data():
	studentDf = pd.read_csv("test_task_data.csv")
	# create dict from dataframe
	return studentDf.to_dict('list')


def test_dict_data():
    if not isinstance(data(), dict):
        raise TypeError('Please provide a string argument')
      