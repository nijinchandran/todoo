const modeToggleButton = document.getElementById('mode-toggle-button');
const htmlElement = document.documentElement;

modeToggleButton.addEventListener('click', function () {
  htmlElement.classList.toggle('dark-mode');
  htmlElement.classList.toggle('light-mode');
});
