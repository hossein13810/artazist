function filter_orders() {
    let filters_div = document.getElementById('filters_div');
    let user_orders_list = document.getElementById('user_orders_list');
    let filters = [];
    let all_check = true;
    for (let check of filters_div.getElementsByTagName('input')) {
        if (check.checked) {
            all_check = false;
            if (check.id === 'accept_order_check') {
                filters.push('تایید شده')
            } else if (check.id === 'not_accept_order_check') {
                filters.push('رد شده')
            } else if (check.id === 'pending_order_check') {
                filters.push('در انتظار')
            } else if (check.id === 'delete_order_check') {
                filters.push('لغو شده')
            }
        }
    }

    if (all_check) {
        filters = ['تایید شده', 'رد شده', 'در انتظار', 'لغو شده']
    }
    for (let order of user_orders_list.querySelectorAll('div.one_order_div')) {
        if (filters.includes(order.querySelector('span.status_span').innerText)) {
            order.classList.remove('display_none');
        } else {
            order.classList.add('display_none');
        }
    }
}