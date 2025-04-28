import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv('MultipleFiles/screen_time.csv')

# Menampilkan deskripsi data
print(data.describe())