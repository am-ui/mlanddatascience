# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:15:58 2020

@author: AMIT
"""

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib as plt
from matplotlib.subplots import make_subplots
import matplotlib.graph_objects as go
import matplotlib.graph_objs as go
import warnings
warnings.filterwarnings("ignore")

# Input data files are available in the "../input/" directory.
# For example, running this (by clicking run or pressing Shift+Enter) will list all files under the input directory

import os
for dirname, _, filenames in os.walk('/kaggle/input'):
    for filename in filenames:
        print(os.path.join(dirname, filename))

# Any results you write to the current directory are saved as output.
df = pd.read_csv(r"C:\Users\AMIT\Desktop\2019-coronavirus-dataset-01212020-01262020"
                 )
df.head()
#Format Dataset
#Format Date and Time Column
#Rename Column Name
#Drop Sno Column
df['Date'] = df['Date'].apply(pd.to_datetime)
df['Last Update'] = df['Last Update'].apply(pd.to_datetime)
df = df.rename(columns={'Last Update':'Last_Update'})
df.drop(columns='Sno',axis=1,inplace=True)
df.head()
#Feature Engineering - I
#Get Day and Month from Data-Time Column
#Through this technique, we can analyze spread of Corono Virus with respect to time (i.e. from January to February, 2020).

df['ev_month'] = [df.Date[i].month for i in range(df.shape[0])]
df['ev_day']   = [df.Date[i].day   for i in range(df.shape[0])]
df.drop(columns='Date',axis=1,inplace=True)

df['ls_month'] = [df.Last_Update[i].month for i in range(df.shape[0])]
df['ls_day']   = [df.Last_Update[i].day   for i in range(df.shape[0])]
df.drop(columns='Last_Update',axis=1,inplace=True)

df.head()
#Feature Engineering - II
#Mainland China and China are same, thus renaming the entries.

df.Country[df.Country=='Mainland China']='China'
df.groupby('Country').sum()[['Confirmed','Deaths','Recovered']]

#Impact of Novel Corona Virus (Outside China)
#China has the highest number of records of Corona Virus infection confirmation, when compared to rest of the world. Therefore, the numbers obtained for China is out of scale from rest of the World, as of now. Thus, special attention is given on China in subsequent analysis, while currently focussing on rest of the world.

df_wc = df[df.Country!='China']
g= df_wc.groupby('Country').sum()[['Confirmed','Deaths','Recovered']]

fig = make_subplots(rows=3, cols=1,subplot_titles=("Confirmed", "Deaths", "Recovered"))
fig.add_trace(go.Bar(x=g.index, y=g.Confirmed),row=1, col=1)
fig.add_trace(go.Bar(x=g.index, y=g.Deaths   ),row=2, col=1)
fig.add_trace(go.Bar(x=g.index, y=g.Recovered),row=3, col=1)
fig.update_layout(height=700, width=1000, title_text="Corona Virus Report (Except China)")
fig.show()

#Impact of Novel Corona Virus (Within China)
#By focussing on China, we can have a much granular view i.e. state-wise assesment of the infection. This will expedite the search for origin of virus.

g = df[df.Country=='China'].groupby('Province/State').sum()[['Confirmed','Deaths','Recovered']]
fig = make_subplots(rows=3, cols=1,subplot_titles=("Confirmed", "Deaths", "Recovered"))
fig.add_trace(go.Bar(x=g.index, y=g.Confirmed),row=1, col=1)
fig.add_trace(go.Bar(x=g.index, y=g.Deaths   ),row=2, col=1)
fig.add_trace(go.Bar(x=g.index, y=g.Recovered),row=3, col=1)
fig.update_layout(height=800, width=1000, title_text="Corona Virus Report (In States of China)")
fig.show()


g = g[g.Confirmed<max(g.Confirmed)]
fig = make_subplots(rows=3, cols=1,subplot_titles=("Confirmed", "Deaths", "Recovered"))
fig.add_trace(go.Bar(x=g.index, y=g.Confirmed),row=1, col=1)
fig.add_trace(go.Bar(x=g.index, y=g.Deaths   ),row=2, col=1)
fig.add_trace(go.Bar(x=g.index, y=g.Recovered),row=3, col=1)
fig.update_layout(height=700, width=1000, title_text="Corona Virus Report (In States of China)")
fig.show()


print("Granular view for following nations were available\n")
g4 = df[df.Country=='Australia'].groupby('Province/State').sum()[['Confirmed','Deaths','Recovered']]
print("\nStats for Australia\n",'_'*50,'\n',g4)
g4 = df[df.Country=='US'].groupby('Province/State').sum()[['Confirmed','Deaths','Recovered']]
print("\nStats for United States of America\n",'_'*50,'\n',g4)


#Growth of Corona Virus across Time in China
dft = df[df.Country=='China']
g1 = pd.DataFrame(dft[['Country','ev_day','ev_month','Confirmed']].groupby(['ev_month','ev_day']).sum()['Confirmed'])

a=[i for i in range(g1.shape[0])]

fig = px.bar(x=a, y=g1.Confirmed)
fig.update_layout(height=300, width=800, title_text="Corona Virus (In China)")

fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [i for i in range(g1.shape[0]+1)],
        ticktext = g1.index
    )
)
fig.show()

#Growth of Corona Virus across Time outside China
dft = df[df.Country!='China']
g2 = pd.DataFrame(dft[['Country','ev_day','ev_month','Confirmed']].groupby(['ev_month','ev_day']).sum()['Confirmed'])

a=[i for i in range(g1.shape[0])]

fig = px.bar(x=a, y=g2.Confirmed)
fig.update_layout(height=300, width=800, title_text="Corona Virus (Rest of the World)")
fig.update_layout(
    xaxis = dict(
        tickmode = 'array',
        tickvals = [i for i in range(g1.shape[0]+1)],
        ticktext = g1.index
    )
)
fig.show()
