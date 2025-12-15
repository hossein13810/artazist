window.addEventListener('load', function () {
    $(document).ready(function () {
        $("#datepicker_from_input").persianDatepicker({
            format: 'YYYY/MM/DD',
            initialValue: true,
            autoClose: true,
            calendar: {
                persian: {
                    leapYearMode: "astronomical"
                }
            }
        });
    });

    $(document).ready(function () {
        const fiveDaysLater = new persianDate().add('days', 5).format('YYYY/MM/DD');
        let datepicker_to = $("#datepicker_to_input");
        datepicker_to.persianDatepicker({
            format: 'YYYY/MM/DD',
            initialValue: false,
            autoClose: true,
            calendar: {
                persian: {
                    leapYearMode: "astronomical"
                }
            }
        });
        datepicker_to.val(fiveDaysLater);
    });
})

function check_inputs() {
    let order_title_input = document.getElementById('order_title_input').value;
    let order_description_input = document.getElementById('order_description_input').value;
    let save_button = document.getElementById('save_button');

    if (order_title_input !== '' && order_description_input !== '') {
        save_button.disabled = false;
        save_button.classList.remove('disabled_element');
    } else {
        save_button.disabled = true;
        save_button.classList.add('disabled_element');
    }
}