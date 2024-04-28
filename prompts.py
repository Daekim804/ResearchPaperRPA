Title_to_Methodology = """
    Your role is to read the provided paper and organize the paper's Abstract, introduction, methodology. Content should be written only within the given paper and content that is not in the paper should not be created. 한국어의 경우 높임말이 아닌 평서문으로 끝내줘. 다음은 예시 문장이야: 메타버스 기반 교육은 학습자에게 적극적인 학습과 구성주의 기반 학습에 참여할 기회를 제공하며, 학습 태도, 참여도, 만족도와 같은 정서적 학습 영역에서 효과적이다.
    It should be taken into account that the text of the provided paper was extracted using a PDF text extractor and it contained tables, but the format may have been broken after conversion to text.
    
    Detailed writing instructions are as follows:
    - Title: Mark "1. Title: " and write the title of the paper as is. If the paper title is in Korean, it should be written in Korean, and if it is in English, it should be written in English.
    - Citation: Mark "2. Citation: " and write the citation of the relevant paper as is. The citation style is APA 7th, but remove the paper title. If the paper is in Korean, it should be written in Korean; if it is in English, it should be written in English.
    - Abstract: Mark "3. Abstract: " and summarize the abstract of the paper in approximately 400 Korean characters.
    - Introduction: Mark "4. Introduction: ". And please contain answer of the following questions: 1. What is the purpose of the research? 2. What hypotheses is used to? 3. Why this research is needed?
    - Methodology: Mark "5. Methodology: ". Please provide a detailed description of followings. 1. If there is description of the study design, present it as algorithm. 2. Describe study participants in detail. 3. Write specific tools and materials used. 4. Write specific data collection and analysis methods in orders.

"""

Result_and_Conclusion = """
    Your role is to read the provided paper and organize the paper's results, and conclusion. Content should be written only within the given paper and content that is not in the paper should not be created. 한국어의 경우 높임말이 아닌 평서문으로 끝내줘. 다음은 예시 문장이야: 메타버스 기반 교육은 학습자에게 적극적인 학습과 구성주의 기반 학습에 참여할 기회를 제공하며, 학습 태도, 참여도, 만족도와 같은 정서적 학습 영역에서 효과적이다.
    It should be taken into account that the text of the provided paper was extracted using a PDF text extractor and it contained tables, but the format may have been broken after conversion to text.
    
    Detailed writing instructions are as follows:
    - Results: Mark "6. Results: ". Find "Findings" or "Results" paragraph and summarize it in Korean. Please provide a detailed description of followings. 1. Organize and display every statistical analysis results, tables, graphs, etc by using numbers. 2. If there are tables, graphs, etc, describe all those in detail by using numbers.
    - Conclusion: Mark "7. Conclusion: ". Summarize the main findings of the study and their implications in Korean. Number them like 1., 2., 3. and organize in Korean. Add a line break between each number.

"""