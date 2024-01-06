document.getElementById("submit").onclick = function(){
    original_url = document.getElementById("url").value;
    endpoint = "https://shortapi.kioydio.org/create/?url="+original_url
    

    const Http = new XMLHttpRequest();
    Http.open("GET", endpoint);
    Http.send();

    Http.onreadystatechange=(e)=>{
        document.getElementById("output").innerHTML = Http.responseText;
        document.getElementById("link").href = Http.responseText;
        console.log(Http.response);
    }

}


document.getElementById("copy").onclick = function(){
    console.log("copy clicked")
    var copyText = document.getElementById("output");

    /* Create a temporary textarea element to copy the text */
    var tempTextarea = document.createElement("textarea");
    tempTextarea.value = copyText.textContent;

    /* Append the textarea to the document */
    document.body.appendChild(tempTextarea);

    /* Select and copy the text */
    tempTextarea.select();
    document.execCommand("copy");

    /* Remove the temporary textarea */
    document.body.removeChild(tempTextarea);

    /* Provide some visual feedback (optional) */
    document.getElementById("confirm").style.opacity = "1";
    setTimeout(function(){
        document.getElementById("confirm").style.opacity = "0";
    },2000);
}
