<?php
highlight_file("index.php");
// flag在环境变量$flag中

if (isset($_GET['file'])) {
    include_once($_GET['file']);
}

$content = $_GET['content'];
if (strpos($content, "php") === 0 || strpos($content, "php") || (!isset($content) && !isset($_GET['file']))) {
    die("byebye");
}

if (isset($content)) {
    $path = "/tmp/" . md5(time()) . ".txt";
    echo $path;
    file_put_contents($path, $content);
}

?>
byebye