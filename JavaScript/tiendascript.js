const products = [
    { name: "Libros Oficiales", price: 300, image: "../imagenes/Libro.jpg" , id: 1, quantity: 1,},
    { name: "Camisetas Oficiales", price: 150, image: "../imagenes/Camisa.jpg", id: 2, quantity: 1,},
    { name: "Utencilios oficiales", price: 250, image: "../imagenes/Utencilios.jpg", id: 3, quantity: 1, },
    { name: "Manteles Oficiales", price: 150, image: "../imagenes/Manteles.jpg", id: 4, quantity: 1, },
  ];
  

  let cart = []
  
  const productsHTML = products.map(
    (product) => `<div class="product-card">
          <h2 class="product-name">${product.name}</h2>
          <img class ="imgprod" src="${product.image}" alt="Imagen de producto">
          <p><strong>$${product.price}</strong><p>
          <button class="product-btn" id=${product.id}>Agregar a el carrito</button>
      </div>`
  );
  const result = document.querySelector(".result");
  result.innerHTML = productsHTML.join("");
  
  
  function updateCart() {
    const cartHTML = cart.map(
      (item) => `<div class="cart-item">
              <h3>${item.name}</h3>
              <div class="cart-detail"><div class="mid">
                  <button onclick={decrItem(${item.id})}>-</button>
                  <p>${item.quantity}</p>
                  <button onclick={incrItem(${item.id})}>+</button>
              </div>
              <p>$${item.price}</p>
              <button onclick={deleteItem(${item.id})} class="cart-product" id=${item.id}>D</button></div>
             </div>`
    );
  
    const cartItems = document.querySelector(".cart-items");
    cartItems.innerHTML = cartHTML.join("");
  }
  
  let num = document.querySelectorAll(".product-btn").length;
  for (let i = 0; i < num; i++) {
    document
      .querySelectorAll(".product-btn")
    [i].addEventListener("click", function (e) {
      addToCart(products, parseInt(e.target.id));
    });
  }
  
  function addToCart(products, id){
    const product = products.find((product) => product.id === id);
    const cartProduct = cart.find((product) => product.id === id);
    if (cartProduct != undefined && product.id == cartProduct.id) {
      incrItem(id);
    } else {
      cart.unshift(product);
    }
    updateCart();
    getTotal(cart);
  };
  
  function getTotal(cart) {
    let { totalItem, cartTotal } = cart.reduce(
      (total, cartItem) => {
        total.cartTotal += cartItem.price * cartItem.quantity;
        total.totalItem += cartItem.quantity;
        return total;
      },
      { totalItem: 0, cartTotal: 0 }
    );
    const totalItemsHTML = document.querySelector(".noOfItems");
    totalItemsHTML.innerHTML = `${totalItem} objetos`;
    const totalAmountHTML = document.querySelector(".total");
    totalAmountHTML.innerHTML = `$${cartTotal}`;
  }
  
  function incrItem(id) {
    for (let i = 0; i < cart.length; i++) {
      if (cart[i] && cart[i].id == id) {
        cart[i].quantity += 1;
      }
    }
    updateCart();
    getTotal(cart);
  }
  
  function decrItem(id) {
    for (let i = 0; i < cart.length; i++) {
      if (cart[i].id == id && cart[i].quantity > 1) {
        cart[i].quantity -= 1;
      }
    }
    updateCart();
    getTotal(cart);
  }
  
  function deleteItem(id) {
    for (let i = 0; i < cart.length; i++) {
      if (cart[i].id === id) {
        cart[i].quantity = 1;
        cart.splice(i, 1);
      }
    }
    updateCart();
    getTotal(cart);
  }

  // Codigo para mostrar y ocultar calculadora

  document.addEventListener("DOMContentLoaded", () => {
    const boton = document.querySelector(".ocultar");
    const calculadora = document.querySelector(".calculator");
    const result = document.querySelector(".result");
  
    boton.addEventListener("click", () => {
      if (calculadora.style.display === "none") {
        boton.textContent = "Ocultar Calculadora"
        calculadora.style.display = "block";
        result.style.flex = "1";
      } else {
        boton.textContent = "Mostrar Calculadora"
        calculadora.style.display = "none";
        result.style.flex = "1 1 100%";
      }
    });
  });


  // Codigo Calculadora // 
  const display = document.querySelector(".display");
const buttons = document.querySelectorAll(".botonescalc");

let currentInput = "";
let currentOperator = "";
let shouldClearDisplay = false;

buttons.forEach((button) => {
button.addEventListener("click", () => {
const buttonText = button.textContent;

if (buttonText.match(/[0-9, .]/)) {

if (shouldClearDisplay) {
display.textContent = "";
shouldClearDisplay = false;
}

display.textContent += buttonText;
}

else if (buttonText === "C") {
display.textContent = "0";
currentInput = "";
currentOperator = "";
}

else if (buttonText === "Cos()") {
   const coseno = cos(currentInput)
   display.textContent = coseno;
   currentInput = result;
   shouldClearDisplay = true;
}

else if (buttonText === "=") {
if (currentOperator && currentInput) {
const result = calculate(parseFloat(currentInput), currentOperator, parseFloat(display.textContent));
display.textContent = result;
currentInput = result;
currentOperator = "";
shouldClearDisplay = true;
}
} else {
currentOperator = buttonText;
currentInput = display.textContent;
shouldClearDisplay = true;
}
});
});


function cos (num1){
return Math.cos(num1);
}

function calculate(num1, operator, num2) {
switch (operator) {
case "Cos()":
return Math.cos(num1);
case "^": 
return Math.pow(num1, num2);
case "+":
return num1 + num2;
case "-":
return num1 - num2;
case "*":
return num1 * num2;
case "/":
if (num2 !== 0) {
return num1 / num2;
} else {
return "Error";
}
default:
return num2;
}
}