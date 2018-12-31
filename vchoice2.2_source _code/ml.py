import pandas as pd 
import numpy as np 
import re
import os
import pickle
from sklearn.externals import joblib

data=pd.read_csv("data\\data.csv")


def isSequel(film,sequel):
    if film['name'] in sequel:
        return 1
    else:
        return 0

def AddSequelMark(data):
    all_names=list(data.name)
    regex=re.compile(r'^(.)*\d：(.)*|^.*\d$')
    sequel=[]
    for i in all_names:
        if regex.search(i) is not None:
            sequel.append(i)
    #mark all sequels
    data['isSequel']=data.apply(isSequel,axis=1,sequel=sequel)
    return data

def getAllDirectors(data):
    directors=[]
    for i in data.director:
        names=i.split(',')
        for name in names:
            if name not in directors:
                directors.append(name)
    return directors

def getAllActors(data):
    actors=[]
    for i in data.actor:
        names=i.split(',')
        for name in names:
            if name not in actors:
                actors.append(name)
    return actors

def getAllGenres(data):
    genres=[]
    for i in range(data.shape[0]):
        entry=data.iloc[i]
        genre=entry['genre'].split(',')
        for i in genre:
            if i not in genres:
                genres.append(i)
    return genres

directors=getAllDirectors(data)
actors=getAllActors(data)
genres=getAllGenres(data)

def boxfileContribution(data):
    from collections import OrderedDict
    directorBoxfile={}
    actorBoxfile={}
    for i in range(data.shape[0]):
        directors=data.iloc[i].director.split(',')
        actors=data.iloc[i].actor.split(',')
        boxfile=data.iloc[i]['boxfile']
        for director in directors:
            if director not in directorBoxfile:
                directorBoxfile[director]=boxfile
            else:
                directorBoxfile[director]+=boxfile
        for actor in actors:
            if actor not in actorBoxfile:
                actorBoxfile[actor]=boxfile
            else:
                actorBoxfile[actor]+=boxfile
    return directorBoxfile,actorBoxfile

directorBoxfile,actorBoxfile=boxfileContribution(data)

joblib.dump(directorBoxfile,'data\\model\\directorBoxfile.pickle')
joblib.dump(actorBoxfile,'data\\model\\actorBoxfile.pickle')

def topMonth(data):
    #Statics for 12 months
    #filter: ordered by average boxfile per month
    from collections import OrderedDict
    topMonth={}
    for i in range(data.shape[0]):
        month=data.iloc[i]['month']
        value=data.iloc[i].boxfile
        if month not in topMonth:
            topMonth[month]=[0,0]
        topMonth[month][0]+=value
        topMonth[month][1]+=1
    for m in topMonth.keys():
        topMonth[m][1]=topMonth[m][0]/topMonth[m][1]
    topMonth=OrderedDict(sorted(topMonth.items(),key=lambda t:t[1][1],reverse=True))
    return topMonth

boxfileDistribution=topMonth(data)

def add_weight_month(film,month_weight):
    month=film['month']
    return month_weight[month][0]

def AddWeightMonth(data,boxfileDistribution):
    x=list(boxfileDistribution.keys())
    y=[i[1] for i in list(boxfileDistribution.values())]

    from sklearn.preprocessing import MinMaxScaler
    minMaxScaler = MinMaxScaler((0.1,0.9))
    month_weight=minMaxScaler.fit(np.asarray(y).reshape(-1,1))
    month_weight=minMaxScaler.transform(np.asarray(y).reshape(-1,1))
    month_weight=dict(zip(x,list(month_weight)))

    data['monthWeight']=data.apply(add_weight_month,axis=1,month_weight=month_weight)
    return data

'''
add new data 
'''
data=AddSequelMark(data)
data=AddWeightMonth(data,boxfileDistribution)

def dimension_reduced(data,directorBoxfile,actorBoxfile):
    train_data=pd.DataFrame(data,columns=['month','director','actor','genre','isSequel','monthWeight'])
    train_data=np.asarray(train_data)

    train_label=data['boxfile']
    train_label=np.asarray(train_label)

    for entry in train_data:
        actor_names=entry[2].split(',')
        director_names=entry[1].split(',')
        genre=entry[3].split(',')
        
        actor_value=0.0
        director_value=0.0
        genre_vector=[0]*len(genres)
        for name in actor_names:
            actor_value+=actorBoxfile[name]
        entry[2]=actor_value/len(actor_names)
        
        for name in director_names:
            director_value+=directorBoxfile[name]
        entry[1]=director_value/len(director_names)
        
        for i in genre:
            index=genres.index(i)
            genre_vector[index]=1
        entry[3]=genre_vector
    
    new_train_data=list(train_data)
    for i in range(len(new_train_data)):
        entry=new_train_data[i]
        new_train_data[i]=[entry[0],entry[1],entry[2]]+entry[3]+[32.98*entry[4],entry[5]]
    train_data=np.asarray(new_train_data)
    return train_data,train_label


'''
分割训练集和测试集，比例4:1
'''
x_data,y_data=dimension_reduced(data,directorBoxfile,actorBoxfile)
x_train=x_data[:800]
y_train=y_data[:800]
x_val=x_data[800:]
y_val=y_data[800:]

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

tree_reg=DecisionTreeRegressor()
tree_reg.fit(x_data,y_data)

lin_reg=LinearRegression()
lin_reg.fit(x_data,y_data)

forest_reg=RandomForestRegressor()
forest_reg.fit(x_data,y_data)

# 保存模型
if not os.path.exists('data\\model'):
    os.makedirs('data\\model')
joblib.dump(tree_reg, "data\\model\\tree_reg.pickle")
joblib.dump(lin_reg,'data\\model\\lin_reg.pickle')
joblib.dump(forest_reg,'data\\model\\forest_reg.pickle')


def check_model():
    if os.path.exists("data\\model\\tree_reg.pickle"):
        if os.path.exists("data\\model\\lin_reg.pickle"):
            if os.path.exists('data\\model\\forest_reg.pickle'):
                print('All models has trained')
check_model()