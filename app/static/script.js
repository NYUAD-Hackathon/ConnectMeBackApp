$(document).ready(function() {

    $('#myModal').on('shown.bs.modal', function () {
      $('#myInput').focus()
    })

    $("#main-form").submit(function(e) {
        console.log("Form is being submitted!");
        e.preventDefault();
        var name = $("#input-recipient").val();
        var searchingForName = $("#input-destination").val();
        var message = $("#input-message").val();
        var phoneNumber = $("#input-phone").val();

        var values = {"name": name, "searchingForName": searchingForName, "message": message, "phoneNumber": phoneNumber};

        $.ajax({
            type: "POST",
            url: "http://www.connectmeback.org/",
            data: values,
            success: function(data){
                if (JSON.stringify(data) == "{}") {
                    $("#main-form").hide();
                    var newElement = "<div class='bounceIn panel' style='height:226px; text-shadow: none; padding-left: 15px; padding-right: 15px; width: 75%; margin: 0 auto; margin-bottom:23px; margin-top:20px; padding-top: 10%; color:#5C5C5C; font-size: 18px'>سيتم اعلامك عبر الرسائل النصية بأقرب وقت لحين استلامنا لأي رسالة لك من الشخص الذي تبحث عنه.اذا أردت ارسال رسالة اخرى <a href='http://127.0.0.1:5000/'>اضغط هنا</a></div>"
                    $("#slogan").append(newElement);
                } 
                if ('name' in data) {
                    $("#main-form").hide();
                    console.log("Got a response from the server, going to present it to the user now.");
                    console.log(data);

                    var searchingForName = data['name'];
                    var myName = data['searchingForName'];
                    var message = data['message'];
                    var phoneNumber = data['phone'];
                    var newElement = "<div class='bounceIn panel' style='height:226px; text-shadow: none; padding-left: 15px; padding-right: 15px; width: 75%; margin: 0 auto; margin-bottom:23px; margin-top:20px; padding-top: 10%; color:#5C5C5C; font-size: 18px'>وجدناهم! الاسم: "+ searchingForName + ". الهاتف: "+ phoneNumber +". الرسالة: "+ message +".</div>";
                    $("#slogan").append(newElement);
                }
            }
        });
    });

});