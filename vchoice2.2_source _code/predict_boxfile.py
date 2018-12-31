from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.externals import joblib
import os
import pandas as pd 
import numpy as np 



class PredictModel():
    """docstring for PredictModel"""
    '''
    options:以字典格式传入参数
            options['month']: 月份(int)
            options['directors']:['xxx','xxx'] 字符串列表
            options['actors']:['xxx','xxx']字符串列表
            options['genres']:['武侠','动作']字符串列表
            options['isSequel']: 该电影是否为续集 True/False 

    使用方法：
           new=PredictModel(options)
           result=new.predict()
    '''
    def __init__(self, options):
        self.month=options['month']
        self.directors=options['directors']
        self.actors=options['actors']
        self.genres=options['genres']
        self.isSequel=options['isSequel']

    def reshapeSettings(self):
        self.settings=[]
        self.settings.append(self.month)

        directorBoxfile=joblib.load('data\\model\\directorBoxfile.pickle')
        actorBoxfile=joblib.load('data\\model\\actorBoxfile.pickle')
        director_value=0.0
        actor_value=0.0
        if self.directors is not []:
            for director in self.directors:
                if director in directorBoxfile:
                    director_value+=directorBoxfile[director]
            director_value=director_value/len(self.directors)
        if self.actors is not []:
            for actor in self.actors:
                if actor in self.actors:
                    actor_value+=actorBoxfile[actor]
            actor_value=actor_value/len(self.actors)
        self.settings.append(director_value)
        self.settings.append(actor_value)

        genres=['喜剧','奇幻','古装','动作','惊悚','犯罪','冒险','爱情','科幻','动画','剧情','悬疑',
        '战争','灾难','家庭','历史','运动','传记','武侠','歌舞','恐怖','音乐','纪录片','短片','戏曲','黑色电影','西部']

        genre_vector=[0]*len(genres)
        for i in self.genres:
            if i in genres:
                genre_vector[genres.index(i)]=1
        self.settings+=genre_vector

        if self.isSequel is True:
            self.settings.append(1*32.98)
        else:
            self.settings.append(0)

        month_weight={2: 0.9,7: 0.68805142,12: 0.50963301,9: 0.47076091,1: 0.44998649,6: 0.42800305,4: 0.41731774,3: 0.40943997,
        5: 0.38883641,8: 0.34509157,11: 0.26438609,10: 0.1}
        self.settings.append(month_weight[self.month])

        self.settings=np.asarray(self.settings)

    def predict(self):
        '''
        调取模型，使用三种模型预测的平均值作为预测结果
        '''
        self.reshapeSettings()
        tree_reg = joblib.load('data\\model\\tree_reg.pickle')
        lin_reg = joblib.load('data\\model\\lin_reg.pickle')
        forest_reg = joblib.load('data\\model\\forest_reg.pickle')

        prediction = float(tree_reg.predict([self.settings])+lin_reg.predict([self.settings])+forest_reg.predict([self.settings]))/3
        return prediction