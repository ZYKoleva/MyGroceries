let btnsDelete = document.querySelectorAll('.default-page-delete')
let btnsEdit = document.querySelectorAll('.default-page-edit')
let btnAddProduct = document.querySelector('.add-product')

for (const btnDelete of btnsDelete) {
    btnDelete.addEventListener('click', hideElement)
}

function hideElement(e) {
    e.preventDefault();
    let parentEl = this.parentElement.parentElement;
    parentEl.style = "display: none;"

}

for (const btnEdit of btnsEdit) {
    btnEdit.addEventListener('mouseover', showEditForm)
    btnEdit.addEventListener('mouseout', hideEditForm)
}

btnAddProduct.addEventListener('mouseover', showAddForm)
btnAddProduct.addEventListener('mouseout', hideAddForm)

function showEditForm(e) {
    e.preventDefault();
    let parentEl = this.parentElement.parentElement;
    let edit_pop_up = parentEl.querySelector('.edit-create-product');
    edit_pop_up.style = "display: block;";

    let name_prod = parentEl.querySelector('.product-name')
    let brand_prod = parentEl.querySelector('.product-brand')

    let input_name = edit_pop_up.querySelector('#product-name')
    input_name.value = name_prod.innerText
    let input_brand = edit_pop_up.querySelector('#product-brand')
    try {
         input_brand.value = brand_prod.innerHTML
    } catch (e) {
    }

}

function showAddForm(e) {
     e.preventDefault();
      let parentEl = this.parentElement
     let add_pop_up = parentEl.querySelector('.add-product-popup');
     add_pop_up.style = "display: block;";
}

function hideEditForm(e) {
    e.preventDefault();
    let parentEl = this.parentElement.parentElement;
    let edit_pop_up = parentEl.querySelector('.edit-create-product');
    edit_pop_up.style = "display: none;";
}

function hideAddForm(e){
        e.preventDefault();
    let parentEl = this.parentElement
    let add_pop_up = parentEl.querySelector('.add-product-popup');
     add_pop_up.style = "display: none;";
}

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

function zoomInOut(e) {
    e.preventDefault()
    let zoomIcon = this
    console.log(zoomIcon)
    let productWrapper = this.nextElementSibling
    let imgWrapper = productWrapper.firstElementChild
    imgWrapper.classList.add('large')
    setTimeout(function () {
        imgWrapper.classList.remove('large')
    }, 1000);
}


