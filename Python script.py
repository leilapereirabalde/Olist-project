
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import random as r

#Q1
df = pd.read_csv("C:\\Users\\LeilaP(DA-LON13)\\Desktop\\Python\\Project\\GP_A11b 1.csv", header = 0)
df.columns = ['Region', 'CountryRegion', 'total_sales']
fig = plt.figure(figsize=(8, 5))
plt.bar(df.Region, df.total_sales)
#plt.bar_label()
plt.xlabel('Regions in US')
plt.ylabel('Total Sales in millions')
plt.title('Total Sales by Region in US')
plt.show()


#Q2
df = pd.read_csv("C:\\Users\\LeilaP(DA-LON13)\\Desktop\\Python\\Project\\GP_A22 1.csv", header = 0)
fig = plt.figure(figsize=(8,5))
plt.scatter(df.annual_leave,df.bonus)
#plt.scatter_label()
plt.xlabel('Annual Leave(in hours)')
plt.ylabel('Bonus(in $)')
plt.title('Relationship between Bonus & Annual Leave')
z = np.polyfit(df.annual_leave, df.bonus, 1)
p = np.poly1d(z)
plt.plot(df.annual_leave,p(df.annual_leave))
plt.show()


#Q3
df = pd.read_csv("C:\\Users\\LeilaP(DA-LON13)\\Desktop\\Python\\Project\\GP_A33.csv", header = 0)
fig = plt.figure(figsize=(8,5))
#plt.plot_label()
plt.plot(df.Name, df.total_sum)
for i, value in enumerate(df.total_sum):
    plt.annotate(f"{value:,}", (df.Name[i], df.total_sum[i]), textcoords="offset points", xytext=(30, -20), ha='right', rotation = 45)
 
plt.title('Total Sales per Country')
plt.xlabel('Country')
plt.ylabel('Total Sales(in millions)')
plt.xticks(rotation = 90)
plt.show()


#Q4
df = pd.read_csv("C:\\Users\\LeilaP(DA-LON13)\\Desktop\\Python\\Project\\GP_A44 1.csv", header = 0)
fig = plt.figure(figsize=(8,5))
plt.barh(df.JobTitle, df.average_hours)
plt.xlabel('Average Sick Leave Hours')
plt.ylabel('Job Title', fontsize = 1)
plt.title('Average Sick Leave Hours per Job Title')
plt.xticks(rotation = 45)
plt.show()

#Q4 additional 
df = pd.read_csv("C:\\Users\\LeilaP(DA-LON13)\\Desktop\\Python\\Project\\Additional_1.csv", header=0)
fig = plt.figure(figsize=(8, 5))
plt.pie(
    df['SickLeaveHours'],              
    labels=df['OrganizationLevel'],
    autopct='%1.1f%%',
    startangle=90
)
plt.title('Average Sick Leave Hours per Job Level')
plt.axis('equal')
plt.show()

#Q5
df = pd.read_csv("C:\\Users\\LeilaP(DA-LON13)\\Desktop\\Python\\Project\\GP_A55.csv", header = 0)
years = []

for year in df.YearOpened:
    if year < 1980:
        years.append(year)
    elif 1980 <= year < 1990:
        years.append(year)
    elif 1990 <= year < 2000:
        years.append(year)
    else:
        years.append(year)

plt.scatter(df.YearOpened ,df.AnnualRevenue)
#ticks = ['1970','1980','1990','2000']
plt.grid(axis = 'y')
#plt.xticks(np.arange(4), labels = ticks)
plt.title('Trade duration by annual revenue')
plt.show()



#Q6
df = pd.read_csv("C:\\Users\\LeilaP(DA-LON13)\\Desktop\\Python\\Project\\GP_A66 2.csv", header = 0)
fig = plt.figure(figsize=(8,5)) 
color= []

for val in df.AnnualRevenue:
    if val < 99999:
        color.append('red')
    elif 100000 <= val <= 199999:
        color.append('orange')
    else:
        color.append('blue')
plt.scatter(x = df.NumberEmployees, y = df.store_size_sqfeet, s = np.array(df.AnnualRevenue) / 1000, c = color, alpha = 0.2)

z = np.polyfit(df.NumberEmployees, df.store_size_sqfeet, 1)
p = np.poly1d(z)
plt.plot(df.NumberEmployees,p(df.NumberEmployees))
plt.xlabel('Number of Employees')
plt.ylabel('Store Size')
plt.title('Relationship of store size, employee count and revenue')
plt.legend()

plt.grid(True)

plt.show()