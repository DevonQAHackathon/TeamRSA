<html>
<head>
  <meta charset="UTF-8">
  <title>Weather API Testing : TeamRSA</title>  
  
      <link rel="stylesheet" href="css/style.css">
  
</head>
<body>
<script src='http://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.3/jquery.min.js'></script>

<script src="js/index.js"></script>
<?php

$city_from = $_POST["From"];
$city_to= $_POST["To"];
$travel_date = $_POST["date"];

$url_from = 
$response_from = file_get_contents('http://api.openweathermap.org/data/2.5/weather?q='.$city_from.'&appid=1e094d4150bb132956c6ad7367ca8b9c');
$response_To = file_get_contents('http://api.openweathermap.org/data/2.5/weather?q='.$city_to.'&appid=1e094d4150bb132956c6ad7367ca8b9c');

$response_currency = "";
$from_cur = "";

$from_value= "";
$to_value = "";
$json = json_decode($response_from, true);
	
	$path = "";
	foreach ($json as $key => $value)
	{
		
		$from_key = $key;
		if ( strcasecmp( $key, 'main' ) == 0 )
		 {
		 	$from_value = implode(":",$value);		 	
		 }	
		 if(strcasecmp( $key, 'sys' ) == 0)
		 {
		 	$from_cur = implode(":",$value);
		 }
	}	
	$from_city_cur = explode(":",$from_cur);
	
	
$json = json_decode($response_To, true);
	
	$path = "";
	foreach ($json as $key => $value)
	{
		
		$from_key = $key;
		if ( strcasecmp( $key, 'main' ) == 0 )
		 {
		 	$to_value = implode(":",$value);
		 	
		 }	
		 if(strcasecmp( $key, 'sys' ) == 0)
		 {
		 	$to_cur = implode(":",$value);
		 }

	}	
	$to_city_cur = explode(":",$to_cur);

$from_city_value = explode(":", $from_value);
$to_city_value = explode(":", $to_value);
$from_temp = (float)$from_city_value[0];
$to_temp = (float)$to_city_value[0];

$comment = "";
if($from_temp > $to_temp)
{
	$comment = "Your are going to cooler place.  \n Please Carry Warm Cloths";
}
else if ($from_temp == $to_temp)
{
	$comment = "You are a tester";
}
else
{
	$comment = "Your are going to warmer place.  \n Please Carry Sunscream lotion";
}

echo 
<<<MYTAG

<table class="responstable" id = "city_table">  
  <tr>
    <th>City</th>    
    <th>Temperature</th>
    <th>Humidity</th>
    <th>Min_Temp</th>
    <th>Max_Temp</th>   
  </tr>  
  <tr>    
    <td>$city_from</td>
    <td>$from_city_value[0]</td>
    <td>$from_city_value[1]</td>
    <td>$from_city_value[2]</td>
    <td>$from_city_value[3]</td>
  </tr>
  <tr>    
    <td>$city_to</td>
    <td>$to_city_value[0]</td>
    <td>$to_city_value[1]</td>
    <td>$to_city_value[2]</td>
    <td>$to_city_value[3]</td>
  </tr>   
  </table>

  <table class="responstable">
  <tr>
  <th>$comment</th>  
  <tr>
  </table>  
MYTAG;
?>
</body>
</html>
