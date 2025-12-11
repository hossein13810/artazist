let map;

window.addEventListener('load', async function () {
    await load_map_data();
    await getAddress(38.251558, 48.297227);
    let next_button = document.getElementById('next_button');
    next_button.disabled = false;
    next_button.classList.remove('disabled_element');
    next_button.classList.add('background_color_0');
})

async function load_map_data() {
    let coords_lat_input = document.getElementById('coords_lat_input');
    let coords_lng_input = document.getElementById('coords_lng_input');

    const API_KEY = "web.1055f2c1ecdb4a9ebde0da823aa2f8b5";

    map = new L.Map("map", {
        key: API_KEY,
        maptype: "neshan",
        poi: true,
        traffic: true,
        center: [38.251558, 48.297227],
        detectRetina: true,
        tileSize: 512,
        zoomOffset: -1,
        zoom: 14,
        maxZoom: 19,
        zoomControl: false,
        preferCanvas: false,
        zoomAnimation: true,
        fadeAnimation: true,
        markerZoomAnimation: true,
    });

    function updateCenterCoords() {
        const center = map.getCenter();
        coords_lat_input.value = center.lat.toFixed(6);
        coords_lng_input.value = center.lng.toFixed(6);
    }

    map.on('moveend', async () => {
        const center = map.getCenter();
        await getAddress(center.lat, center.lng);
        updateCenterCoords()
    });

    updateCenterCoords();
}

function go_to_my_location() {
    let coords_lat_input = document.getElementById('coords_lat_input');
    let coords_lng_input = document.getElementById('coords_lng_input');

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const lat = position.coords.latitude;
                const lng = position.coords.longitude;

                map.setView([lat, lng], 15);
                coords_lat_input.value = lat;
                coords_lng_input.value = lng;
            },
            (error) => {
                switch (error.code) {
                    case error.PERMISSION_DENIED:
                        break;
                    case error.POSITION_UNAVAILABLE:
                        break;
                    case error.TIMEOUT:
                        break;
                    default:
                }
            }
        );
    }
}

function set_location(button_element) {
    let coords_lat_input = document.getElementById('coords_lat_input');
    let coords_lng_input = document.getElementById('coords_lng_input');

    let lat = button_element.id.split('__')[0];
    let lng = button_element.id.split('__')[1];
    map.setView([lat, lng], 18);
    coords_lat_input.value = lat;
    coords_lng_input.value = lng;
}

async function getAddress(lat, lng) {
    let address_input = document.getElementById('address_input');
    let loc_address_input = document.getElementById('loc_address_input');
    const url = `https://api.neshan.org/v5/reverse?lat=${lat}&lng=${lng}`;
    try {
        const res = await fetch(url, {
            headers: {"Api-Key": 'service.ff0468f8995a4ec0bfcd290a44efb0f0'},
        });
        const data = await res.json();
        if (data.formatted_address) {
            address_input.value = data.formatted_address;
            loc_address_input.value = data.formatted_address;
        }
    } catch (err) {

    }
}

function show_dates() {
    let dates_div = document.getElementById('dates_div');
    dates_div.innerHTML = '';
    const textOptions = {
        weekday: 'long',
        day: 'numeric',
        month: 'long',
        calendar: 'persian'
    };

    const numericOptions = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        calendar: 'persian'
    };

    const today = new Date();

    let first = true;
    for (let i = 0; i < 5; i++) {
        const nextDay = new Date(today);
        nextDay.setDate(today.getDate() + i);

        const textDate = new Intl.DateTimeFormat('fa-IR', textOptions).format(nextDay);
        const numericDate = new Intl.DateTimeFormat('fa-IR-u-nu-latn', numericOptions).format(nextDay).replace(/‏/g, '').replace(/-/g, '/');

        let date_input = document.getElementById('date_input');
        let class_list = 'background_color_0_4 text_color_2';
        if (first) {
            class_list = 'background_color_2 text_color_0';
            first = false;
            date_input.value = numericDate;
        }
        dates_div.innerHTML += `
            <button class="one_date_button ${class_list}" id="date_${numericDate}" type="button" onclick="select_option('date', this)">${textDate}</button>
        `
    }
}

function show_timeline_div() {
    const now = new Date();
    const hour = now.getHours();
    let timeline_input = document.getElementById('timeline_input');
    let time_buttons = document.getElementById('times_div').getElementsByTagName('button');

    for (let time of time_buttons) {
        time.classList.remove('background_color_2', 'text_color_0');
    }

    for (let time of time_buttons) {
        if (Number(time.id.split('__')[1].split('_')[1]) <= hour) {
            time.classList.add('disabled_element');
            time.classList.remove('background_color_0_4', 'text_color_2');
            time.disabled = true;
        }
    }

    for (let time of time_buttons) {
        if (!time.disabled) {
            time.classList.add('background_color_2', 'text_color_0');
            time.classList.remove('background_color_0_4', 'text_color_2');
            timeline_input.value = time.id.split('time__')[1];
            break
        }
    }

    let address_div = document.getElementById('address_div');
    let address_input = document.getElementById('address_input');
    let dates_div = document.getElementById('dates_div');
    let my_location_button = document.getElementById('my_location_button');
    let times_div = document.getElementById('times_div');
    let options_div = document.getElementById('options_div');
    let map_lock_div = document.getElementById('map_lock_div');
    let next_button = document.getElementById('next_button');
    let submit_button = document.getElementById('submit_button');
    let selected_address_list = document.getElementById('selected_address_list');

    address_input.classList.add('display_none');
    dates_div.classList.remove('display_none');
    address_div.classList.remove('display_none');
    address_div.innerHTML = 'آدرس: ' + address_input.value + '<i class="bi bi-pencil-square" onclick="edit_address()"></i>';
    my_location_button.classList.add('display_none');
    times_div.classList.remove('display_none');
    options_div.classList.remove('display_none');
    map_lock_div.classList.remove('display_none');
    next_button.classList.add('display_none');
    selected_address_list.classList.add('display_none');
    submit_button.classList.remove('display_none');
    show_dates();
}

function edit_address() {
    let address_div = document.getElementById('address_div');
    let address_input = document.getElementById('address_input');
    let dates_div = document.getElementById('dates_div');
    let my_location_button = document.getElementById('my_location_button');
    let times_div = document.getElementById('times_div');
    let options_div = document.getElementById('options_div');
    let map_lock_div = document.getElementById('map_lock_div');
    let next_button = document.getElementById('next_button');
    let submit_button = document.getElementById('submit_button');
    let selected_address_list = document.getElementById('selected_address_list');

    address_input.classList.remove('display_none');
    dates_div.classList.add('display_none');
    address_div.classList.add('display_none');
    address_div.innerHTML = '';
    my_location_button.classList.remove('display_none');
    times_div.classList.add('display_none');
    options_div.classList.add('display_none');
    map_lock_div.classList.add('display_none');
    next_button.classList.remove('display_none');
    selected_address_list.classList.remove('display_none');
    submit_button.classList.add('display_none');
}

function select_option(mode, button_element) {
    let date_input = document.getElementById('date_input');
    let timeline_input = document.getElementById('timeline_input');
    const today = new Date();
    const hour = today.getHours();
    const numericOptions = {
        year: 'numeric',
        month: '2-digit',
        day: '2-digit',
        calendar: 'persian'
    };
    const numericDate = new Intl.DateTimeFormat('fa-IR-u-nu-latn', numericOptions).format(today).replace(/‏/g, '').replace(/-/g, '/');
    if (mode === 'date') {
        document.getElementById('dates_div').querySelector('button.background_color_2.text_color_0').classList.remove('background_color_2', 'text_color_0');
        for (let button of document.getElementById('dates_div').getElementsByTagName('button')) {
            if (!button.classList.contains('disabled_element')) {
                button.classList.add('background_color_0_4', 'text_color_2');
            }
        }
        date_input.value = button_element.id.split('date_')[1];
        let time_buttons = document.getElementById('times_div').getElementsByTagName('button');
        if (numericDate !== button_element.id.split('_')[1]) {
            let first = true;
            for (let time of time_buttons) {
                time.classList.remove('disabled_element');
                if (first) {
                    time.classList.add('background_color_2', 'text_color_0');
                    time.classList.remove('background_color_0_4', 'text_color_2');
                    timeline_input.value = time.id.split('time__')[1];
                    first = false;
                } else {
                    time.classList.add('background_color_0_4', 'text_color_2');
                    time.classList.remove('background_color_2', 'text_color_0');
                }
                time.disabled = false;
            }
        } else {
            for (let time of time_buttons) {
                time.classList.remove('background_color_2', 'text_color_0');
            }

            for (let time of time_buttons) {
                if (Number(time.id.split('__')[1].split('_')[1]) <= hour) {
                    time.classList.add('disabled_element');
                    time.classList.remove('background_color_0_4', 'text_color_2');
                    time.disabled = true;
                }
            }

            for (let time of time_buttons) {
                if (!time.disabled) {
                    time.classList.add('background_color_2', 'text_color_0');
                    time.classList.remove('background_color_0_4', 'text_color_2');
                    timeline_input.value = time.id.split('time__')[1];
                    break
                }
            }
        }
    } else {
        document.getElementById('times_div').querySelector('button.background_color_2.text_color_0').classList.remove('background_color_2', 'text_color_0');
        for (let button of document.getElementById('times_div').getElementsByTagName('button')) {
            if (!button.classList.contains('disabled_element')) {
                button.classList.add('background_color_0_4', 'text_color_2');
            }
        }
        timeline_input.value = button_element.id.split('time__')[1];
    }
    button_element.classList.add('background_color_2', 'text_color_0');
    button_element.classList.remove('background_color_0_4', 'text_color_2');
}