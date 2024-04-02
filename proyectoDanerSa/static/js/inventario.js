// inventario.js

/////////////////////////////////// ELIMINAR ///////////////////////////////////
$(document).ready(function() {
    $('.btn-eliminar').click(function() {
        var productoId = $(this).data('producto-id');
        var productoNombre = $(this).data('producto-nombre');

        // Muestra el modal
        $('#eliminarProductoModal').modal('show');

        // Actualiza el nombre del producto en el modal
        $('#producto-nombre').text(productoNombre);

        // Configura el botón de eliminación dentro del modal
        $('#btn-confirmar-eliminar').off('click').on('click', function() {
            // Obtiene el token CSRF de la cookie
            var csrftoken = document.cookie.match(/csrftoken=([^ ;]+)/)[1];

            // Realiza la solicitud AJAX para eliminar el producto
            $.ajax({
                type: 'POST',
                url: '/inventario/eliminar/' + productoId + '/',
                data: {
                    csrfmiddlewaretoken: csrftoken
                },
                success: function(data) {
                    console.log('Respuesta exitosa:', data);

                    // Cierra el modal después de eliminar el producto
                    $('#eliminarProductoModal').modal('hide');
                    // Actualiza la página o realiza alguna acción adicional si es necesario
                    location.reload();
                },
                error: function(error) {
                    console.log('Error en la solicitud AJAX:', error);
                    // Maneja los errores si es necesario
                }
            });
        });
    });

    // Configura el botón de cancelar dentro del modal
    $('#btn-cancelar-eliminar').click(function() {
        console.log('Cancelando eliminación');
        // Cierra el modal sin realizar la eliminación
        $('#eliminarProductoModal').modal('hide');
    });
});


/////////////////////////////////// MODIFICAR /////////////////////////////////

$(document).ready(function() {
    // Configura el botón de modificación
    $('.btn-modificar').click(function() {
        var productoId = $(this).data('producto-id');
        var productoNombre = $(this).data('producto-nombre');
        
        console.log('Configurando formulario con datos del producto:', productoId, productoNombre);

        // Muestra el modal de modificación
        $('#modificarProductoModal').modal('show');

        // Configura el formulario con los datos actuales y la acción correcta
        $('#producto_id').val(productoId);
        $('#nombre').val(productoNombre);
        // Utiliza val() para los campos de entrada
        $('#existencia').val($(this).data('producto-existencia'));
        $('#precio_venta').val($(this).data('producto-precio-venta'));
        $('#precio_compra').val($(this).data('producto-precio-compra'));
        $('#estado').val($(this).data('producto-estado'));

        // Agrega logs adicionales para verificar otros campos
        console.log('Existencia:', $('#existencia').val());
        console.log('Precio Venta:', $('#precio_venta').val());
        console.log('Precio Compra:', $('#precio_compra').val());
        console.log('Estado:', $('#estado').val());
    });

    // Configura el botón de cancelar dentro del modal de modificación
    $('#btn-cancelar-modificar').click(function() {
        // Cierra el modal sin realizar la modificación
        $('#modificarProductoModal').modal('hide');
    });

    // Configura el botón de guardar cambios dentro del modal
    $('#btn-guardar-cambios').click(function() {
        var productoId = $('#producto_id').val();
        var nombre = $('#nombre').val();
        var existencia = $('#existencia').val();
        var precioVenta = $('#precio_venta').val();
        var precioCompra = $('#precio_compra').val();
        var estado = $('#estado').val();

        console.log('Enviando datos modificados del producto:', nombre, existencia, precioVenta, precioCompra, estado);

        // Realiza la solicitud AJAX para modificar el producto
// Realiza la solicitud AJAX para modificar el producto
$.ajax({
    url: '/inventario/modificar/' + productoId + '/',  // Ajusta la URL según tu configuración
    type: 'POST',
    data: {
        'producto_id': productoId,
        'nombre': nombre,
        'existencia': existencia,
        'precio_venta': precioVenta,
        'precio_compra': precioCompra,
        'estado': estado,
        'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
    },
    success: function(response) {
        console.log('Producto modificado exitosamente');
        // Cierra el modal después de modificar el producto
        $('#modificarProductoModal').modal('hide');
        // Actualiza la página o realiza alguna acción adicional si es necesario
        location.reload();
    },
    error: function(error) {
        console.log('Error al modificar el producto:', error);
    }
});

    });
});
