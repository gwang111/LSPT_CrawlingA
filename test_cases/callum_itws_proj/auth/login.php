<?php include("../includes/initsub.inc.php"); ?>
<div class="about-us-content-body content-body middle-align">
  <h4>Please log in</h4>
  <form action="db.php" method="post">
    <?php if (isset($_GET['error'])) { ?>
      <p class="error"><?php echo $_GET['error']; ?></p>
    <?php } ?>
    <input type="text" name="username" placeholder="Username"><br />
    <input type="password" name="password" placeholder="Password"><br />
    <button name="login" type="submit">Login</button>
  </form>
  <p>
    <a href="register.php">Or, register here</a>
  </p>
</div>
</body>
</html>