window.addEventListener('load', function () {
    setTimeout(hide_message_div, 3000);
    try {
        set_menu_button_active_style();
    } catch {

    }
});

function hide_message_div() {
    let message_div = document.getElementById('message_div');
    if (message_div) {
        message_div.style.transform = 'translateX(100%)';
    }
}

function set_menu_button_active_style() {
    let page_title = document.title;
    if (page_title !== 'Login Users') {
        let pages_titles = {
            'orders_list_page_link': ['لیست درخواست ها', 'جزئیات درخواست'],
            'financial_requests_list_page_link': ['لیست درخواست های مالی', 'نمودار درخواست های مالی'],
            'send_message_page_link': ['ارسال پیغام'],
            'users_list_page_link': ['لیست کاربران'],
            'admins_list_page_link': ['لیست مدیران', 'مدیر جدید', 'ویرایش مدیر'],
            'data_definition_page_link': ['تعریف داده ها', 'دسته بندی جدید', 'ویرایش دسته بندی', 'واحد جدید', 'زباله جدید', 'ویرایش زباله'],
            'admin_account_settings_page_link': ['تنظیمات حساب کاربری'],
        }

        const key_1 = Object.keys(pages_titles).find(key => pages_titles[key].includes(page_title));
        let bottom_button_element = document.getElementById(key_1);
        try {
            bottom_button_element.classList.remove('text_color_1');
            bottom_button_element.classList.add('text_color_2');
        } catch {

        }
    }
}

function show_hide_popup(mode) {
    let popup_back_div = document.getElementById('popup_back_div')
    let popup_div = document.getElementById('popup_div')
    if (mode === 'show') {
        popup_back_div.classList.remove('display_none');
        popup_div.style.top = '50%';
        popup_div.style.transform = 'translate(-50%, -50%)';
    } else {
        popup_back_div.classList.add('display_none');
        popup_div.style.top = '0';
        popup_div.style.transform = 'translate(-50%, -100%)';
    }
}

function set_searchable_select(element_id, placeholder='انتخاب کنید') {
    const $select = $(`#${element_id}`);

    if ($select.hasClass('select2-hidden-accessible')) {
        $select.select2('destroy');
    }

    let select2_options = {
        placeholder: placeholder,
        minimumResultsForSearch: 0,
        dir: "rtl"
    };

    if (element_id === 'garbage_categories_select' || element_id === 'garbage_item_select' || element_id === 'garbage_list_select') {
        select2_options.templateResult = function (data) {
            if (!data.id) return data;
            if (data.element?.getAttribute('data-hidden') === 'true') {
                return null;
            }
            return data.text;
        };
    }

    $select.select2(select2_options);
}

function show_hide_menu(mode) {
    let menu_back_div = document.getElementById('menu_back_div');
    let menu_div = document.getElementById('menu_div');
    let close_button = document.getElementById('close_button');

    if (mode === 'show') {
        menu_back_div.style.transform = 'translateX(0)';
        menu_div.style.transform = 'translateX(0)';
        close_button.style.transform = 'translate(-100%, 0)';
    } else {
        menu_back_div.style.transform = 'translateX(-100%)';
        menu_div.style.transform = 'translateX(100%)';
        close_button.style.transform = 'translate(-100%, -100%)';
    }
}