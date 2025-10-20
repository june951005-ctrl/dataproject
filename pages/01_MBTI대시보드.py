import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 페이지 설정
st.set_page_config(page_title="국가별 MBTI 비율 시각화", page_icon="🌍", layout="wide")

# 데이터 불러오기
@st.cache_data
def load_data():
    df = pd.read_csv("countriesMBTI_16types.csv")
    return df

df = load_data()

st.title("🌍 국가별 MBTI 비율 시각화")
st.markdown("#### 선택한 국가의 16가지 MBTI 유형 분포를 확인해보세요!")

# 국가 선택
country_list = df["Country"].sort_values().tolist()
selected_country = st.selectbox("국가를 선택하세요", country_list, index=0)

# 선택된 국가 데이터 추출
country_data = df[df["Country"] == selected_country].iloc[0, 1:]
country_data = country_data.sort_values(ascending=False)

# 색상 설정 (1등 빨강, 나머지 점점 옅어지는 색상)
colors = ['#FF4C4C'] + ['#FFA07A' for _ in range(len(country_data) - 1)]

# Plotly 그래프 생성
fig = go.Figure(
    data=[
        go.Bar(
            x=country_data.index,
            y=country_data.values,
            marker=dict(color=colors),
            text=[f"{v*100:.2f}%" for v in country_data.values],
            textposition='auto',
        )
    ]
)

fig.update_layout(
    title=dict(
        text=f"🇨🇳 {selected_country}의 MBTI 유형 비율",
        font=dict(size=22)
    ),
    xaxis_title="MBTI 유형",
    yaxis_title="비율",
    yaxis=dict(tickformat=".0%"),
    template="plotly_white",
    height=600,
    margin=dict(l=40, r=40, t=80, b=60)
)

# 그래프 출력
st.plotly_chart(fig, use_container_width=True)

# 데이터 테이블 표시
with st.expander("📋 원본 데이터 보기"):
    st.dataframe(df[df["Country"] == selected_country].T.rename(columns={df["Country"] == selected_country: "비율"}))
