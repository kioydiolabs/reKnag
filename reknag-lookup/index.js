document.getElementById("submit").onclick = function(){
    original_url = document.getElementById("url").value;
    endpoint = "https://api.reknag.com/lookup/?id="+original_url.slice(-6);
    console.log(endpoint)

    const Http = new XMLHttpRequest();
    Http.open("GET", endpoint);
    Http.send();

    Http.onreadystatechange=(e)=>{
        document.getElementById("output").innerHTML = Http.responseText;
        document.getElementById("link").href = Http.responseText;
        console.log(Http.response);
        var output = Http.responseText;
    }

    document.getElementById("viewfull").style.display = "block";
    document.getElementById("vtotal").style.display = "block";

}

document.getElementById("vtotal").onclick = function(){
    output = document.getElementById("output").innerHTML;
    endpoint = "https://api.reknag.com/get_vt_total_link/?url="+output;
    console.log("Output : ",output)
    console.log("Endpoint : ",endpoint)


    const Http = new XMLHttpRequest();
    Http.open("GET", endpoint);
    Http.send();

    Http.onloadend=(e)=>{
        vtotalink = Http.responseText;
        console.log(vtotalink)
        var a = document.querySelector('a[href="https://reknag.com"]');
        if (a) {
            a.setAttribute('href', vtotalink)
        }
        document.getElementById("vtotalurl").style.opacity = "1";
    }


}

document.getElementById("viewfull").onclick = function(){
    original_url = document.getElementById("url").value;
    endpoint = "https://api.reknag.com/lookup/?id="+original_url.slice(-6);
    console.log(endpoint)

    const Http = new XMLHttpRequest();
    Http.open("GET", endpoint);
    Http.send();

    Http.onloadend=(e)=>{
        window.alert(Http.responseText);
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

