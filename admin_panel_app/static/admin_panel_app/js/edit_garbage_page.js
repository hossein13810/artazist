function delete_garbage_popup(garbage_id) {
    let popup_div = document.getElementById('popup_div');
    popup_div.innerHTML = `
        <div class="analyze_color_8 font_Ray">هشدار!</div>
        <div class="text_color_2 font_Ray">آیا برای حذف زباله مطمئن هستید؟</div>
        <div class="button_group_div margin_top_20 w_100 ju_con_sp_bet">
            <button class="button_element background_color_0_2 text_color_1 font_Ray border_none w_48" onclick="show_hide_popup('hide')">لغو</button>
            <a class="button_element background_color_2 text_color_0 font_Ray w_48" href="/delete_garbage/?garbage_id=${garbage_id}">حذف</a>
        </div>
    `

    show_hide_popup('show');
}