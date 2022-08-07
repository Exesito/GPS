jQuery(document).ready( function () {
    jQuery('#horarios').DataTable({
        "bDeferRender": true,
        "oLanguage": {
        "sEmptyTable": "No hay registros disponibles",
        "sInfo": "Hay _TOTAL_ registros. Mostrando de (_START_ a _END_)",
        "sLoadingRecords": "Por favor espera - Cargando...",
        "sSearch": "Filtro:",
        "sLengthMenu": "Mostrar _MENU_",
        "oPaginate": {
        "sLast": "Última página",
        "sFirst": "Primera",
        "sNext": "Siguiente",
        "sPrevious": "Anterior"
        }
        }
        } );
        
    $('body').on('click', '#btn_submit',function() { //Función que se activa al hacer click en editar
        var currentTD = $(this).parents('tr').find('td');
        if ($(this).html() == 'Editar') {                     //Si dice editar, se cambia el texto a guardar y activa el prop editable 
            $.each(currentTD, function () {
                $(this).prop('contenteditable', true)
                
            });
            $(this).html("Guardar")
        } else {        //si dice guardar, debe revisar el contenido y enviarlo a la base de datos
            
            var id = currentTD.get(0).textContent
            var nombre = currentTD.get(1).textContent
            var apertura = currentTD.get(2).textContent
            var cierre = currentTD.get(3).textContent
            var dia_inicio = currentTD.get(4).textContent
            var dia_fin = currentTD.get(5).textContent
            
            empty = false
            error = false
            errortxt = ''
            if(!nombre || !apertura || !cierre || !dia_inicio || !dia_fin){
            empty = true
            }
            if(empty){
            alert('por favor, rellene todos los campos.')
            return
            }
            error, errortxt = checkdatos(apertura, cierre, dia_inicio, dia_fin)
            if(error){
            alert(errortxt)
            return
            }

            var url= window.location.pathname;
            $.ajax({
            type: "POST",
            url: url,
            contentType: "application/json",
            data: JSON.stringify(
            {   "nombre":nombre,
                "apertura":apertura,
                "cierre":cierre,
                "dia_inicio":dia_inicio,
                "dia_fin":dia_fin,
                "id":id
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
        $.each(currentTD, function () {
                $(this).prop('contenteditable', false)
                
            });
            $(this).html("Editar")
        }
    });
    
    $("body").on("click", ".btn-delete", function(){  
        $(this).parents("tr").remove();  
    });  
    $('#nuevo').on('click', function(){
        
        $('#horarios > tbody:last-child').append(
            '<tr> <th> *Nuevo*</th> <td hidden></td> <td></td> <td></td> <td></td> <td></td> <td></td> <th><a value id="btn_submit" class="btn btn-secondary table-row-edit edit-button" >Editar</a></th><th><a href="#" class="btn btn-danger btn-delete" onclick="return confirm(\'¿Estás seguro de eliminar este horario?\');">Eliminar</a></th> </tr>');
        
    })
    }
); 

function checktime(time){
    
    arr = []
    for(i = 0; i< time.length; i++)
    arr[i] = time[i]
    
    count = 0
    for(ch in arr){
    if(count == 0 || count == 1 || count == 3 || count == 4 || count == 6 || count == 7){
        if(!/\d/.test(arr[ch])){
        return false
        }
    }else if(count == 2 || count == 5){
        if(arr[ch] != ':'){
        return false
        }
    }else if(count > 7){
        return false
    }

    count++
    }
    return true
}
function checkday(day){
    valid = [0, 1, 2, 3, 4, 5, 6];
    if(valid.indexOf(parseInt(day)) == -1)
        return false;
    
    return true
}
function checkdatos(apertura, cierre, dia_inicio, dia_fin){
    if(!checktime(apertura)){
        errortxt += ' Formato de Apertura Incorrecto '
        error = true
        }
        if(!checktime(cierre)){
        errortxt += ' Formato de Cierre Incorrecto '
        error = true
        }
        if(!checkday(dia_inicio)){
        errortxt += ' Día inicio debe estar entre 0 y 6 '
        error = true
        }
        if(!checkday(dia_fin)){
        errortxt += ' Día fin debe estar entre 0 y 6 '
        error = true
        }
    return error, errortxt
}
