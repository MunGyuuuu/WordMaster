from openpyxl import Workbook

# 새로운 워크북(엑셀 파일) 생성
workbook = Workbook()

# 활성 시트 선택
sheet = workbook.active

# 데이터 추가
words = ["apple", "banana", "cherry", "dog", "elephant", "fish", "grape",
         "horse", "ice cream", "jellyfish", "kite", "lemon", "monkey", 
         "noodle", "orange", "peach", "quilt", "rabbit", "strawberry", 
         "turtle", "umbrella", "violin", "watermelon", "xylophone", 
         "yacht", "zebra", "ant", "bird", "cat", "dog"]

# 엑셀 파일에 데이터 추가
for index, word in enumerate(words, start=1):
    sheet.cell(row=index, column=1, value=word)

# 엑셀 파일 저장
workbook.save(filename="words.xlsx")
print("엑셀 파일이 생성되었습니다.")
