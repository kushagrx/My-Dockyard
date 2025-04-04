import streamlit as st
from streamlit_option_menu import option_menu
import yfinance as yf
import pandas as pd
import requests

# Set page config
st.set_page_config(page_title="Stock Analysis App", layout="wide")

# Sidebar navigation
selected = option_menu(
    menu_title="Stock Analysis",
    options=["Home", "Stock Overview", "Technical Analysis", "News & Sentiment"],
    icons=["house", "bar-chart", "activity", "newspaper"],
    menu_icon="cast",
    default_index=0,
    orientation="horizontal",
)

# Home Page
if selected == "Home":
    st.title("Welcome to Stock Analysis App")
    st.write("Use this app to analyze stocks, track technical trends, and view latest news.")

# Stock Overview Page
elif selected == "Stock Overview":
    st.title("Stock Overview")
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    if stock_symbol:
        stock = yf.Ticker(stock_symbol)
        hist = stock.history(period="1y")
        st.write(f"## {stock_symbol} Stock Data")
        st.line_chart(hist['Close'])
        st.write(hist.tail())

# Technical Analysis Page
elif selected == "Technical Analysis":
    st.title("Technical Analysis")
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    if stock_symbol:
        stock = yf.Ticker(stock_symbol)
        hist = stock.history(period="6mo")
        st.write(f"## {stock_symbol} Moving Averages")
        hist['MA50'] = hist['Close'].rolling(window=50).mean()
        hist['MA200'] = hist['Close'].rolling(window=200).mean()
        st.line_chart(hist[['Close', 'MA50', 'MA200']])

# News & Sentiment Page
elif selected == "News & Sentiment":
    st.title("News & Sentiment Analysis")
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    if stock_symbol:
        news_api = f'https://newsapi.org/v2/everything?q={stock_symbol}&apiKey=YOUR_NEWS_API_KEY'
        response = requests.get(news_api)
        if response.status_code == 200:
            articles = response.json().get('articles', [])[:5]
            for article in articles:
                st.write(f"### {article['title']}")
                st.write(article['description'])
                st.write(f"[Read more]({article['url']})")
                st.write("---")
        else:
            st.error("Error fetching news")
