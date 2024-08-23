$('.alphavalid').on('keypress paste', function (e) {
    checkInputValidation(e, this, 'alphavalid');
});

$('.alphanumericvalid').on('keypress paste', function (e) {
    checkInputValidation(e, this, 'alphanumericvalid');
});

$('.numericvalid').on('keypress paste', function (e) {
    checkInputValidation(e, this, 'numericvalid');
});

$('#emailvalid').on('keypress paste', function (e) {
    checkInputValidation(e, this, 'emailvalid');
});

function checkInputValidation(e, pointer, validtype) {
//     debugger
    var c = this.selectionStart,
        v = pointer.value,
        key;
    if (e.type == "keypress") {
        key = String.fromCharCode(e.charCode ? e.which : e.charCode);
    } else if (e.type == "paste") {
        key = e.originalEvent.clipboardData.getData('text');
    }
    var val = v.substr(0, c) + key + v.substr(c);

    if (validtype == 'alphavalid') {
        var regex = /^[a-zA-Z\s()]*$/;
        var msg = 'Only  Alphabets are allowed in this field';
    } else if (validtype == 'alphannumericvalid') {
        var regex = /^[a-zA-Z0-9\s()\.]*$/;
        var msg = 'Only patterns Alphanumeric are allowed in this field';
    }  else if (validtype == 'numericvalid') {
        var regex = /^[0-9\s\-]*$/;
        var msg = 'Only Numbers are allowed in this field';
    } else if (validtype == 'universalvalid') {
        var regex = /^[a-zA-Z0-9\[\]\(\)<>\/\\&\%\"\'\:\;\!\,\.]*$/;
        var msg = 'Only patterns between [a-z] | [A-Z] | [0-9] & _ ;,*, ! are allowed in this field';
    } else if (validtype == 'emailvalid') {
        var regex = /^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
        var msg = 'Only Numbers are allowed in this field';
    }
    var check = val.match(regex);
    if (!check) {
        e.preventDefault();
        alert(msg);
        return false;
    } else {
        return true;
    }
}
