import os
import kaggle
from kaggle import KaggleApi
import zipfile



api = KaggleApi()
api.authenticate()


dataset = 'mayankanand2701/netflix-stock-price-dataset'
download_path = '/home/nisha/Downloads'


if not os.path.exists(download_path):
    os.makedirs(download_path)


api.dataset_download_files(dataset, path=download_path, unzip=False)


zip_file_path = os.path.join(download_path, 'netflix-stock-price-dataset.zip')


with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(download_path)

print("Dataset downloaded and extracted successfully.")
