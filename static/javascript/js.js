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

function openDropDownMenu(){
    let burgerBtnWrapper = document.querySelector('.burger-btn-wrapper')
    let burgetToggle = document.querySelector('.burger-menu-upper-buttons')
    burgerBtnWrapper.style.display = 'block';
    burgetToggle.style.display = 'none'
}

function closeDropDownMenu(){
    let burgerBtnWrapper = document.querySelector('.burger-btn-wrapper')
    let burgetToggle = document.querySelector('.burger-menu-upper-buttons')
    burgerBtnWrapper.style.display = 'none';
    burgetToggle.style.display = 'block'
}

let linkToScrollList = document.querySelectorAll('.link-to-scroll')

for (const item of linkToScrollList) {
    item.addEventListener('click', scrollToElement)
}


function scrollToElement(e){
    e.preventDefault()
    let targetSection = this
    let targetSectionClass = targetSection.getAttribute('id')
    let elementToScroll = document.getElementsByClassName(targetSectionClass)[0]
    elementToScroll.scrollIntoView();
    closeDropDownMenu()
}