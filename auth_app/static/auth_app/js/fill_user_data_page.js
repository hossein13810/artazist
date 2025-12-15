function check_inputs() {
    let firstname_input = document.getElementById('firstname_input').value;
    let lastname_input = document.getElementById('lastname_input').value;
    let national_code_input = document.getElementById('national_code_input').value;
    let save_button = document.getElementById('save_button');

    if (firstname_input !== '' && lastname_input !== '' && national_code_input !== '') {
        save_button.classList.remove('disabled_element');
        save_button.disabled = false;
    } else {
        save_button.classList.add('disabled_element');
        save_button.disabled = true;
    }
}