let currentIndex = 0;
const images = document.querySelectorAll('.slider-image');
const totalImages = images.length;

function showSlide(index) {
    if (index >= totalImages) {
        currentIndex = 0;
    } else if (index < 0) {
        currentIndex = totalImages - 1;
    } else {
        currentIndex = index;
    }

    const imageWidth = images[0].clientWidth; // ✅ حساب العرض ديناميكي
    const offset = -currentIndex * imageWidth;
    document.querySelector('.slider').style.transform = `translateX(${offset}px)`;
}

// التنقل التلقائي كل ثانيتين
setInterval(() => {
    showSlide(currentIndex + 1);
}, 2000);

// وظيفة الأسهم
function moveSlide(step) {
    showSlide(currentIndex + step);
}

  
// عرض الصورة الأولى
showSlide(currentIndex);



