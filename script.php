<?php

$estado=$_POST['valor_estado'];
switch ($estado) {
	case 1:
		shell_exec('sudo python /var/www/html/python/frente.py');
		break;
	case 2:
		echo exec('sudo python /var/www/html/python/esquerda.py');
		break;
	case 3:
		echo exec('sudo python /var/www/html/python/direita.py');
		break;
	case 4:
		echo exec('sudo python /var/www/html/python/re.py');
		break;
	case 44:
		echo exec('sudo python /var/www/html/python/ligarluz.py');
		break;
	case 45:
		echo exec('sudo python /var/www/html/python/desligarluz.py');
		break;
	case 0:
		echo exec('sudo python /var/www/html/python/panico.py');
		break;
	default:
		echo exec('sudo python /var/www/html/python/panico.py');
		break;
}


?>
