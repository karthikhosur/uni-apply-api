import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestRegressor 
from sklearn import metrics
import pickle

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

    #print(My_prediced_chance)
    rate_int = float(My_prediced_chance[0]*100)
    
    return rate_int

