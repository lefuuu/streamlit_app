# Streamlit Приложение с Датасетами Apple и Tips

##Описание проекта
Данное приложение создано на платформе **Streamlit** и предоставляет следующие возможности:

1. **Данные о котировках компании Apple**:
   - Используется библиотека `yfinance` для получения данных о котировках.
   - Визуализация данных с использованием интерактивных графиков.

2. **Визуализация данных о чаевых** (датасет `tips.csv`):
   - Исследование и анализ данных о чаевых.
   - Построение различных графиков и диаграмм.

---

## Функционал
- **Боковая панель**:
  - Все виджеты приложения вынесены в `st.sidebar` для удобного взаимодействия.
  
- **Загрузка данных**:
  - Возможность загрузки собственного CSV-файла через `st.file_uploader`.

- **Скачивание графиков**:
  - Пользователи могут скачивать созданные графики через `st.download_button`.

- **Деплой в облаке**:
  - Приложение доступно онлайн благодаря развертыванию в облаке. Доступно по ссылке здесь.


