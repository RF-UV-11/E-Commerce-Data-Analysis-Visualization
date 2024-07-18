document.addEventListener("DOMContentLoaded", function() {
    const figureNames = {{ figures | tojson }};
    figureNames.forEach(name => {
        fetch(`/figure/${name}`)
            .then(response => response.json())
            .then(data => {
                Plotly.newPlot(`figure-${name}`, data.data, data.layout);
            });
    });
});