#!/usr/bin/env python
# coding: utf-8

# In[52]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from mpl_toolkits.mplot3d import Axes3D
import plotly.graph_objs as go
import seaborn as seabornInstance 
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 
from sklearn import metrics
import pickle


# In[53]:


def university_evaluation(gre, toefl, uni_rate, sop_rate, lor_rate, cgpa, research):    
    
    Pkl_Filename = "Pickle_RL_Model.pkl"  
    with open(Pkl_Filename, 'rb') as file:  
        rf = pickle.load(file)


    my_chance1=[gre, toefl, uni_rate, sop_rate, lor_rate, cgpa, research]
    creds=np.array(my_chance1)
    my_chance=creds.reshape(-1, 7)
    My_prediced_chance = rf.predict(my_chance)
    #print(My_prediced_chance)

    low_margin = 0.14
    high_margin = 0.10
    score = abs(uni_rate - 3)

    if uni_rate > 3:
        if (gre > 325) or (cgpa > 9):
            My_prediced_chance = My_prediced_chance
        else:
            My_prediced_chance -= score*high_margin

    else :
        My_prediced_chance +=score*low_margin
        if My_prediced_chance > 0.95:
            My_prediced_chance -= 3*score

    final_rating = int(My_prediced_chance)
    #print(My_prediced_chance)
    rate_int = float(My_prediced_chance[0]*100)
    
    return rate_int


# In[21]:


#With a Gre score of 315, TOEFL score of 105, University Rating of 4, SOP of score 4, 4 LORs, CGPA of 9.5 and having research papers, What are the chances of me getting into my dream University?  


# In[51]:





# In[ ]:




