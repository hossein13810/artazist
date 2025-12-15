window.addEventListener('load', function () {
    check_inputs();

    let firstname_input = document.getElementById("firstname_input");
    let lastname_input = document.getElementById("lastname_input");
    let national_code_input = document.getElementById("national_code_input");
    let identification_code_input = document.getElementById("identification_code_input");

    control_placeholder(firstname_input);
    control_placeholder(lastname_input);
    control_placeholder(national_code_input);
    control_placeholder(identification_code_input);
});


function check_inputs() {
    let firstname_input = document.getElementById('firstname_input').value;
    let lastname_input = document.getElementById('lastname_input').value;
    let national_code_input = document.getElementById('national_code_input').value;
    let save_button = document.getElementById('save_button');

    if (national_code_input.length === 10 || national_code_input.length === 0) {
        save_button.classList.remove('disabled_element');
        save_button.disabled = false;
    } else {
        save_button.classList.add('disabled_element');
        save_button.disabled = true;
    }
}

function control_placeholder(input) {
    let originalPlaceholder = input.placeholder;
    input.addEventListener("focus", function () {
        input.placeholder = "";
    });

    input.addEventListener("blur", function () {
        input.placeholder = originalPlaceholder;
    });
}
