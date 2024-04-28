const formStatusForm = document.getElementById('form-status-message')
if(!formStatusForm){
    var currentURL = window.location.href;
    var previousURL = document.referrer;

    if (previousURL === currentURL) {
        window.history.go(-2);
    }
}