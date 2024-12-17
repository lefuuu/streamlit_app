import streamlit as st
import yfinance as yf
import pandas as pd


st.title("Котировки Apple")

st.write("Это приложение отображает данные о котировках компании Apple, используя библиотеку **yfinance**.")

tickerData = yf.Ticker('AAPL')
tickerdf = tickerData.history(period='1y')
st.subheader('Котировки за год')
st.dataframe(tickerdf)

# График цен
st.subheader("График цен за последний год")
st.line_chart(tickerdf["Close"], x_label='Месяц', y_label='Цена, $')


