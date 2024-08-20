d3.csv('static/resources/crypto_market_data.csv').then(data => {
    // Create the hover text, including the cluster name
    let hoverText = data.map(obj => 
        `Name: ${obj.coin_id}<br>Cluster: ${obj.cluster}<br>24h Change: ${obj.price_change_percentage_24h}%<br>7d Change: ${obj.price_change_percentage_7d}%<br>14d Change: ${obj.price_change_percentage_14d}%`
    );

    // Extract keys from the data (if needed)
    let keys = Object.keys(data[0]);
    console.log(keys);

    // Map the data to their respective arrays
    let price_change_percentage_24h = data.map(obj => obj.price_change_percentage_24h);
    let price_change_percentage_7d = data.map(obj => obj.price_change_percentage_7d);
    let price_change_percentage_14d = data.map(obj => obj.price_change_percentage_14d);

    // Create the first trace with hover information
    var trace1 = {
        x: price_change_percentage_24h, 
        y: price_change_percentage_7d, 
        z: price_change_percentage_14d,
        mode: 'markers',
        marker: {
            size: 12,
            line: {
                color: 'rgba(217, 217, 217, 0.14)',
                width: 0.5
            },
            opacity: 0.8
        },
        text: hoverText, // Include hover text with cluster name
        hoverinfo: 'text', // Specifies that only the text should be displayed on hover
        type: 'scatter3d'
    };

    // Create the second trace (if needed)
    var trace2 = {
        x: price_change_percentage_24h, 
        y: price_change_percentage_7d, 
        z: price_change_percentage_14d,
        mode: 'markers',
        marker: {
            color: 'rgb(127, 127, 127)',
            size: 12,
            symbol: 'circle',
            line: {
                color: 'rgb(204, 204, 204)',
                width: 1
            },
            opacity: 0.8
        },
        text: hoverText, // Include hover text with cluster name
        hoverinfo: 'text', // Specifies that only the text should be displayed on hover
        type: 'scatter3d'
    };

    // Combine traces and define layout
    var data = [trace1, trace2];
    var layout = {
        margin: {
            l: 0,
            r: 0,
            b: 0,
            t: 0
        }
    };

    // Render the plot
    Plotly.newPlot('myDiv', data, layout);
});
