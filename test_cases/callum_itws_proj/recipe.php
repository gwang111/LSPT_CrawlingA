<?php
// This path requires some additional information, namely a recipeid to lookup and display
// We will require that here or else redirect back to the homepage.

// The recipeid will be encoded in a query string
$recipeid_exists = isset($_GET["recipe"]);
if (!$recipeid_exists) {
    header('Location: ./index.php', true, 302);
    die();
}
include('includes/functions.inc.php');
// Now here begins the HTML portion
include('includes/init.inc.php');
// All that's left is to add the title and any other head information,
// then close the head tag.
// We do also need to close the html tag at the very end.
?>
<div class="recipe-body content-body">
    <?php
    // Again, let's connect to the database and output some recipes, if possible.
    $conn = db_connect();

    $recipeid = htmlspecialchars($_GET["recipe"]);
    // We need to fetch this entry!

    $pstmt = $conn->prepare("SELECT recipes.title, accounts.username, recipes.instructions, recipes.submitted_date FROM recipes LEFT JOIN accounts ON recipes.user_id=accounts.user_id WHERE recipe_id=:recipe_id");
    $result = $pstmt->execute([':recipe_id' => $recipeid]);
    
    if ($result) {
        $record = $pstmt->fetch();
        $date = strtotime($record['submitted_date']);
        echo '<span><h1>"' . $record['title'] . '"</h1> by ' . $record['username'] . '</span>';
        echo '</br><span><em>' . date("F j, Y", $date) . '</em></span>';
        echo '</br><p class="recipe">' . $record['instructions'] . '</p>';
    }
    ?>
    <div class="block"></div>
</div>
</body>
</html>