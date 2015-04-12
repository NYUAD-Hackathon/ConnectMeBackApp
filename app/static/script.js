$(document).ready(function() {

    $("#main-form").submit(function(e) {
        console.log("Form is being submitted!");
        e.preventDefault();
        var name = $("#input-recipient").val();
        var searchingForName = $("#input-destination").val();
        var message = $("#input-message").val();
        var phoneNumber = $("#input-phone").val();

        var values = {"name": name, "searchingForName": searchingForName, "message": message, "phoneNumber": phoneNumber};
        $("#main-form").hide();

        $.ajax({
            type: "POST",
            url: "http://7b3eabbd.ngrok.com",
            data: values,
            success: function(data){
                if (JSON.stringify(data) == "{}") {
                    console.log("Nothing came back from the server.");
                    var newElement = "<div class='bounceIn panel' style='height:226px; text-shadow: none; padding-left: 15px; padding-right: 15px; width: 75%; margin: 0 auto; margin-bottom:23px; margin-top:20px; padding-top: 20px; color:black; font-size: 18px'>You'll be notified via SMS as soon as your loved one submits a message. Please submit another <a href='http://127.0.0.1:5000/'>here.</a></div>"
                    $("#slogan").append(newElement);
                } else {
                    console.log("Got a response from the server, going to present it to the user now.");
                    var newElement = "<div class='bounceIn panel' style='height:226px; text-shadow: none; padding-left: 15px; padding-right: 15px; width: 75%; margin: 0 auto; margin-bottom:23px; margin-top:20px; padding-top: 20px; color:black; font-size: 18px'>You'll be notified via SMS as soon as your loved one submits a message. Please submit another <a href='http://127.0.0.1:5000/'>here.</a></div>"
                    $("#slogan").append(newElement);
                }
            }
        });
    });

});