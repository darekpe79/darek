#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 17:39:32 2021

@author: darek
"""

import requests

url = "https://api-football-v1.p.rapidapi.com/v2/teams/league/"

headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': "3e405b6251mshd60581ae73af7bap1e26e1jsn43625ecf6667"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
#%%
import requests

url = "https://api-football-beta.p.rapidapi.com/teams"

querystring = {"season":"2019","l":"39"}

headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': "3e405b6251mshd60581ae73af7bap1e26e1jsn43625ecf6667"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)
import requests

url = "https://api-football-beta.p.rapidapi.com/leagues"

querystring = {"country":"poland"}

headers = {
    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
    'x-rapidapi-key': "3e405b6251mshd60581ae73af7bap1e26e1jsn43625ecf6667"
    }

response = requests.request("GET", url, headers=headers, params=querystring).json()

print(response)
#%%
import requests
import pandas as pd
import json
import streamlit as st
import plotly.express as px
from PIL import Image
#url = "https://api-football-beta.p.rapidapi.com/teams/statistics"

#querystring = {"team":"3498","season":"2021","league":"107"}

#headers = {
#    'x-rapidapi-host': "api-football-beta.p.rapidapi.com",
#    'x-rapidapi-key': "3e405b6251mshd60581ae73af7bap1e26e1jsn43625ecf6667"
#    }

#response = requests.request("GET", url, headers=headers, #params=querystring)
#print(response.text)

#with open("sample.json", "w") as outfile:
#    outfile.write(response.text)
#%%
with open('sample.json', 'r') as openfile:
 
    # Reading from json file
    json_object = json.load(openfile)
 
print(json.dumps(json_object, indent=4))
forma=json_object['response']['form']
fixtures=json_object['response']['fixtures']
pd1=pd.DataFrame.from_dict(fixtures)
goals=json_object['response']['goals']
#goals FOR
goals2=json_object['response']['goals']['for']['average']
golas3=json_object['response']['goals']['for']['total']
averagegoals={}
averagegoals['avereage_goals_for']={}
averagegoals['avereage_goals_for']=goals2
totalgoals={}
totalgoals['total_goals_for']={}
totalgoals['total_goals_for']=golas3
#goals Against
goalsagainst2=json_object['response']['goals']['against']['average']
golasagainst3=json_object['response']['goals']['against']['total']
averagegoalsagainst={}
averagegoalsagainst['avereage_goals_against']={}
averagegoalsagainst['avereage_goals_against']=goalsagainst2
totalgoalsagainst={}
totalgoalsagainst['total_goals_against']={}
totalgoalsagainst['total_goals_against']=golasagainst3
#Merging Dictionaries
averagegoals.update(totalgoals)
averagegoalsagainst.update(totalgoalsagainst)
averagegoals.update(averagegoalsagainst)
pd2=pd.DataFrame.from_dict(averagegoals)
#print(pd1)
#print(pd2) 
#minutes Goals For, Against
goalsforminutes=json_object['response']['goals']['for']['minute']
pd3=pd.DataFrame.from_dict(goalsforminutes)
df_goalsforminutes = pd3.rename(index={'total': 'total_for', 'percentage':'percentage_for'})
golasagainstminutes=json_object['response']['goals']['against']['minute']
#df_goalsforminutes.drop('index1',axis='columns')
pd4=pd.DataFrame.from_dict(golasagainstminutes)
df_goalsagainstminutes = pd4.rename(index={'total': 'total_against', 'percentage':'percentage_against'})
result = df_goalsforminutes.append(df_goalsagainstminutes)
#%% streamlit run sportAPI.py
st.set_page_config(page_title='ŁKS STATISTICS',layout='wide')

st.header('Form: '+forma)
st.header('Fixtures')
#pd1['index1'] = pd1.index
#cols = pd1.columns.tolist()
#cols = cols[-1:] + cols[:-1]
#pd1=pd1[cols]
#df_reset=pd1.reset_index(drop=True)

st.dataframe(pd1)

fig = px.bar(pd1, x=['wins','draws','loses'], y=["home", "away", "total"], title="Played Games")
st.plotly_chart(fig)
st.header('Goals')
def left_align(df):
    left_aligned_df = df.style.set_properties(**{'text-align': 'left'})
    left_aligned_df = left_aligned_df.set_table_styles(
        [dict(selector='th', props=[('text-align', 'left')])]
    )
    return left_aligned_df
left_align(pd2)


st.table(pd2)
#df_goalsforminutes[df_goalsforminutes.columns] = df_goalsforminutes.apply(lambda x: x.str.strip('%'))
df_goalsforminutes.replace('%', '', regex=True, inplace=True)
df_goalsforminutes=df_goalsforminutes.astype(float)


df_goalsforminutes = df_goalsforminutes.round(decimals = 2)

st.header('Goals For, Minutes')
st.table(df_goalsforminutes.style.format({'0-15': '{:.1f}', '16-30': '{:.1f}', '31-45': '{:.1f}','46-60':'{:.1f}','61-75':'{:.1f}','76-90':'{:.1f}', '91-105':'{:.1f}','106-120':'{:.1f}'}))
#st.dataframe(df_goalsforminutes)
df_goalsagainstminutes.replace('%', '', regex=True, inplace=True)
df_goalsagainstminutes=df_goalsagainstminutes.astype(float)
st.header('Goals Against, Minutes')
st.table(df_goalsagainstminutes.style.format({'0-15': '{:.1f}', '16-30': '{:.1f}', '31-45': '{:.1f}','46-60':'{:.1f}','61-75':'{:.1f}','76-90':'{:.1f}', '91-105':'{:.1f}','106-120':'{:.1f}'}))
#st.dataframe(df_goalsforminutes)


##df['col'] = df['col'].str.rstrip('%').astype('float') / 100.0
