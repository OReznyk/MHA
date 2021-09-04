var i = 0;
var radio_i = 0
$(document).ready(function() {


    $("#title").click(function() {
        swal("הכנס כותרת:", {
                content: "input",
            })
            .then((value) => {
                i++;
                $(".section2").append("<div  class='element'  id='el-" + i + "'><h2 class='edit_text' contenteditable='true'>" + value + "</h2>  <div class='edit'>    <input type='button' value='שמור שינויים' onclick='saveEdits(this)'/><span class='update'> - ערוך את הטקסט ולחץ לשמור</span> <button onClick='duplicate(this)'> שכפל</button> <button class='delete' onclick='delete_e(this)'> מחק</button>  </div></div>");
                drag();
            });

    });


    $("#text").click(function() {
        (async() => {

            const {
                value: text
            } = await Swal.fire({
                input: 'textarea',
                inputLabel: 'הכנס טקסט',
                inputPlaceholder: 'הקלד טקסט ארוך...',
                inputAttributes: {
                    'aria-label': 'הקלד טקסט ארוך'
                },
                showCancelButton: true
            })

            if (text) {
                i++;
                $(".section2").append("<div  class='element'  id='el-" + i + "'><p>" + text + "</p>    <div class='edit'> <button onClick='duplicate(this)'> שכפל</button> <button class='delete' onclick='delete_e(this)'> מחק</button>  </div></div>");
            }
            drag();
        })()

    });

    $("#url").click(function() {
        (async() => {

            const {
                value: url
            } = await Swal.fire({
                input: 'url',
                inputLabel: ' הכנס כתובות יוטוב צריך להראות כך: https://www.youtube.com/embed/U2X4Rt8pyXg',
                inputPlaceholder: 'Enter the URL'
            })

            if (url) {
                i++;
                $(".section2").append("<div  class='element'  id='el-" + i + "'><iframe width='560' height='315' src='" + url + "'> </iframe>    <div class='edit'> <button onClick='duplicate(this)'> שכפל</button> <button class='delete' onclick='delete_e(this)'> מחק</button>  </div></div>");



            }
            drag();
        })()


    });

    $("#question-radio").click(function() {
        (async() => {

            const {
                value: formValues
            } = await Swal.fire({
                title: 'הכנס שאלה עם אפשרות לתשובה אחת',
                html: ' שאלה: <input id="swal-input1" class="swal2-input"><br>' +
                    'תשובה 1<input id="swal-input2" class="swal2-input"><br>' +
                    'תשובה 2<input id="swal-input3" class="swal2-input"><br>' +
                    'תשובה 3<input id="swal-input4" class="swal2-input"><br>' +
                    'תשובה 4<input id="swal-input5" class="swal2-input"><br>',
                focusConfirm: false,
                preConfirm: () => {
                    return [
                        $('#swal-input1').val(),
                        $('#swal-input2').val(),
                        $('#swal-input3').val(),
                        $('#swal-input4').val(),
                        $('#swal-input5').val()
                    ]


                }
            })

            if (formValues) {

                i++;
                radio_i++;
                $(".section2").append("<div  class='element el-radio'  id='el-" + i + "'><p>" + formValues[0] + "</p><input type='radio' name='radio" + radio_i + "' value='" + formValues[1] + "'><label for='" + formValues[1] + "'>" + formValues[1] + "</label><br><input type='radio' name='radio" + radio_i + "' value='" + formValues[2] + "'><label for='" + formValues[2] + "'>" + formValues[2] + "</label><br><input type='radio' name='radio" + radio_i + "' value='" + formValues[3] + "'><label for='" + formValues[3] + "'>" + formValues[3] + "</label><br><input type='radio' name='radio" + radio_i + "' value='" + formValues[4] + "'><label for='" + formValues[4] + "'>" + formValues[4] + "</label> <div class='edit'> <button onClick='duplicate(this)'> שכפל</button> <button class='delete' onclick='delete_e(this)'> מחק</button>  </div></div>");

            }
            drag();
        })()


    });

    $("#image").click(function() {
        (async() => {
            i++;
            $(".section2").append("<div  class='element'  id='el-" + i + "'><p><input type='file' accept='image/*'' name='image' id='file' onchange='loadFile(event)'' style='display: none;''></p><p><label for='file' style='cursor: pointer;''>הוסף תמונה</label></p><p><img id='output' width='800' /></p><div class='edit'> <button onClick='duplicate(this)'> שכפל</button> <button class='delete' onclick='delete_e(this)'> מחק</button>  </div>");
            drag();
        })()

    });



    $("#save").click(function() {

        swal({
            // position: 'top-end',
            icon: 'success',
            title: 'השאלון נשמר',
            showConfirmButton: false,
            timer: 2200
        })

    });

    //////////////
    $("#myBtn").click(function() {
        var elem = $('.section2');
        elem.clone().appendTo(".modal-body");

        $("#myModal").modal();
    });

    $("#myModal").on('hide.bs.modal', function() {

        $(".modal-body").empty();
    });

});



function delete_e(e) {
    swal({
            title: "למחוק בטוח?",
            text: "לאחר שנמחק, לא תוכל לשחזר את האלמנט הזה!",
            icon: "warning",
            buttons: true,
            dangerMode: true,
        })
        .then((willDelete) => {
            if (willDelete) {

                $(e).parents(".element").remove();
            }
        });



}

//////////////גרירה///////////////


function drag() {
    // $(".element").draggable({
    //     cancel: ".edit_text"
    // });

}
////////////////העלת תמונה/////////////


var loadFile = function(event) {
    var image = document.getElementById('output');
    image.src = URL.createObjectURL(event.target.files[0]);
};

/////////////////שכפול אלמנט/////////


function duplicate(this_el) {
    // var itm = $(this_el).parents('.element').attr('id');
    // console.log(itm);

    var elem = $(this_el).parents('.element');
    var clone = elem.clone().appendTo(".section2");
    clone.removeAttr('id');

    i++;
    clone.attr("id", "el" + i);
    $(this_el).find(".update").text("לאחר השינויים יש לשמור");

    radio_i++;
    clone.find("input").attr("name", "radio" + i);
    drag();

}

/////////////////עריכת טקסט ושינוי/////////

function saveEdits(this_el) {


    //get the editable element

    var editElem = $(this_el).siblings(".edit_text");


    //get the edited element content
    var userVersion = editElem.text();

    //save the content to local storage
    localStorage.userEdits = userVersion;

    //write a confirmation to the user

    $(this_el).siblings(".update").text("עריכה נשמרה");

}

function checkEdits() {

    //find out if the user has previously saved edits
    if (localStorage.userEdits != null)
        $(".edit_text").text(localStorage.userEdits);
}