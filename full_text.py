# -*- coding: utf-8 -*-
import pdfplumber

with pdfplumber.open("마인크래프트를 활용한 메타버스 기반 프로그래밍 수업이 학습정서와 학습동기, 학습몰입도에 미치는 영향.pdf") as pdf:
    full_text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:  # 텍스트가 있는 경우에만 추가
            full_text += page_text

# 줄바꿈 제거
full_text = full_text.replace('\n', '')

# full_text를 'output.txt' 파일로 저장
with open('full_text.txt', 'w', encoding='utf-8') as file:
    file.write(full_text)

print("파일이 저장되었습니다.")
