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
