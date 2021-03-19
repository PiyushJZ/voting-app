$("form[name=login_form").submit(function(e){
    var $form = $(this)
    var $error = $form.find(".error");
    var data = $form.serialize();

    if($("input[name='admin']").is(':checked')) {
        $.ajax({
            url:"/login/admin/",
            type: "POST",
            data: data,
            dataType: "json",
            success: function(resp) {
                console.log(resp);
                window.location.href = "/admin/"
            },
            error: function(resp) {
                console.log(resp)
                $error.text(resp.responseJSON.error).removeClass("error--hidden")
            }
        })
    } else {
        $.ajax({
            url:"/login/user/",
            type: "POST",
            data: data,
            dataType: "json",
            success: function(resp) {
                console.log(resp);
                window.location.href = "/user/"
            },
            error: function(resp) {
                console.log(resp)
                $error.text(resp.responseJSON.error).removeClass("error--hidden")
            }
        })
    }

    e.preventDefault();
})

$("form[name=vote_form").submit(function(e){
    var $form = $(this)
    var $error = $form.find(".error");
    var data = document.getElementsByName('vote')
    for(i = 0; i < data.length; i++) {
        if (data[i].checked) {
            data = data[i].value;
            break;
        }
    }

    $.ajax({
        url: "/logout/" + {data},
        type: "POST",
        data: data,
        dataType: "json",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/"
        },
        error: function(resp) {
            console.log(resp)
            $error.text(resp.responseJSON.error).removeClass("error--hidden")
        }
    })
})

$("form[name=logout_form").submit(function(e){
    $.ajax({
        url: "/",
        type: "GET",
        success: function(resp) {
            console.log(resp);
            window.location.href = "/"
        }
    })
})