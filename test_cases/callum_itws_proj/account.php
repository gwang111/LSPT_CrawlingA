<?php
include('includes/init.inc.php');
// All that's left is to add the title and any other head information,
// then close the head tag.
// We do also need to close the html tag at the very end.
    if (isset($_SESSION['user_id']) && isset($_SESSION['username'])) {
?>
<div class="content-body middle-align small-body">
    <?php
    include('includes/functions.inc.php');
    
    // Let's connect to the database and output some recipes, if possible.
    $conn = db_connect();

    // user input validation
    function validate($data) {
      $data = trim($data);
      $data = stripslashes($data);
      $data = htmlspecialchars($data);
      return $data;
    }

    if (isset($_POST["save"])) {
        // todo:: check inputs and double-check sanitization is sufficient
        $title = validate($_POST["title"]);
        $recipe = validate($_POST["recipe"]);

        $submitted_date = date('Y-m-d'); // This gives us the time as yyyy-mm-dd

        // This is where we try to submit!
        $pstmt = $conn->prepare("INSERT INTO recipes(title, instructions, user_id)
                                VALUES(:title, :instructions, :user_id)");
        $result = $pstmt->execute([':title' => $title, ':instructions' => nl2br($recipe), ':user_id' => $_SESSION['user_id']]);
        // // We first hard code the insert and prepare it with the database
        // $insert_query = "INSERT INTO recipes(`title`, `instructions`,`user_id`) VALUES(?,?,?,?)";
        // $insert_statement = $db->prepare($insert_query);

        if (!$result) {
            echo '<div class="db-status error">Error inserting into database.</div>';
        }
        else {
            echo '<div class="db-status">Added!</div>';
            $stmt = $conn->query("SELECT LAST_INSERT_ID()");
            $inserted_id = $stmt->fetch();
            // Now we should add the tags!
            add_tags($recipe, array_values($inserted_id)[0]);
        }
    }
    ?>

    <h1>Add a recipe:</h1>
    <form action="account.php" method="POST">
        <label for="title">Title:</label>
        <input type="text" size="60" name="title" id="title" /><br/>
        <br />
        <label for="recipe">Recipe:</label>
        <textarea type="text" rows="6" columns="160" name="recipe" id="recipe"></textarea>
        <br /><br />
        <input type="submit" value="save" id="save" name="save" />
    </form>
</div>
</body>

</html>

<?php 
}
else {
  session_start();
  header("Location: auth/login.php");
  exit();
}
?>
