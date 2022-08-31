var a = parseInt(document.getElementById("afo").innerHTML, 10);
var afoMax = parseInt(document.getElementById("afoM").innerHTML, 10);

function incrementar(){
    console.log(document.getElementById("afo").innerHTML);
    a = Math.min(a+1, afoMax);
    display(afoMax, a);
    console.log(a);
}

function reducir(){
    console.log(document.getElementById("afo").innerHTML);
    a = Math.max(a-1, 0);
    display(afoMax, a);
    console.log(a);

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
            "aforo":a
        },
        ),
        dataType: "json",
        success: function(response) {
            console.log("se actualizó");
            console.log(response);
        },
        error: function(err) {
            console.log("no se actualizó");
            console.log(err);
        }
    })
    }
    
setInterval(comprometer(), 20000);

