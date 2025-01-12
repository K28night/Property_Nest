function previewAndSubmit(event) {
    var reader = new FileReader();
    reader.onload = function(){
        var output = document.getElementById('image-preview');
        output.src = reader.result;
        output.style.display = 'block';
    };
    reader.readAsDataURL(event.target.files[0]);

    // Submit the form after the image has been selected and previewed
    setTimeout(function() {
        event.target.form.submit();
    }, 500);  // Small delay to ensure preview is shown before submission
}
document.getElementById('image-upload').onchange = function(event) { if (event.target.files.length > 0) {
    alert('File selected: ' + event.target.files[0].name);
} else {
    alert('No file selected');
}}