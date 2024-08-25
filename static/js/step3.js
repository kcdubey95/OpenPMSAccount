
    $(document).ready(function(){
        $("form").submit(function(event){
            var nfull_name = $("#nfull_name").val().trim();
            var dob = $("#dob").val().trim();
            var naddress = $("#address").val().trim();
            var phone = $("#phone").val().trim();
            var relation = $("#exampleFormControlSelect1").val();

            var nameRegex = /^[A-Za-z\s]+$/;
            var dateRegex = /^(0[1-9]|1[0-2])\/(0[1-9]|[12]\d|3[01])\/\d{4}$/; // MM/DD/YYYY format
            var phoneRegex = /^\d{10}$/; // 10-digit phone number

            if (!nameRegex.test(nfull_name)) {
                alert("Please enter a valid full name (only alphabets allowed).");
                event.preventDefault();
            }

//            if (!dateRegex.test(dob)) {
//                alert("Please enter a valid date of birth (DD/MM/YYYY).");
//                event.preventDefault();
//            }

            if (naddress.length == 0) {
                alert("Please enter the nominee's address.");
                event.preventDefault();
            }

            if (!phoneRegex.test(phone)) {
                alert("Please enter a valid 10-digit phone number.");
                event.preventDefault();
            }

            if (relation === "Select Relation") {
                alert("Please select a valid relation with the nominee.");
                event.preventDefault();
            }
        });

         $('.datepicker').datepicker({
            language: "es",
            autoclose: true,
            format: "dd/mm/yyyy"
          });
    });

