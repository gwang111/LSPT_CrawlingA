/* Lab 5 JavaScript File 
   Place variables and functions in this file */
// save whether the comments field has been edited or not
var comments_edited = false;

function validate(formObj) {
  // string to hold the alert text
  var missing_fields = "";

  // check each field, and if it's missing then add alert text
  // also, if it's the first missing field then focus on it as well
  if (formObj.firstName.value == "") {
    if (!missing_fields) formObj.firstName.focus();
    missing_fields += "You must enter a first name\n";
  }
  if (formObj.lastName.value == "") {
    if (!missing_fields) formObj.lastName.focus();
    missing_fields += "You must enter a last name\n";
  }
  if (formObj.title.value == "") {
    if (!missing_fields) formObj.title.focus();
    missing_fields += "You must enter a title\n";
  }
  if (formObj.org.value == "") {
    if (!missing_fields) formObj.org.focus();
    missing_fields += "You must enter an organization\n";
  }
  if (formObj.pseudonym.value == "") {
    if (!missing_fields) formObj.pseudonym.focus();
    missing_fields += "You must enter a nickname\n";
  }
  if (comments_edited === false || formObj.comments.value == "") {
    if (!missing_fields) formObj.comments.focus();
    missing_fields += "You must enter a comment\n";
  }

  if (missing_fields) {
    alert(missing_fields);
    return false;
  }
  else {
    alert("Successfully submitted!")
    return true;
  }
}

// focus the first element of the form on page load
function focusForm() {
  document.getElementById("firstName").focus();
}

// remove placeholder text only if it's the first time the field is being edited
function removeText() {
  if (comments_edited === false) {
    document.getElementById("comments").innerHTML = "";
    comments_edited = true;
  }
}

// alert popup for the nickname of the person entering info
function nickname() {
  first_name = document.getElementById("firstName").value;
  last_name = document.getElementById("lastName").value;
  pseudonym = document.getElementById("pseudonym").value;
  alert(first_name + " " + last_name + " is " + pseudonym);
}