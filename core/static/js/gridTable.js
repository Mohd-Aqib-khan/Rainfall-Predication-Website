function table(dataset, col, id,limitValue) {
    const grid = new gridjs.Grid({
        columns: col,
        data: dataset,
        pagination: {
            enabled: true,
            limit: limitValue,
            summary: false
        },
        style: {
            table: {
                border: '3px solid #ccc'
            },
            th: {
                'background-color': 'rgba(0, 0, 0, 0.1)',
                color: '#000',
                'border-bottom': '3px solid #ccc',
                'text-align': 'center'
            },
            td: {
                'text-align': 'center',
                'width': "10px"
            }
        }
    }).render(document.getElementById(id));
}