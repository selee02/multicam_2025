import pandas as pd
import numpy as np
from gensim.models import Word2Vec
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, accuracy_score
from sklearn.feature_extraction.text import TfidfVectorizer
from konlpy.tag import Komoran
from sklearn.linear_model import LogisticRegression

def bulid_tokenize():
    try:
        # 라이브러리 로드 -> 라이브러리가 존재하면 코드를 실행
        from konlpy.tag import Komoran
        komoran = Komoran()
        allow_pos = ['NNP' ,'NNG', 'VV', 'VA', 'SL', 'MAG']
        def tokenize(text):
            tokens = []
            for word, pos in komoran.pos(text):
                if pos in allow_pos:
                    tokens.append(word)
            return tokens
        # tokenize 함수를 결과로 되돌려준다.
        return tokenize
    except Exception as e:
        print("Komoran 사용 불가 :", e)
        return lambda x : x.split()


def run_model(X, Y, test_size=0.2, model='svc'):
    # X는 독립변수
    # Y는 종속변수
    X_train, X_test, Y_train, Y_test = train_test_split(
        X, Y, test_size=test_size, random_state=42, stratify=Y
    )
    svc = SVC(random_state=42)
    logi = LogisticRegression(random_state=42)
    # 모델에 학습
    if model == 'svc':
        svc.fit(X_train, Y_train)
        # 학습된 모델에 예측 값
        y_pred = svc.predict(X_test)
        print("정확도 :", round(accuracy_score(Y_test, y_pred), 4))
        print("분류 레포트 :", classification_report(Y_test, y_pred))
    elif model == 'logistic':
        logi.fit(X_train, Y_train)
        # 학습된 모델에 예측 값
        y_pred = logi.predict(X_test)
        print("정확도 :", round(accuracy_score(Y_test, y_pred), 4))
        print("분류 레포트 :", classification_report(Y_test, y_pred))

def predict_sentence_list(sentences, model):
    # sentences : 문장들의 리스트
    # 문장들을 토큰화 -> 임베딩
    X_test = []
    for sent in sentences:
        # token() 함수를 호출하여 토큰화
        tokens = tokenize(sent)
        # 토큰화된 문장을 sent_embed_mean 함수에 입력하여 호출(단위 벡터의 평균)
        vec = sent_embed_mean(tokens)
        X_test.append(vec)
    
    preds = model.predict(X_test)
    result = []
    for sent, pred in zip(sentences, preds):
        label = '긍정' if pred == 1 else '부정'
        result.append([sent, label])
    return result