
const filePhoto = document.getElementById('file-photo');
const imageOptions = document.getElementById('image-options');
const addOption = document.getElementById('add-option');
const removeOption = document.getElementById('remove-option');
const previewImage = document.getElementById('preview-image');
const imageInput = document.getElementById('image-input');

    // Ocultar opciones al alejar el mouse del div
filePhoto.addEventListener('mouseout', function() {
imageOptions.style.display = 'none';
});
// Mostrar opciones al acercar el mouse al div
filePhoto.addEventListener('mouseover', function() {
imageOptions.style.display = 'flex';
});
// Mostrar imagen seleccionada por el usuario
imageInput.addEventListener('change', function(e) {
const file = e.target.files[0];
const reader = new FileReader();
reader.onload = function(event) {
    previewImage.src = event.target.result;
};
if (file) {
    reader.readAsDataURL(file);
}
});
// Funcionalidad de las opciones
addOption.addEventListener('click', function() {
imageInput.click();
});
removeOption.addEventListener('click', function() {
previewImage.src = "/static/agregar.png"; 
imageInput.value = null;
});
