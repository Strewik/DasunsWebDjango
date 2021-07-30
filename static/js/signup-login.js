const loginValid = () =>{
    let username = document.getElementById("username");
    let password = document.getElementById("password");

    let uErr = document.getElementById("usernameErr");
    let pErr = document.getElementById("passwordErr");

    if(username.value == ""){
        username.style.border= "1px solid red"
        uErr.innerHTML = "Please provide the username"
        uErr.style =  "color: red; font-size:11px; font-family:Arial, Helvetica, sans-serif;";
        return false;
    }else 
        username.style.border= "1px solid green"
        uErr.innerHTML = ""

    if(password.value == ""){
        password.style.border= "1px solid red"
        pErr.innerHTML = "Please provide the password"
        pErr.style =  "color: red; font-size:11px; font-family:Arial, Helvetica, sans-serif;";
        return false;
    }else
        password.style.border= "1px solid green"
        pErr.innerHTML = " "
}

const signupValid = () =>{
    // let usernameEl = document.getElementById('username');
	// let firstnameEl = document.getElementById('firstname');
	// let lastnameEl = document.getElementById('lastname');
	// let genderEl = document.getElementById('gender');
	// let phoneEl = document.getElementById('phone');
	// let emailEl = document.getElementById('email');
	// let password1El = document.getElementById('password1');
	// let password2El = document.getElementById('password2');

    let username = document.registerform.username
	let firstname = document.registerform.firstname
	let lastname = document.getElementById('lastname');
	let genderEl = document.getElementById('gender');
	let phoneEl = document.getElementById('phone');
	let emailEl = document.getElementById('email');
	let password1El = document.getElementById('password1');
	let password2El = document.getElementById('password2');
    let terms = document.getElementById('terms');

    //Get error ids 
    let unErr = document.getElementById('unErr');
	let fnErr = document.getElementById('fnErr');
	let lnErr = document.getElementById('lnErr');
	let gErr = document.getElementById('gErr');
	let pErr = document.getElementById('pErr');
	let emErr = document.getElementById('emErr');
	let pass1Err = document.getElementById('pass1Err');
	let pass2Err = document.getElementById('pass2Err');
    let termsErr = document.getElementById('termsErr');

    // Trim off spaces

    // let username = usernameEl.value.trim()
	// let firstname = firstnameEl.value.trim() 
	// let lastname = lastnameEl.value.trim()
	// let gender = genderEl.value.trim()
	// let phone = phoneEl.value.trim()
	// let email = emailEl.value.trim()
	// let password1= password1El.value.trim()
	// let password2 = password2El.value.trim()

    if(username.value == ""){
        username.style.border= "1px solid red"
        unErr.innerHTML = "Please provide the username"
        unErr.style =  "color: red; font-size:11px; font-family:Arial, Helvetica, sans-serif;";
        return false;
    }

    if(firstname.value == ""){
        firstname.style.border= "1px solid red"
        fnErr.innerHTML = "Please provide the password"
        fnErr.style =  "color: red; font-size:11px; font-family:Arial, Helvetica, sans-serif;";
        return false;
    }

    if(lastname.value == ""){
        firstname.style.border= "1px solid red"
        fnErr.innerHTML = "Please provide your last name"
        fnErr.style =  "color: red; font-size:11px; font-family:Arial, Helvetica, sans-serif;";
        return false;
    }

    if(terms.checked == false){
        termsErr.innerHTML = "Please agree to terms to proceed"
        termsErr.style =  "color: red; font-size:11px; font-family:Arial, Helvetica, sans-serif;";
        return false;

    }
}