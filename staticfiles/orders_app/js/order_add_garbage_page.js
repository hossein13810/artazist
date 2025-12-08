window.addEventListener('load', function () {
    set_searchable_select('garbage_categories_select');
    set_searchable_select('garbage_item_select', 'ابتدا دسته بندی زباله را انتخاب کنید');

    load_garbage_categories_data();

    let garbage_categories_select = $('#garbage_categories_select');
    let garbage_categories_description_span = document.getElementById('garbage_categories_description_span');
    garbage_categories_select.on('select2:select', function () {
        let selectedOption = $(this).find('option:selected');
        garbage_categories_description_span.innerText = selectedOption.attr('name');
        document.getElementById('garbage_unit_span').innerText = '';
        document.getElementById('garbage_unit_price_span').innerText = '';
        document.getElementById('garbage_item_description_span').innerText = '';

        set_searchable_select('garbage_item_select');
        load_garbage_items_data();
    });

    let garbage_item_select = $('#garbage_item_select');
    let garbage_item_description_span = document.getElementById('garbage_item_description_span');
    garbage_item_select.on('select2:select', function () {
        let selectedOption = $(this).find('option:selected');
        garbage_item_description_span.innerText = selectedOption.attr('name').split('-.-.-')[0];
        set_garbage_info_span(selectedOption.attr('name').split('-.-.-')[1], selectedOption.attr('name').split('-.-.-')[2]);
    });
});

function load_garbage_categories_data() {
    let garbage_categories_select = document.getElementById('garbage_categories_select');
    fetch('/load_garbage_categories_data/', {
        method: 'POST',
    }).then(response => response.json()).then(data => {
        for (let category of data) {
            garbage_categories_select.innerHTML += `
                <option value="${category['id']}" name="${category['description']}">${category['categories_name']}</option>
            `
        }
    })
}

function load_garbage_items_data() {
    let garbage_categories_select = document.getElementById('garbage_categories_select');
    let garbage_item_select = document.getElementById('garbage_item_select');

    garbage_item_select.innerHTML = `
        <option value="">انتخاب کنید</option>
    `;

    let form_data = new FormData();
    form_data.append('category_db_id', garbage_categories_select.value);

    fetch('/load_garbage_items_data/', {
        method: 'POST',
        body: form_data
    }).then(response => response.json()).then(data => {
        for (let item of data) {
            garbage_item_select.innerHTML += `
                <option value="${item['id']}" name="${item['description']}-.-.-${item['unit_name']}-.-.-${item['price_per_unit']}">${item['garbage_item_name']}</option>
            `
        }
    })
}

function set_garbage_info_span(unit, price) {
    let garbage_unit_span = document.getElementById('garbage_unit_span');
    let garbage_unit_price_span = document.getElementById('garbage_unit_price_span');

    garbage_unit_span.innerText = ` (${unit}) `;
    garbage_unit_price_span.innerText = `قیمت هر ${unit} ${price} تومان`;
}

function check_inputs() {
    let garbage_categories_select = document.getElementById('garbage_categories_select').value;
    let garbage_item_select = document.getElementById('garbage_item_select').value;
    let garbage_amount_input = document.getElementById('garbage_amount_input').value;
    let description_input = document.getElementById('description_input').value;
    let add_button = document.getElementById('add_button');

    if (garbage_categories_select !== '' && garbage_item_select !== '' && garbage_amount_input !== '' && description_input !== '') {
        add_button.disabled = false;
        add_button.classList.remove('disabled_element');
    } else {
        add_button.disabled = true;
        add_button.classList.add('disabled_element');
    }
}