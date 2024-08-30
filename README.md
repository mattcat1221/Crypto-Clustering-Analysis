# Crypto Clustering Analysis
![MIT](https://img.shields.io/badge/License-MIT-blue)

## Website: [Dash](https://crypto-clustering-analysis-git-main-caseys-projects-78b1de0d.vercel.app/)
![clustersandcentroids](https://github.com/user-attachments/assets/ae31e7c3-2ee0-4ad9-a0cf-f05806fd8a38)

## Description
This project involved the analysis and clustering of cryptocurrencies based on market data using K-Means clustering and Principal Component Analysis (PCA). The process included data preprocessing, scaling, clustering, and visualization to uncover meaningful patterns and insights in the cryptocurrency market. Below is a detailed overview of the steps undertaken:

Data Preprocessing

Loading the Data:
The analysis began by loading cryptocurrency market data into a pandas DataFrame. The dataset included various features such as price changes over different periods, market capitalization, and trading volume.

Handling Missing Values:
The data was examined for missing or null values, which were addressed either by removal or imputation with appropriate values.

Feature Selection:
Relevant features were selected to contribute to effective clustering, including price change percentages, market capitalization, and trading volume.

Data Scaling

Standardization:
The data was standardized to ensure that each feature had a mean of zero and a standard deviation of one. This step was crucial as K-Means clustering is sensitive to the scale of input features.

Principal Component Analysis (PCA):
PCA was applied to reduce the dimensionality of the data while retaining most of the variance. This step simplified the clustering process and made visualization more interpretable.

K-Means Clustering

Elbow Method:
The Elbow Method was employed to determine the optimal number of clusters. A plot of the Within-Cluster-Sum of Squared Errors (WSS) for different numbers of clusters was created, with the "elbow point" indicating the optimal number of clusters.

Clustering:
Once the optimal number of clusters was identified, K-Means clustering was applied to group the cryptocurrencies into clusters, with each cluster representing a group of cryptocurrencies with similar market behavior.

Cluster Analysis:
After clustering, the characteristics of each cluster were analyzed to understand the common features within each group, providing insights into the similarities and differences among the various cryptocurrencies.

Visualization

Visualizing Clusters:
The clusters were visualized using both the original features and the principal components obtained from PCA. Scatter plots and 3D plots depicted the distribution of cryptocurrencies across different clusters.

Combined Metric Visualization:
A combined metric was created by summing specific features like price_change_percentage_24h and price_change_percentage_7d. This new metric was visualized alongside the original features to facilitate trend analysis.

Elbow Curve:
The Elbow Curve was plotted to visually determine the optimal number of clusters, which helped validate the chosen clusters.

Conclusion
The project successfully clustered cryptocurrencies based on their market data, providing insights into their similarities and differences. The use of K-Means clustering and PCA enabled effective analysis of complex market data, while the visualizations offered an intuitive understanding of the results. This analysis serves as a foundation for further exploration of the cryptocurrency market, including predictive modeling and deeper market segmentation.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Credits](#credits)
- [License](#license)
- [Features](#features)
- [Tests](#tests)
- [Contact](#contact)
- [Requirements](https://github.com/mattcat1221/Crypto-Clustering-Analysis/blob/main/requirements.txt)
## Installation
Pandas: For data manipulation and analysis. scikit-learn: For machine learning algorithms, including K-Means clustering and PCA. matplotlib: For plotting basic visualizations. hvplot: For creating interactive visualizations. holoviews: For creating high-level interactive plots. bokeh: A backend for HoloViews to render the plots.


## Usage
Data analysis

## Credits
Catherine Matthews

## License
MIT

## Features
Interactive scatter plots, cluster plots and line plots.

## Tests
Data Loading and Preparation:  Verify that the data is loaded correctly from the CSV file. Check if the selected features are present in the DataFrame. Ensure the data is scaled correctly. K-Means Clustering:  Test the computation of inertia values for different values of k. Verify the correct number of clusters is identified using the Elbow method. Ensure the K-Means model fits the data without errors. Check the cluster labels are correctly added to the DataFrame. Principal Component Analysis (PCA):  Ensure the PCA transformation retains the expected amount of variance. Verify the dimensionality reduction is performed correctly. Check the PCA-transformed data for consistency. Interactive Visualizations:  Verify the scatter plots are created without errors. Ensure the hover tools display the correct information.

## Contact
If there are any questions of concerns, I can be reached at:
##### [github: mattcat1221](https://github.com/mattcat1221)
##### [email: caseyvmatthews@gmail.com](mailto:caseyvmatthews@gmail.com)
