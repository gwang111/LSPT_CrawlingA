<?php

const TAGS = array("chicken", "beef", "pasta", "spaghetti", "pork", "bacon", "vegan", "milk", "bread", "cooking", "cook", "baking", "bake", "snack", "dinner", "lunch", "breakfast", "brunch", "sandwich", "soup");
function get_tags(string $desc) {
    $ret = array();

    $possible = explode(" ", str_replace("\n", " ", $desc));

    foreach($possible as $p) {
        // Sanitize p
        $test = strtolower(trim($p, " \n\r\t\0\v.,/()"));
        // See if it is a tag
        if (in_array($test, TAGS)) {
            // Make sure it's unique, and add it!
            if (!in_array($test, $ret)) array_push($ret, $test);
        }
    }

    return $ret;
}

function add_tags(string $desc, int $recipe_id) {
    $tags = get_tags($desc);
    $conn = db_connect();
    $pstmt = $conn->prepare("INSERT INTO tags (recipe_id, tag)
                            VALUES(:recipe_id, :tag)");
    foreach($tags as $tag) {
        $result = $pstmt->execute([':recipe_id' => $recipe_id, ':tag' => $tag]);
        if (!$result) {
          echo '<div class="db-status error">Error inserting into database.</div>';
        }
    }
}

function db_connect() {
    $db = parse_ini_file("config.ini");
    $dbhost = $db['dbhost'];
    $dbname = $db['dbname'];
    $dbuser = $db['dbuser'];
    $dbpass = $db['dbpass'];
    $options = array(
        PDO::ATTR_ERRMODE => PDO::ERRMODE_EXCEPTION,
        PDO::ATTR_DEFAULT_FETCH_MODE => PDO::FETCH_ASSOC);
    return $dbconn = new PDO("mysql:host=$dbhost;dbname=$dbname", $dbuser, $dbpass, $options);
}

?>