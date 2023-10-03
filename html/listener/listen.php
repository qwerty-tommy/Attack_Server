<?php
$pythonScript = 'listener.py';
$command = "python3 $pythonScript > /dev/null 2>&1 &"; // 파이썬 스크립트를 백그라운드로 실행
exec($command);

// "/"로 이동
header("Location: /");
exit;
?>

