document.addEventListener('DOMContentLoaded', () => {
  const toggle = document.querySelector('.menu-toggle');
  const navLinks = document.querySelector('.nav-links');
  if (toggle) {
    toggle.addEventListener('click', () => navLinks.classList.toggle('open'));
  }
  document.addEventListener('click', (e) => {
    if (!e.target.closest('nav')) navLinks.classList.remove('open');
  });
});
