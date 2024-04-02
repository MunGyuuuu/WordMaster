import win32com.client as win32

def create_korean_file_from_hwp(file_path, output_file_path):
    hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")

    try:
        hwp.RegisterModule("FilePathCheckDLL", "SecurityModule")
        hwp.Open(file_path)
        hwp.InitScan(0)
        hwp.GetText()

        # 새로운 한글 파일 생성
        hwp.HAction.GetDefault("DocumentNew")
        hwp.HAction.Execute()

        # 표의 텍스트를 읽어옴
        table_count = hwp.GetTableCount()
        for table_index in range(table_count):
            hwp.MoveToTable(table_index)
            row_count = hwp.GetTableRowCount()
            # 각 행에 대해
            for row_index in range(row_count):
                # 한 행에 4열씩 있으므로 각 열을 읽어옴
                for col_index in range(0, hwp.GetTableColCount() - 1, 2):
                    # 영어 단어와 해당 단어의 한글 해석을 읽어와서 한글 파일에 추가
                    word = hwp.GetTextFromTable(table_index, row_index, col_index)
                    translation = hwp.GetTextFromTable(table_index, row_index, col_index + 1)
                    # 한글 파일에 단어와 해당 단어의 한글 해석 추가
                    if word and translation:
                        with open(output_file_path, 'a', encoding='utf-8') as output_file:
                            output_file.write(f"{word}: {translation}\n")

        return output_file_path

    finally:
        hwp.Quit()

# 테스트용 파일 경로와 생성할 한글 파일 경로
hwp_file_path = "C:\\Users\\CKIRUser\\Desktop\\새 폴더\\sample.hwp"
output_file_path = "C:\\Users\\CKIRUser\\Desktop\\새 폴더\\output_korean.txt"

# HWP 파일로부터 한글 파일 생성
create_korean_file_from_hwp(hwp_file_path, output_file_path)

# 생성된 한글 파일 경로 출력
print(f"한글 파일이 생성되었습니다: {output_file_path}")
