const API_publicKey = "FLWPUBK_TEST-55b64116182b240760d2f6aa82808270-X";
  function payWithRave() {
    var currency = document.querySelector("#customer_currency").value;
    var country = document.querySelector("#customer_country").value;
    var amount = document.querySelector("#customer_amount").value;
    var customer_email = document.querySelector("#customer_email").value;

    var x = getpaidSetup({
      PBFPubKey: API_publicKey,
      // customer_phone: "0751319201",
      // pay_button_text: "Dasunspay",
      txref: "RX1",
      amount,
      country,
      currency,
      customer_email,
      onclose: function () {},
	    customizations: {
        title: "Dasuns Ltd",
        description: "Payment for service recieved",
        // logo: "https://assets.piedpiper.com/logo.png",
		   logo: "/static/images/Logo.png"
      },
      callback: function (response) {
        var txref = response.data.txRef; // collect flwRef returned and pass to a server page to complete status check.
        console.log("This is the response returned after a charge", response);
        if (
          response.tx.chargeResponseCode == "00" ||
          response.tx.chargeResponseCode == "0"
        ) {
        //   window.location = "https://www.flutterwave.com/";
		      // window.location = "https://dasuns.org/splist/";
          window.location = "http://127.0.0.1:8000/booking/1";
        } else {
          // redirect to a failure page.
        }
        x.close(); // use this to close the modal immediately after payment.
      },
    });
  }