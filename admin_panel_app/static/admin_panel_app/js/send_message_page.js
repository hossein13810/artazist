let message_interval = null;
window.addEventListener('load', function () {
    set_searchable_select('users_list_select', 'همه');
});

function start_send_messages() {
    let inputs_div = document.getElementById('inputs_div');
    let logger_div = document.getElementById('logger_div');
    let users_list_select = $('#users_list_select').select2();
    let message_text_input = document.getElementById('message_text_input');
    let send_mode_notif_input = document.getElementById('send_mode_notif_input');
    let logger_text_area = document.getElementById('logger_text_area');

    inputs_div.classList.add('display_none');
    logger_div.classList.remove('display_none');

    if (users_list_select.val().length === 0) {
        users_list_select = 'all';
    } else {
        users_list_select = users_list_select.val();
    }

    let form_data = new FormData();
    form_data.append('users_list_select', users_list_select);
    form_data.append('message_text_input', message_text_input.value);
    form_data.append('send_mode_notif_input', send_mode_notif_input.checked);

    message_interval = setInterval(operation_messages_data_manager, 200);
    fetch('/send_message/', {
        method: 'POST',
        body: form_data
    }).then(response => response.text()).then(data => {
        if (data === 'done') {
            clearInterval(message_interval);
            logger_text_area.innerHTML += `
                <div class="analyze_color_4 font_Ray">---------------------------------------------------------</div>
                <div class="analyze_color_9 font_Ray">اتمام فرآیند</div>
            `
            logger_text_area.scrollTo({
                top: logger_text_area.scrollHeight,
                behavior: 'smooth'
            });
        }
    })
}

function operation_messages_data_manager() {
    let logger_text_area = document.getElementById('logger_text_area');
    fetch('/operation_messages_data_manager/', {
        method: 'GET',
    }).then(response => response.text()).then(data => {
        if (data !== 'None') {
            let phone = data.split(' --- ')[0];
            let status = data.split(' --- ')[1];
            let mode = data.split(' --- ')[2];
            if (status === '200') {
                logger_text_area.innerHTML += `
                    <div class="analyze_color_9 font_Ray"><span class="text_color_3 font_Ray_Bold">${mode} --> </span>${phone}: ارسال موفق</div>
                `
            } else {
                logger_text_area.innerHTML += `
                    <div class="text_color_error font_Ray"><span class="text_color_3 font_Ray_Bold">${mode} --> </span>${phone}: ارسال ناموفق</div>
                `
            }
        }
        logger_text_area.scrollTo({
            top: logger_text_area.scrollHeight,
            behavior: 'smooth'
        });
    })
}