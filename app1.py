import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# Define the layout of the app
app.layout = html.Div([
    html.H1('Cryptocurrency Clustering Analysis'),
    dcc.Graph(id='example-graph', figure={
        'data': [
            {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'Crypto 1'},
            {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': 'Crypto 2'},
        ],
        'layout': {
            'title': 'Basic Cryptocurrency Comparison'
        }
    })
])

# Run the app
if __name__ == '__main__':
    app.run_server(debug=True)
