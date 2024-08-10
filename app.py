from flask import Flask, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
import plotly.express as px
import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# Initialize the Flask app
app = Flask(__name__)

# Initialize the Dash app
dash_app = dash.Dash(__name__, server=app, url_base_pathname='/dash/')

# Load and preprocess data
df = pd.read_csv('crypto_market_data.csv')

# Print column names and first few rows for debugging
print(df.columns)
print(df.head())

# Initialize the PCA DataFrame
pca_df = pd.DataFrame()

# Assuming the correct column name is 'id' or whatever the actual name is
pca_df['coin_id'] = df['coin_id']  # Replace 'id' with the actual column name

# Continue with the PCA transformation
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df.drop(columns=['coin_id']))  # Exclude the 'id' column from scaling
pca = PCA(n_components=3)
pca_data = pca.fit_transform(scaled_data)

# Add PCA results to the pca_df
pca_df['PC1'] = pca_data[:, 0]
pca_df['PC2'] = pca_data[:, 1]
pca_df['PC3'] = pca_data[:, 2]

# Continue with the rest of your processing...

