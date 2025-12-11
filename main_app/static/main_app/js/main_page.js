let current = 0;
let animating = false;
let mode = true;
let lastDataHash = null;

window.addEventListener('load', function () {
    setInterval(function () {
        next_slide();
    }, 4000);
    set_slider();
    play_audio();
    convertAllNumbersInPage();
    load_new_orders_list();
    get_identification_code();
    setInterval(load_new_orders_list, 100);
});

function goToSlide(next, from) {
    const slides = Array.from(document.querySelectorAll('.one_slide_div'));
    if (animating || next === current || next < 0 || next >= slides.length) return;
    animating = true;

    const currentSlide = slides[current];
    const nextSlide = slides[next];

    let currentSpan = document.getElementById(`span_${currentSlide.id.split('_')[1]}`);
    let nextSpan = document.getElementById(`span_${nextSlide.id.split('_')[1]}`);

    currentSpan.classList.remove('on_circle');
    nextSpan.classList.add('on_circle');

    if (from === 'left') {
        nextSlide.style.transform = 'translateX(-100%)';
        nextSlide.classList.add('active');
        requestAnimationFrame(() => {
            nextSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transform = 'translateX(100%)';
            nextSlide.style.transform = 'translateX(0)';
        });
    } else if (from === 'right') {
        nextSlide.style.transform = 'translateX(100%)';
        nextSlide.classList.add('active');
        requestAnimationFrame(() => {
            nextSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transform = 'translateX(-100%)';
            nextSlide.style.transform = 'translateX(0)';
        });
    }

    setTimeout(() => {
        currentSlide.classList.remove('active');
        animating = false;
        current = next;
    }, 500);
}

function next_slide() {
    if (current === 3) {
        mode = false;
    } else if (current === 0) {
        mode = true;
    }

    if (mode) {
        goToSlide(current + 1, 'left');
    } else {
        goToSlide(current - 1, 'right');
    }
}

function delete_order(order_db_id) {
    let popup_div = document.getElementById('popup_div');
    popup_div.innerHTML = `
        <div class="font_Ray_Black">لغو درخواست</div>
        <div class="text_color_0_3 font_Ray font_12px">لطفا بهمون بگین چرا قصد دارین درخواستتون رو لغو کنین؟</div>
        <div class="cancel_order_radios_div margin_top_20">
            <div class="radio_group_div">
                <input type="radio" class="cursor_pointer" name="delete_order" id="radio_1" onchange="enable_delete_button('از زمان مورد انتظارم عبور کرده و نمیتونم حضور داشه باشم', ${order_db_id})"><label class="font_Ray cursor_pointer font_12px" for="radio_1">از زمان مورد انتظارم عبور کرده و نمیتونم حضور داشه باشم</label>
            </div>
            <div class="hr_line_div"></div>
            <div class="radio_group_div">
                <input type="radio" class="cursor_pointer" name="delete_order" id="radio_2" onchange="enable_delete_button('به روش دیگه ای تحویل دادم', ${order_db_id})"><label class="font_Ray cursor_pointer font_12px" for="radio_2">به روش دیگه ای تحویل دادم</label>
            </div>
            <div class="hr_line_div"></div>
            <div class="radio_group_div">
                <input type="radio" class="cursor_pointer" name="delete_order" id="radio_3" onchange="enable_delete_button('دلیل خاصی ندارم؛ خوشم میاد', ${order_db_id})"><label class="font_Ray cursor_pointer font_12px" for="radio_3">دلیل خاصی ندارم؛ خوشم میاد</label>
            </div>
        </div>
        <div class="button_group_div margin_top_20">
            <a class="button_element font_Ray w_100 text_color_0 border_none disabled_element" id="delete_button" disabled onclick="show_loading_div()">تایید و لغو درخواست</a>
        </div>
    `

    show_hide_popup('show');
}

function enable_delete_button(text, order_db_id) {
    let delete_button = document.getElementById('delete_button');
    delete_button.disabled = false;
    delete_button.classList.remove('disabled_element');
    delete_button.classList.add('background_color_2');
    delete_button.href = `/cancel_order/?order_db_id=${order_db_id}&text=${text}`
}

function set_slider() {
    const slides = Array.from(document.querySelectorAll('.one_slide_div'));
    let startX = 0;

    const slider = document.getElementById('slider_div');

    slider.addEventListener('touchstart', e => startX = e.touches[0].clientX);
    slider.addEventListener('touchend', e => {
        const diff = e.changedTouches[0].clientX - startX;
        if (Math.abs(diff) < 50) return;
        if (diff > 0 && current < slides.length - 1) {
            goToSlide(current + 1, 'left');
        } else if (diff < 0 && current > 0) {
            goToSlide(current - 1, 'right');
        }
    });

    let mouseDown = false;
    slider.addEventListener('mousedown', e => {
        mouseDown = true;
        startX = e.clientX;
    });
    window.addEventListener('mouseup', e => {
        if (!mouseDown) return;
        mouseDown = false;
        const diff = e.clientX - startX;
        if (Math.abs(diff) < 50) return;
        if (diff > 0 && current < slides.length - 1) goToSlide(current + 1, 'left');
        else if (diff < 0 && current > 0) goToSlide(current - 1, 'right');
    });
}

function play_audio() {
    let audio_play = document.getElementById('audio_play');
    let audio = document.getElementById('myAudio');
    let order_db_id = document.getElementById('order_db_id').value;

    if (audio_play.value === 'play') {
        let popup_div = document.getElementById('popup_div');
        popup_div.innerHTML = `
            <form action="/save_selected_address/" method="post">
                <div class="check_div"><i class="bi bi-check-circle"></i></div>
                <div class="font_Ray_Black w_100 text_align_center margin_top_20">درخواست شما با موفقیت ثبت شد!</div>
                <div class="font_Ray font_12px w_100 text_align_center text_color_0_3">میتونین آدرس رو به لیست آدرس های منتخب اضافه کنین.</div>
                <div class="input_group_div w_100 margin_top_20">
                    <input type="hidden" id="order_db_id" name="order_db_id" value="${order_db_id}">
                    <input class="input_element background_color_0_4 text_color_0_3 font_Ray border_0_2" aria-label="" placeholder="عنوان آدرس منتخب" id="selected_address_title_input" name="selected_address_title_input" onkeyup="check_address_title_input()" autocomplete="off">
                </div>
                <div class="button_group_div margin_top_10">
                    <button class="button_element font_Ray w_48 text_color_0 disabled_element border_none" disabled id="add_button" onclick="show_loading_div()">افزودن</button>
                    <button class="button_element font_Ray background_color_0_2 w_48 text_color_3 border_0_2" type="button" onclick="show_hide_popup('hide')">نمیخوام</button>
                </div>
            </form>
        `
        audio.currentTime = 0;
        audio.play();
        show_hide_popup('show');
    }
}

function check_address_title_input() {
    let selected_address_title_input = document.getElementById('selected_address_title_input');
    let add_button = document.getElementById('add_button');
    if (selected_address_title_input.value.length >= 3) {
        add_button.classList.remove('disabled_element');
        add_button.classList.add('background_color_2');
        add_button.disabled = false;
    } else {
        add_button.classList.add('disabled_element');
        add_button.classList.remove('background_color_2');
        add_button.disabled = true;
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

function load_new_orders_list() {
    let new_orders_list = document.getElementById('new_orders_list');
    fetch('/load_new_orders_list/', {
        method: 'POST',
    }).then(response => response.json()).then(data => {
        let dataHash = JSON.stringify(data);
        if (dataHash === lastDataHash) {
            return;
        }
        lastDataHash = dataHash;
        let html_str = '';
        for (let item of data) {
            html_str += `
                <div class="one_order_div w_90">
                    <div class="order_data_div">
                        <div class="text_color_1 font_Ray_Black"><span>${item['access_token']}</span></div>
                        <div class="text_color_1 data_text">
                            <span class="font_12px">بازه انتخابی</span>
                            <span class="font_12px">${item['timeline']}</span>
                        </div>
                        <div class="text_color_1 data_text">
                            <span class="font_12px">وضعیت</span>
                            <span class="font_12px status_span"><i class="bi bi-circle-fill"></i>در انتظار</span>
                        </div>
                        <div class="text_color_0_3 font_Ray text_align_justify font_12px margin_top_10">${item['address']}</div>
                        <div class="analyze_color_7 font_Ray w_100 text_align_center font_12px margin_top_10 delete_order_span" onclick="delete_order('${item['id']}')"><i class="bi bi-x"></i>لغو درخواست</div>
                        <div class="order_date_div font_Ray">
                            <span class="text_color_0_3 font_12px">برای ${item['order_date']}</span>
                        </div>
                    </div>
                </div>
            `
        }
        new_orders_list.innerHTML = html_str;
    })
}

function get_identification_code() {
    let identification_code = document.getElementById('identification_code').value;
    if (identification_code === 'true') {
        let popup_div = document.getElementById('popup_div');
        popup_div.innerHTML = `
            <form action="/save_identification_code/" method="post">
                <div class="check_div"><i class="bi bi-check-circle"></i></div>
                <div class="font_Ray_Black w_100 text_align_center margin_top_20">ورود شما با موفقیت ثبت شد!</div>
                <div class="font_Ray font_12px w_100 text_align_center text_color_0_3">اگه کد معرف دارین وارد کنین.</div>
                <div class="input_group_div w_100 margin_top_20">
                    <input class="input_element background_color_0_4 text_color_0_3 font_Ray border_0_2" type="tel" aria-label="" id="identification_code_input" name="identification_code_input" onkeyup="check_identification_code_input()" autocomplete="off">
                </div>
                <div class="button_group_div margin_top_10">
                    <button class="button_element font_Ray w_48 text_color_0 disabled_element border_none" disabled id="save_button" onclick="show_loading_div()">ذخیره</button>
                    <button class="button_element font_Ray background_color_0_2 w_48 text_color_3 border_0_2" type="button" onclick="show_hide_popup('hide')">ندارم</button>
                </div>
            </form>
        `
        show_hide_popup('show');
    }
}

function check_identification_code_input() {
    let identification_code_input = document.getElementById('identification_code_input');
    let save_button = document.getElementById('save_button');
    if (identification_code_input.value.length === 5) {
        save_button.classList.remove('disabled_element');
        save_button.classList.add('background_color_2');
        save_button.disabled = false;
    } else {
        save_button.classList.add('disabled_element');
        save_button.classList.remove('background_color_2');
        save_button.disabled = true;
    }
}

function introducing_to_friends() {
    let popup_div = document.getElementById('popup_div');
    let my_identification_code = document.getElementById('my_identification_code').value;
    popup_div.innerHTML = `
        <form action="/save_selected_address/" method="post">
            <div class="font_Ray_Black w_100 text_align_center margin_top_20">معرفی به دوستان!</div>
            <div class="font_Ray font_12px w_100 text_align_justify text_color_0_3">با معرفی برنامه به دوستاتون 10 هزار تومان به کیف پولتون اضافه میشه. کد معرفی شما این پایینه، دوستاتتون بعد از وارد شدن به برنامه میتونن اینو وارد کنن و شما رو به عنوان معرف ثبت کنن.</div>
            <div class="input_group_div w_100 margin_top_20">
                <input class="input_element background_color_0_4 text_color_1 font_Ray border_0_2 text_align_center" aria-label="" readonly id="my_identification_code_input" name="my_identification_code_input" value="${my_identification_code}">
            </div>
            <div class="button_group_div margin_top_10">
                <button class="button_element font_Ray background_color_2 w_48 text_color_0 border_none copy_button" type="button" onclick="copy_text('${my_identification_code}', this)">کپی کردن</button>
                <button class="button_element font_Ray background_color_0_2 w_48 text_color_3 border_0_2" type="button" onclick="show_hide_popup('hide')">بستن</button>
            </div>
        </form>
    `
    show_hide_popup('show');
}

function copy_text(text, button_element) {
    navigator.clipboard.writeText(text).then(r => {
        button_element.innerHTML = `<i class="bi bi-check-lg"></i>`
    })
}
