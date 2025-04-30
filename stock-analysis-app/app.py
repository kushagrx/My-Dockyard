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
        try:
            hist = yf.download(stock_symbol, period="1y")
            if not hist.empty:
                st.write(f"## {stock_symbol} Stock Data")
                st.line_chart(hist['Close'])
                st.write(hist.tail())
            else:
                st.warning("No data found for the given symbol.")
        except Exception as e:
            st.error("Failed to fetch stock data. Please try again later.")
            st.write(e)

# Technical Analysis Page
elif selected == "Technical Analysis":
    st.title("Technical Analysis")
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    if stock_symbol:
        try:
            hist = yf.download(stock_symbol, period="6mo")
            if not hist.empty:
                hist['MA50'] = hist['Close'].rolling(window=50).mean()
                hist['MA200'] = hist['Close'].rolling(window=200).mean()
                st.write(f"## {stock_symbol} Moving Averages")
                st.line_chart(hist[['Close', 'MA50', 'MA200']])
            else:
                st.warning("No data found for the given symbol.")
        except Exception as e:
            st.error("Failed to fetch technical data. Please try again later.")
            st.write(e)

# News & Sentiment Page
elif selected == "News & Sentiment":
    st.title("News & Sentiment Analysis")
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., AAPL, TSLA):", "AAPL")
    if stock_symbol:
        # Replace with your News API key
        api_key = "YOUR_NEWS_API_KEY"
        news_api = f'https://newsapi.org/v2/everything?q={stock_symbol}&apiKey={api_key}'
        try:
            response = requests.get(news_api)
            if response.status_code == 200:
                articles = response.json().get('articles', [])[:5]
                if articles:
                    for article in articles:
                        st.write(f"### {article['title']}")
                        st.write(article['description'])
                        st.write(f"[Read more]({article['url']})")
                        st.write("---")
                else:
                    st.info("No recent news found for this stock.")
            else:
                st.error("News API error. Please check your API key and usage.")
        except Exception as e:
            st.error("Error fetching news.")
            st.write(e)
