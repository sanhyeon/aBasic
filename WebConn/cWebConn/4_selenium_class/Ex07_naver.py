import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from selenium import webdriver  # pip install selenium
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import re
import time
import selenium

selenium.__version__  # 4.3.0

path = './webdriver/chromedriver.exe'
source_url = "https://map.kakao.com/"
driver = webdriver.Chrome(path)
driver.get(source_url)
# id="search.keyword.query" 태그 선택=> input 태그
searchbox = driver.find_element(By.ID, "search.keyword.query")
searchbox.send_keys("가산디지털단지역 초밥")  # 강남역 고기집 값입력
# id="search.keyword.submit" 태그 선택=> input 태그
searchbutton = driver.find_element(By.ID, "search.keyword.submit")
# script를 실행
# arguments[0].click(); : 첫번째 매개변수값을 클릭
driver.execute_script("arguments[0].click();", searchbutton)  # 검색버튼클릭.
time.sleep(2)  # 2초동안 대기 => 강남역 고기집 검색 결과가 브라우저에 표시됨

html = driver.page_source  # 현재브라우저의 소스(html)
soup = BeautifulSoup(html, "html.parser")  # BeautifulSoup 분석
# name="a": a태그
# attrs={"class":"moreview" : a태그중에 class속성이 moreview인 태그
moreviews = soup.find_all(name="a", attrs={"class": "moreview"})  # 상세보기들
page_urls = []
for moreview in moreviews:
    # moreview: 한개의 상세보기. a태그
    page_url = moreview.get("href")  # a태그의 href 속성의 값
    page_urls.append(page_url)  # 상세보기의 href 속성값들 목록. 강남역 고기집의 URL 정보 목록
driver.close()
print(page_urls)
print(len(page_urls))

# 상세보기에 조회된 고기집 목록을 조회
columns = ['score', 'review']
df = pd.DataFrame(columns=columns)  # 컬럼만 조회
driver = webdriver.Chrome(path)  # 브라우저 실행

for page in page_urls:
    driver.get(page)  # 고기집 상세화면
    time.sleep(2)  # 2초 쉬기
    html = driver.page_source  # html 소스 데이터 (page 소스를 html에 세팅)
    soup = BeautifulSoup(html, 'html.parser')
    try:
        total_strong = soup.find(name="strong", attrs={"class": "total_evaluation"})
        tot_num = total_strong.find(name="span", attrs={"class": "color_b"})  # 등록된 리뷰 갯수
        contents_div = soup.find(name='div', attrs={"class": "evaluation_review"})  # 리뷰 영역. 별점, 내용
        rates = contents_div.find_all(name="em", attrs={"class": "num_rate"})  # 별점값 목록
        reviews = contents_div.find_all(name="p", attrs={"class": "txt_comment"})  # 리뷰 목록
    except:
        continue  # try 구문에서 오류 발생된 경우 다음 페이지로 이동

    # 리뷰의 1페이지 정보를 df에 저장
    for rate, review in zip(rates, reviews):  # (별점목록, 리뷰목록)
        row = [rate.text[0], review.find(name="span").text]
        series = pd.Series(row, index=df.columns)  # score, review 인덱스 설정. 시리즈 객체로 생성.
        df = df.append(series, ignore_index=True)

    # tot_num.text : 전체 등록된 리뷰의 건수. (ex.197건)
    page_num = int(tot_num.text) // 5 + 1  # 197 // 5 = 39.4
    for button_num in range(2, page_num + 1):  # 2페이지 ~ page_num 까지
        try:
            # 페이지 숫자의 테그
            another_reviews = driver.find_element("xpath", "//a[@data-page='" + str(button_num) + "']")
            another_reviews.click()  # 페이지 숫자 클릭
            time.sleep(2)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            contents_div = soup.find(name="div", attrs={"class": "evaluation_review"})
            rates = contents_div.find_all(name="em", attrs={"class": "num_rate"})  # 별점목록
            reviews = contents_div.find_all(name="p", attrs={"class": "txt_comment"})  # 리뷰목록

            for rate, review in zip(rates, reviews):
                row = [rate.text[0], review.find(name="span").text]
                series = pd.Series(row, index=df.columns)
                df = df.append(series, ignore_index=True)
        except:
            break
driver.close()

df.info()  # 719
df.head()

# 별점별 건수 조회하기
df["score"].value_counts(dropna=False)
# 별점 5,4 => 긍정(1)
# 별점 1,2,3 => 부정(0)
df["y"] = df["score"].apply(lambda x: 1 if float(x) > 3 else 0)
df["y"].value_counts()
df.info()
# df 데이터를 review_data.csv 파일로 저장하기
df.to_csv("data/review_data.csv", index=False)

# data/review_data.csv 읽어서 df에 저장하기
df = pd.read_csv("data/review_data.csv")
df.info()
df.head(10)


# 한글 부분만 리뷰에 남김.
def text_cleaning(text):
    '''
    [^ ㄱ-ㅣ가-힣]+
        [문자]+: 문자
        [^]: not
        공백ㄱ-ㅣ가-힣:, 공백, ㄱ~ㅣ(모음이)가~힣
    '''
    hangul = re.compile('[^ ㄱ-ㅣ가-힣]+')
    result = hangul.sub("", text)  # 정규식에 맞는 데이터를 반문자열로 치환
    return result  # 한글, 공백만 남김


text_cleaning("abc가나다123라마사아ㅋㅋ 123abc 암렁ds23asㅇㅈㄷ******()")
# 리뷰에서 한글과 공백만 남김.
df["ko_text"] = df["review"].apply(lambda x: text_cleaning(str(x)))
df.info()
df.head(10)
# ko_text 컬럼의 내용이 있는 경우만 df에 다시 저장하기
# strip(): 양쪽 문자열을 제거.
df = df[df["ko_text"].str.strip().str.len() > 0]
df.head(10)
# review 컬럼 제거
del df["review"]
df.info()

# 한글 형태소 분리하기
from konlpy.tag import Okt


def get_pos(x):
    okt = Okt()
    pos = okt.pos(x)  # 한글을 분석하여 형태소와 품사로 분리함수
    #    print(pos)
    # word: 형태소, t: 품사 => {0}/{1} 형태소/품사형태로 표시
    pos = ['{0}/{1}'.format(word, t) for word, t in pos]  # 컴프리헨선 방식으로 리스트 객체 생성
    return pos


result = get_pos(df["ko_text"].values[0])
result

# 글뭉치 변환하기
from sklearn.feature_extraction.text import CountVectorizer

# 안녕 나는 홍길동 이야.
#  1    2     3    4  => 인덱스화
# 반가워 나는 김삿갓 이야
#   5     2    6     4
index_vectorizer = CountVectorizer(tokenizer=lambda x: get_pos(x))
# df["ko_text"].tolist(): ko_text 컬럼의 값들을 리스트
X = index_vectorizer.fit_transform(df["ko_text"].tolist())
X.shape
for a in X[0]:
    print(a)
df.info()
print(str(index_vectorizer.vocabulary_)[:100] + "..")  # 100개 데이터만 조회
'''
    TfidfTransformer:
        TF-IDF (Term Frequency-Inverse Document Frequency)
            TF: 한 문장에 등장하는 빈도수
                예) 맛집 단어가 3번 등장 => TF의 값은 3
            IDF: 전체 문서에서 등장하는 단어의 빈도수의 역산
                예) 전체 문서에서 맛집이라는 단어가 10번 등장 => 1/10 = 0.1
            TF-IDF: 
                3 * 0.1 = 0.3
            => 전체 문서에서 많이 나타나지 않고, 현재 문장에서 많이 나타난다고 가정하면
                현재 문장에서 해당 단어의 중요성을 수치로 표현.
'''
from sklearn.feature_extraction.text import TfidfTransformer

tfidf_vectorizer = TfidfTransformer()
X = tfidf_vectorizer.fit_transform(X)
X.shape  # (587,3985) 578행, 3985열
print(X[0])
y = df["y"]
y

# 훈련데이터, 테스트데이터로 분리
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3)
x_train.shape
x_test.shape  # (177, 3985)
# 3985 피처 : 형태소 분석된 단어

# Logistic Regression 알고리즘을 이용하여 분류
from sklearn.linear_model import LogisticRegression

lr = LogisticRegression(random_state=0)
lr.fit(x_train, y_train)
y_pred = lr.predict(x_test)
y_pred[:10]  # 예측된 긍정부정
y_test.values[:10]  # 실제 긍정부정

# 각 피처별 가중치값 조회하기
lr.coef_[0]

# 가중치값을 그래프로 출력하기
plt.rcParams["figure.figsize"] = [10, 8]
plt.bar(range(len(lr.coef_[0])), lr.coef_[0])

# 긍정의 가중치 값 5개 : 가중치계수를 내림차순 정렬하여 최상위 5개 값
# index = lr.coef[0]의 인덱스
# value = lr.coef[0]의 가중치
# reverse=True : 내림차순정렬
# value 값의 내림차순으로 정렬
sorted(((value, index) for index, value in enumerate(lr.coef_[0])), reverse=True)[:5]
# 부정의 가중치 값 5개 : 가중치계수를 내림차순 정렬하여 최상위 5개 값
sorted(((value, index) for index, value in enumerate(lr.coef_[0])), reverse=False)[:5]
# 가중치계수의 내림차순정렬하여 마지막 5개값 조회
sorted(((value, index) for index, value in enumerate(lr.coef_[0])), reverse=True)[-5:]

# 회귀계수값으로 정렬하기
coef_pos_index = sorted(((value, index) for index, value in enumerate(lr.coef_[0])), reverse=True)
coef_pos_index[:10]
# index_vectorizer : 단어들을 인덱스와한 객체
# k : 형태소 값
# v : 형태소 번호. 인덱스
# invert_index_vectorizer : {인덱스:형태소값(단어)}
invert_index_vectorizer = {v: k for k, v in index_vectorizer.vocabulary_.items()}

cnt = 0
for k, v in index_vectorizer.vocabulary_.items():
    print(k, v)
    cnt += 1
    if cnt >= 10:
        break

# invert_index_vectorizer : {형태소번호(인덱스) : 형태소값(단어)} 딕셔너리객체
# 상위 20개의 긍정 형태소 출력
for coef in coef_pos_index[:20]:
    # coef[1] : 형태소 인덱스
    # coef[0] : 가중치계수. 회귀계수
    # invert_index_vectorizer[coef[1]] : 형태소인덱스에 해당되는 형태소(단어) 출력
    print(invert_index_vectorizer[coef[1]], coef[0])

# 하위 20개의 부정 형태소 출력
# coef_pos_index[-20:] : 가중치계수의 내림차순 정렬된 데이터의 마지막 20개 데이터.
#                        가중치계수가 작은 데이터 20개 조회
for coef in coef_pos_index[-20:]:
    # coef[1] : 형태소 인덱스
    # coef[0] : 가중치계수. 회귀계수
    # invert_index_vectorizer[coef[1]] : 형태소인덱스에 해당되는 형태소(단어) 출력
    print(invert_index_vectorizer[coef[1]], coef[0])

# 명사(Noun) 기준으로 긍적순의 단어 10개, 부정순의 10개의 단어 출력하기
noun_list = []
adj_list = []

for coef in coef_pos_index:
    category = invert_index_vectorizer[coef[1]].split("/")[1]
    if category == 'Noun':  # 명사
        noun_list.append((invert_index_vectorizer[coef[1]], coef[0]))
    if category == 'Adjective':  # 형용사
        adj_list.append((invert_index_vectorizer[coef[1]], coef[0]))

noun_list[:10]  # 긍정명서 10개
noun_list[-10:]  # 부정명사 10개

# 형용사(Adjective) 기준으로 긍적순의 단어 10개, 부정순의 10개의 단어 출력하기
adj_list[:10]  # 긍정명서 10개
adj_list[-10:]  # 부정명사 10개

# 평가하기
# 혼동행렬
from sklearn.metrics import confusion_matrix

confmat = confusion_matrix(y_test, y_pred)
confmat
# 정확도, 정밀도, 재현율, f1-score 조회하기
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

print("정확도", accuracy_score(y_test, y_pred))
print("정밀도", precision_score(y_test, y_pred))
print("재현율", recall_score(y_test, y_pred))
print("f1-score", f1_score(y_test, y_pred))
