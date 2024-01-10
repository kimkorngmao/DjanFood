const navLinks = document.querySelectorAll(".st-nav-bar-link");
const currentUrl = window.location.href;

navLinks.forEach((link) => link.classList.toggle("text-red-600", link.href === currentUrl));

window.addEventListener("hashchange", () => navLinks.forEach((link) => link.classList.toggle("text-red-600", link.href === currentUrl)));

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

function AlertMessage(title, message, confirmBtnName="Confirm") {
  // Create main container
  const mainContainer = document.createElement("div");
  mainContainer.className = "fixed z-50 inset-0 overflow-y-auto";

  // Create outer flex container
  const flexContainer = document.createElement("div");
  flexContainer.className = "flex items-end justify-center min-h-screen pt-4 px-4 pb-20 text-center sm:block sm:p-0";

  // Create background overlay
  const overlay = document.createElement("div");
  overlay.className = "fixed inset-0 transition-opacity";
  const overlayBg = document.createElement("div");
  overlayBg.className = "absolute inset-0 bg-gray-500 opacity-75";
  overlay.appendChild(overlayBg);

  // Create hidden span for screen reader text
  const hiddenSpan = document.createElement("span");
  hiddenSpan.className = "hidden sm:inline-block sm:align-middle sm:h-screen";
  hiddenSpan.innerHTML = "&#8203;";

  // Create modal content container
  const modalContainer = document.createElement("div");
  modalContainer.className = "inline-block align-bottom bg-white rounded-lg px-4 pt-5 pb-4 text-left overflow-hidden shadow-xl transform transition-all sm:my-8 sm:align-middle sm:max-w-lg sm:w-full sm:p-6";
  modalContainer.setAttribute("role", "dialog");
  modalContainer.setAttribute("aria-modal", "true");
  modalContainer.setAttribute("aria-labelledby", "modal-headline");

  // Create close button
  const closeButtonContainer = document.createElement("div");
  closeButtonContainer.className = "hidden sm:block absolute top-0 right-0 pt-4 pr-4";
  const closeButton = document.createElement("button");
  closeButton.type = "button";
  closeButton.className = "bg-white rounded-md text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500";
  closeButton.innerHTML = `
      <span class="sr-only">Close</span>
      <svg class="h-6 w-6" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
      </svg>
  `;
  closeButtonContainer.appendChild(closeButton);

  // Create modal content
  const modalContent = document.createElement("div");
  modalContent.className = "sm:flex sm:items-start";
  const modalTextContainer = document.createElement("div");
  modalTextContainer.className = "mt-3 text-center sm:mt-0 sm:ml-4 sm:text-left";
  const modalTitle = document.createElement("h3");
  modalTitle.className = "text-lg leading-6 font-medium text-gray-900";
  modalTitle.id = "modal-headline";
  modalTitle.textContent = title;
  const modalBody = document.createElement("div");
  modalBody.className = "mt-2";
  const modalBodyText = document.createElement("p");
  modalBodyText.className = "text-sm text-gray-500";
  modalBodyText.textContent = message;
  modalBody.appendChild(modalBodyText);
  modalTextContainer.appendChild(modalTitle);
  modalTextContainer.appendChild(modalBody);
  modalContent.appendChild(modalTextContainer);

  // Create buttons container
  const buttonsContainer = document.createElement("div");
  buttonsContainer.className = "mt-5 sm:mt-4 sm:flex sm:flex-row-reverse";
  const commitButton = document.createElement("button");
  commitButton.type = "button";
  commitButton.className = "w-full inline-flex justify-center rounded-md border border-transparent shadow-sm px-4 py-2 bg-blue-600 text-base font-medium text-white hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:ml-3 sm:w-auto sm:text-sm";
  commitButton.textContent = confirmBtnName;
  const cancelButton = document.createElement("button");
  cancelButton.type = "button";
  cancelButton.className = "mt-3 w-full inline-flex justify-center rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-base font-medium text-gray-700 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 sm:mt-0 sm:w-auto sm:text-sm";
  cancelButton.textContent = "Cancel";
  buttonsContainer.appendChild(commitButton);
  buttonsContainer.appendChild(cancelButton);

  // Append elements to the document
  closeButtonContainer.appendChild(closeButton);
  modalContainer.appendChild(closeButtonContainer);
  modalContainer.appendChild(modalContent);
  modalContainer.appendChild(buttonsContainer);
  flexContainer.appendChild(overlay);
  flexContainer.appendChild(hiddenSpan);
  flexContainer.appendChild(modalContainer);
  mainContainer.appendChild(flexContainer);
  document.body.appendChild(mainContainer);


  cancelButton.addEventListener("click", () => {
    document.body.removeChild(mainContainer);
  });

  closeButtonContainer.addEventListener("click", () => {
    document.body.removeChild(mainContainer);
  });

  commitButton.addEventListener("click", () => {
    document.body.removeChild(mainContainer);
  });
}