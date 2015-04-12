# -*- coding: utf-8 -*-
"""
Created on Wed Apr 08 18:31:15 2015

@author: alsherman
"""
import pandas as pd
import numpy as np

train_data = r'C:\Users\alsherman\Desktop\GitHub\DataScience_GeneralAssembly\Data\train.csv'
test_data = r'C:\Users\alsherman\Desktop\GitHub\DataScience_GeneralAssembly\Data\test.csv'

train = pd.read_csv(train_data)
test = pd.read_csv(test_data)

train.columns
test['Survived'] = ''
test.columns

data = pd.merge(test,train, how='inner')
data = train.append(test)
data.to_csv(r'C:\Users\alsherman\Desktop\GitHub\DataScience_GeneralAssembly\Data\result.csv')

data.Name[0:5].split(',')

