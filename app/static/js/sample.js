
function show_password()
            {
                var y = document.getElementById("t2");
                if(y.type == "password")
                {
                    y.type = "text"
                }
                else
                {
                    y.type = "password"
                }
            }

  function myFunction(id)
    {
    var x = document.getElementById(id);
    x.value = x.value.toUpperCase();
    }

function validate(id) {
    var x = document.getElementById(id);
    x.value = x.value.toLowerCase();
}

function show() {
        var msg
         msg = "            Password Alert\n" +
               "Must Contain at Least One Number\n" +
               "Must Contain at Least One Uppercase Letter\n" +
               "Must Contain at Least One Lowercase Letter\n" +
               "Must Contain at Least One Special Symbol\n" +
               "Must Contain at Least 8 or More Characters"
            alert(msg)
    }

