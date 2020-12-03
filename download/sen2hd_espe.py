#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 20 10:59:01 2020

@author: sef35id

Download of Sentinel-2 products covering Bavaria 

Project: <PROJECT ID>
Username: <USER>
Password: <YOUR PASSWORD>
E-mail: <FOUR EMAIL>
Firstname: <YOUR FN>
Lastname: <YOUR LN>

#%% is a spyder-editor cell
 
"""
from sentinelsat import SentinelAPI
import click


# points, used for tile search
points = ['POINT(10 51)', # 32UNB
 'POINT(11 51)', # 32UPB
 'POINT(8 50)', # 32UMA
 'POINT(10 50)', # 32UNA
 'POINT(11 50)', # 32UPA
 'POINT(12 50)', # 32UQA
 'POINT(10 49)', # 32UNV 
 'POINT(11 49)', # 32UPV
 'POINT(12 49)', # 32UQV 
 'POINT(13.5 49)', # 33UUQ   
 'POINT(14 49)', #  33UVQ
 'POINT(10 48)', # 33UNU
 'POINT(11 48)', # 32UPU
 'POINT(12 48)', # 32UQU
 'POINT(13.5 48)', # 33UUP 
 'POINT(14 48)', # 33UVP
 'POINT(10 47)', # 32TNT
 'POINT(11 47)', # 32TPT
 'POINT(12 47)', # 32TQT
 'POINT(13.5 47)'] # 32TUN
#
user = 'USER'
password = 'PASSWORD'
api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
products = {}  
#%%

@click.command()
@click.option('--product', default='S2MSI2A', help='Sentinel-2 Product to Downaload. Default <S2MSI2A> ')
@click.option('--output', default='~/Desktop', help='Output directory. Default <~/Desktop>')

def sen2hd(product, output):
     
    for q in points:
        products.update(api.query(q,
                                  date=('NOW-7DAYS', 'NOW'),
                                  producttype=product,
                                  cloudcoverpercentage=(0,100)))
        
    api.download_all(products, output)
        
if __name__ == '__main__':
    sen2hd()
    
#%%
#for q in points:
 #        products.update(api.query(q,
  #                                date=('NOW-1DAYS', 'NOW'),
   #                               producttype='S2MSI2A',
    #                              cloudcoverpercentage=(0,100)))
#        api.download_all(products, output)
