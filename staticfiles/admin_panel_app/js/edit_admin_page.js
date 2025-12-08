function delete_user_popup(user_id) {
    let popup_div = document.getElementById('popup_div');
    popup_div.innerHTML = `
        <div class="analyze_color_8 font_Ray">هشدار!</div>
        <div class="text_color_2 font_Ray">آیا برای حذف مدیر مطمئن هستید؟</div>
        <div class="button_group_div margin_top_20 w_100 ju_con_sp_bet">
            <button class="button_element background_color_0_2 text_color_1 font_Ray border_none w_48" onclick="show_hide_popup('hide')">لغو</button>
            <a class="button_element background_color_2 text_color_0 font_Ray w_48" href="/delete_admin/?user_id=${user_id}">حذف</a>
        </div>
    `

    show_hide_popup('show');
}

function check_inputs() {
    let firstname_input = document.getElementById('firstname_input').value;
    let lastname_input = document.getElementById('lastname_input').value;
    let phone_number_input = document.getElementById('phone_number_input').value;
    let national_code_input = document.getElementById('national_code_input').value;
    let password_input = document.getElementById('password_input').value;
    let re_password_input = document.getElementById('re_password_input').value;
    let save_button = document.getElementById('save_button');
    let checks_div = document.getElementById('checks_div');

    let check_one = false;
    for (let input of checks_div.querySelectorAll('input.parrent_check')) {
        if (input.checked) {
            check_one = true;
            break;
        }
    }

    if (firstname_input !== '' && lastname_input !== '' && phone_number_input !== '' && national_code_input !== '' && (password_input === re_password_input) && (phone_number_input.length === 11 && national_code_input.length === 10) && check_one) {
        save_button.disabled = false;
        save_button.classList.remove('disabled_element');
        save_button.classList.add('background_color_2');
    } else {
        save_button.disabled = true;
        save_button.classList.add('disabled_element');
        save_button.classList.remove('background_color_2');
    }
}

function show_sub_checks(parrent_check) {
    let write_orders_list_page_check_div = document.getElementById('write_orders_list_page_check_div');
    let write_financial_requests_list_page_check_div = document.getElementById('write_financial_requests_list_page_check_div');
    let write_admins_list_page_check_div = document.getElementById('write_admins_list_page_check_div');
    let write_data_definition_page_check_div = document.getElementById('write_data_definition_page_check_div');
    if (parrent_check.id === 'orders_list_page_check') {
        if (parrent_check.checked) {
            write_orders_list_page_check_div.classList.remove('display_none');
        } else {
            write_orders_list_page_check_div.classList.add('display_none');
        }
    } else if (parrent_check.id === 'financial_requests_list_page_check') {
        if (parrent_check.checked) {
            write_financial_requests_list_page_check_div.classList.remove('display_none');
        } else {
            write_financial_requests_list_page_check_div.classList.add('display_none');
        }
    } else if (parrent_check.id === 'admins_list_page_check') {
        if (parrent_check.checked) {
            write_admins_list_page_check_div.classList.remove('display_none');
        } else {
            write_admins_list_page_check_div.classList.add('display_none');
        }
    } else if (parrent_check.id === 'data_definition_page_check') {
        if (parrent_check.checked) {
            write_data_definition_page_check_div.classList.remove('display_none');
        } else {
            write_data_definition_page_check_div.classList.add('display_none');
        }
    }
}