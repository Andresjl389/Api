// Obtén el botón y el div con la clase "options"
const menuIcon = document.getElementById("menu-icon");
const optionsDiv = document.querySelector(".options");
const listDiv = document.querySelector(".list");

// Agrega un evento de clic al botón
menuIcon.addEventListener("click", function() {
    // Toggle (agregar o quitar) la clase "active" en el div "options" para mostrar u ocultar
    optionsDiv.classList.toggle("active");
    listDiv.classList.toggle("active");
});