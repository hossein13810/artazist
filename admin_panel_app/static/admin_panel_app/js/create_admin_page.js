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

    if (firstname_input !== '' && lastname_input !== '' && phone_number_input !== '' && national_code_input !== '' && password_input !== '' && (password_input === re_password_input) && (phone_number_input.length === 11 && national_code_input.length === 10) && check_one) {
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