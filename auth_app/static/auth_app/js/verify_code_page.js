window.addEventListener('load', function () {
    timer_func();
});

function timer_func() {
    let time = 2 * 60;

    const timer_span = document.getElementById('timer_span');
    const send_code_again_span = document.getElementById('send_code_again_span');

    const countdown = setInterval(() => {
        const minutes = Math.floor(time / 60);
        const seconds = time % 60;

        timer_span.innerText = `${minutes}:${seconds < 10 ? '0' : ''}${seconds}`;

        time--;

        if (time < 0) {
            clearInterval(countdown);
            send_code_again_span.innerHTML = "<button type='button' onclick='show_loading_div(), location.reload();' class='text_color_2 font_Ray background_color_0 border_2 button_element font_12px'>ارسال مجدد کد</button>";
        }
    }, 1000);
}

function check_input() {
    let random_code_input = document.getElementById('random_code_input');
    let next_button = document.getElementById('next_button');

    if (random_code_input.value.trim() !== '' && random_code_input.value.length === 5) {
        next_button.classList.remove('disabled_element');
        next_button.classList.add('background_color_0');
        next_button.disabled = false;
    } else {
        next_button.classList.add('disabled_element');
        next_button.classList.remove('background_color_0');
        next_button.disabled = true;
    }
}