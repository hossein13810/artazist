window.addEventListener('load', async function () {
    let selected_address_list = document.getElementById('selected_address_list');
    for (let map of selected_address_list.querySelectorAll('div.map_div')) {
        await load_map_data(`${map.id}`, map.getAttribute('aria-label').split('__')[0], map.getAttribute('aria-label').split('__')[1]);
    }
})

async function load_map_data(map_id, lat, lng) {
    const API_KEY = "web.1055f2c1ecdb4a9ebde0da823aa2f8b5";

    map = new L.Map(map_id, {
        key: API_KEY,
        maptype: "neshan",
        poi: true,
        traffic: true,
        center: [lat, lng],
        zoom: 16,
        maxZoom: 19,
        zoomControl: false,
    });
}

function delete_order(address_db_id) {
    let popup_div = document.getElementById('popup_div');
    popup_div.innerHTML = `
        <div class="font_Ray_Black">حذف آدرس منتخب</div>
        <div class="text_color_0_3 font_Ray font_12px">از حذف آدرس منتخب مطمئن هستید؟</div>
        <div class="button_group_div margin_top_20">
            <a class="button_element background_color_2 font_Ray w_48 text_color_0 border_none" href="/delete_selected_address/?selected_adderss_id=${address_db_id}">تایید و حذف آدرس</a>
            <button class="button_element background_color_0_2 font_Ray w_48 text_color_3 border_none" onclick="show_hide_popup('hide')">لغو</button>
        </div>
    `

    show_hide_popup('show');
}