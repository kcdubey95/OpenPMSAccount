
  $(document).ready(function(){
        $("form").submit(function(event){
            var fullname = $("#fullname").val().trim();
            var gender = $("input[name='gender']:checked").val();
            var dob = $("#dob").val().trim();
            var address = $("#address").val().trim();
            var income = $("input[name='income']:checked").length;
            var occupation = $("#exampleFormControlSelect1").val();

            var nameRegex = /^[A-Za-z\s]+$/;
            var dateRegex = /^(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])\/\d{4}$/;

            if (!nameRegex.test(fullname)) {
                alert("Please enter a valid full name (only alphabets allowed).");
                event.preventDefault();
            }

            if (!gender) {
                alert("Please select your gender.");
                event.preventDefault();
            }

//            if (!dateRegex.test(dob)) {
//                alert("Please enter a valid date of birth (DD/MM/YYYY).");
//                event.preventDefault();
//            }
            if (address.length == 0) {
                alert("Please enter your address.");
                event.preventDefault();
            }
            if (income == 0) {
                alert("Please select at least one income range.");
                event.preventDefault();
            }
            if (occupation == "Select Occupation") {
                alert("Please select a valid occupation.");
                event.preventDefault();
            }
        });
        $('.datepicker').datepicker({
            language: "es",
            autoclose: true,
            format: "dd/mm/yyyy"
        });
    });
