const navLinks = document.querySelectorAll(".st-nav-bar-link");
const currentUrl = window.location.href;

navLinks.forEach((link) => link.classList.toggle("text-blue-600", link.href === currentUrl));

window.addEventListener("hashchange", () => navLinks.forEach((link) => link.classList.toggle("text-blue-600", link.href === currentUrl)));

document.getElementById('toggler').addEventListener('click', () => {
  var mobileMenu = document.getElementById('mobile-menu');
  mobileMenu.classList.toggle('hidden');
});

// prevent link into the same url
var navigationLinks = document.querySelectorAll('a');
navigationLinks.forEach(function (link) {
  link.addEventListener('click', function (event) {
    // Prevent navigation if the link leads to the same page
    if (link.href === window.location.href) {
      event.preventDefault();
    }
  });
});

const alertMsg = document.getElementById('st-alert-message')
function AlertMessage(title, message) {
  alertMsg.classList.remove('hidden')

  // Automatically remove the alert after 5 seconds
  setTimeout(function () {
    alertMsg.classList.add('hidden')
  }, 5000);
}

const closeAlertMsg = document.getElementById('st-close-alert-message')
if(closeAlertMsg){
  closeAlertMsg.addEventListener('click',()=>{
    alertMsg.classList.add('hidden')
  })
}