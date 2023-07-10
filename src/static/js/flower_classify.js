$(document).ready(function() {
    function readURL(input) {
        if (input.files && input.files[0]) {
            var reader = new FileReader();
            reader.onload = function(e) {
                $("#image-preview").removeClass("not-visible");
                $("#image-preview").attr("src", e.target.result);
            }
            reader.readAsDataURL(input.files[0]); // convert to base64 string
        }
    }

    // show uploaded flower image in screen
    $("#flower").change(function() {
        readURL(this);
        $("#flower-result").html("");
    });

    // predict flower
    $("#flower-classify-form").on("submit", function(event) {
        event.preventDefault();
        $("#status").html("");
        fetch(location.href, {
            method: "POST",
            body: new FormData($(this)[0])
        })
        .then( response => {
            if (response.ok) {
                return response.json();
            }
            throw response;
        })
        .then( result => {
            $("#flower-result").html("Prediction: " + result["flower_type"]);
        })
        .catch( error => {
            error.json().then( errorMessage => {
                $('#image-preview').addClass("not-visible");
                $("#status").html("<h5 class='text-danger'>"+errorMessage["error_message"]+"</h5>");
            })
            .catch( error => {
                $("#flower-result").html("Prediction: Cannot Predict!");
            });
        });
    });
});
