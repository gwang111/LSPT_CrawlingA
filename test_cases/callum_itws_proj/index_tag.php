<?php
    $tag = isset($_GET["tag"]);
    if (!$tag) {
        header('Location: ./index.php', true, 302);
        die();
    }
    include("includes/init.inc.php");
    include('includes/functions.inc.php');
?>
<div class="content-body">
    <div class="content-title">
        <div><h1>Best Greatest Yummiest Delicious Cooking Website (Ever!)</h1></div>
        <div>
          <span>Search by tag:</span> 
          <form action="index_tag.php" method="GET">
              <input type="text" id="tag" name="tag" placeholder="Enter a tag here">
              <button type="submit" id="submit">Submit</button>
          </form>
        </div>
    </div>
    
    <table class="recipes-table">
        <tbody>
            <tr>
                <?php
                // Let's connect to the database and output some recipes, if possible.
                $conn = db_connect();
                
                $pstmt = $conn->prepare("SELECT recipes.title, accounts.username, recipes.submitted_date, recipes.recipe_id FROM recipes LEFT JOIN accounts ON recipes.user_id=accounts.user_id LEFT JOIN tags ON recipes.recipe_id=tags.recipe_id WHERE tag = :tag");
                $result = $pstmt->execute([':tag' => $_GET["tag"]]);

                $rows = $pstmt->fetchAll();

                $row_num = count($rows);
                for ($i = 0; $i < $row_num; $i++) {
                    $record = $rows[$i];

                    echo '<td><div><a href="./recipe.php?recipe=';
                    echo htmlspecialchars($record['recipe_id']) . '">';
                    echo '<h1>' . htmlspecialchars($record['title']) . '</h1>';
                    echo '<span>' . htmlspecialchars($record['username']) . "</span></a></div></td>\n";

                    if ($i % 3 == 2) {
                        echo "</tr><tr>\n";
                    }
                }
                ?>
            </tr>
        </tbody>
    </table>
    <?php
    echo '<div class="body-end-text">You\'ve scrolled past <strong>' . $row_num . '</strong> recipes and haven\'t found the one for you!?</div>';
    ?>

    <div class="block"></div>
</div>
</body>
</html>
