from flask import Flask, render_template
import pandas as pd

# Initialize the Flask app
app = Flask(__name__)

# Load the data from the CSV file
df = pd.read_csv('crypto_market_data.csv')

# You can preprocess the data here if needed (e.g., filtering, sorting)
# For example, get the top 10 cryptocurrencies by market cap:
top_cryptos = df.sort_values(by='market_cap', ascending=False).head(10)

# Convert the DataFrame to a list of dictionaries to pass to the template
crypto_data = top_cryptos.to_dict(orient='records')

@app.route('/')
def index():
    return render_template('index.html', cryptos=crypto_data)

if __name__ == '__main__':
    app.run(debug=True)
