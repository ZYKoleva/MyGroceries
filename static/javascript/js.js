let img_elements = document.querySelectorAll('.image-wrapper')

for (const img_element of img_elements) {
    img_element.addEventListener('click', updateAvailability)
}

function updateAvailability(e) {
    e.preventDefault()
    let img = this.querySelector('img')
    let xMark = this.querySelector('div')
    if (img.className === 'True') {
        img.className = 'False';
        xMark.id = 'available-False'
    } else {
        img.className = 'True';
        xMark.id = 'available-True'
    }
}

let zoomIcons = document.querySelectorAll('.zoom-in-out-icon')

for (const zoomIcon of zoomIcons){
    zoomIcon.addEventListener('click', zoomInOut)
}

function zoomInOut(e){
    e.preventDefault()
    let zoomIcon = this
    console.log(zoomIcon)
   let productWrapper = this.nextElementSibling
    let imgWrapper = productWrapper.firstElementChild
    imgWrapper.classList.add('large')
    setTimeout(function(){ imgWrapper.classList.remove('large') }, 1000);


}