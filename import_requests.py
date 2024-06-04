import kaggle 
import zipfile 
with zipfile.ZipFile('/home/nisha/Downloads/', 'r') as zip_ref:
    zip_ref.extractall('Downloads')
import requests
from bs4 import BeautifulSoup

url = "https://www.kaggle.com/datasets/mayankanand2701/netflix-stock-price-dataset"
r = requests.get(url)
# print(r.text)
soup = BeautifulSoup (r.text,"lxml")
print(soup)
