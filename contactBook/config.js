

let rootPath = "https://mysite.itvarsity.org/api/ContactBook/";
// The exact address to the folder directory on the server where we will be working.
let apiKey = checkApiKey();

function checkApiKey() {
    if (!localStorage.getItem("apiKey")) {
        window.open("enter-api-key.html", "_self");
    }
    return localStorage.getItem("apiKey");
}
