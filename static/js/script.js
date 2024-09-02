const init = async () => {
    let url = 'static/Resources/crypto_market_data.csv';

    // Load the data using d3.csv
    const data = await d3.csv(url);

    // Extract the features (column names)
    const features = Object.keys(data[0]);

    // Populate the select elements with the features
    features.forEach(feature => {
        d3.select('#x').append('option').attr('value', feature).text(feature);
        d3.select('#y').append('option').attr('value', feature).text(feature);
        d3.select('#z').append('option').attr('value', feature).text(feature);
    });

    // Set up event listeners after data is loaded and selects are populated
    setupEventListeners(data);
};

// Function to set up event listeners
function setupEventListeners(data) {
    const xSelect = document.getElementById('x');
    const ySelect = document.getElementById('y');
    const zSelect = document.getElementById('z');
    const myDiv = document.getElementById('myDiv');

    function updateChart() {
        const xValue = xSelect.value;
        const yValue = ySelect.value;
        const zValue = zSelect.value;

        // Map the selected feature to data arrays
        const xData = data.map(d => +d[xValue]);
        const yData = data.map(d => +d[yValue]);
        const zData = data.map(d => +d[zValue]);

        // Create the trace for Plotly
        const trace = {
            x: xData,
            y: yData,
            z: zData,
            type: 'scatter3d',
            mode: 'markers'
        };

        // Render the plot
        Plotly.newPlot(myDiv, [trace]);
    }

    // Set up event listeners to update the chart when a selection changes
    xSelect.addEventListener('change', updateChart);
    ySelect.addEventListener('change', updateChart);
    zSelect.addEventListener('change', updateChart);

    // Initial chart rendering
    updateChart();
}

// Initialize the script
init();

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
