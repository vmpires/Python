import pandas as pd

##  Scrapped URL    ##
url = 'https://news.google.com/covid19/map?hl=en-US&gl=US&ceid=US%3Aen'

##  "read_html" method of the Pandas library to read the HTML tables    ##
df_list = pd.read_html(url)

##  Output number of tables on webpage  ##
# print(len(df_list))

##  If there are multiples tables, we can select table with [table_number]  ##
# print(df_list)

##  creating a .txt file with table data scrapped from website    ##
with open('data_scrapped.txt', 'a') as file:
    file.write(str(df_list))