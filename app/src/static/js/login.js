const signUpBtn = document.getElementById('signUp');
const signInBtn = document.getElementById('signIn');
const container = document.getElementById('container');

signUpBtn.addEventListener('click', () => {
  container.classList.add("right-panel-active");
});

signInBtn.addEventListener('click', () => {
  container.classList.remove("right-panel-active");
});

function togglePassword(inputId, toggleIcon) {
    const input = document.getElementById(inputId);
  
    if (input.type === "password") {
      input.type = "text";
      toggleIcon.textContent = "🙈";
    } else {
      input.type = "password";
      toggleIcon.textContent = "👁️";
    }
  }
  