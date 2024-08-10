import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('crypto_market_data.csv')

# For example, let's compare cryptocurrencies based on their 24-hour price change
cryptos_to_compare = df.head(10)  # Get the top 10 cryptocurrencies

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    html.H1('Cryptocurrency 24h Price Change Analysis'),
    dcc.Graph(id='24h-price-change-comparison', figure={
        'data': [
            {'x': cryptos_to_compare['coin_id'], 'y': cryptos_to_compare['price_change_percentage_24h'], 'type': 'bar', 'name': '24h Price Change'},
        ],
        'layout': {
            'title': '24-Hour Price Change Comparison'
        }
    })
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
    
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
import pandas as pd

# Load the data from the CSV file
df = pd.read_csv('Resources/crypto_market_data.csv')

# Select relevant columns
coin_ids = df['coin_id']
price_changes_24h = df['price_change_percentage_24h']

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    html.H1('Cryptocurrency 24h Price Change Analysis'),
    dcc.Graph(id='24h-price-change-comparison', figure={
        'data': [
            {'x': coin_ids, 'y': price_changes_24h, 'type': 'bar', 'name': '24h Price Change'},
        ],
        'layout': {
            'title': '24-Hour Price Change Comparison'
        }
    })
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)

