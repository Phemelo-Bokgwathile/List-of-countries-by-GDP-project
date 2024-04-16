import numpy as np
import pandas as pd
import bs4 as BeautifulSoup
import requests
import lxml 

def warn(*args, **kwargs):
  pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

url = "https://web.archive.org/web/20230902185326/https://en.wikipedia.org/wiki/List_of_countries_by_GDP_%28nominal%29"
tables = pd.read_html(url)
df = table[2]

df.columns = range(df.shape[1])
df = df[0, 2]
df = df.iloc[1:10, :]
df.columns = ["Country", "GDP (Million USD)"]
#when i run it i get an import error;lxml not found, please install it. When i try to run it remotely on juypter i get a different error; SSL certVerification failed. 
