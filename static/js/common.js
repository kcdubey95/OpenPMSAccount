




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


function setActiveStep(step) {
  const steps = document.querySelectorAll('.progress-step');
  const progressBar = document.querySelector('.progress-bar-highlight');
  if (progressBar) {
    steps.forEach((element, index) => {
      if (index < step) {
        element.classList.add('completed');
        element.classList.remove('active');
      } else if (index === step) {
        element.classList.add('active');
        element.classList.remove('completed');
      } else {
        element.classList.remove('active', 'completed');
      }
    });
    const stepPercentage = (step / (steps.length - 1)) * 100;
    progressBar.style.width = `${stepPercentage}%`;
  } else {
    console.error('Progress bar element not found');
  }
}
step= parseInt($('#progress_bar').val())
setActiveStep(step);
document.addEventListener('DOMContentLoaded', function () {
    var prevButton = document.getElementById('prevButton');
    prevButton.addEventListener('click', function (event) {
        event.preventDefault();
        var confirmation = confirm('You have unsaved changes. Are you sure you want to go back?');
            step= parseInt($('#progress_bar').val())
        if (confirmation) {
            var formData = {
                step: step,
            };
            fetch('/update-step', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(formData)
            })
            .then(response => response.json())
            .then(data => {
                if (data.status === 'success') {
                    window.location.href = '/step1';
                } else {
                    alert('An error occurred while saving your data. Please try again.');
                }
            })
            .catch(error => {
                alert('An error occurred while saving your data. Please try again.');
            });
        }
    });
});
