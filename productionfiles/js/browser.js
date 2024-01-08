alert("Hello")
// Get the current and previous URLs
var currentURL = window.location.href;
var previousURL = document.referrer;

// Check if the previous page has the same URL
if (previousURL === currentURL) {
  // Continue going back
  window.history.back();
} else {
  // Handle the case where the previous page has a different URL
  console.log("Previous page has a different URL");
}