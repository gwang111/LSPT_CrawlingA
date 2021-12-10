<?php
include('../includes/functions.inc.php');
session_start();

$conn = db_connect();

// user input validation
function validate($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}

// If a user is trying to login
if (isset($_POST['login']) && isset($_POST['username']) && isset($_POST['password'])) {
  $uname = validate($_POST['username']);
  $pass = validate($_POST['password']);

  // Error if either username or password is required
  if (empty($uname)) {
    header("Location: login.php?error=Username is required");
  }
  else if(empty($pass)) {
    header("Location: login.php?error=Password is required");
  }
  // If username/password are entered
  else {
    // Query for the user account
    $pstmt = $conn->prepare("SELECT * FROM accounts WHERE username=:username");
    $pstmt->execute(array(':username' => $uname));
    $result = $pstmt->fetchAll();

    // If user exists
    if (count($result) === 1) {
      $row = $result[0];
      // If account credentials verify
      if ($row['username'] === $uname && password_verify($pass, $row['password'])) {
        echo "Logged in!";
        $_SESSION['username'] = $row['username'];
        $_SESSION['user_id'] = $row['user_id'];
        header("Location: ../index.php");
      } else {
        header("Location: login.php?error=Incorrect credentials");
      }
    }
    // If user not found
    else {
      header("Location: login.php?error=User doesn't exist");
    }
  }
}
// If a user is registering
else if (isset($_POST['register']) && isset($_POST['username']) && isset($_POST['password'])) {
  $uname = validate($_POST['username']);
  $pass = validate($_POST['password']);

  // Error if either username or password is required
  if (empty($uname)) {
    header("Location: register.php?error=Username is required");
  }
  else if(empty($pass)) {
    header("Location: register.php?error=Password is required");
  }
  // If username/password are entered
  else {
    // Check to make sure the username isn't taken
    $pstmt = $conn->prepare("SELECT * FROM accounts WHERE username=:username");
    $pstmt->execute(array(':username' => $uname));
    $result = $pstmt->fetchAll();

    // Error if the username is taken
    if (count($result) === 1) {
      header("Location: register.php?error=Username is taken");
    }
    // Otherwise salt + hash password and insert into array
    else {
      $pstmt = $conn->prepare("INSERT INTO accounts (username, password)
                              VALUES(:username, :password)");
      $result = $pstmt->execute(array(':username' => $uname, ':password' => password_hash($pass, PASSWORD_DEFAULT)));
      // If there was somehow a DB error
      if (!$result) {
        header("Location: register.php?error=Couldn't create new user");
      }
      // If everything went well send them to login
      else {
        header("Location: login.php");
      }
    }
  }
} 
else {
  header("Location: ../index.php");
}
exit();
?>
