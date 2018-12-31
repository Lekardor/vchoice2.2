import pandas as pd

class sift:
    def __init__(self,path="data\\"):
        years = ["2018", "2017", "2016", "2015"]
        self.films=pd.DataFrame()
        for year in years:
            self.films=self.films.append(pd.read_csv(path+"data_"+year+".csv",encoding='gbk'))
        self.films.index=range(self.films.shape[0])
        for x in ['director','actor','genre']:
            self.films[x]=self.films[x].apply(lambda x:x.split(','))

    def find(self,option,target,sortby='boxfile',reverse=True):
        #option is name ,director,genre,actor
        #target is what you want to find
        #sortby is how to sort
        #the max length of res is maxlen
        #if reverse is true , res is descending 
        dicname = ["name", "year", "month", "boxfile", "director", "actor", "genre", "score"]
        if option=='name' or option=='director' or option=='genre' or option=='actor':
            res=[]
            for i in range(self.films.shape[0]):
                if target in self.films.iloc[i][option]:
                    res.append(self.films.iloc[i])
            if sortby=='boxfile':
                res=sorted(res,key=lambda x:x[3],reverse=reverse)
            else:
                res=sorted(res,key=lambda x:x[-1],reverse=reverse)
            res = list(map(lambda x:{i:j for i,j in zip(dicname,x)},res))
            return res

s=sift()
print(s.find('actor','舒淇',"score"))
