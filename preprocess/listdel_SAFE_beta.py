#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 11:42:29 2020

@author: sef35id
"""


import glob
import os
import shutil
import pandas as pd
#import datetime as dt
#%%
# function for dir size, considering all subdir and files giving MB
def SAFE_size(start_path = '.'):
    size_sum = 0
    for path, dir_name, file in os.walk(start_path):
        for i in file:
            j = os.path.join(path, i)
            if not os.path.islink(j):
                size_sum += os.path.getsize(j)
    return size_sum/10**6
#print(SAFE_size(), 'MB')
#% /media/sef35id/32e4c67e-ea08-4a4f-a421-d32fb6d7d316/BDC
# collecting SAFE information
dir_list = []
tile_list = []
data_path = []
sensing_date = []
creation_date = []
identifier_list =[]
size = []
for i in glob.glob('/media/sef35id/32e4c67e-ea08-4a4f-a421-d32fb6d7d316/2017/*'):
#for i in glob.glob('/media/data2/S2/*/'):
    dir_list.append(i)

for i in dir_list:
    #for j in glob.glob(i+"*.SAFE"):
    for j in glob.glob(i):
#        print(j)
        data_path.append(j)
        tile_list.append(j.split('/')[5])
for i in data_path:
    sensing_date.append(pd.to_datetime(((i.split('_'))[2])))
    creation_date.append(pd.to_datetime(((i.split('_'))[6].split('.')[0])))
    identifier_list.append(''.join((i.split('_')[5])+(i.split('_')[2].split('T')[0])+(i.split('_')[2].split('T')[1])))
    size.append(SAFE_size(i))
    #
#%%
    #%%

#%
#pd.to_datetime(((data_path[0].split('_'))[6].split('.')[0]))
#% 
# extracts to dataframe and sort all scenes using id 
del_df = pd.DataFrame(zip(identifier_list,sensing_date, #sensing_time, creation_time,
                          creation_date, data_path, size), index=identifier_list,
                        columns=['id','sd','cd','path', 'size'])
del_df = del_df.sort_values(by='id')
del_df
del_df.to_csv('/home/sef35id/Desktop/TEST/delete/deldf.csv')
#%% deletes scenes in wrong dirs
#for i in data_path:
#    if i.split('/')[4] != i.split('_')[5]:
#        print(i)
#        shutil.rmtree(i)
        
#%% deletes data prior timestamp
#del_1516 = []
#sd_list = []
#for i in range(del_df.shape[0]):
#    if del_df.iloc[i,1] < pd.to_datetime('20160331'):
#        sd_list.append(del_df.iloc[i,1])
#        del_1516.append(del_df.iloc[i,3])
#
## data frame and export
##del_1516 = pd.DataFrame(del_1516)    
#del_1516.to_csv('/home/UNI-WUERZBURG.EU/sef35id/Desktop/TEST/delete/deletionlist.csv')
# delete list deletes list
#for i in range(del_1516.shape[0]):
#    print(del_1516.iloc[i,0])
#    shutil.rmtree(del_1516.iloc[i,0])        
#%% write all multiple scenes to dataframe
id_false = del_df[del_df.duplicated('id', keep=False)]
id_false.to_csv('/home/sef35id/Desktop/TEST/delete/id_false.csv')
#%%
# sorting id and size ascending
id_false_sort = id_false.sort_values(by=['id', 'size'])
id_false_sort.to_csv('/home/sef35id/Desktop/TEST/delete/id_false_sort.csv')
#%%
# get bigger scenes
id_false_sort_big = id_false_sort[id_false_sort.duplicated('id', keep='last')]
id_false_sort_big.to_csv('/home/sef35id/Desktop/TEST/delete/id_false_sort_big.csv')
#%%
# delete double ones
for i in range(id_false_sort_big.shape[0]):
#    print(id_false_sort_big.iloc[i,3])
    shutil.rmtree(id_false_sort_big.iloc[i,3])
#%% # # # # # # # # # # # # # # # #  # # # # # # # # # # # # # # # # 
 # # # # # # # # # # # # # # # # 
# similar to above, using a filename template

data_2015 = pd.read_csv('/home/sef35id/Desktop/2015.csv', header = None)
#%%

tile2_list = []
data2_path = []
sensing2_date = []
creation2_date = []
identifier2_list =[]
size = []
for i in range(len(data_2015)):
    #print(data_2015.loc[i, 0].split('/')[8])
    tile2_list.append(data_2015.loc[i, 0].split('/')[8])
#%%
for i in tile2_list:
    sensing2_date.append(pd.to_datetime(((i.split('_'))[2])))
    creation2_date.append(pd.to_datetime(((i.split('_'))[6].split('.')[0])))
    identifier2_list.append(''.join((i.split('_')[5])+(i.split('_')[2].split('T')[0])+(i.split('_')[2].split('T')[1])))
    #

del_df2 = pd.DataFrame(zip(identifier2_list,sensing2_date, #sensing_time, creation_time,
                          creation2_date,), index=identifier2_list,
                        columns=['id','sd','cd'])
del_df2 = del_df2.sort_values(by='id')
del_df2
del_df2.to_csv('/home/sef35id/Desktop/TEST/delete/deldf2.csv')


#%% write all multiple scenes to dataframe
id_false2 = del_df2[del_df2.duplicated('id', keep = 'first')]
id_false2.to_csv('/home/sef35id/Desktop/TEST/delete/id_false2.csv')
#%%
# sorting id and size ascending
id_false_sort2 = id_false2.sort_values(by=['id', 'cd'])
id_false_sort2.to_csv('/home/sef35id/Desktop/TEST/delete/id_false_sort2.csv')
#%%