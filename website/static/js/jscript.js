var i = 0;
var radio_i = 0
var range_i = 0;
var txt_edit = "<div class='edit'> <button class='duplicate' type='button' onClick='duplicate(this)'> שכפל</button> <button type='button' class='delete' onclick='delete_e(this)'> מחק</button></div>"

$(document).ready(function() {

    const state = {
        currentUser: {
            firstName: '',
            lastName: '',
            email: '',
            birtDate: '',
            creationDate: '',
            permission: ''
        }
    }

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

    $("#table").click(function() {
        (async() => {

            const {
                value: formValues
            } = await Swal.fire({
                title: 'איזה טבלה תרצו ?',
                html: ' עמודות: <input id="swal-input1" type="number"  class="swal2-input"><br>' +
                    'שורות <input id="swal-input2" type="number" class="swal2-input">',


                focusConfirm: false,
                preConfirm: () => {
                    return [
                        $('#swal-input1').val(),
                        $('#swal-input2').val(),


                    ]


                }
            })

            if (formValues) {

                i++;


                $(".section2 .information" + currentTab).append("<div  class='element'  id='el-" + i + "'><table class='table table-striped'> <tbody> </tbody> </table>" + txt_edit + "</div>");
                for (var w = 0; w < formValues[1]; w++) {
                    var $tr = $('<tr></tr>');
                    for (var j = 0; j < formValues[0]; j++) {
                        $tr.append('<td contenteditable="true">לחץ לשינוי מלל</td>');
                    }
                    $('#el-' + i + ' table tbody').append($tr);
                }


            }
            drag();
        })()


    });



    $("#category").click(function() {
        (async() => {

            const { value: category } = await Swal.fire({

                input: 'select',
                inputOptions: {

                    בריאות: 'בריאות',
                    אבחנה: 'אבחנה',
                    פסיכולגיה: 'פסיכולגיה',
                    תרופות: 'תרופות',
                    אחר: 'אחר'
                },
                inputPlaceholder: 'בחר קטגוריה',
                showCancelButton: true,
                inputValidator: (value) => {
                    return new Promise((resolve) => {
                        if (value === 'אחר') {
                            swal("הוסף קטגוריה חדשה:", {
                                    content: "input",

                                })
                                .then((value) => {

                                    $(".category").text(value);
                                    resolve()
                                });


                        } else {
                            $(".category").text(value);
                            resolve()
                        }
                    })
                }


            })


            // if (text) {
            //     i++;
            //     $(".section2 .information" + currentTab).append("<div  class='element'  id='el-" + i + "'><p class='edit_text' contenteditable='true'>" + text + "</p>" + txt_edit + "</div>");
            // }
            drag();
        })()

    });

    $("#subject").click(function() {
        swal(" מה נושא ההחלטה:", {
                content: "input",

            })
            .then((value) => {
                $(".subject").text(value);
                drag();
            });

    });

    $("#title").click(function() {
        swal("הכנס כותרת:", {
                content: "input",


            })
            .then((value) => {
                i++;
                $(".section2 .information" + currentTab).append("<div  class='element'  id='el-" + i + "'><h2 class='edit_text' contenteditable='true'>" + value + "</h2>" + txt_edit + "</div>");
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
                $(".section2 .information" + currentTab).append("<div  class='element'  id='el-" + i + "'><p class='edit_text' contenteditable='true'>" + text + "</p>" + txt_edit + "</div>");
            }
            drag();
        })()

    });

    $("#yes_no").click(function() {
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
                $(".section2 .information" + currentTab).append("<div  class='element'  id='el-" + i + "'><p class='edit_text' contenteditable='true'>" + text + "</p>" + txt_edit + "</div>");
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
                $(".section2 .information" + currentTab).append("<div  class='element'  id='el-" + i + "'><iframe width='560' height='315' src='" + url + "'> </iframe>" + txt_edit + "</div>");



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

    $("#question-radio").click(function() {
        (async() => {

            const {
                value: formValues
            } = await Swal.fire({
                title: 'הכנס שאלה עם אפשרות לתשובה אחת',
                html: ' שאלה: <input id="swal-input1" class="swal2-input"><br>' +
                    'תשובה 1<input id="swal-input2" value="כן" class="swal2-input"><br>' +
                    'תשובה 2<input id="swal-input3" value="לא"  class="swal2-input"><br">' +
                    'תשובה 3<input id="swal-input4" value="לא יודע"  class="swal2-input"><br>',

                focusConfirm: false,
                preConfirm: () => {
                    return [
                        $('#swal-input1').val(),
                        $('#swal-input2').val(),
                        $('#swal-input3').val(),
                        $('#swal-input4').val(),

                    ]


                }
            })

            if (formValues) {

                i++;
                radio_i++;
                $(".section2 .information" + currentTab).append("<div  class='element el-radio'  id='el-" + i + "'><p>" + formValues[0] + "</p><input type='radio' name='radio" + radio_i + "' value='" + formValues[1] + "'><label for='" + formValues[1] + "'>" + formValues[1] + "</label><br><input type='radio' name='radio" + radio_i + "' value='" + formValues[2] + "'><label for='" + formValues[2] + "'>" + formValues[2] + "</label><br><input type='radio' name='radio" + radio_i + "' value='" + formValues[3] + "'><label for='" + formValues[3] + "'>" + formValues[3] + "</label>" + txt_edit + "</div>");

            }
            drag();
        })()


    });

    $("#image").click(function() {
        (async() => {
            i++;
            $(".section2 .information" + currentTab).append("<div  class='element'  id='el-" + i + "'><p><input type='file' accept='image/*'' name='image' id='file' onchange='loadFile(event)'' style='display: none;''></p><p><label for='file' style='cursor: pointer;''>לחצו כאן להוספת תמונה</label></p><p><img class='img_info' id='output' /></p>" + txt_edit);
            drag();
        })()

    });

    $("#range").click(function() {
        (async() => {

            const {
                value: formValues
            } = await Swal.fire({
                title: 'הכנס שאלה עם אפשרות לדירוג 1-10',
                html: ' <input id="swal-input" class="swal2-input"><br>',
                focusConfirm: false,
                preConfirm: () => {
                    return [
                        $('#swal-input').val(),
                    ]
                }
            })

            if (formValues) {

                i++;
                range_i++;
                $(".section2 .information" + currentTab).append("<div  class='element el-range'  id='el-" + i + "'>   <div class='range-wrap' contenteditable='true'> " + formValues[0] + "<input type='range' class='range' min='1' max='10'><output class='bubble'></output></div>" + txt_edit + "</div>");

            }
            range();
            drag();
        })()


    });



    $("#options").click(function() {
        (async() => {

            const { value: formValues } = await Swal.fire({
                title: 'אפשרויות ההחלטה',
                html: '<p class="option_score">אפשרות א:<input id="swal-input1" class="swal2-input">ניקוד <input type="number" id="score-input1" class="swal2-input" > </p>' +
                    '<p class="option_score">אפשרות ב:<input id="swal-input2" class="swal2-input">ניקוד <input type="number" id="score-input2" class="swal2-input"> </p>',
                focusConfirm: false,
                preConfirm: () => {
                    return [
                        $('#swal-input1').val(),
                        $('#score-input1').val(),
                        $('#swal-input2').val(),
                        $('#score-input2').val()
                    ]
                }
            })

            if (formValues) {
                i++;

                $(".options").append("<div  class='element'  id='el-" + i + "'><p class='option1 edit_text' contenteditable='true'>אפשרות א' :" + formValues[0] + "<span>" + formValues[1] + " </span> </p><p class='option2 edit_text' contenteditable='true'>אפשרות ב' :" + formValues[2] + "<span>" + formValues[3] + " </span></p>" + txt_edit + "</div>");
                $(".information4 .options1").text(formValues[0]);
                $(".information4 .options2").text(formValues[2]);
            }
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

    $('#user_row').click(function() {
        state.currentUser = {
            firstName: $(".first_name").html(),
            lastName: $(".last_name").html(),
            email: $(".email").html(),
            birtDate: $(".birth_date").html(),
            creationDate: $(".creation_date").html(),
            permission: $(".permission").html()
        }
    });

    $('#user_details_modal').on('show.bs.modal', function() {
        const userElement =
            `<div>
        <div>${state.currentUser.firstName}</div>
        <div>${state.currentUser.lastName}</div>
        <div>${state.currentUser.email}</div>
        <div>${state.currentUser.birtDate}</div>
        <div>${state.currentUser.creationDate}</div>
        <div>${state.currentUser.permission}</div>
     </div>`
        let modal = $(this);
        modal.find('.modal-body').html(userElement);
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
    var clone = elem.clone().appendTo(".section2 .information");
    clone.removeAttr('id');

    // i++;
    // clone.attr("id", "el" + i);
    // $(this_el).find(".update").text("לאחר השינויים יש לשמור");

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

////////////////////////////////////////
var currentTab = 0;
var stop = 0;
var url;

function showTab(n) {
    // This function will display the specified tab of the form...
    var x = document.getElementsByClassName("tab_from");
    x[n].style.display = "block";
    //... and fix the Previous/Next buttons:
    if (n == 0) {
        document.getElementById("prevBtn").style.display = "none";
    } else {
        document.getElementById("prevBtn").style.display = "inline";
    }
    if (n == (x.length - 1)) {
        document.getElementById("nextBtn").innerHTML = "שליחת טופס";
        document.getElementById("nextBtn").style.display = "none";
    } else {
        document.getElementById("nextBtn").style.display = "inline";
        document.getElementById("nextBtn").innerHTML = "הבא &gt;";
    }

    var currentTab = 0;

    //... and run a function that will display the correct step indicator:
    fixStepIndicator(n)
}



function nextPrev(n) {
    // This function will figure out which tab to display
    var x = document.getElementsByClassName("tab_from");
    // Exit the function if any field in the current tab is invalid:
    if (n == 1 && !validateForm()) return false;
    // Hide the current tab:
    x[currentTab].style.display = "none";
    // Increase or decrease the current tab by 1:
    currentTab = currentTab + n;
    console.log(currentTab);
    // if you have reached the end of the form...
    if (currentTab >= x.length) {
        // ... the form gets submitted:
        document.getElementById("regForm").submit();
        //    location.href = "send.html";



        // console.log("חיעחיעח");
        // location.href = "send.html";
        return false;
    }

    if (currentTab == 1) {

        $(".section1").show();


    }

    if (currentTab == 2) {



    }



    // Otherwise, display the correct tab:
    showTab(currentTab);
}

function validateForm() {
    // This function deals with validation of the form fields
    var x, y, i, valid = true;
    x = document.getElementsByClassName("tab_from");
    y = x[currentTab].getElementsByClassName("required");
    var tel = $('#tel').val();
    var email = $('#email').val();
    var tz = $('#tz').val();
    var day = $('#day').val();
    var mon = $('#mon').val();
    var year = $('#year').val();

    // A loop that checks every input field in the current tab:
    // for (i = 0; i < y.length; i++) {
    //     // If a field is empty...
    //     if (y[i].value == "") {
    //         // add an "invalid" class to the field:
    //         y[i].className += " invalid";



    //         // and set the current valid status to false
    //         valid = false;
    //     }
    // if (!validNumber(tel)) {
    //     alert("נא למלא את מספר הטלפון בצורה הנכונה")
    //     return false;
    // }
    // if (!validMail(email)) {
    //     alert('אנא מלא דוא"ל תקניּ')
    //     return false;
    // }

    // if (currentTab == 1) {

    //     if (day > 31 || day < 1) {
    //         alert('נא למלא יום באופן תקני')
    //         return false;
    //     }

    //     if (mon > 12 || mon < 1) {
    //         alert('נא למלא חודש באופן תקני')
    //         return false;
    //     }
    //     if (year > 2000 || year < 1900) {

    //         alert('נא למלא שנה באופן תקני')
    //         return false;
    //     }


    // }


    //  }

    //   console.log(currentTab);
    // if (currentTab == 3) {
    //     x = $("#signature").jSignature('getData', 'base30')[1].length > 20 ? 0 : 1;
    //     if (x == 1) {
    //         alert('בבקשה לחתום..');
    //         valid = false;
    //     }
    // }

    // If the valid status is true, mark the step as finished and valid:
    if (valid) {
        document.getElementsByClassName("step")[currentTab].className += " finish";
    }
    return valid; // return the valid status
}

function fixStepIndicator(n) {
    // This function removes the "active" class of all steps...
    var i, x = document.getElementsByClassName("step");
    for (i = 0; i < x.length; i++) {
        x[i].className = x[i].className.replace(" active", "");
    }
    //... and adds the "active" class on the current step:
    x[n].className += " active";
}

function validNumber(num) //if valid number - return true
{
    var re = /^0\d([\d]{0,1})([-]{0,1})\d{7}$/;
    return re.test(num);
}

function validMail(strEmail) //if valid mail - return true
{
    var r, re;
    var email = new String(strEmail);
    re = /\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*/ig;
    if (email.search(re) == 0)
        return true;
    else
        return false;
}

////////////////////////////////////


$(document).ready(function() {
    range();

    const file = "";
    // $('#referrer').val(document.referrer);
    showTab(currentTab);
    // var uploadField = document.getElementById("file");

    // uploadField.onchange = function() {
    //     if (this.files[0].size > 500000) {
    //         alert("הקובץ גדול מידי!");
    //         this.value = "";

    //     };
    // };





    $("#regForm").submit(function() {


        $("#submit_btn").prop("disabled", true);


        // var data = $("form").serialize();
        var data2 = {};
        $("form").serializeArray().map(function(x) { data2[x.name] = x.value; });

        send_again(data2);


        return false;
    });



    function send_again(data2) {
        var ok;


        data2.text_long2 = "https://join.zionutdatit.org.il/pdf_cv/" + data2.tz + ".pdf";


        $.ajax({
            method: "post",
            data: data2,
            // contentType: "application/x-www-form-urlencoded",
            // url: "https://closeapp.co.il/campaigns/?project=ichood_leumi&id=133&action=create",
            success: function(answer) {
                if (answer.success) {

                    $(".main").hide();
                    $(".toda").show();
                    getPdf(data2).finally(() => {

                    });
                } else {
                    alert("שגיאה בשליחת הנתונים");
                }
            },


        });

    }





    /////////////////מד/////////

});

function range()

{

    const allRanges = document.querySelectorAll(".range-wrap");
    allRanges.forEach(wrap => {
        const range = wrap.querySelector(".range");
        const bubble = wrap.querySelector(".bubble");

        range.addEventListener("input", () => {
            setBubble(range, bubble);
        });
        setBubble(range, bubble);
    });
}


function setBubble(range, bubble) {
    const val = range.value;
    const min = range.min ? range.min : 0;
    const max = range.max ? range.max : 10;
    const newVal = Number(((val - min) * 100) / (max - min));
    bubble.innerHTML = val;

    // Sorta magic numbers based on size of the native UI thumb
    bubble.style.right = `calc(${newVal}% + (${8 - newVal * 0.15}px))`;
}

//find out if the user has previously saved edits
if (localStorage.userEdits != null)
    $(".edit_text").text(localStorage.userEdits);
