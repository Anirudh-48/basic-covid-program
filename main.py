import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model
from tkinter import *
file_inf=""
state1=""
def file(state):
    global state1
    state1+=state
    

def fun1():
    covid19_df=pd.read_csv("covid_19_india.csv")
    covid19_df_latest = covid19_df[covid19_df['State/UnionTerritory']==state1]
    covid19_df_latest.head()
    covid19_df_latest = covid19_df_latest.sort_values(by=['Confirmed'], ascending = True)
    plt.figure(figsize=(20,10), dpi=80)
    plt.bar(covid19_df_latest['Date'][-10:], covid19_df_latest['Confirmed'][-10:],align='center',color='lightgrey')
    plt.ylabel('Number of Confirmed Cases', size = 12)
    plt.title('A graphical representation of number of cases in '+state1, size = 16)
    plt.show()
    temp=covid19_df_latest['Deaths'].sum()
    temp1=covid19_df_latest['Cured'].sum()
    print("Deaths:"+str(temp))
    print("Cured:"+str(temp1))
def state():
    statewise_df=pd.read_csv('StatewiseTestingDetails.csv')
    statewise_df_latest=statewise_df[statewise_df['Date']=="2020-09-28"]
    statewise_df_latest.head()
    statewise_df_latest=statewise_df_latest.sort_values(by=['Positive'],ascending=False)
    plt.figure(figsize=(25,15),dpi=155)
    plt.bar(statewise_df_latest['State'][:-10],statewise_df_latest['Positive'][:-10],color='lightblue')
    plt.show()
    temp1=statewise_df_latest['Positive'].sum()
    print("Positive cases: "+str(int(temp1)))
def predict():
    global state1
    covid19_df=pd.read_csv("covid_19_india.csv")
    covid19_df_latest = covid19_df[covid19_df['State/UnionTerritory']==state1]
    X=np.c_[covid19_df_latest['Deaths']]
    Y=np.c_[covid19_df_latest['Cured']]
    model=sklearn.linear_model.LinearRegression()
    model.fit(X,Y)
    print("Enter number of deaths to estimate the number of cured people in the state: "+str(state1))
    X_new=[[int(input())]]
    print(model.predict(X_new))

top=Tk()
Label(top,text='Enter the state name').pack(side=TOP)
ent1=Entry(top)
ent1.pack(side=TOP)
btn=Button(top,text="Submit",command= lambda:file(ent1.get()))
btn.pack(side=TOP)
top.mainloop()
fun1()
state()
predict()
