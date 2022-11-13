import sqlite3, re, numpy as np, pandas as pd, matplotlib.pyplot as plt

acr_to_name = {
    'BE':'Belgium', 
    'EL':'Greece',
    'LT':'Lithuania',
    'PT':'Portugal',
    'BG':'Bulgaria',
    'ES':'Spain',
    'LU':'Luxembourg',
    'RO':'Romania',
    'CZ':'Czechia',
    'FR':'France', 
    'HU':'Hungary',
    'SI':'Slovenia',
    'DK':'Denmark',
    'HR':'Croatia',
    'MT':'Malta',
    'SK':'Slovakia',
    'DE':'Germany',
    'IT':'Italy',
    'NL':'Netherlands',
    'FI':'Finland',
    'EE':'Estonia',
    'CY':'Cyprus',
    'AT':'Austria',
    'SE':'Sweden',
    'IE':'Ireland',
    'LV':'Latvia',
    'PL':'Poland',
    'EU28':'Enlargement of the European Union', 
    'IS':'Iceland',
    'NO':'Norway',
    'LI':'Liechtenstein',
    'CH':'Switzerland', 
    'ME':'Montenegro',
    'MK':'North Macedonia', 
    'AL':'Albania',
    'RS':'Serbia',
    'TR':'Türkiye',
    'EU27_2020':'European Union after UK exit',
    'EA19':'Euro Area 2019',
    'UK':'United Kingdom', 
    'EU15': 'European Union 2015'
}

def createTableStatement(tableName, columns, types):
  return f"CREATE TABLE IF NOT EXISTS {tableName} ('{columns[0]}' {types[0]}" + (
      ", {} {}"*(len(columns)-1)).format(*[i for j in zip(columns[1:], types[1:]) for i in j]) + ")"
