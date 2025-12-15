window.addEventListener('load', function () {
    convertAllNumbersInPage();
    set_inventory_standard_style();
    show_account_error();
});

function withdrawal_all_inventory() {
    let withdrawal_amount_input = document.getElementById('withdrawal_amount_input');
    let user_inventory_input = document.getElementById('user_inventory_input');

    withdrawal_amount_input.value = user_inventory_input.value;
    check_inputs();
}

function check_inputs() {
    let user_inventory_input = document.getElementById('user_inventory_input').value;
    let withdrawal_amount_input = document.getElementById('withdrawal_amount_input').value;
    let sheba_number_input = document.getElementById('sheba_number_input').value;
    let save_button = document.getElementById('save_button');

    if (withdrawal_amount_input !== '' && sheba_number_input !== '' && (Number(withdrawal_amount_input) <= Number(user_inventory_input)) && (Number(withdrawal_amount_input) >= 50000) && sheba_number_input.length === 24) {
        save_button.classList.remove('disabled_element');
        save_button.classList.add('background_color_0');
        save_button.disabled = false;
    } else {
        save_button.classList.add('disabled_element');
        save_button.classList.remove('background_color_0');
        save_button.disabled = true;
    }
}

const englishToPersianDigits = {
    '0': '۰',
    '1': '۱',
    '2': '۲',
    '3': '۳',
    '4': '۴',
    '5': '۵',
    '6': '۶',
    '7': '۷',
    '8': '۸',
    '9': '۹'
};

function convertNumbersToPersian(str) {
    return str.replace(/\d/g, d => englishToPersianDigits[d]);
}

function convertAllNumbersInPage() {
    const elements = document.querySelectorAll('body *');

    elements.forEach(el => {
        if (el.children.length === 0 && el.nodeName !== "SCRIPT" && el.nodeName !== "STYLE") {
            el.textContent = convertNumbersToPersian(el.textContent);
        }
    });
}

function set_inventory_standard_style() {
    let inventory_div = document.getElementById('inventory_div').innerText;
    inventory_div = inventory_div.replace(/[^0-9۰-۹]/g, "");
    inventory_div = inventory_div.replace(/[۰-۹]/g, d => "۰۱۲۳۴۵۶۷۸۹".indexOf(d));
    let formatted = Number(inventory_div).toLocaleString("fa-IR");
    document.getElementById('inventory_div').innerText = formatted;
}

function show_account_error() {
    let error = document.getElementById('error').value;
    if (error === 'account_data') {
        let popup_div = document.getElementById('popup_div');
        popup_div.innerHTML = `
            <div class="font_Ray_Black w_100">اطلاعات حساب کاربری شما تکمیل نشده!</div>
            <div class="font_Ray font_12px w_100 text_color_0_3">میتونین با زدن دکمه زیر اطلاعاتتون رو تکمیل کنین.</div>
            <div class="button_group_div margin_top_10">
                <a class="button_element font_Ray w_48 text_color_0 background_color_2 border_none" href="/account_settings_page/">تکمیل اطلاعات</a>
                <button class="button_element font_Ray background_color_0_2 w_48 text_color_3 border_0_2" type="button" onclick="show_hide_popup('hide')">لغو</button>
            </div>
        `
        show_hide_popup('show');
    }
}
