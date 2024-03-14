from openpyxl import Workbook

# 엑셀 파일을 생성할 횟수
num_files = 10

# 파일을 생성할 반복문
for i in range(1, num_files+1):
    # Workbook 객체 생성
    wb = Workbook()
    
    # 파일명 설정
    file_name = f"output_{i}.xlsx"
    
    # Workbook을 엑셀 파일로 저장
    wb.save(file_name)
    
    print(f"{file_name} 생성 완료.")
