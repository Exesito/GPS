setInterval(comprometer(), 20000);
a = parseInt(document.getElementById("afo").innerHTML);
afoMax = parseInt(document.getElementById("afoM").innerHTML);

function incrementar(){
    a = min(a+1, afoMax);
    display()

}

function reducir(){
    a = max(a-1, 0);
    display()
}

function display(aforomax, aforo){
    document.getElementById("afo").innerHTML = aforo;
    document.getElementById("afoM").innerHTML = aforomax;
}

function comprometer(){
    display(parseInt(document.getElementById("afoM").innerHTML), a);
    urlact = window.location.pathname + "/actualizar"
    $.ajax({
        type: "POST",
        url: urlact,
        contentType: "application/json",
        data: JSON.stringify(
        {   "id": document.getElementById("rtr_id").innerHTML,
            "aforo":nombre
        },
        ),
        dataType: "json",
        success: function(response) {
            console.log(response);
        },
        error: function(err) {
            console.log(err);
        }
    })
}
