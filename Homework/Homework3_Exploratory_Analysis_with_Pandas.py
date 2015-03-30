
# coding: utf-8

# ## Homework 3 - Exploratory Data Analysis with Pandas
# 
# Use the automotive mpg data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.csv) 
# to complete the following parts.  Please turn in your code for each part.  Before each code chunk, give a brief description (one line) of what the code is doing (e.g. "Loads the data" or "Creates scatter plot of mpg and weight").  If 
# the code output produces a plot or answers a question, give a brief interpretation of the output (e.g. "This plot shows X,Y,Z" or "The mean for group A is higher than the mean for group B which means X,Y,Z").

# ### Part 1
# Load the data (https://raw.githubusercontent.com/justmarkham/DAT5/master/data/auto_mpg.txt) into a DataFrame.  Try looking at the "head" of the file in the command line to see how the file is delimited and how to load it.

# In[65]:

import pandas as pd
import matplotlib.pyplot as plt
get_ipython().magic(u'matplotlib inline')
import numpy as np

pd.set_option('display.max_rows', 500)

#import data in DataFrame, separated by the pipe symbol
data = pd.read_table(r'C:\Users\alsherman\Desktop\DAT5\data\auto_mpg.txt', sep='|')
data.head()


# ###Part 2
# Get familiar with the data.  Answer the following questions:
# - What is the shape of the data?  How many rows and columns are there?
# - What variables are available?
# - What are the ranges for the values in each numeric column?
# - What is the average value for each column?  Does that differ significantly
#   from the median?

# In[20]:

data.shape #rows, columns


# In[32]:

for var in data.columns: #available variables
    print var


# In[36]:

#calculate the range for each variable
Data_Range = data.describe().T #get the statistical measures and transpose the variables into a single column
Data_Range['range'] = Data_Range['max'] - Data_Range['min'] #create new column with range calculation
Data_Range = Data_Range[['max','min','range']] #subset dataframe to pertinent columns - max, min, and range
Data_Range


# In[27]:

#Determine the average, median, and difference for each (numeric) variable
Average_Temp = []
for i in data.columns:
    if data[i].dtype != object: #exclude non-numeric variables
        Average_Temp.append([i, data[i].mean(), data[i].median(),data[i].mean() - data[i].median()])
Average_Data = pd.DataFrame(Average_Temp,  columns=['variable','average','median','diff'])
Average_Data


# ###Part 3
# Use the data to answer the following questions:
# - Which 5 cars get the best gas mileage?  
# - Which 5 cars with more than 4 cylinders get the best gas mileage?
# - Which 5 cars get the worst gas mileage?  
# - Which 5 cars with 4 or fewer cylinders get the worst gas mileage?

# In[38]:

# Get 5 cars with best mpg by reording data by mpg  
data.sort_index(by='mpg', ascending=False)[0:5][['car_name','mpg']]


# In[39]:

#Get max mpg for 5 cars with > 4 cylinders 
data[data.cylinders > 4].sort_index(by='mpg', ascending=False)[0:5][['car_name','mpg']]


# In[40]:

# Get 5 cars with worst mpg by reordering data by mpg asending == True  
data.sort_index(by='mpg', ascending=True)[0:5][['car_name','mpg']]


# In[41]:

#Get min mpg for 5 cars with <= 4 cylinders 
data[data.cylinders <= 4].sort_index(by='mpg', ascending=True)[0:5][['car_name','mpg']]


# ###Part 4
# Use groupby and aggregations to explore the relationships between mpg and the other variables.  Which variables seem to have the greatest effect on mpg?
# Some examples of things you might want to look at are:
# - What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders, 4 cylinders, 5 cylinders, etc)?
# - Did mpg rise or fall over the years contained in this dataset?
# - What is the mpg for the group of lighter cars vs the group of heaver cars?

# In[46]:

# What is the mean mpg for cars for each number of cylindres (i.e. 3 cylinders, 4 cylinders, 5 cylinders, etc)?
data.groupby('cylinders').mpg.mean()


# In[67]:

# Did mpg rise or fall over the years contained in this dataset?
data.plot(kind='scatter', x='model_year', y='mpg')
# mpg rose over the years 


# In[47]:

# What is the mpg for the group of lighter cars vs the group of heavier cars?


# In[76]:

data.weight.hist()


# In[84]:

data.groupby([data.weight < data.weight.median()]).mpg.mean()

