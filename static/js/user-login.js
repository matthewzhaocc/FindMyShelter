function signup(form) {
    var detailsCont = document.querySelector("#moreDetails");
    // Render before disabling
    var collected = {
        'phone': detailsCont.querySelector("#phoneIgnore")["value"],
        'website': detailsCont.querySelector("#websiteIgnore")["value"],
        'email': detailsCont.querySelector("#emailIgnore")["value"],
        'address': detailsCont.querySelector("#addressIgnore")["value"]
    };
    // Disable Details Input:
    detailsCont.querySelectorAll("input").forEach(function (element) {
        element.disabled = true;
    });
    // Build the FormData from HTML Form:
    var formData = new FormData(form);
    // Collect details data:
    if (formData.get("usertype") == "org") {
        formData.set("details", JSON.stringify(collected));
    }
    else {
        formData.set("details", "{}");
    }
    // Create XMLHttpRequest:
    var req = new XMLHttpRequest();
    req.open("POST", "/register");
    req.onreadystatechange = function () {
        if (req.readyState == XMLHttpRequest.DONE) {

            //location.reload();
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
            alert("login!")
        }
    };
    // Send Request:
    req.send(formData);
}