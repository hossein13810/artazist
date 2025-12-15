let current = 0;
let animating = false;

window.addEventListener('load', function () {
    const slides = Array.from(document.querySelectorAll('.one_slide_div'));
    let startX = 0;

    const slider = document.getElementById('slider_div');

    slider.addEventListener('touchstart', e => startX = e.touches[0].clientX);
    slider.addEventListener('touchend', e => {
        const diff = e.changedTouches[0].clientX - startX;
        if (Math.abs(diff) < 50) return;
        if (diff > 0 && current < slides.length - 1) {
            goToSlide(current + 1, 'left');
        } else if (diff < 0 && current > 0) {
            goToSlide(current - 1, 'right');
        }
    });

    let mouseDown = false;
    slider.addEventListener('mousedown', e => {
        mouseDown = true;
        startX = e.clientX;
    });
    window.addEventListener('mouseup', e => {
        if (!mouseDown) return;
        mouseDown = false;
        const diff = e.clientX - startX;
        if (Math.abs(diff) < 50) return;
        if (diff > 0 && current < slides.length - 1) goToSlide(current + 1, 'left');
        else if (diff < 0 && current > 0) goToSlide(current - 1, 'right');
    });
});

function goToSlide(next, from) {
    let next_link = document.getElementById('next_link');
    let start_link = document.getElementById('start_link');
    const slides = Array.from(document.querySelectorAll('.one_slide_div'));
    if (animating || next === current || next < 0 || next >= slides.length) return;
    animating = true;

    const currentSlide = slides[current];
    const nextSlide = slides[next];

    let currentSpan = document.getElementById(`span_${currentSlide.id.split('_')[1]}`);
    let nextSpan = document.getElementById(`span_${nextSlide.id.split('_')[1]}`);

    if (nextSlide.id.split('_')[1] === '4') {
        next_link.classList.add('display_none');
        start_link.classList.remove('display_none');
    } else {
        next_link.classList.remove('display_none');
        start_link.classList.add('display_none');
    }

    currentSpan.classList.remove('on_circle');
    nextSpan.classList.add('on_circle');

    if (from === 'left') {
        nextSlide.style.transform = 'translateX(-100%)';
        nextSlide.classList.add('active');
        requestAnimationFrame(() => {
            nextSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transform = 'translateX(100%)';
            nextSlide.style.transform = 'translateX(0)';
        });
    } else if (from === 'right') {
        nextSlide.style.transform = 'translateX(100%)';
        nextSlide.classList.add('active');
        requestAnimationFrame(() => {
            nextSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transition = 'transform 0.5s ease';
            currentSlide.style.transform = 'translateX(-100%)';
            nextSlide.style.transform = 'translateX(0)';
        });
    }

    setTimeout(() => {
        currentSlide.classList.remove('active');
        animating = false;
        current = next;
    }, 500);
}

function next_slide() {
    goToSlide(current + 1, 'left');
}
