$(document).ready(function() {
    $('#id_profile').on('change', function(event) {
        const file = event.target.files[0];
        if (file) {
            const reader = new FileReader();
            reader.onload = function(e) {
                $('#profile-pic').attr('src', e.target.result);
            };
            reader.readAsDataURL(file);
        }
    });
    
});