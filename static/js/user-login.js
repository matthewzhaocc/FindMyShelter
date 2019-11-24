function signup(form) {
    // Build the FormData from HTML Form:
    var formData = new FormData(form);
    // Create XMLHttpRequest:
    var req = new XMLHttpRequest();
    req.open("POST", "/register");
    req.onreadystatechange = function () {
        if (req.readyState == XMLHttpRequest.DONE) {
            alert(req.responseText);
        }
    };
    // Send Request:
    req.send(formData);
}
function login(form) {
    // Build the FormData from HTML Form:
    var formData = new FormData(form);
    // Create XMLHttpRequest:
    var req = new XMLHttpRequest();
    req.open("POST", "/login");
    req.onreadystatechange = function () {
        if (req.readyState == XMLHttpRequest.DONE) {
            alert(req.responseText);
        }
    };
    // Send Request:
    req.send(formData);
}
