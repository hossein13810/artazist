let lastDataHash = null;
let garbage_num = 1;
window.addEventListener('load', async function () {
    await load_orders_data();

    let orders_list_div = document.getElementById('orders_list_div');
    await sleep(1000);
    for (let map of orders_list_div.querySelectorAll('div.map_div')) {
        await load_map_data(`${map.id}`, map.getAttribute('aria-label').split('__')[0], map.getAttribute('aria-label').split('__')[1]);
    }

    setInterval(load_orders_data, 1000);
})

async function load_orders_data() {
    let orders_list_div = document.getElementById('orders_list_div');
    let write_orders_list_page_input = document.getElementById('write_orders_list_page_input').value;
    fetch('/load_orders_data/', {
        method: 'POST',
    }).then(response => response.json()).then(data => {
        let dataHash = JSON.stringify(data);
        let exist = false;
        if (dataHash === lastDataHash) {
            exist = true;
        }
        if (!exist) {
            lastDataHash = dataHash;
            let html_str = '';
            let number_count = 1;
            for (let order of data) {
                let status_html = '';
                if (order['order_status'] === null) {
                    if (write_orders_list_page_input === 'True') {
                        status_html = `
                            <div class="button_group_div w_100">
                                <a class="button_element background_color_success text_color_1 order_status_button w_48 border_success" onclick="save_order_details_popup('${order['access_token']}')">تایید</a>
                                <a class="button_element background_color_error text_color_1 order_status_button w_48 border_error" href="/save_order_status/?access_token=${order['access_token']}&status=false">رد</a>
                            </div>
                        `
                    } else {
                        status_html = `
                            <span class="analyze_color_8 font_Ray_Bold">در انتظار</span>
                        `
                    }
                } else if (order['order_status']) {
                    status_html = `
                        <span class="analyze_color_9 font_Ray_Bold">تایید شده</span>
                    `
                } else if (!order['order_status']) {
                    status_html = `
                    <span class="text_color_error font_Ray_Bold">رد شده</span>
                `
                }
                html_str += `
                    <div class="one_order_div">
                        <div class="map_main_div">
                            <div class="map_hide_div">
                                <div class="map_lock_div"></div>
                                <div class="center_marker"></div>
                                <div class="copy_location_div" onclick="copy_text('https://www.google.com/maps/search/?api=1&query=${order['order_map_lat_location']},${order['order_map_lng_location']}')">کپی آدرس</div>
                                <div id="map_${number_count}" class="map_div" aria-label="${order['order_map_lat_location']}__${order['order_map_lng_location']}"></div>
                            </div>
                        </div>
                        <div>${order['access_token']}</div>
                        <div>${order['user_data__user_firstname']} ${order['user_data__user_lastname']}</div>
                        <div>${order['user_data__phone_number']}</div>
                        <div>${order['get_jalali_created_datetime']}</div>
                        <div>${order['get_str_order_date']} - ${order['order_timeline']}</div>
                        <div class="margin_left_10">${status_html}</div>
                    </div>
                `
                number_count += 1;
            }
            orders_list_div.innerHTML = html_str;
        }
    })
    return null;
}

async function load_map_data(map_id, lat, lng) {
    const API_KEY = "web.1055f2c1ecdb4a9ebde0da823aa2f8b5";

    map = new L.Map(map_id, {
        key: API_KEY,
        maptype: "neshan",
        poi: true,
        traffic: true,
        center: [lat, lng],
        zoom: 16,
        maxZoom: 19,
        zoomControl: false,
    });
}

function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}

function copy_text(text) {
    let alert_div = document.getElementById('alert_div');
    navigator.clipboard.writeText(text).then(r => {
        alert_div.innerText = 'لینک موقعیت مکانی با موفقیت کپی شد';
        alert_div.classList.add('message_success');
        alert_div.classList.remove('display_none');
        setTimeout(() => {
            alert_div.style.transform = 'translateX(100%)';
        }, 3000);
    })
}

function save_order_details_popup(access_token) {
    let popup_div = document.getElementById('popup_div');
    popup_div.style.width = '45%';
    popup_div.style.maxHeight = '80%';

    popup_div.innerHTML = `
        <form action="/save_order_details/" method="post">
            <input type="hidden" value="${access_token}" name="access_token">
            <div class="font_Ray">لیست زباله ها</div>
            <div class="garbage_groups_list_div" id="garbage_groups_list_div"></div>
            <div class="button_group_div">
                <button class="button_element background_color_0_4 font_Ray w_100 border_0_2" type="button" onclick="add_garbage_group_div()">+</button>
            </div>
            <div class="all_price_div font_Ray margin_top_20">
                <span>جمع مبلغ: </span>
                <span id="all_price_span">0</span>
                <span id="all_price_span">تومان </span>
            </div>
            <div class="button_group_div margin_top_20 w_100 ju_con_sp_bet">
                <button class="button_element background_color_0_2 text_color_1 font_Ray border_none w_49" type="button" onclick="show_hide_popup('hide')">لغو</button>
                <button class="button_element text_color_0 font_Ray w_49 border_none disabled_element" id="save_button" type="submit" disabled>ذخیره</button>
            </div>
        </form>
        `
    set_searchable_select('garbage_list_select', 'انتخاب کنید');
    show_hide_popup('show');
}

$(document).on('select2:select', '[id^="garbage_list_select_"]', function (e) {
    const idx = this.id.split('_').pop();
    const span = document.getElementById(`garbage_description_span_${idx}`);
    const garbage_amount_input = document.getElementById(`garbage_amount_input_${idx}`);
    const selectedData = e.params.data;
    span.innerText = selectedData.description || '';
    garbage_amount_input.placeholder = `مقدار (${selectedData.units_of_measurement_data})`;
    garbage_amount_input.dataset.price = selectedData.price_per_unit;

    garbage_amount_input.disabled = false;
});

function add_garbage_group_div() {
    const garbage_groups_list_div = document.getElementById('garbage_groups_list_div');

    fetch('/load_garbages_data/', {method: 'POST'})
        .then(resp => resp.json())
        .then(data => {
            console.log(data)
            const options_list = data.map(g => ({
                id: g.id ?? g['garbage_item_id'] ?? g['garbage_item_name'],
                text: g['garbage_item_name'] + ' - ' + g['price_per_unit'] + ' تومان',
                description: g['description'],
                units_of_measurement_data: g['units_of_measurement_data'],
                price_per_unit: g['price_per_unit'],
            }));

            const newHtml = `
                <div class="garbage_group_div margin_bottom_20" id="garbage_group_div_${garbage_num}">
                    <div class="input_group_div w_49 margin_left_10">
                        <select aria-label="" class="input_element w_100 font_Ray background_color_0_4 cursor_pointer" id="garbage_list_select_${garbage_num}" name="garbage_list_select_${garbage_num}">
                            <option value="" data-hidden="true">انتخاب کنید</option>
                        </select>
                        <span class="font_Ray text_color_0_3 margin_right_10 description_span" id="garbage_description_span_${garbage_num}"></span>
                    </div>
                    <div class="input_group_div w_49 margin_left_10">
                        <input class="input_element background_color_0_4 font_Ray border_0_2 amount_input" disabled type="number" onkeyup="set_all_price_span()" onchange="set_all_price_span()" id="garbage_amount_input_${garbage_num}" name="garbage_amount_input_${garbage_num}">
                        <span class="font_Ray text_color_0_3 margin_right_10 description_span"></span>
                    </div>
                    <div class="delete_button_div">
                        <span class="delete_button cursor_pointer" onclick="delete_garbage_group(this)"><i class="bi bi-trash-fill"></i></span>
                    </div>
                </div>
            `;

            garbage_groups_list_div.insertAdjacentHTML('beforeend', newHtml);

            let garbage_amount_input = document.getElementById(`garbage_amount_input_${garbage_num}`);
            control_placeholder(garbage_amount_input);

            const $select = $(`#garbage_list_select_${garbage_num}`);
            document.getElementById(`garbage_list_select_${garbage_num}`)
                .setAttribute("data-options", JSON.stringify(options_list));
            $select.select2({
                dir: "rtl",
                data: options_list,
                placeholder: "انتخاب کنید",
                allowClear: false,
                templateResult: function (data) {
                    if (data.element && data.element.dataset.hidden === "true") return null;
                    return data.text;
                },
                templateSelection: function (data) {
                    if (!data.id) return "انتخاب کنید";
                    return data.text;
                }
            });

            garbage_num += 1;
            set_button_disabled(true);
        })
        .catch(err => console.error(err));
}

function control_placeholder(input) {
    let originalPlaceholder = input.placeholder;
    input.addEventListener("focus", function () {
        input.placeholder = "";
    });

    input.addEventListener("blur", function () {
        input.placeholder = originalPlaceholder;
    });
}

function set_all_price_span() {
    const garbage_groups_list_div = document.getElementById('garbage_groups_list_div');
    let all_price_span = document.getElementById('all_price_span');

    let new_price = 0;
    for (let input of garbage_groups_list_div.querySelectorAll('input.amount_input')) {
        if (input.value !== '') {
            new_price += Number(input.value) * Number(input.dataset.price);
        }
    }
    all_price_span.innerText = String(new_price);
    set_button_disabled();
}

function delete_garbage_group(button) {
    const group = button.closest('.garbage_group_div');
    group.remove();
    reorder_garbage_groups();
    set_all_price_span();
    if (garbage_num === 1) {
        set_button_disabled(true);
    } else {
        set_button_disabled();
    }
}

function reorder_garbage_groups() {

    let groups = document.querySelectorAll('.garbage_group_div');

    groups.forEach((group, index) => {
        let i = index + 1;

        group.id = `garbage_group_div_${i}`;

        let select = group.querySelector('select');
        let oldValue = $(select).val();

        $(select).select2('destroy');

        select.id = `garbage_list_select_${i}`;
        select.name = `garbage_list_select_${i}`;

        let span = group.querySelector('.description_span');
        if (span) span.id = `garbage_description_span_${i}`;

        let input = group.querySelector('input.amount_input');
        if (input) {
            input.id = `garbage_amount_input_${i}`;
            input.name = `garbage_amount_input_${i}`;
        }

        $(select).select2({
            dir: "rtl",
            placeholder: "انتخاب کنید",
            data: JSON.parse(select.getAttribute("data-options"))
        }).val(oldValue).trigger("change");
    });

    garbage_num = groups.length + 1;
}

function set_button_disabled(value = false) {
    const garbage_groups_list_div = document.getElementById('garbage_groups_list_div');

    if (!value) {
        for (let input of garbage_groups_list_div.querySelectorAll('input.amount_input')) {
            if (input.value === '') {
                value = true;
            }
        }
    }

    let save_button = document.getElementById('save_button');
    save_button.disabled = value;

    if (!value) {
        save_button.classList.remove('disabled_element');
        save_button.classList.add('background_color_2');
    } else {
        save_button.classList.add('disabled_element');
        save_button.classList.remove('background_color_2');
    }
}