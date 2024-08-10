import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('crypto_market_data.csv')

# For example, let's assume the CSV contains columns like 'coin_id', 'price', 'market_cap', etc.
# Here we'll create a simple comparison between two cryptocurrencies based on market cap
cryptos_to_compare = df.head(2)  # Get the top 2 cryptocurrencies by market cap

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    html.H1('Cryptocurrency Clustering Analysis'),
    dcc.Graph(id='market-cap-comparison', figure={
        'data': [
            {'x': cryptos_to_compare['coin_id'], 'y': cryptos_to_compare['market_cap'], 'type': 'bar', 'name': 'Market Cap'},
        ],
        'layout': {
            'title': 'Market Cap Comparison'
        }
    })
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
