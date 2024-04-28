# -*- coding: utf-8 -*-
import os
from openai import OpenAI
import pdfplumber
from dotenv import load_dotenv, find_dotenv
import prompts
import win32com.client as win32
import re

_ = load_dotenv(find_dotenv())
client = OpenAI(
    api_key=os.environ.get('OPENAI_API_KEY'),
)

model = "gpt-4-turbo-preview"
temperature = 0.2

# 섹션별 텍스트 추출 함수
def extract_section(text, start_pattern, end_pattern=None):
    start_match = re.search(start_pattern, text, re.IGNORECASE)
    if not start_match:
        return ""  # 시작 패턴이 없으면 빈 문자열 반환
    
    start_index = start_match.end()
    if end_pattern:
        end_match = re.search(end_pattern, text[start_index:], re.IGNORECASE)
        if end_match:
            return text[start_index:start_index + end_match.start()]
    
    return text[start_index:]  # 끝 패턴이 없다면, 문서 끝까지 반환

# helper function
def get_summary():
    completion = client.chat.completions.create(
        model = model,
        messages = messages,
        temperature = temperature,
    )
    return completion.choices[0].message.content

# PDF 파일에서 텍스트 추출
with pdfplumber.open("Analyzing Higher Education Instructors perception on Metaverse based Education.pdf") as pdf:
    full_text = ""
    for page in pdf.pages:
        page_text = page.extract_text()
        if page_text:  # 텍스트가 있는 경우에만 추가
            full_text += page_text

# 챗GPT에 요약 요청
system_message = prompts.Title_to_Methodology
prompt = full_text

messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
]

summarized_text = get_summary()
# 각 섹션별로 추출
Title = extract_section(summarized_text, r"1\. Title:\s*", r"2\. Citation:\s*")
Citation = extract_section(summarized_text, r"2\. Citation:\s*", r"3\. Abstract:\s*")
Abstract = extract_section(summarized_text, r"3\. Abstract:\s*", r"4\. Introduction:\s*")
Introduction = extract_section(summarized_text, r"4\. Introduction:\s*", r"5\. Methodology:\s*")
Methodology = extract_section(summarized_text, r"5\. Methodology:\s*", r"6\. Results:\s*")

system_message = prompts.Result_and_Conclusion
prompt = full_text
messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": prompt}
]

summarized_text = get_summary()

Results = extract_section(summarized_text, r"6\. Results:\s*", r"7\. Conclusion:\s*")
Conclusion = extract_section(summarized_text, r"7\. Conclusion:\s*")


#한글 양식에 입력
hwp = win32.gencache.EnsureDispatch("HWPFrame.HwpObject")
hwp.Open(r"D:\ResearchPaperRPA\논문 분석 양식.hwp")
hwp.PutFieldText("논문제목", Title)
hwp.PutFieldText("인용", Citation)
hwp.PutFieldText("요약", Abstract)
hwp.PutFieldText("서론", Introduction)
hwp.PutFieldText("연구방법", Methodology)
hwp.PutFieldText("연구결과", Results)
hwp.PutFieldText("결론", Conclusion)
hwp.SaveAs(r"D:\ResearchPaperRPA\논문 분석 테스트.hwp")
hwp.Quit()

#print(summarized_text)