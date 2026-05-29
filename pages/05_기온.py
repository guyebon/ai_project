
# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# 페이지 제목
st.title("날짜별 기온분석")

# 데이터 불러오기
df = pd.read_csv("seoul.csv", encoding="cp949")

# 날짜 데이터 처리
df['날짜'] = pd.to_datetime(df['날짜'])
df['연도'] = df['날짜'].dt.year
df['월'] = df['날짜'].dt.month
df['일'] = df['날짜'].dt.day

# 사용자 입력
month = st.selectbox("월 선택", range(1, 13))
day = st.selectbox("일 선택", range(1, 32))

# 선택한 날짜 데이터 필터링
filtered = df[(df['월'] == month) & (df['일'] == day)]

# 데이터가 있을 경우 그래프 출력
if not filtered.empty:

    fig, ax = plt.subplots(figsize=(12, 6))

    # 최고기온
    ax.plot(
        filtered['연도'],
        filtered['최고기온(℃)'],
        color='hotpink',
        label='최고기온',
        marker='o'
    )

    # 최저기온
    ax.plot(
        filtered['연도'],
        filtered['최저기온(℃)'],
        color='lightblue',
        label='최저기온',
        marker='o'
    )

    # 그래프 설정
    ax.set_title("날짜별 기온분석")
    ax.set_xlabel("연도")
    ax.set_ylabel("온도(℃)")
    ax.legend()
    ax.grid(True)

    st.pyplot(fig)

else:
    st.warning("해당 날짜의 데이터가 없습니다.")
