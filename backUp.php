<?php

$command = escapeshellcmd('BackUp.py');
$output = shell_exec($command);
echo $output;

?>