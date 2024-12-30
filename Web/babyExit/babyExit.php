<?php
error_reporting(0);
include 'flag.php';
highlight_file(__FILE__);


if (!$_COOKIE['admin']) {
    exit("\nNot authenticated.\n");
}

if (!preg_match('/^{"hash": [\w\"]+}$/', $_COOKIE['admin'])){
    exit("还看不懂正则表达式? 还不快去百度! \n");
}
$session_data = json_decode($_COOKIE['admin'], true);

if ($session_data['hash'] != strtoupper(MD5($flag))) {
    echo("给你个提示吧 \n");
    for ($i = 0; $i < 32; $i++) {
        echo(ord(MD5($flag)[$i]) >> 6);
    }
    exit("\n");
}

class WHUCTF {
    protected $stu;

    function __construct() {
        $this->stu = new Study();
    }
 
    function __destruct() {
        $this->stu->action();
    }
}
 
class Study {
    function action() {
        echo "CTF 真好玩~";
    }
}
 
class Evil {
    function action() {
        system('cat ./flag.php');
    }
}

echo "这么明显了,你懂我意思吧";
unserialize($_GET['whuctf']);
Not authenticated.