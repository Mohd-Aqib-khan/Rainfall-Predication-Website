function lineChart(data, colour, id,name){
    const totalDuration = 10000;
    const delayBetweenPoints = totalDuration / data.length;
    const previousY = (ctx) => ctx.index === 0 ? ctx.chart.scales.y.getPixelForValue(100) : ctx.chart.getDatasetMeta(ctx
        .datasetIndex).data[ctx.index - 1].getProps(['y'], true).y;
    const ctx = document.getElementById(id).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
        data: {
            datasets: [{
                label: name,
                borderColor: colour,
                borderWidth: 1,
                radius: 2,
                data: data,
            }
                /*{
                    label: stateSecond,
                    borderColor: '#f67019',
                    borderWidth: 1,
                    radius: 3,
                    data: data2,
                }*/
            ]
        },
        options: {
            animation: {
                x: {
                    type: 'number',
                    easing: 'linear',
                    duration: delayBetweenPoints,
                    from: NaN, // the point is initially skipped
                    delay(ctx) {
                        if (ctx.type !== 'data' || ctx.xStarted) {
                            return 0;
                        }
                        ctx.xStarted = true;
                        return ctx.index * delayBetweenPoints;
                    }
                },
                y: {
                    type: 'number',
                    easing: 'linear',
                    duration: delayBetweenPoints,
                    from: previousY,
                    delay(ctx) {
                        if (ctx.type !== 'data' || ctx.yStarted) {
                            return 0;
                        }
                        ctx.yStarted = true;
                        return ctx.index * delayBetweenPoints;
                    }
                }
            },
            responsive: false,
            interaction: {
                intersect: false
            },
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Annual Rainfall'
                },
            },
            scales: {
                x: {
                    type: 'linear'
                }
            }
        }
    });
    return myChart;
}