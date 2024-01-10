var currentURL = window.location.href;
var previousURL = document.referrer;

if (previousURL === currentURL) {
  window.history.back();
}