let order_date_filter = ['', ''];
let myPieChart;
let myBarChart;

window.addEventListener('load', async function () {
    const today = new persianDate().subtract('day', 0);
    const fiveDaysAgo = new persianDate().subtract('day', 4);
    $("#from_date_input").val(fiveDaysAgo.format("YYYY/MM/DD"));

    order_date_filter[0] = convertPersianNumbersToEnglish(fiveDaysAgo.format("YYYY/MM/DD"));
    order_date_filter[1] = convertPersianNumbersToEnglish(today.format("YYYY/MM/DD"));

    await set_charts_data()

    $(function () {
        $("#from_date_input").persianDatepicker({
            format: "YYYY/MM/DD",
            initialValue: false,
            autoClose: true,
            calendar: {
                persian: {
                    leapYearMode: "astronomical"
                }
            },
            onSelect: function (unix) {
                let date = new persianDate(unix);
                let pretty = date.format("D MMMM YYYY");
                $("#from_date_input").val(pretty);
                filter_from_date(unix);
            }
        });

        $("#to_date_input").persianDatepicker({
            format: "YYYY/MM/DD",
            initialValue: true,
            autoClose: true,
            calendar: {
                persian: {
                    leapYearMode: "astronomical"
                }
            },
            onSelect: function (unix) {
                let date = new persianDate(unix);
                let pretty = date.format("D MMMM YYYY");
                $("#to_date_input").val(pretty);
                filter_to_date(unix);
            }
        });
    });
})

async function set_charts_data() {
    await (async () => {
        let chrts_data = await load_charts_data();
        draw_circle_chart(chrts_data['circle_chart_data']);
        draw_bar_chart(chrts_data['bar_chart_data']);
    })();
}

async function load_charts_data() {
    let form_data = new FormData();
    form_data.append('order_date_filter', JSON.stringify(order_date_filter))
    const response = await fetch('/load_charts_data/', {
        method: 'POST',
        body: form_data
    });
    return await response.json();
}

function draw_circle_chart(data) {
    const ctx = document.getElementById('myPieChart').getContext('2d');

    if (myPieChart) {
        myPieChart.destroy();
    }

    myPieChart = new Chart(ctx, {
        type: 'pie',
        data: {
            labels: ['پرداخت نشده', 'پرداخت شده', 'مشکل دار'],
            datasets: [{
                label: '',
                data: data,
                backgroundColor: [
                    'rgba(255,253,109,0.7)',
                    'rgba(16,100,0,0.7)',
                    'rgba(255,79,79,0.7)',
                ],
                borderColor: [
                    'rgb(0,0,0)',
                    'rgb(0,0,0)',
                    'rgb(0,0,0)',
                ],
                borderWidth: 0
            }]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        font: {
                            family: 'Ray',
                            size: 12,
                        },
                        color: '#333'
                    }
                },
                title: {
                    display: true,
                    text: 'نمودار دایره‌ای وضعیت درخواست ها',
                    font: {
                        family: 'Ray',
                        size: 16,
                        weight: 'bold'
                    },
                    color: '#444'
                },
                tooltip: {
                    titleFont: {
                        family: 'Ray',
                        size: 10,
                        weight: 'bold'
                    },
                    bodyFont: {
                        family: 'Ray',
                        size: 10
                    }
                }
            }
        }
    });
}

function draw_bar_chart(bar_chart_data) {
    let days_list = [];
    let pay_false = [];
    let pay_true = [];
    let pay_error = [];
    for (let [day, data_list] of Object.entries(bar_chart_data)) {
        days_list.push(day);
        pay_false.push(data_list[0])
        pay_true.push(data_list[1])
        pay_error.push(data_list[2])
    }
    const ctx = document.getElementById('myBarChart').getContext('2d');

    if (myBarChart) {
        myBarChart.destroy();
    }

    myBarChart = new Chart(ctx, {
        type: 'bar',
        data: {
            labels: days_list,
            datasets: [
                {
                    label: 'پرداخت نشده',
                    data: pay_false,
                    backgroundColor: 'rgba(255,253,109,0.7)'
                },
                {
                    label: 'پرداخت شده',
                    data: pay_true,
                    backgroundColor: 'rgba(16,100,0,0.7)'
                },
                {
                    label: 'مشکل دار',
                    data: pay_error,
                    backgroundColor: 'rgba(255,79,79,0.7)'
                }
            ]
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                    labels: {
                        font: {
                            family: 'Ray',
                            size: 14
                        }
                    }
                },
                title: {
                    display: true,
                    text: 'نمودار میله‌ای چندسری',
                    font: {
                        family: 'Ray',
                        size: 18,
                        weight: 'bold'
                    }
                },
                tooltip: {
                    titleFont: {
                        family: 'Ray'
                    },
                    bodyFont: {
                        family: 'Ray'
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'روزها',
                        font: {
                            family: 'Ray',
                            size: 16
                        }
                    },
                    ticks: {
                        font: {
                            family: 'Ray',
                            size: 14
                        }
                    }
                },
                y: {
                    beginAtZero: true,
                    title: {
                        display: true,
                        text: 'تعداد',
                        font: {
                            family: 'Ray',
                            size: 16
                        }
                    },
                    ticks: {
                        font: {
                            family: 'Ray',
                            size: 14
                        }
                    }
                }
            }
        }
    });
}

function convertPersianNumbersToEnglish(input) {
    const persianNumbers = ['۰', '۱', '۲', '۳', '۴', '۵', '۶', '۷', '۸', '۹'];
    const englishNumbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'];

    let output = '';
    for (let i = 0; i < input.length; i++) {
        const index = persianNumbers.indexOf(input[i]);
        output += index > -1 ? englishNumbers[index] : input[i];
    }
    return output;
}

async function filter_from_date(selected) {
    let date = new persianDate(selected);
    let formatted = convertPersianNumbersToEnglish(date.format("YYYY/MM/D"));
    order_date_filter[0] = formatted;
    await set_charts_data()
}

async function filter_to_date(selected) {
    let date = new persianDate(selected);
    let formatted = convertPersianNumbersToEnglish(date.format("YYYY/MM/D"));
    order_date_filter[1] = formatted;
    await set_charts_data()
}