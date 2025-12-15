function check_input() {
    let phone_number_input = document.getElementById('phone_number_input');
    let next_button = document.getElementById('next_button');

    if (phone_number_input.value.trim() !== '' && phone_number_input.value.length === 11 && phone_number_input.value.startsWith('0')) {
        next_button.classList.remove('disabled_element');
        next_button.classList.add('background_color_0');
        next_button.disabled = false;
    } else {
        next_button.classList.add('disabled_element');
        next_button.classList.remove('background_color_0');
        next_button.disabled = true;
    }
}