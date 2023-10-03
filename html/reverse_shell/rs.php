<?php
$filename = 'shell/p0wny-shell.php';    //b374kmini.phar
?>
<!DOCTYPE html>
<html>
<head>
    <title>Raw Data - <?php echo $filename?></title>
</head>
<body>
    <pre>
<?php

if (file_exists($filename)) {
    echo htmlspecialchars(file_get_contents($filename));
} else {
    echo "Err";
}
?>
    </pre>
</body>
</html>