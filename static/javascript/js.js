let img_elements = document.querySelectorAll('.image-wrapper')

for (const img_element of img_elements) {
    img_element.addEventListener('click', updateAvailability)
}

function updateAvailability(e) {
     e.preventDefault()
    this.classList.add('modified-availability')
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

let subtractCountEls = document.getElementsByClassName('product-counter-detract')
let AddCountEls = document.getElementsByClassName('product-counter-add')

for (const subtractEl of subtractCountEls) {
    subtractEl.addEventListener('click', decreaseCounterAndAddClassModified)
}

for (const addEl of AddCountEls) {
    addEl.addEventListener('click', increaseCounterAndAddClassModified)
}

function increaseCounterAndAddClassModified(e){
    e.preventDefault();
    let prodCountWrapper = this.parentNode
    let counter = prodCountWrapper.querySelector('.product-count')
    counter.classList.add('modified-quantity')
    counter.textContent = Number(counter.textContent) + 1
}

function decreaseCounterAndAddClassModified(e){
    e.preventDefault();
    let prodCountWrapper = this.parentNode
    let counter = prodCountWrapper.querySelector('.product-count')
    counter.classList.add('modified-quantity')
    if (Number(counter.textContent) > 0) {
        counter.textContent = Number(counter.textContent) - 1
    }
}