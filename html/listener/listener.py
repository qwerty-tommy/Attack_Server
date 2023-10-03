import subprocess
from datetime import datetime

def start_netcat_listener(port, timeout_seconds):
    try:
        current_datetime = datetime.now()
        timestamp = current_datetime.strftime("%Y-%m-%d_%H-%M-%S")
        output_filename = f"/var/www/html/listener/result/{timestamp}"
        
        # nc 명령을 실행하고 타임아웃 설정
        process = subprocess.Popen(['nc', '-lvp', str(port)],
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE,
                                   universal_newlines=True,
                                   bufsize=1,
                                   preexec_fn=lambda: signal.alarm(timeout_seconds))
        
        # 데이터를 파일에 저장
        with open(output_filename, 'w') as output_file:
            for line in process.stdout:
                output_file.write(line)
                print(line, end='')  # 데이터를 터미널에 출력
        
        process.stdout.close()
        process.stderr.close()
        process.wait()
        
    except subprocess.CalledProcessError as e:
        print(f"오류 발생: {e}")
    except KeyboardInterrupt:
        print("사용자에 의해 중단되었습니다.")
    except TimeoutError:
        print(f"{timeout_seconds}초 동안 데이터가 수신되지 않아 타임아웃되었습니다.")
    finally:
        # 타임아웃 시그널을 해제
        signal.alarm(0)

import signal
port = 7000  # 사용할 포트를 지정하세요.
timeout_seconds = 30  # 타임아웃 시간 (초)
start_netcat_listener(port, timeout_seconds)
