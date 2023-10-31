<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>XSS 연습</title>
</head>
<body>
    <h1>XSS 테스트 페이지</h1>
    <form method="GET" action="xss_test.php">
        <label for="input">텍스트 입력:</label>
        <input type="text" id="input" name="input" placeholder="여기에 텍스트를 입력하세요.">
        <button type="submit">제출</button>
    </form>

    <?php
    	setcookie("sessionID", "123456789", time() + 3600);

        if(isset($_GET['input'])) {
            echo $_GET['input'];
        }
    ?>
</body>
</html>
