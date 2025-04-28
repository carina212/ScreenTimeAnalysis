import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Membaca data dari file CSV
data = pd.read_csv('MultipleFiles/screen_time.csv')

# Melihat beberapa baris pertama dari data
print(data.head())

# Informasi data
print(data.info())

# Statistik deskriptif
print(data.describe())

# Histogram distribusi waktu layar
plt.figure(figsize=(10, 6))
sns.histplot(data['Average Screen Time (hours)'], bins=30, kde=True)
plt.title('Distribusi Rata-rata Waktu Layar')
plt.xlabel('Rata-rata Waktu Layar (jam)')
plt.ylabel('Frekuensi')
plt.show()  # Menampilkan grafik pertama
plt.close()  # Menutup grafik pertama

# Box plot perbandingan waktu layar berdasarkan jenis kelamin
plt.figure(figsize=(10, 6))
sns.boxplot(x='Gender', y='Average Screen Time (hours)', data=data)
plt.title('Perbandingan Waktu Layar Berdasarkan Jenis Kelamin')
plt.show()  # Menampilkan grafik kedua
plt.close()  # Menutup grafik kedua

# Bar chart rata-rata waktu layar berdasarkan tipe hari dan jenis kelamin
plt.figure(figsize=(10, 6))
sns.barplot(x='Day Type', y='Average Screen Time (hours)', hue='Gender', data=data)
plt.title('Rata-rata Waktu Layar Berdasarkan Tipe Hari dan Jenis Kelamin')
plt.show()  # Menampilkan grafik ketiga
plt.close()  # Menutup grafik ketiga