jQuery(document).ready( function () {
    $('.edit-button').data('editar', false)

    jQuery('#horarios').DataTable({ //paginación de tabla
        paging: true,
        pagingType: "full_numbers",
        ordering: true,
    } );
    styleTableButtons()
    table_width = $('#horarios').width()
    //$('.table-dependant').css({"position": "relative", "left": table_width*0.8})
    
    $('body').on('click', '#btn_submit',function() { //Función que se activa al hacer click en editar
        var currentTD = $(this).parents('tr').find('td');
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
            
            
            var id = currentTD.get(1).textContent.trim('')
            var nombre = currentTD.get(2).textContent
            var apertura = currentTD.get(3).textContent
            var cierre = currentTD.get(4).textContent
            var dia_inicio = currentTD.get(5).textContent
            var dia_fin = currentTD.get(6).textContent
            
            
            currentTD.data("id", id)
            currentTD.data("nombre", nombre)
            currentTD.data("apertura", apertura)
            currentTD.data("cierre", cierre)
            currentTD.data("dia_inicio", dia_inicio)
            currentTD.data("dia_fin", dia_fin)

        } else {        //si dice guardar, debe revisar el contenido y enviarlo a la base de datos
           var names = getrtrnames($('#rtr_names').html().split(','));

            
            var id = currentTD.get(0).textContent
            var nombre = currentTD.get(2).textContent
            var apertura = currentTD.get(3).textContent
            var cierre = currentTD.get(4).textContent
            var dia_inicio = currentTD.get(5).textContent
            var dia_fin = currentTD.get(6).textContent
            var rtr_id = currentTD.get(1).textContent
            if(/[a-zA-Z]/.test(id))
                id = null
            if(!rtr_id)
                for(j=0;j-names[0].length;j++){
                    if( String(names[0][j][1]).trim(' ') === String($(this).parents('tr').find('#combo :selected').val()).trim(' '))
                        rtr_id = names[0][j][0].replaceAll('"', '')
                }
            
            console.log('rtr_id: ' + rtr_id)
                
            
            
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
                    "id":id,
                    "rtr_id": rtr_id,
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
            $(this).parents('#btn-submit').toggleClass('half')
            $.each(currentTD, function () {
                $(this).prop('contenteditable', false)
                    
                });
            $(this).html("Editar")
            $(this).toggleClass('half');
            $(this).toggleClass('btn-secundary');
            $(this).toggleClass('btn-success');
            $(this).parents('th').find('.cancel-button').remove()
        }
    });
    
    $("body").on("click", ".btn-delete", function(){  
        if(confirm('¿Estás seguro de eliminar este horario?'))
        var currentTD = $(this).parents('tr').find('td');
        id = currentTD[0].textContent
        
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
        $(this).parents("tr").remove();  
        styleTableButtons()
           

    }); 

    $('body').on('click','#nuevo', function(){
        //var nuevo = $("horarios").load("CRUD-Horarios\nuevo_horario.html")
        var names = getrtrnames($('#rtr_names').html().split(','));
        
        new_row = '<tr> \n\
                    <th>*Nuevo*</th> \n\
                    <td> <select id="combo" class="nuevo-combo" onChange="combo(this, "demo")"></td> \n\
                    <td hidden></td> \n\
                    <td></td> \n\
                    <td></td> \n\
                    <td></td> \n\
                    <td></td> \n\
                    <td></td> \n\
                    <th><a value id="btn_submit" class="btn btn-secondary table-row-edit edit-button" >Editar</a></th> \n\
                    <th><a href="#" class="btn btn-danger btn-delete" onclick="return confirm("¿Estás seguro de eliminar este horario?");">Eliminar</a></th> \n\
                   </tr>'             
        
        $('#horarios > tbody:last-child').append(new_row);
        
            for(j=0;j-names[0].length;j++){
                $('.nuevo-combo').append("<option>" + names[0][j][1] + "</option>")
            }
        
         $('.nuevo-combo').toggleClass('nuevo-combo')
        
        $('.edit-button').data('editar', false)
    })

    $('body').on('change', function(){
        styleTableButtons()
    })

    $('body').on('click', '.cancel-button', function(){
        var currentTD = $(this).parents('tr').find('td');
        currentTD.get(1).textContent = currentTD.data("id")
        currentTD.get(2).textContent = currentTD.data('nombre')
        currentTD.get(3).textContent = currentTD.data('apertura')
        currentTD.get(4).textContent = currentTD.data('cierre')
        currentTD.get(5).textContent = currentTD.data('dia_inicio')
        currentTD.get(6).textContent = currentTD.data('dia_fin')
        

        $.each(currentTD, function () {
            $(this).prop('contenteditable', false)
                
            });
        
        $(this).parents('th').find('.edit-button').html("Editar")
        $(this).parents('th').find('.edit-button').toggleClass('half');
        $(this).parents('th').find('.edit-button').toggleClass('btn-secundary')
        $(this).parents('th').find('.edit-button').toggleClass('btn-success')
        $(this).parents('th').find('.cancel-button').remove()
})
}); 

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
        if(dia_inicio > dia_fin){
            errortxt += ' El dia final debe ser mayor o igual al dia de inicio '
            error = true
        }
        if(apertura >= cierre){
            errortxt += ' Horario de cierre debe ser posterior al de apertura '
            error = true
        }
    return error, errortxt
}
function styleTableButtons(){
    $('.paginate_button').toggleClass('btn-primary btn')
    $('.dataTables_length').toggleClass('btn-primary btn')
    $('.dataTables_filter').toggleClass('table-dependant')
    $('.paginate_button').css("display","inline-flex")
    $('.dataTables_length').css("display","inline-flex")
    $('.dataTables_filter').css("display","inline-flex")
}
function replaceAll(str, find, replace) {
    var escapedFind=find.replace(/([.*+?^=!:${}()|\[\]\/\\])/g, "\\$1");
    return str.replace(new RegExp(escapedFind, 'g'), replace);
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