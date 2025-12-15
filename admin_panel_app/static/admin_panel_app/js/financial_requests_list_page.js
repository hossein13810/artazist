let filters = {
    'status_filters': ['unpaied_check_input', 'paied_check_input', 'error_check_input'],
    'order_date': ['', '']
};

let lastDataHash = null;
window.addEventListener('load', function () {
    load_requests_data();
    setInterval(load_requests_data, 500);

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
                $("#to_date_input").val(pretty);
                filter_to_date(unix);
            }
        });
    });
})

function load_requests_data() {
    let table_tbody = document.getElementById('table_tbody');
    let write_financial_requests_list_page_input = document.getElementById('write_financial_requests_list_page_input').value;
    fetch('/load_financial_requests_data/', {
        method: 'POST',
    }).then(response => response.json()).then(data => {
        let dataHash = JSON.stringify(data);
        if (dataHash === lastDataHash) {
            return;
        }
        lastDataHash = dataHash;
        let html_str = '';
        let number_count = 1;
        for (let request of data) {
            let status_html = '';
            if ((request['status'] === null && filters['status_filters'].includes('unpaied_check_input')) || (request['status'] === true && filters['status_filters'].includes('paied_check_input')) || (request['status'] === false && filters['status_filters'].includes('error_check_input'))) {
                let from_date = null;
                let to_date = null;
                if (filters['order_date'][0] !== '') {
                    from_date = filters['order_date'][0];
                }
                if (filters['order_date'][1] !== '') {
                    to_date = filters['order_date'][1];
                }

                let show = true;
                if (from_date !== null) {
                    if (parsePersian(request['get_jalali_request_datetime']) < parsePersian(from_date)) {
                        show = false;
                    }
                }
                if (to_date !== null) {
                    if (parsePersian(request['get_jalali_request_datetime']) > parsePersian(to_date)) {
                        show = false;
                    }
                }

                if (show) {
                    if (request['status'] === null) {
                        if (write_financial_requests_list_page_input === 'True') {
                            status_html = `
                                <div class="button_group_div w_100">
                                    <a class="button_element background_color_success text_color_1 order_status_button w_48 border_success" href="/save_financial_status/?id=${request['id']}">تایید پرداخت</a>
                                    <button class="button_element background_color_error text_color_1 order_status_button w_48 border_error font_Ray" onclick="dont_pay('${request['id']}')">عدم تایید پرداخت</button>
                                </div>
                            `
                        } else {
                            status_html = `
                                <span class="analyze_color_8 font_Ray_Bold">در انتظار</span>
                            `
                        }

                    } else {
                        if (request['status'] === true) {
                            status_html = `
                                <span class="analyze_color_9 font_Ray_Bold">پرداخت شده</span>
                            `
                        } else {
                            status_html = `
                                <span class="analyze_color_7 font_Ray_Bold">مشکل دار</span>
                            `
                        }
                    }

                    html_str += `
                        <tr>
                            <td>${number_count}</td>
                            <td>${request['wallet_data__user_data__user_firstname']} ${request['wallet_data__user_data__user_lastname']}</td>
                            <td>${request['wallet_data__user_data__phone_number']}</td>
                            <td>${request['wallet_data__sheba_number']}</td>
                            <td>${request['withdrawal_amount']}</td>
                            <td>${request['get_jalali_request_datetime']}</td>
                            <td>${status_html}</td>
                        </tr>
                    `
                    number_count += 1;
                }
            }
        }
        table_tbody.innerHTML = html_str;
    })
}

function exportExcel() {
    const table = document.getElementById("requests_table");

    let wb = XLSX.utils.table_to_book(table, {sheet: "Sheet1"});
    let ws = wb.Sheets["Sheet1"];

    Object.keys(ws).forEach(cell => {
        if (cell[0] === "!") return;
        let val = ws[cell].v;

        if (typeof val === "number" || /^\d+$/.test(val)) {
            ws[cell] = {t: "s", v: String(val)};
        }
    });
    XLSX.writeFile(wb, "table.xlsx");
}

function dont_pay(req_id) {
    let popup_div = document.getElementById('popup_div');
    popup_div.innerHTML = `
        <form action="/save_financial_status/" method="post">
            <input type="hidden" value="${req_id}" name="req_id_input">
            <div class="analyze_color_8 font_Ray">عدم تایید پرداخت!</div>
            <div class="text_color_2 font_Ray">لطفا مشکل عدم تایید را وارد کرده و سپس دکمه ذخیره را بزنید.</div>
            <div class="input_group_div margin_top_10 w_100">
                <textarea class="input_element text_area background_color_0_4 font_Ray w_100 border_0_2" name="text_area_input"></textarea>
            </div>
            <div class="button_group_div margin_top_20 w_100 ju_con_sp_bet">
                <button class="button_element background_color_0_2 text_color_1 font_Ray border_none w_48" type="button" onclick="show_hide_popup('hide')">لغو</button>
                <button class="button_element background_color_2 text_color_0 font_Ray w_48 border_none" type="submit">ذخیره</button>
            </div>
        </form>
    `

    show_hide_popup('show');
}

function filter_status() {
    lastDataHash = null;
    let unpaied_check_input = document.getElementById('unpaied_check_input');
    let paied_check_input = document.getElementById('paied_check_input');
    let error_check_input = document.getElementById('error_check_input');

    let status_filters = []
    if (unpaied_check_input.checked) {
        status_filters.push('unpaied_check_input');
    }
    if (paied_check_input.checked) {
        status_filters.push('paied_check_input');
    }
    if (error_check_input.checked) {
        status_filters.push('error_check_input');
    }

    filters['status_filters'] = status_filters;
    load_requests_data();
}

function parsePersian(str) {
    const parts = str.split(" ");

    const day = parseInt(parts[0]);
    const month = getMonthNumber(parts[1]);
    const year = parseInt(parts[2]);

    return new persianDate([year, month, day]).toDate();
}

function getMonthNumber(name) {
    const months = {
        "فروردین": 1, "اردیبهشت": 2, "خرداد": 3, "تیر": 4,
        "مرداد": 5, "شهریور": 6, "مهر": 7, "آبان": 8,
        "آذر": 9, "دی": 10, "بهمن": 11, "اسفند": 12
    };
    return months[name];
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

function filter_from_date(selected) {
    lastDataHash = null;
    let date = new persianDate(selected);
    let formatted = convertPersianNumbersToEnglish(date.format("D MMMM YYYY"));
    filters['order_date'][0] = formatted;
    load_requests_data();
}

function filter_to_date(selected) {
    lastDataHash = null;
    let date = new persianDate(selected);
    let formatted = convertPersianNumbersToEnglish(date.format("D MMMM YYYY"));
    filters['order_date'][1] = formatted;
    load_requests_data();
}

function clear_filters() {
    lastDataHash = null;
    filters = {
        'status_filters': ['unpaied_check_input', 'paied_check_input', 'error_check_input'],
        'order_date': ['', '']
    };

    $("#unpaied_check_input").prop("checked", true);
    $("#paied_check_input").prop("checked", true);
    $("#error_check_input").prop("checked", true);
    $("#from_date_input").val('');
    $("#to_date_input").val('');
    load_requests_data();
}