import pandas as pd
import streamlit as st
import numpy as np
from io import BytesIO
import matplotlib.pyplot as plt
import os
import zipfile

# path = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv'
# path = '../learning/datasets/tips.csv'
# Возьмите своё исследование по чаевым (датасет tips.csv)
# визуализируйте его на платформе Streamlit

st.title('Визуализация из датасета tips.csv')
st.write('В  данном приложение произведена визуализация различных данных из датасета tips.csv')

uploaded_file = st.sidebar.file_uploader('Загрузите tips.csv')
if uploaded_file is not None:
    tips = pd.read_csv(uploaded_file)
else:
    def_df = st.sidebar.button('Хотите ли загрузить дефолтный tips.csv?')
    if def_df:
        tips = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv')

folder_path = "graphs"
zip_file_name = "all_graphs.zip"
with zipfile.ZipFile(zip_file_name, "w") as zipf:
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path):  # Проверка, что это файл
            zipf.write(file_path, arcname=file_name)  # Добавляем файл в архив

with open(zip_file_name, "rb") as zipf:
    zip_data = zipf.read()
st.sidebar.download_button(
    label="Скачать все графики из приложения",
    data=zip_data,
    file_name=zip_file_name,
    mime="application/zip"
)


st.subheader('Оригинальный датасет')

start_date = "2023-01-01"
end_date = "2023-01-31"
start = pd.to_datetime(start_date)
end = pd.to_datetime(end_date)
tips['time_order'] = start + pd.to_timedelta(np.random.randint(0, (end - start).days + 1, size=len(tips)), unit='D')
st.dataframe(tips)

st.subheader('График сумм чаевых по дням')
st.write("Этот график отображает общую сумму чаевых за каждый день января.")
df = tips.set_index('time_order').sort_index()
df.reset_index()
df1 = df.groupby(df.index.date)[['tip']].sum().reset_index()
df1.columns = ['date', 'tip']
df1.index = range(1, 32)
chart_data = pd.DataFrame({
    'День': df1.index,
    'Сумма чаевых': df1['tip']
}).set_index('День')
st.line_chart(chart_data)

st.subheader('Гистограмма сумм счетов')
st.write("Эта гистограмма показывает распределение значений 'сумма счета' из набора данных.")
hist_data = tips['total_bill']
hist_df = pd.DataFrame({
    'Интервалы': pd.cut(hist_data, bins=10).value_counts().index.astype(str),
    'Частота': pd.cut(hist_data, bins=10).value_counts().values
}).set_index('Интервалы')
st.bar_chart(hist_df)

st.subheader('График зависимости чаевых от суммы счёта')
st.write("Этот график показывает, как размер чаевых зависит от общей суммы счета.")
st.scatter_chart(tips, x='total_bill', y='tip', x_label='Сумма заказа, $', y_label='Размер чаевых,$')

st.subheader('Зависимость между общей суммой заказа, размером заказа и чаевыми')
st.write("Этот график показывает, как сумма чаевых зависит от суммы счета и размера группы.")
st.scatter_chart(data=tips, x='total_bill', y='tip', color='size', x_label='Сумма заказа, $', y_label='Размер чаевых,$')

st.subheader('Связь между днем недели и размером счета с учетом пола ')
st.write("Этот график показывает зависимость чаевых от дня недели, где точки окрашены по полу.")
st.scatter_chart(data=tips, x='day', y='total_bill', color='sex', x_label='День недели', y_label='Сумма заказа, $', )

st.subheader('Гистограммы чаевых для обеда и ужина')
st.write("Этот график показывает распределение чаевых для обеда и ужина")
lunch_tips = tips[tips['time'] == 'Lunch']
dinner_tips = tips[tips['time'] == 'Dinner']
st.write("Гистограмма чаевых на обед")
st.bar_chart(lunch_tips['tip'].value_counts().sort_index())
st.write("Гистограмма чаевых на ужин")
st.bar_chart(dinner_tips['tip'].value_counts().sort_index())

