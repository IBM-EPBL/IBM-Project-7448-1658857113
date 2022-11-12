function preview() {
    frame.src=URL.createObjectURL(event.target.files[0]);
}

$(document).ready(function() {
    $('#clear_button').on('click', function() {
    $('#image').val('');
    $('#frame').attr('src',"");
 });
});
var input = document.getElementById('image');
var infoArea = document.getElementById('frame');

input.addEventListener('change', showFileName);

function showFileName(event) {
    var input = event.srcElement;
    var fileName = input.files[0].name;
    infoArea.textContent = 'File name: ' + fileName;
}