<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <!-- Google Fonts -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,300;0,400;1,300;1,400&family=Readex+Pro:wght@400;500;600;700&display=swap" rel="stylesheet">
    
    <link rel="stylesheet" href="./../resources/index.css">
    <title>BGYD Cooking</title>
</head>

<body>
<?php
    session_start();
    $is_logged_in = (isset($_SESSION['user_id']) && isset($_SESSION['username']));
?>
    <div id="header">
        <h1>BGYD Cooking Website</h1>
        <span><a href="../">Home</a></span>
        <span><a href="../about-us.php">About Us</a></span>
        <?php
            if ($is_logged_in) {
                echo '<span><a href="../account.php">Write Recipe</a></span>';
                echo '<span><a href="../auth/logout.php">Logout</a></span>';
            } else {
                echo '<span><a href="../auth/login.php">Login</a></span>';
            }
        ?>
    </div>
