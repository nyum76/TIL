# Week5 : 앙상블학습
- 앙상블 학습 (Ensembel Learning)
    - 여러 개의 학습 모델을 결합해 하나의 모델을 만듬
    - 단일 모델보다 더 높은 예측 성능과 일반화 능력을 얻음
- 모든 모델 실습에 쓰일 공통 코드
```py
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeRegressor   # 의사결정 나무??-부스팅
from sklearn.metrics import mean_squared_error   # mse로 평가 -> 값이 0에 가까울수록 모델 성능 good
from sklearn.datasets import load_breast_cancer  # 유방암 데이터셋
from sklearn.model_selection import train_test_split   # 테스트와 트레이닝 데이터 나누기
from sklearn.preprocessing import StandardScaler    # 스케일링

# 유방암 데이터 로드
cancer_data = load_breast_cancer()
X, y = cancer_data.data, cancer_data.target

# 데이터 분할
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 데이터 스케일링
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```
## 배깅과 부스팅

### 배깅 
(Bootstrap Aggregating)
* 여러 개의 학습 모델 병렬 학습
* 예측 결과를 **평균 또는 다수결**로 결합
* 데이터 샘플링 과정에서 Bootstrap 기법을 사용해 원본 데이터셋에서 중복 허용한 무작위 샘플 생성
* 장점
  * 과적합 감소
  * 안정성 향상
  * 병렬 처리 가능 : 여러 개의 학습 모델을 병렬로 학습시킴


### 부스팅
(Boosting)
* **여러 개의 약한 학습기**를 **순차척**으로 학습 → 예측 결과를 결합해 **강한 학습기**로 만듬
* 이전 모델이 잘못 예측한 데이터 포인트에 가중치를 부여해 다음 모델 보완
* 장점
  * 높은 예측 성능
  * 과적합 방지
  * 순차적 학습

## 랜덤 포레스트

(Random Forest)
: 의사결정 트리를 앙상블학습으로 개선한 것
* 배깅 기법을 기반으로 한 앙상블 학습 모델
* 여러 개의 결정트리를 학습시킴, 그 예측 결과를 결합해 최종 예측 수행
* 장점 : 각 트리 독립적 학습
  - 과적합 방지
  - 다형성 증가
  - 높은 예측 정확성
  - 변수에 중요도 평가를 할 수 있음
  - 해석이 쉬운 모델


## 그래디언트 부스팅 머신 (GBM)
: 랜덤 포레스트 모델 대신 사용할 수 있음
* 결정 트리를 부스팅 기법으로 만들어낸 모델
* 기존 모델이 만든 오차를 다음모델이 개선하도록 미분 사용



## **XGBoost** : 성능 GOOD!!!!
 (eXtreme Gradient Boosting)
 : 그래디언트 부스팅 알고리즘을 기반으로 한 고성능 앙상블 학습 기법
 * 최적화 단계가 이미 포함됨
 * 장점
   * 병렬처리 : 학습 속도 향상
    * 조기 종료 : 데이터셋 성능이 향상되지 않을 때 학습 조기 종료 가능. 과적합 방지
    * 정규화 : 과적합 방지
    * 유연성

---
### 정리


* 앙상블학습 : 여러 개의 학습 모델 결합 -> 하나의 강력한 모델
  * 베깅 : 여러 개의 학습 모델 병렬 학습-> 평균 또는 다수결 결합
    * 랜덤 포레스트
  * 부스팅 : 여러 개의 약한 학습기를 순차적 학습 -> 결과 결합해 강한 학습기 만들기
    * 그래디언트 부스팅 머신(GBM)
    * XGBoost

: XGBoost가 성능이 좋다고 모든 상황에서 쓰는게 좋은 것은 아니고 각 모델마다 사용하기 좋은 상황이 있음!
