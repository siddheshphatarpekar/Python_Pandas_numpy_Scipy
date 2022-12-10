#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 04:06:48 2022

@author: admini
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from tabulate import tabulate

rdf = pd.read_csv(r'https://raw.githubusercontent.com/siddheshphatarpekar/Dataset/main/IPL_deliveries_list_Batsmen_Data.csv',
                  usecols=['batting_team','batsman','bowler','batsman_runs','total_runs'])
ipl_team_total_run = pd.pivot_table(rdf,index=['batting_team']
                                    ,values=['total_runs']
                                    ,aggfunc=np.sum).sort_values(by=['total_runs'],ascending=False)


ipl_batsman_total_run = pd.pivot_table(rdf,index=['batting_team','batsman']
                                    ,values=['total_runs']
                                    ,aggfunc=np.sum).sort_values(by=['total_runs','batting_team'],ascending=False)


print('Top_Scoring_teamm_IPL')
print(ipl_team_total_run)
print('Top_Ten_Batsman_IPL')
print(ipl_batsman_total_run.head(10))