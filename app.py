from flask import Flask, request, redirect, render_template
import pandas as pd
import os
import yfinance as yf

app = Flask(__name__)
app.config['SECRET_KEY'] = 'Thisisasecret!'

def add_x(text):
    return text + 'x'

def get_mean_price(tickers_list):
    data = pd.DataFrame(columns=tickers_list)
    for ticker in tickers_list:
        data[ticker] = yf.download(ticker,'2016-01-01','2019-08-01')['Adj Close']
    return data.iloc[:,0].mean()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/portfolio_info', methods = ['POST'])
def result():
    name = request.form['name']
    name = [name]
    mean_price = get_mean_price(tickers_list = name)
    return render_template('portfolio_info.html', name = mean_price)


if __name__ == '__main__':
    app.run(debug=True)
