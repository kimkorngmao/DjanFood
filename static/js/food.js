const decrementButton = document.getElementById('decrement-button');
const incrementButton = document.getElementById('increment-button');
const quantityInput = document.getElementById('food-quantity');
const buyNowButton = document.getElementById('buy-now-button')

// Add event listeners
decrementButton.addEventListener('click', decrementQuantity);
incrementButton.addEventListener('click', incrementQuantity);

// Functions for increment and decrement
function decrementQuantity() {
    let currentQuantity = parseInt(quantityInput.value);
    if (currentQuantity > 0) {
        quantityInput.value = currentQuantity - 1;
    }
}

function incrementQuantity() {
    let currentQuantity = parseInt(quantityInput.value);
    if (currentQuantity < 99) {
        quantityInput.value = currentQuantity + 1;
    }
}

buyNowButton.addEventListener('click',()=>{
    AlertMessage("Please note","This website is made for educational purpose only.")
})