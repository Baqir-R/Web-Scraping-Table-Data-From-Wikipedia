from bs4 import BeautifulSoup
import requests

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, "html.parser")

#print(soup.prettify())

tables = soup.find_all("table")[0]

head_column_temp = tables.find_all("th")
#print(head_column[0])

head_column = [title.text.strip() for title in head_column_temp]
#print(head_column)

import pandas as pd

df = pd.DataFrame(columns = head_column)

table_data = tables.find_all("tr")
#print(table_data)

row_data = [table.text.strip() for table in table_data]


row_data.pop(0)
#print(row_data)

for row in table_data[1:]:
    td_rows = row.find_all("td");
    #print(td_rows)
    
    df_rows = [row.text.strip() for row in td_rows]
    
    length = len(df)
    
    df.loc[length] = df_rows
    
print(df)

df.to_csv(r"F:\Data Analyst\Python\Web Scraping Project\revenue.csv", index = False)






