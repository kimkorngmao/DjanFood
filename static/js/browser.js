// Get the current and previous URLs
var currentURL = window.location.href;
var previousURL = document.referrer;

if (previousURL === currentURL) {
  window.history.back();
}