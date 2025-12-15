function check_inputs() {
    let firstname_input = document.getElementById('firstname_input').value;
    let lastname_input = document.getElementById('lastname_input').value;
    let password_input = document.getElementById('password_input').value;
    let re_password_input = document.getElementById('re_password_input').value;
    let save_button = document.getElementById('save_button');

    if (firstname_input !== '' && lastname_input !== '' && (password_input === re_password_input)) {
        save_button.disabled = false;
        save_button.classList.remove('disabled_element');
        save_button.classList.add('background_color_2');
    } else {
        save_button.disabled = true;
        save_button.classList.add('disabled_element');
        save_button.classList.remove('background_color_2');
    }
}
