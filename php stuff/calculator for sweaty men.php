
<!DOCTYPE html> 
<html> 
      
<head> 
    <title> 
        BEEEAAAAAANS
    </title>
    <link rel="icon" href="https://vignette2.wikia.nocookie.net/dayz-standalone/images/8/86/Canned_Baked_Beans_%28Open%29.png/revision/latest?cb=20150628022625">
</head> 
  
<body style="text-align:left"> 
      
    <h1 style="color:blue"> 
        Calculator for sweaty men
    </h1> 

    <form action="site.php" method="get">
        number: <input type="text" name="num1">
        <br>
        number: <input type="text" name="num2">
        <br>
        <br>
        <input type="submit" name="submit" value="calculate for me pls">
    </form>
    <br>

    <?php
        if (isset($_REQUEST['submit'])) {
            $num1 = $_GET["num1"];
            $num2 = $_GET["num2"];
            $resultMinusTwo = $num1 + $num2 - 2;

            echo "Answer: <b>$resultMinusTwo + 2</b>";
        }
    ?>
</body>
