const submit = document.getElementById("submit");

submit.addEventListener("click", validate);

function validate(e) {
  e.preventDefault();

  const firstNameField = document.getElementById("firstname");
  let valid = true;

  if (!firstNameField.value) {
    const nameError = document.getElementById("nameError");
    nameError.classList.add("visible");
    firstNameField.classList.add("invalid");
    nameError.setAttribute("aria-hidden", false);
    nameError.setAttribute("aria-invalid", true);
  }
  return valid;
}


function InvalidMsg(textbox) {
  
    if (textbox.value === '') {
        textbox.setCustomValidity
              ('Entering an email-id is necessary!');
    } else if (textbox.validity.typeMismatch) {
        textbox.setCustomValidity
              ('Please enter an email address which is valid!');
    } else {
        textbox.setCustomValidity('');
    }

    return true;
}

// input:valid {
//     border-bottom: 1px solid $color-success;
//    }input:invalid {
//     border-bottom: 1px solid $color-error;
//    }