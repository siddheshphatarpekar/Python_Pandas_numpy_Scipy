# -*- coding: utf-8 -*-
"""

@author: Siddhesh Phatarpekar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv(r'https://raw.githubusercontent.com/siddheshphatarpekar/Dataset/main/Data_Science_Jobs_in_India.csv')
col_company_name = df['company_name'].astype(str)
col_job_title = df['job_title'].astype(str)
col_min_experience = df[(df.min_experience <= 15)]
col_avg_salary = df['avg_salary'].astype(np.float64)
col_min_salary = df['min_salary'].astype(np.float64)
col_max_salary = df['max_salary'].astype(np.float64)
col_num_of_salaries = df['num_of_salaries']


fig, axs = plt.subplots(1, 2, figsize=(12, 5))

axs[0].barh(col_job_title,col_avg_salary)
axs[0].set_xlabel('Salary(Lakhs)')


axs[1].scatter(df.min_experience,col_avg_salary,color='red')
axs[1].set_xlabel('Total Experience')
axs[1].set_ylabel('Salary (lakhs)')

plt.show()
