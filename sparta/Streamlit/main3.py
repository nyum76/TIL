import streamlit as st

## 1. 데이터 상태와 캐싱 최적화
  # 데코레이터는 골뱅이를 붙여 함수 위에서 작동함
  
  # ttl 안적으면 기본값 600초로 10분임
@st.cache_data(ttl=600)  # time to live (ttl) : 캐시를 유지 시키는 시간 (초단위)
def fetch_data(): # 데이터 로딩 예시
    return{"data":[1,2,3,4]}
st.write(fetch_data())


# 데코레이터 (Decorator) : def, 함수가 실행되기 직전에 바로 실행되는 함수

# 캐시(Cache) : 브라우저에 남아있는 휘발성 데이터
# 캐시로 이전 대화 내용을 저장하는 방법도 있다. (or 따로 저장)

## 2. 세션 상태 초기화 방법

# 세션 (Session) : 인터넷 연결이 유지되는 것 -> 내 상태가 나갔다 들어오더라도 유지

import streamlit as st

if "user_name" not in st.session_state:
    st.session_state.user_name = "Guest"
name = st.text_input("Your Name:", st.session_state.user_name)
if st.button("Save Name"):
    st.session_state.user_name = name
st.write(f"Hello, {st.session_state.user_name}!")


## 3. 

import pandas as pd
import streamlit as st

@st.cache_data
def load_file(file):
    return pd.read_csv(file)

file = st.file_uploader("Upload a CSV File", type=["csv"])
if file:
    df = load_file(file)
    st.dataframe(df)

    # 필터링 기능 추가
    filter_value = st.text_input("Filter by column value")
    filtered_df = df[df.iloc[:, 0].astype(str).str.contains(filter_value, na=False)]
    st.write("Filtered Data:", filtered_df)
    
###
## 1. HTML/CSS 기반 커스터마이징 -> 사이트를 꾸밀 수 있다

import streamlit as st

st.markdown(
    """
    <style>
    .custom-title {
        color: #4CAF50;
        font-size: 30px;
        font-weight: bold;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<p class="custom-title">Customized Title</p>', unsafe_allow_html=True)

## 2. JavaScript 와 연동

import streamlit as st

st.components.v1.html(
    """
    <button onclick="alert('Button clicked!')">Click Me</button>
    """,  # 삽입할 HTML 코드
)


### 고급 레이아웃 설계

## 1. st.tab
import streamlit as st

tab1, tab2 = st.tabs(["Tab 1", "Tab 2"]) # 내가 만들 탭 리스트 형태로 넣기
with tab1:
    st.write("Content for Tab 1")
with tab2:
    st.write("Content for Tab 2")
    
    
    
import streamlit as st

st.sidebar.header("Sidebar")
st.sidebar.button("Sidebar Button")

col1, col2 = st.columns(2)
with col1:
    st.write("Column 1")
with col2:
    st.write("Column 2")
    
    
### 데이터 시각화와 심화
## 1. 데이터
    
import streamlit as st
import pandas as pd

df = pd.read_csv("test.csv")  # 어제 받으셨던 파일

selected_columns = st.multiselect("Select columns to display", df.columns)
if selected_columns:
    st.write(df[selected_columns])   
    
### 외부 라이브러리 연동 심화'
## streamlit-chat 라이브러리 사용하기
# 설치 - pip install streamlit-chat

import streamlit as st
from streamlit_chat import message

message("My message") 
message("Hello bot!", is_user=True)  # align's the message to the right


# Streamlit - Components 에서 보기


##
import time
import streamlit as st

placeholder = st.empty()
for i in range(10):
    placeholder.write(f"Iteration {i}")
    time.sleep(1)
    
### ML 
from sklearn.linear_model import LinearRegression
import streamlit as st
import numpy as np

# 모델 학습
model = LinearRegression()
X = np.array([[1], [2], [3], [4]])
y = np.array([2, 4, 6, 8])
model.fit(X, y)

# 사용자 입력
user_input = st.number_input("Enter a value for prediction:")
if st.button("Predict"):
    prediction = model.predict([[user_input]])
    st.write(f"Prediction: {prediction[0]:.2f}")