window.addEventListener('load', function () {
    convertAllNumbersInPage();
    set_inventory_standard_style();
});

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

function set_inventory_standard_style() {
    let inventory_div = document.getElementById('price_div').innerText;
    inventory_div = inventory_div.replace(/[^0-9۰-۹]/g, "");
    inventory_div = inventory_div.replace(/[۰-۹]/g, d => "۰۱۲۳۴۵۶۷۸۹".indexOf(d));
    let formatted = Number(inventory_div).toLocaleString("fa-IR");
    document.getElementById('price_div').innerText = formatted;
}
