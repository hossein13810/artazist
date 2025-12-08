function delete_garbage(order_garbage_db_id) {
    let popup_div = document.getElementById('popup_div');
    let access_token = document.getElementById('access_token').value;
    popup_div.innerHTML = `
        <div class="text_color_error font_Ray">آبا برای حذف زباله از لیست مطمئن هستید؟</div>
        <div class="button_group_div margin_top_20">
            <a class="button_element font_Ray background_color_2 w_48 text_color_0" href="/order_delete_garbage/?access_token=${access_token}&order_garbage_db_id=${order_garbage_db_id}">حذف</a>
            <button class="button_element font_Ray background_color_0_2 w_48 text_color_3 border_3" onclick="show_hide_popup('hide')">لغو</button>
        </div>
    `

    show_hide_popup('show');
}