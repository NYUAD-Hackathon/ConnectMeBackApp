$(document).ready(function() {

    $("#main-form").submit(function(e) {
        console.log("Form is being submitted!");
        e.preventDefault();
        var name = $("#input-recipient").val();
        var searchingForName = $("#input-destination").val();
        var message = $("#input-message").val();
        var phoneNumber = $("#input-phone").val();

        var values = {"name": name, "searchingForName": searchingForName, "message": message, "phoneNumber": phoneNumber}
        $.ajax({
            type: "POST",
            url: "http://7b3eabbd.ngrok.com",
            data: values,
            success: function(data){
                if (JSON.stringify(data) == "{}") {
                    
                }
            }
        })
    });

});