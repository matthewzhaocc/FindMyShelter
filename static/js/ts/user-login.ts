function signup(form: HTMLFormElement){
    let detailsCont = document.querySelector("#moreDetails");

    // Render before disabling
    const collected = {
        'phone': (detailsCont.querySelector("#phoneIgnore") as HTMLInputElement)["value"],
        'website': (detailsCont.querySelector("#websiteIgnore") as HTMLInputElement)["value"],
        'email': (detailsCont.querySelector("#emailIgnore") as HTMLInputElement)["value"],
        'address': (detailsCont.querySelector("#addressIgnore") as HTMLInputElement)["value"]
    }

    // Disable Details Input:
    detailsCont.querySelectorAll("input").forEach(element => {
        element.disabled = true;
    });

    // Build the FormData from HTML Form:
    const formData: FormData = new FormData(form);

    // Collect details data:
    if(formData.get("usertype") == "org"){
        formData.set("details", JSON.stringify(collected))
    } 
    else {
        formData.set("details", "{}");
    }

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
            postLogin(req.responseText);
        }
    }

    // Send Request:
    req.send(formData);
}

function postLogin(text) {
    window.sessionStorage.setItem("sessionKey", btoa(text));
}
