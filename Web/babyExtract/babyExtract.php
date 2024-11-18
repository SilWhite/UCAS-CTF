<?php
header("Content-Type: text/html; charset=UTF-8");
error_reporting(0);
include("flag.php");
$b = 'ssAEDsssss';
extract($_GET);
if (isset($a)) {
    $c = trim(file_get_contents($b));
    if ($a == $c) {
        echo $myFlag;
    } else {
        echo "Wrong password!";
    }
}
?>