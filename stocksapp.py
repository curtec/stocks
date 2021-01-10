import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

 Shown are stock closing price and volume Tesla

""" )

tickerSymbol = 'TSLA'

tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period='id', start='2010-5-31', end='2021-1-9')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)