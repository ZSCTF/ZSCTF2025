<?php
error_reporting(0);
highlight_file(__FILE__);
include("zsctfflag.php");

function filter($num){
    $num=str_replace("0x","1",$num);
    $num=str_replace("0","1",$num);
    $num=str_replace(".","1",$num);
    $num=str_replace("e","1",$num);
    $num=str_replace("+","1",$num);

    return $num;
}
function ordArrayToString($str) {
    $result = '';
    $i = 0;
    while ($i < strlen($str)) {
        $num = intval(substr($str, $i, 2));
        if ($num >= 32 && $num <= 126) {
            $result .= chr($num);
            $i += 2;
        } else {
            $num = intval(substr($str, $i, 3));
            $result .= chr($num);
            $i += 3;
        }
    }
    return $result;
}

$num=$_GET['Z_S_C.T.F'];
$c=$_GET['Z_S_C_T_F'];
if(is_numeric($num) and $num!=='66' and trim($num)!=='66' and filter($num)=='66'){

    $res=ordArrayToString($c);
    eval($res);
    echo "yes1";

}else{
    echo "hacker!!!";
}