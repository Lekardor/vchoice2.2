import pandas as pd
import numpy as np
def split_years(years,combined_data_path):
	'''
	params:years(list of years)
		   combined_data_path
	return: different year's data.csv
	'''
	combined_data=pd.read_csv('combined_data_path')
	for year in years:
		combined_data[combined_data['year']==year].to_csv('data\\data_{}.csv'.format(year),index=False)


def combine_years(years,combined_data_path):
	'''
	params: years(list of years)
			combined_data_path(target path for storing combined_data)
	'''
	combined_data=pd.read_csv('data\\data_{}.csv'.format(years[0]),encoding='GBK')
	for year in years[1:]:
		year_df=pd.read_csv('data\\data_{}.csv'.format(year),encoding='GBK')
		combined_data=pd.concat([combined_data,year_df],ignore_index=True)
	combined_data.to_csv(combined_data_path,index=False)

def extract_actors(path='data\\actor.csv'):
	data=pd.read_csv('data\\data.csv')
	actors=data.actor.unique()
	Actors=[]
	for group in actors:
		sets=group.split(',')
		for man in sets:
			if man not in Actors:
				Actors.append(man)
	Actors=pd.Series(Actors)
	Actors.to_csv(path,index=None)