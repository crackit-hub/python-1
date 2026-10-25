import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns



df=pd.read_csv("Diwali Sales Data.csv",encoding="latin1")
print(df)
print (df.info)


# to drop colm

print(df.columns)
df.drop(['Status', 'unnamed1'],axis=1,inplace=True)
print(df)

#inspectnull values

print(pd.isnull(df).sum())

df.dropna(inplace=True)
print(df)

#changing datatype

df['Amount']=df['Amount'].astype('int')
print(df)

df['Amount'].dtype
print(df)


print(df.columns)

#EDA

#gender

ax=sns.countplot(x='Gender',data=df)
print(ax)

for bars in ax.containers:
    ax.bar_label(bars)
    


#age

ay=sns.countplot(data=df,x='Age Group',hue='Gender')

for bars in ay.containers:
    ay.bar_label(bars)
    plt.show()


#state

# Total number of orders from top 10 states

sales_state = (
    df.groupby('State', as_index=False)['Orders']
    .sum()
    .sort_values(by='Orders', ascending=False)
    .head(10)
)

plt.figure(figsize=(15, 5))

sns.barplot(data=sales_state, x='State', y='Orders')

plt.title('Top 10 States by Number of Orders')
plt.xlabel('State')
plt.ylabel('Total Orders')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


# Total sales amount from top 10 states

sales_state = (
    df.groupby('State', as_index=False)['Amount']
    .sum()
    .sort_values(by='Amount', ascending=False)
    .head(10)
)

plt.figure(figsize=(15, 5))

sns.barplot(data=sales_state, x='State', y='Amount')

plt.title('Top 10 States by Total Sales Amount')
plt.xlabel('State')
plt.ylabel('Total Sales Amount')
plt.xticks(rotation=45)

plt.tight_layout()
plt.show()


#marital status

sales_state = df.groupby(
    ['Marital_Status', 'Gender'], as_index=False
)['Amount'].sum().sort_values(
    by='Amount', ascending=False
)

sns.set(rc={'figure.figsize': (6, 5)})

sns.barplot(
    data=sales_state,
    x='Marital_Status',
    y='Amount',
    hue='Gender'
)
plt.show()

#occupation

sales_state = (
    df.groupby('Occupation', as_index=False)['Amount']
    .sum()
    .sort_values(by='Amount', ascending=False)
)

plt.figure(figsize=(20, 5))

sns.barplot(data=sales_state, x='Occupation', y='Amount')

plt.title('Total Sales Amount by Occupation')
plt.xlabel('Occupation')
plt.ylabel('Total Sales Amount')

plt.show()


#product category

sales_category = (
    df.groupby('Product_Category', as_index=False)['Amount']
    .sum()
    .sort_values(by='Amount', ascending=False)
)

plt.figure(figsize=(20, 5))

sns.barplot(
    data=sales_category,
    x='Product_Category',
    y='Amount'
)

plt.title('Total Sales Amount by Product Category')
plt.xlabel('Product Category')
plt.ylabel('Total Sales Amount')

plt.show()


