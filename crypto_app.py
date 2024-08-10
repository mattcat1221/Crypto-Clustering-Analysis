from flask import Flask, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


# Initialize the Flask app
app = Flask(__name__)

# Initialize the Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')

# Load and preprocess data
df = pd.read_csv('crypto_market_data.csv')
features = [
    'price_change_percentage_24h',
    'price_change_percentage_7d',
    'price_change_percentage_14d',
    'price_change_percentage_30d',
    'price_change_percentage_60d',
    'price_change_percentage_200d',
    'price_change_percentage_1y'
]

scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[features])
scaled_df = pd.DataFrame(scaled_data, columns=features)

# Perform K-Means clustering
optimal_k = 3
kmeans = KMeans(n_clusters=optimal_k, random_state=42, n_init=10)
kmeans.fit(scaled_df)
df['cluster'] = kmeans.predict(scaled_df)

# Perform PCA transformation
pca = PCA(n_components=3)
pca_data = pca.fit_transform(scaled_df)
pca_df = pd.DataFrame(pca_data, columns=['PC1', 'PC2', 'PC3'])
pca_df['cluster'] = KMeans(n_clusters=optimal_k, random_state=42, n_init=10).fit_predict(pca_df)
pca_df['crypto_id'] = df['crypto_id']

# Define the Dash layout
dash_app.layout = html.Div([
    html.H1("Cryptocurrency Clustering Analysis"),
    dcc.Tabs(id="tabs", children=[
        dcc.Tab(label='Clusters on Scaled Data', children=[
            dcc.Graph(
                id='scaled-data-cluster',
                figure=px.scatter(scaled_df, x=scaled_df.columns[0], y=scaled_df.columns[1], color=df['cluster'], hover_data=[df['crypto_id']])
            )
        ]),
        dcc.Tab(label='Clusters on PCA Data', children=[
            dcc.Graph(
                id='pca-data-cluster',
                figure=px.scatter(pca_df, x='PC1', y='PC2', color='cluster', hover_data=['crypto_id'])
            )
        ])
    ])
])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Flask app
app = Flask(__name__)

# Initialize the Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')

# Load and preprocess data
df = pd.read_csv('crypto_market_data.csv')

# Print column names for debugging
print(df.columns)

# Initialize the PCA DataFrame
pca_df = pd.DataFrame()

# Add the 'crypto_id' to the PCA DataFrame using the correct column name
pca_df['crypto_id'] = df['coin_id']  # Replace 'coin_id' with the correct column name

# Perform scaling
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.drop(columns=['coin_id']))  # Exclude the 'coin_id' column from scaling

# Perform PCA transformation
pca = PCA(n_components=3)
pca_data = pca.fit_transform(scaled_data)

# Add PCA results to the pca_df
pca_df['PC1'] = pca_data[:, 0]
pca_df['PC2'] = pca_data[:, 1]
pca_df['PC3'] = pca_data[:, 2]

# Continue with the rest of your processing...
print(pca_df.head())  # Print the first few rows to verify
