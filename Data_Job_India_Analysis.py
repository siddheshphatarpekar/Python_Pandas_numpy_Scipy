import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

df=pd.read_csv(r'https://github.com/siddheshphatarpekar/Dataset/blob/main/Data_Science_Jobs_in_India.csv')
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


get_cmp_name = input("Enter Company Name :")
get_job_title = input("Enter Job Title :")
top10_ = df.nlargest(10,'avg_salary')
cmp_name = df.loc[(df['company_name'] == get_cmp_name) & (df['job_title'] == get_job_title)]

print(tabulate(cmp_name,headers='keys',tablefmt='noSQL'))