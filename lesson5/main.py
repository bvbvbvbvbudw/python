import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# завантажуємо дані з CSV
data = pd.read_csv('assets/MPI_national.csv')

# очищення даних: видаляємо пропущені значення
data_cleaned = data.dropna()  # видаляє всі рядки, де є пропущені значення

# розрахунок кореляції між Urban MPI та Headcount Ratio Urban
correlation = data_cleaned['MPI Urban'].corr(data_cleaned['Headcount Ratio Urban'])  # кореляція вимірює, наскільки дві змінні пов'язані
print(f"Кореляція між Urban MPI та Headcount Ratio Urban: {correlation}")  # виводимо кореляцію

# країна з найвищим Urban MPI
max_mpi_country = data_cleaned.loc[data_cleaned['MPI Urban'].idxmax()]  # idxmax() повертає індекс найбільшого значення в колонці
print(f"Країна з найвищим Urban MPI: {max_mpi_country['Country']}")  # виводимо країну з найвищим Urban MPI

# побудова скатерплоту між Urban MPI та Headcount Ratio Urban
plt.scatter(data_cleaned['MPI Urban'], data_cleaned['Headcount Ratio Urban'])  # створює точковий графік
plt.title('Залежність Urban MPI від Headcount Ratio Urban')  # заголовок графіка
plt.xlabel('Urban MPI')  # мітка для осі X
plt.ylabel('Headcount Ratio Urban')  # мітка для осі Y
plt.show()  # відображає графік

# побудова парних графіків для багатовимірного аналізу
sns.pairplot(data_cleaned[['MPI Urban', 'Headcount Ratio Urban', 'MPI Rural', 'Headcount Ratio Rural']])  # створює матрицю графіків
plt.show()  # відображає графік парних відношень
