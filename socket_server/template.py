# 定义网页
base_html = """<!DOCTYPE html>
<html>
<head> <title>ESP32 Web Server</title> </head>
<body>
    <h1>ESP32 Web Server</h1>
    <button onclick="forward()">Forward</button>
    <button onclick="backward()">Backward</button>
    <button onclick="left()">Left</button>
    <button onclick="right()">Right</button>
    <button onclick="turnLeft()">Turn Left</button>
    <button onclick="turnRight()">Turn Right</button>
    <button onclick="stop()">Stop</button>
    <script>
        function forward() {
            fetch('/forward');
        }
        function backward() {
            fetch('/backward');
        }
        function left() {
            fetch('/left');
        }
        function right() {
            fetch('/right');
        }
        function turnLeft() {
            fetch('/turnleft');
        }
        function turnRight() {
            fetch('/turnright');
        }
        function stop() {
            fetch('/stop');
        }
    </script>
</body>
</html>
"""