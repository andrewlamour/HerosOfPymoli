#!/usr/bin/env python
# coding: utf-8

# In[63]:


import pandas as pd
    


# In[64]:


file = "Resources/purchase_data.csv"
rawdata_df = pd.read_csv(file)
rawdata_df


# In[65]:


#Total Player Count

player_demographics = player_demographics.drop_duplicates()

player_count = player_demographics.count()[0]
pd.DataFrame({"Total Players": [player_count]})


# In[66]:


#Purchasing Analysis
UniqueItems = len(rawdata_df["Item Name"].unique())
AvgPurchase = rawdata_df["Price"].mean()
Revenue = rawdata_df["Price"].sum()
NumPurchase = len(rawdata_df["Item Name"])

SummaryTable = pd.DataFrame({"Number of Unique Items": [UniqueItems], 
              "Average Price": [AvgPurchase], 
              "Number of Purchases": [NumPurchase], 
              "Total Revenue": [Revenue]})

#Summary Table Formatting
SummaryTable = SummaryTable.round(2)
SummaryTable ["Average Price"] = SummaryTable["Average Price"].map("${:,.2f}".format)
SummaryTable ["Number of Purchases"] = SummaryTable["Number of Purchases"].map("{:,}".format)
SummaryTable ["Total Revenue"] = SummaryTable["Total Revenue"].map("${:,.2f}".format)
SummaryTable = SummaryTable.loc[:,["Number of Unique Items", "Average Price", "Number of Purchases", "Total Revenue"]]

SummaryTable


# In[67]:


gender_count=player_demographics["Gender"].value_counts()
gender_percent=gender_count/player_count*100

gender_demographics=pd.DataFrame({"Percentage of Players":gender_percent,
                                 "Total Count":gender_count})

gender_demographics= gender_demographics.round(2)
gender_demographics.head()


# In[68]:


#Purchasing Analysis for Genders

purchase_count=rawdata_df.groupby(["Gender"]).count()["Price"]
purchase_avg_price=rawdata_df.groupby(["Gender"]).mean()["Price"]
total_purchase_value=rawdata_df.groupby(["Gender"]).sum()["Price"]
normalized_totals=total_purchase_value/gender_count

summary_purchasing_analysis=pd.DataFrame({"Purchase Count":purchase_count,
                                         "Average Purchase Price":purchase_avg_price,
                                         "Total Purchase Value": total_purchase_value,
                                         "Normalized Total":normalized_totals})

summary_purchasing_analysis=summary_purchasing_analysis[["Purchase Count",
                                                         "Average Purchase Price",
                                                         "Total Purchase Value",
                                                         "Normalized Total"]]

summary_purchasing_analysis=summary_purchasing_analysis.round(2)
summary_purchasing_analysis


# In[69]:


#Age Demographics

bins= [0, 9.90, 14.90, 19.90, 24.90, 29.90, 34.90, 39.90, 99999]
group_names=['<10','10-14','15-19','20-24','25-29','30-34','35-39','40+']

unique_heroes=player_demographics.loc[:,["SN","Age"]]
unique_heroes["Age Ranges"] = pd.cut(unique_heroes["Age"], bins, labels=group_names)
unique_heroes

age_demographics_totals = unique_heroes["Age Ranges"].value_counts()
age_demographics_percents = (age_demographics_totals / player_count * 100).round(2)
age_demographics = pd.DataFrame({"Percentage of Total": age_demographics_percents, "Age Group Total": age_demographics_totals})

age_demographics.sort_index()


# In[74]:


#Top Spenders
total_users = rawdata_df.groupby(["SN"]).sum()["Price"].rename("Total Purchase Value")
user_average = rawdata_df.groupby(["SN"]).mean()["Price"].rename("Average Purchase Price")
user_count = rawdata_df.groupby(["SN"]).count()["Price"].rename("Purchase Count")

user_data = pd.DataFrame({"Total Purchase Value": total_users, "Average Purchase Price": user_average, "Purchase Count": user_count})

user_sorted = user_data.sort_values("Total Purchase Value", ascending=False)

user_sorted["Average Purchase Price"] = user_sorted["Average Purchase Price"].map("${:,.2f}".format)
user_sorted["Total Purchase Value"] = user_sorted["Total Purchase Value"].map("${:,.2f}".format)
user_sorted = user_sorted.loc[:,["Purchase Count", "Average Purchase Price", "Total Purchase Value"]]

user_sorted.head(5)


# In[72]:


#Most Popular Items
item_id = rawdata_df.groupby(rawdata_df['Item ID'])

unique_items = item_id['Item ID'].unique().str[0]
item_name = item_id['Item Name'].unique().str[0]
item_purchase_count = item_id['Age'].count()
item_price = item_id['Price'].unique().str[0]
item_purchase_total = item_id['Price'].sum()

item_summary =pd.DataFrame({'Item ID':unique_items,
                'Item Name':item_name,
                'Item Price':item_price,
                'Item Count':item_purchase_count,
                'Total Purchase':item_purchase_total})

item_summary = item_summary.sort_values('Item Count', ascending=False)
item_summary_df = item_summary[['Item Name','Item Count','Item Price','Total Purchase']]
item_summary_df.head()


# In[76]:


#Most Profitable Items
most_profit=item_summary.sort_values('Total Purchase', ascending=False)

most_profit.head(5)


# In[ ]:


#Three Trends with the data:
#1: The vast majority of the player base is betweeen the age of 20-24 (44.79%).
#2: Males are the also the vast majority of the player base (84.3%) and spend more money on items on average then the other genders.
#3: The most popular items that are being purchased are on the expensive side. The average item price is $3.05 but the top grossing items are all $4 and above.

