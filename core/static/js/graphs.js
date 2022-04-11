function barChart(data, id, col,name){
    debugger;
    const ctxLine2 = document.getElementById(id).getContext('2d');
    const mybarChart = new Chart(ctxLine2, {
        type: 'bar',
        data: {
            labels: col,
            datasets: [
                {
                    label: name,
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    data: data,
                    borderWidth: 1
                },
                // {
                //     label: name,
                //     backgroundColor: 'rgba(54, 162, 235, 0.2)',
                //     borderColor: 'rgba(54, 162, 235, 1)',
                //     data: data[1],
                //     borderWidth: 1
                // },
                
                //{
                /* barPercentage: 0.5,
                barThickness: 6,
                maxBarThickness: 8,
                minBarLength: 2,*/
                // data: annual_bar_data,
                // backgroundColor: [
                //     'rgba(255, 99, 132, 0.2)',
                //     'rgba(54, 162, 235, 0.2)',
                //     'rgba(255, 206, 86, 0.2)',
                //     'rgba(75, 192, 192, 0.2)',
                //     'rgba(153, 102, 255, 0.2)',
                //     'rgba(255, 159, 64, 0.2)'
                // ],
                // borderColor: [
                //     'rgba(255, 99, 132, 1)',
                //     'rgba(54, 162, 235, 1)',
                //     'rgba(255, 206, 86, 1)',
                //     'rgba(75, 192, 192, 1)',
                //     'rgba(153, 102, 255, 1)',
                //     'rgba(255, 159, 64, 1)'
                // ],
                // borderWidth: 1
            //}
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
                legend: {
                    position: 'top',
                },
                title: {
                    display: true,
                    text: 'Rainfall Comparesion of two State'
                },
            },
            scales: {
                y: {
                    beginAtZero: true
                }
            }
        }
    });
    return mybarChart;
}

function lineChart(data, colour, id, name) {
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