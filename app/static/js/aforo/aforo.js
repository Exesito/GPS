setInterval(comprometer(), 20000);
a = document.getElementById("afo").innerHTML;

function incrementar(){
    var textBox = document.getElementById("text");
    textBox.value = a;
    a++;
}

function reducir(){
    var textBox = document.getElementById("text");
    textBox.value = a;
    a--;
}

function display(aforomax, aforo){
    document.getElementById("afo").innerHTML = aforo;
    document.getElementById("afoM").innerHTML = aforomax;
}

function comprometer(){
    display(document.getElementById("afoM").innerHTML, a);
    $.ajax({
        type: "POST",
        url: url,
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
