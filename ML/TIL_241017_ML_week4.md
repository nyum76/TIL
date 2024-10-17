# Week4 : 비지도학습
* 비지도학습
  * 지도학습과는 달리 정답데이터가 없음
  * 데이터를 보고 군집화 (유사한 데이터끼리 묶는 것)
* 실습을 위해 사용할 파일 : kaggle "Mall_Customers.csv"
------
## 군집화모델

### K-means clustering
: 데이터를 그림으로 표현했을 때, 가까운 데이터끼리 묶는 것
* 알고리즘 단계
  * k 설정 : 데이터를 k개의 그룹으로 묶음
  * 할당 안 된 데이터들을 가장 가까운 군집중심에 할당
  * 할당되어 합쳐지면서 군집 중심이 바뀌고, 군집중심에 더 이상 변화가 없을 때까지 반복
* 거리 측정 방법
  * 유클리드 거리(일반적인 거리 측정법)
* 엘보우 방법
  * 최적의 k를 선택하기 위해 사용
  * k 가 증가하면 그룹 내의 거리가 줄어듬 -> 더 이상 거리가 의미있게 감소하지 않는 구간을 찾는 방법

* 실습
```py
  # 데이터 로드 및 전처리
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler    # 데이터의 평균을 0, 분산을 1로 스케일링
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns

# 데이터 로드
data = pd.read_csv('Mall_Customers.csv')

# 필요한 열 선택 및 결측값 처리
data = data[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# 데이터 스케일링 : 데이터의 평균을 0, 분산을 1로 스케일링
scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)    # fit_transform(data) : 데이터세트를 스케일링하고 변환
  
```
```py
# 모델 학습 및 군집화
# 최적의 k 찾기 (엘보우 방법)
inertia = []
K = range(1, 11)
for k in K:
    kmeans = KMeans(n_clusters=k, random_state=42)    # k-means 군집화 모델 생성 (n_cluster=k : 군집 수 설정, random_state : 랜덤 시드 값, 결과 재현성)
    kmeans.fit(data_scaled)                           # fit(data_scaled) : 데이터를 학습하여 군집 생성
    inertia.append(kmeans.inertia_)

# 엘보우 그래프 그리기
plt.figure(figsize=(10, 8))
plt.plot(K, inertia, 'bx-')
plt.xlabel('k')
plt.ylabel('Inertia')
plt.title('Elbow Method For Optimal k')
plt.show()

# k=5로 모델 생성 및 학습
kmeans = KMeans(n_clusters=5, random_state=42)
kmeans.fit(data_scaled)

# 군집 결과 할당
data['Cluster'] = kmeans.labels_    # labels_ : 각 데이터 포인트가 속한 군집 레이블 반환
```
![elbow_graph](/ML/pic/elbow_graph.png)
```py
# 군집 시각화
# 2차원으로 군집 시각화 (연령 vs 소득)
plt.figure(figsize=(10, 8))
sns.scatterplot(x=data['Age'], y=data['Annual Income (k$)'], hue=data['Cluster'], palette='viridis') 
plt.title('Clusters of customers (Age vs Annual Income)')
plt.show()

# 2차원으로 군집 시각화 (소득 vs 지출 점수)
plt.figure(figsize=(10, 8))
# sns.scatterplot : 산점도를 그림. (x: x축 데이터, y: y축 데이터, hue: 색상에 따라 군집 구분, palette : 색상 팔레트 설정 )
sns.scatterplot(x=data['Annual Income (k$)'], y=data['Spending Score (1-100)'], hue=data['Cluster'], palette='viridis') 
plt.title('Clusters of customers (Annual Income vs Spending Score)')
plt.show()
```
![](/ML/pic/scatterplot.png)
![](/ML/pic/scatterplot2.png)
### 계층적 군집화 (Hierarchical Clustering)
: 데이터포인트를 점진적으로 병합 or 분할해 군집 형성
* 거리 행렬 만듬 ( 데이터 포인트 간의 거리 계산한 값 )
- 병합 군집화 (Agglomerative Clustering) : 가장 가까운 군집 병합 → m개의 군집에서 최종적으로 군집이 1개가 됨
- 분할 군집화 (Divisive Clustering) : 가장 멀리 떨어진 데이터 분할 → 1개의 군집에서 m개의 군집이 됨
* 실습
```py
## 계층적 군집화

# 데이터 로드 및 전처리
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering
import scipy.cluster.hierarchy as sch

# 데이터셋 불러오기
df = pd.read_csv('Mall_Customers.csv')


# 데이터 확인
print(df.head())

# 필요한 열만 선택
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# 데이터 정규화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
![](/ML/pic/print(df.head()).png)
```py
# 덴드로그램 생성
plt.figure(figsize=(10, 7))
dendrogram = sch.dendrogram(sch.linkage(X_scaled, method='ward'))
plt.title('Dendrogram')
plt.xlabel('Customers')
plt.ylabel('Euclidean distances')
plt.show()
```
![](/ML/pic/Hierarchical_dendrogram.png)
```py
# 계층적 군집화 모델 생성
hc = AgglomerativeClustering(n_clusters=5, metric='euclidean', linkage='ward')

# 모델 학습 및 예측
y_hc = hc.fit_predict(X_scaled)

# 결과 시각화
plt.figure(figsize=(10, 7))
plt.scatter(X_scaled[y_hc == 0, 0], X_scaled[y_hc == 0, 1], s=100, c='red', label='Cluster 1')
plt.scatter(X_scaled[y_hc == 1, 0], X_scaled[y_hc == 1, 1], s=100, c='blue', label='Cluster 2')
plt.scatter(X_scaled[y_hc == 2, 0], X_scaled[y_hc == 2, 1], s=100, c='green', label='Cluster 3')
plt.scatter(X_scaled[y_hc == 3, 0], X_scaled[y_hc == 3, 1], s=100, c='cyan', label='Cluster 4')
plt.scatter(X_scaled[y_hc == 4, 0], X_scaled[y_hc == 4, 1], s=100, c='magenta', label='Cluster 5')
plt.title('Clusters of customers')
plt.xlabel('Age')
plt.ylabel('Annual Income (k$)')
plt.legend()
plt.show()
```
![](/ML/pic/Hierarchical.png)
```py
from sklearn.metrics import silhouette_score

# 실루엣 점수 계산
silhouette_avg = silhouette_score(X_scaled, y_hc)
print(f'Silhouette Score: {silhouette_avg}')
```
![](/ML/pic/Hierarchical_score.png)
### DBSCAN 
( Density-Based Spatial Clustering of Applications with Noise)
* 장점 
  * 이전의 군집화 모델들과 비교했을 때, 군집의 형태가 원형일 필요가 없음
  * 군집 수를 정할 필요 없음
  * 노이즈 효과적 처리
* 단점
  * 밀도가 낮을수록, 군집화 어려움
* 용어
  * eps : 거리
  * min_samples : 하나의 군집을 형성하기 위해 필요한 최소 데이터 포인트 수
  * 노이즈포인트 : 코어나 경계 포인트가 아닌 포인트(외톨이)
* 실습
```py
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler

# 데이터셋 불러오기
df = pd.read_csv('Mall_Customers.csv')


# 데이터 확인
print(df.head())

# 필요한 열만 선택
X = df[['Age', 'Annual Income (k$)', 'Spending Score (1-100)']]

# 데이터 정규화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
![](/ML/pic/print(df.head()).png)
```py
# Scikit-learn의 DBSCAN을 사용하여 DBSCAN 군집화 수행
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
import seaborn as sns

# DBSCAN 모델 생성
dbscan = DBSCAN(eps=5, min_samples=5)

# 모델 학습 및 예측
df['Cluster'] = dbscan.fit_predict(X)

# 군집화 결과 시각화
plt.figure(figsize=(10, 7))
sns.scatterplot(x='Annual Income (k$)', y='Spending Score (1-100)', hue='Cluster', data=df, palette='viridis')
plt.title('DBSCAN Clustering of Mall Customers')
plt.show()
```
![](/ML/pic/DBSCAN_clustering.png)


------
## 차원축소
: 데이터를 줄여줌
* 예시
  * column 이 30개 있는 table 은 30차원이라고 함
  * 차원축소로 이 차원을 낮춰줌 (30차원 ->20차원...)
  * 같은 내용인데 축소된 차원으로 모델 학습시 계산량이 줄어 효율이 증가
* 목적
  * n 차원의 데이터를 n 보다 작은 m 차원의 데이터로 바꿈
  * 이 데이터의 표현력 (추론할 수 있는 데이터)은 그대로 유지
### PCA
- 과정
    - 데이터 중심화 : 표준을 빼서 데이터의 평균을 0으로 맞춤 (스케일링과 유사)
    - 공분산 행렬 계산 : 각 특징 간 얼마나 같이 움직이는지 (데이터의 분포를 봄)
    - 고유값과 고유 벡터 계산 : 데이터가 얼마나 분산되었는지 설명, 고유벡터는 방향 나타냄 *(얘네는 통계학을 공부해야 알 수 있음 )*
    - 주성분 선택 : 고유 값이 큰 순서대로 고유 벡터를 찾고 상위의 고유 벡터를 선택해 주성분을 만듬
    - 선택된 고유 벡터는 새 좌표(하나의 컬럼)가 됨
    - 원본 데이터를 주성분 축으로 변환해 차원 축소 ( 중요한 정보 유지, 불필요한 정보 제거 )

* 실습
```py
# PCA 로 실습

# 데이터 로드
from sklearn.datasets import fetch_openml
import pandas as pd

# MNIST 데이터셋 불러오기
mnist = fetch_openml('mnist_784', version=1)

# 데이터와 레이블 분리
X = mnist.data
y = mnist.target

# 데이터 프레임의 첫 5행 출력
print(X.head())
print(y.head())
```
![](/ML/pic/MNIST_dataset.png)
```py
from sklearn.preprocessing import StandardScaler

# 데이터 표준화
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)
```
```py
# PCA 수행
from sklearn.decomposition import PCA

# PCA 모델 생성
pca = PCA(n_components=0.95)  # 전체 분산의 95%를 설명하는 주성분 선택

# PCA 학습 및 변환
X_pca = pca.fit_transform(X_scaled)

# 변환된 데이터의 크기 확인
print(X_pca.shape)
```
```py
# 선택된 주성분의 수
print(f'선택된 주성분의 수: {pca.n_components_}')

# 각 주성분이 설명하는 분산 비율
print(f'각 주성분이 설명하는 분산 비율: {pca.explained_variance_ratio_}')

# 누적 분산 비율
print(f'누적 분산 비율: {pca.explained_variance_ratio_.cumsum()}')
```


```py
import matplotlib.pyplot as plt
import seaborn as sns

# 2차원 시각화
plt.figure(figsize=(10, 7))
sns.scatterplot(x=X_pca[:, 0], y=X_pca[:, 1], hue=y, palette='viridis', legend=None)
plt.title('PCA of MNIST Dataset (2D)')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()
```
![](/ML/pic/PCA.png)
### t - SNE
(t - Distributed Stochastic Neighbor Embedding)
- 통계적 기법을 통해 고차원 데이터를 저차원으로 변환하여 시각화
- 데이터의 구조, 패턴을 시각적으로 이해
- 작동원리
    - 고차원에서 갖는 데이터의 관계가 저차원에서도 유지되도록 데이터를 저차원으로 바꿈
- 장점
    - 데이터의 구조와 패턴을 쉽게 이해
    - 비선형구조 탐지 가능
    - 데이터 포인터간의 지역적 유사성 보존
    - 다양한 데이터 유형 처리
- 단점
    - 데이터셋이 클 경우 계산 시간이 오래걸림
    - 매개변수를 설정해야 함
    - 결과 해석이 어려움
* 실습 !!***MNIST 데이터셋 로드와 표준화 코드는 같으므로 생략***
```py
# T-SNE 수행
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt
import seaborn as sns

# t-SNE 모델 생성
tsne = TSNE(n_components=2, random_state=42)

# t-SNE 학습 및 변환
X_tsne = tsne.fit_transform(X_scaled)

# 변환된 데이터의 크기 확인
print(X_tsne.shape)


# 시각화

# 2차원 시각화
plt.figure(figsize=(10, 7))
sns.scatterplot(x=X_tsne[:, 0], y=X_tsne[:, 1], hue=y, palette='viridis', legend=None)
plt.title('t-SNE of MNIST Dataset (2D)')
plt.xlabel('t-SNE Component 1')
plt.ylabel('t-SNE Component 2')
plt.show()
```
![](/ML/pic/t-SNE.png)
### LDA
* 차원 축소와 분류를 동시에 수행
* 데이터간 클래스 분산 최대화, 클래스 내 분산 최소화
- 장점
  - 데이터의 주요 특성 유지하며 데이터를 저차원공간에 효율적으로 표시
  - 분류 문제에서 성능 향상, 클래스 간의 데이터가 차이 날 때 좋음
- 단점
  - 데이터가 비선형인 경우 성능이 떨어짐
  - 클래스가 가정에 부합하지 않을 경우 성능이 떨어짐
  - 잡음에 민감
  - 많은 데이터 필요
* 실습 !!***MNIST 데이터셋 로드와 표준화 코드는 같으므로 생략***
```py


from sklearn.discriminant_analysis import LinearDiscriminantAnalysis

# LDA 모델 생성
lda = LinearDiscriminantAnalysis(n_components=9)  # 클래스의 수 - 1 만큼의 선형 판별 축 선택

# LDA 학습 및 변환
X_lda = lda.fit_transform(X_scaled, y)

# 변환된 데이터의 크기 확인
print(X_lda.shape)
```
```py
import matplotlib.pyplot as plt
import seaborn as sns

# 2차원 시각화
plt.figure(figsize=(10, 7))
sns.scatterplot(x=X_lda[:, 0], y=X_lda[:, 1], hue=y, palette='viridis', legend=None)
plt.title('LDA of MNIST Dataset (2D)')
plt.xlabel('LDA Component 1')
plt.ylabel('LDA Component 2')
plt.show()

```
![](/ML/pic/LDA.png)

#### 실습하며 느낀 점
T-SNE를 수행하는 코드가 로딩이 정말 오래 걸렸다. (10분 정도 기다림;)
* 로딩이 너무 오래 걸리는 모습
![](/ML/pic/LOADING.png)