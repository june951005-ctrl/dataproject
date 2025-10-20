import streamlit as st
import folium
from streamlit_folium import st_folium

st.set_page_config(page_title="서울 관광 명소 지도", layout="wide")

st.title("🗺️ 외국인들이 사랑하는 서울 관광지 Top 10")
st.markdown("서울의 인기 관광지를 폴리움 지도 위에 표시했어요! 클릭하면 명소 정보를 볼 수 있습니다 😊")

# 서울 중심 좌표
seoul_center = [37.5665, 126.9780]

# 관광지 데이터 (이름, 위도, 경도, 설명)
places = [
    {"name": "경복궁", "lat": 37.5796, "lon": 126.9770, "desc": "조선 왕조의 대표 궁궐 🇰🇷"},
    {"name": "명동거리", "lat": 37.5636, "lon": 126.9827, "desc": "쇼핑과 먹거리가 가득한 거리 🛍️"},
    {"name": "남산타워 (N서울타워)", "lat": 37.5512, "lon": 126.9882, "desc": "서울의 대표 전망 명소 🌃"},
    {"name": "북촌한옥마을", "lat": 37.5826, "lon": 126.9830, "desc": "전통 한옥의 정취를 느낄 수 있는 곳 🏡"},
    {"name": "홍대거리", "lat": 37.5563, "lon": 126.9220, "desc": "젊음과 예술이 넘치는 거리 🎶"},
    {"name": "이태원", "lat": 37.5347, "lon": 126.9946, "desc": "다국적 문화가 공존하는 거리 🌏"},
    {"name": "청계천", "lat": 37.5700, "lon": 126.9794, "desc": "도심 속 휴식 공간 🌊"},
    {"name": "롯데월드타워", "lat": 37.5131, "lon": 127.1025, "desc": "대한민국에서 가장 높은 빌딩 🏙️"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.5663, "lon": 127.0095, "desc": "미래적인 디자인 명소 🌀"},
    {"name": "한강공원 (여의도)", "lat": 37.5271, "lon": 126.9326, "desc": "서울의 대표적인 힐링 스팟 🌅"},
]

# Folium 지도 생성
m = folium.Map(location=seoul_center, zoom_start=12)

# 마커 추가
for p in places:
    folium.Marker(
        [p["lat"], p["lon"]],
        popup=f"<b>{p['name']}</b><br>{p['desc']}",
        tooltip=p["name"],
        icon=folium.Icon(color="blue", icon="info-sign"),
    ).add_to(m)

# Streamlit에 Folium 지도 표시
st_data = st_folium(m, width=800, height=600)
