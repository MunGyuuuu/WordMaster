import subprocess

def install_openpyxl():
    try:
        # pip 명령어를 통해 openpyxl 모듈 설치
        subprocess.run(['pip', 'install', 'openpyxl'], check=True)
        print("openpyxl 모듈 설치 완료!")
    except subprocess.CalledProcessError as e:
        # 명령어 실행 중 오류 발생 시 예외 처리
        print("openpyxl 모듈 설치 중 오류 발생:", e)

# openpyxl 모듈 설치 함수 호출
install_openpyxl()
