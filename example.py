import requests


url = "https://www.kaggle.com/datasets/mayankanand2701/netflix-stock-price-dataset"
r = requests.get(url)

print(r.text)
