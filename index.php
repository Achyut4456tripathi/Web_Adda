<?php
    $server = "localhost";
    $username = "root";
    $password = "";

    $con = mysqli_connect($server,$username,$password);
    
    $name = $_POST['email'];
    echo $name ;

?>
