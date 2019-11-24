function signup(form: HTMLFormElement){
    // Build the FormData from HTML Form:
    const formData: FormData = new FormData(form);

    // Create XMLHttpRequest:
    let req: XMLHttpRequest = new XMLHttpRequest();
    req.open("POST", "/register");

    req.onreadystatechange = function() {
        if (req.readyState == XMLHttpRequest.DONE) {
            alert(req.responseText);
        }
    }

    // Send Request:
    req.send(formData);
}

function login(form: HTMLFormElement){
    // Build the FormData from HTML Form:
    const formData: FormData = new FormData(form);

    // Create XMLHttpRequest:
    let req: XMLHttpRequest = new XMLHttpRequest();
    req.open("POST", "/login");

    req.onreadystatechange = function() {
        if (req.readyState == XMLHttpRequest.DONE) {
            alert(req.responseText);
        }
    }

    // Send Request:
    req.send(formData);
}
