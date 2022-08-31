$(document).ready( function () {
    new_row ='<tr> \n\
                <form id="dataa" action="/nueva_carta/-1", method = "post" enctype="multipart/form-data"> \n\
                    <th scope="row"> </th>    \n\
                    <td id="id" hidden>-1</td>    \n\
                    <th scope="row"><select class="nuevo-combo" onChange="combo(this, "demo")"></th>   \n\
                    <td id="car_nombre"> <input id="nombre_carta" type="text"/></td>    \n\
                    <th id="linkk">     \n\
                        <input class="plswork" type="file" name = "new_carta">   \n\
                        <input class="plswork" type="submit">    \n\
                    </th>   \n\
                    <th><a hidden value id="btn_submit" class="btn btn-secondary table-row-edit edit-button" >Editar</a>   \n\
                    <a class="btn btn-danger btn-delete">Eliminar</a>   \n\
                    </th>   \n\
                </form> \n\
             </tr>)'


    // $('body').on('click', '#nuevo', function(){
    //     var names = getrtrnames($('#rtr_names').html().split(','))
        
        
    //     $('#cartas > tbody:last-child').append(new_row)

    //     for(j=0;j-names[0].length;j++){
    //         $('.nuevo-combo').append("<option>" + names[0][j][1] + "</option>")
    //     }
    //      $('.nuevo-combo').toggleClass('nuevo-combo')
    //     $('#cartas > tbody:last-child').find('.edit-btn').click()
    // });

    // $('body').on('click', '#nuevo', function(){
    //     var names = getrtrnames($('#rtr_names').html().split(','))
        
        
    //     $('#cartas > tbody:last-child').append(new_row)

    //     for(j=0;j-names[0].length;j++){
    //         $('.nuevo-combo').append("<option>" + names[0][j][1] + "</option>")
    //     }
    //      $('.nuevo-combo').toggleClass('nuevo-combo')
    //     $('#cartas > tbody:last-child').find('.edit-btn').click()


    // });


    $('body').on('click', '#btn_submit',function() { //Función que se activa al hacer click en editar
        var currentTD = $(this).parents('tr').find('td');
        var currentTH = $(this).parents('tr').find('th');
        if ($(this).html() == 'Editar') {                     //Si dice editar, se cambia el texto a guardar y activa el prop editable 
            $.each(currentTD, function () {
                $(this).prop('contenteditable', true)
            });
            
            $(this).html('<svg xmlns="http://www.w3.org/2000/svg" width="20" height="20"  fill="currentColor" class="bi bi-check-square" viewBox="0 0 16 16"> <path d="M14 1a1 1 0 0 1 1 1v12a1 1 0 0 1-1 1H2a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h12zM2 0a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V2a2 2 0 0 0-2-2H2z"></path><path d="M10.97 4.97a.75.75 0 0 1 1.071 1.05l-3.992 4.99a.75.75 0 0 1-1.08.02L4.324 8.384a.75.75 0 1 1 1.06-1.06l2.094 2.093 3.473-4.425a.235.235 0 0 1 .02-.022z"></path></svg>');
            $(this).parents('th').append('<a value class="btn half btn-warning cancel-button" ><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-x-circle-fill" viewBox="0 0 16 16"><path d="M16 8A8 8 0 1 1 0 8a8 8 0 0 1 16 0zM5.354 4.646a.5.5 0 1 0-.708.708L7.293 8l-2.647 2.646a.5.5 0 0 0 .708.708L8 8.707l2.646 2.647a.5.5 0 0 0 .708-.708L8.707 8l2.647-2.646a.5.5 0 0 0-.708-.708L8 7.293 5.354 4.646z"/>svg></a>')
            $(this).toggleClass('half');
            $(this).toggleClass('btn-secundary');
            $(this).toggleClass('btn-success');
            $(this).data('editar', true);

            $(this).parents('tr').find('.link').toggleClass('invisible')
            $(this).parents('tr').find('.plswork').removeAttr('hidden')
            
            currentTD.get(1).textContent
            currentTD.data('id', currentTD.get(0).textContent)
            currentTD.data('nombre', currentTD.get(1).textContent)
            currentTH.data('lastTH', currentTH.get(2).outerHTML)
            
            
        } else {        //si dice guardar, debe revisar el contenido y enviarlo a la base de datos
            empty = false

            nombre = String(currentTD.get(1).textContent)
            id = currentTH.get(0)
            rtr_id = $('#id').textContent;
            
            if(!nombre)
                empty = true
            if(empty){
                alert('por favor, rellene todos los campos.')
                return
            }
            
            var url= window.location.pathname;
                form = $('#dataa')[0]
                var formData = new FormData(form);
                formData.append("nombre", $(this).parents('tr').find("nombre"))
                formData.append("id", $(this).parents('tr').find("id"))
                
                console.log(formData)

                
            //  sendData(formData)
            //     $.ajax({
            //         url: window.location.pathname,
            //         type: 'POST',
            //         data: formData,
            //         success: function (data) {
            //             console.log(data)
            //         },
            //         cache: false,
            //         contentType: false,
            //         processData: false
            //     });
            
            $(this).parents('#btn-submit').toggleClass('half')
            $.each(currentTD, function () {
                $(this).prop('contenteditable', false)
                });
            $(this).html("Editar")
            $(this).toggleClass('half');
            $(this).toggleClass('btn-secundary');
            $(this).toggleClass('btn-success');
            $(this).parents('th').find('.cancel-button').remove()
            styleTableButtons()
        }
    });

    $('body').on('click', '.cancel-button', function(){
        var currentTD = $(this).parents('tr').find('td');
        var currentTH = $(this).parents('tr').find('th');

        currentTD.get(0).textContent = currentTD.data("id")
        currentTD.get(1).textContent = currentTD.data('nombre')
        $(this).parents('tr').find('.link').toggleClass('invisible')
        $(this).parents('tr').find('.plswork').attr('hidden', true)
        $.each(currentTD, function () {
            $(this).prop('contenteditable', false)
                
            });
        
        $(this).parents('th').find('.edit-button').html("Editar")
        $(this).parents('th').find('.edit-button').toggleClass('half');
        $(this).parents('th').find('.edit-button').toggleClass('btn-secundary')
        $(this).parents('th').find('.edit-button').toggleClass('btn-success')
        $(this).parents('th').find('.cancel-button').remove()
    })

    $("body").on("click", ".btn-delete", function(){  
        if(confirm('¿Estás seguro de eliminar esta carta?')){
        
        //id = $(this).parents('tr').find('#id').html()
        id = $(this).parents('tr').find('#car_id').html()
        console.log(id);
        delData(id)
        $(this).parents("tr").remove(); 
    }

    });

    $('#cartas').DataTable({ //paginación de tabla
        paging: true,
        pagingType: "full_numbers",
        ordering: true,
    } );
    styleTableButtons()
    $('body').on('change', function(){
        styleTableButtons()
    })
}); 

function styleTableButtons(){
    $('.paginate_button').toggleClass('btn-primary btn')
    $('.dataTables_length').toggleClass('btn-primary btn')
    $('.dataTables_filter').toggleClass('table-dependant')
    $('.paginate_button').css("display","inline-flex")
    $('.dataTables_length').css("display","inline-flex")
    $('.dataTables_filter').css("display","inline-flex")
}

function getrtrnames(jq){
    var names = []
    names.push(jq)
    for(i = 0; i< names.length;i++){
        names[0][i] = replaceAll(names[0][i], ']', ' ')
        names[0][i] = replaceAll(names[0][i], '[', '')
        names[0][i] = replaceAll(names[0][i], '\'', '')
        names[0][i] = names[0][i].split('-')
    }
    return names;
}

function replaceAll(str, find, replace) {
    var escapedFind=find.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1");
    return str.replace(new RegExp(escapedFind, 'g'), replace);

}

function delData(id){
    if(id){
        var url= window.location.pathname;
        url += '/del'
        $.ajax({
            type: "POST",
            url: url,
            contentType: "application/json",
            data: JSON.stringify(
            {   "id": id
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
}

