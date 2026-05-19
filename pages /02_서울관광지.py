import streamlit as st
import folium
from streamlit_folium import st_folium

# 1. 페이지 기본 설정
st.set_page_config(
    page_title="외국인이 좋아하는 서울 관광지 TOP 10",
    page_icon="🗺️",
    layout="wide"
)

st.title("🗺️ 외국인이 좋아하는 서울의 주요 관광지 TOP 10")
st.markdown("외국인 관광객들에게 가장 인기 있는 서울의 명소 10곳을 지도에서 확인해 보세요!")

# 2. 서울 주요 관광지 TOP 10 데이터 (명칭, 위도, 경도, 설명)
tourist_spots = [
    {"name": "경복궁", "lat": 37.5796, "lng": 126.9770, "desc": "조선 왕조의 법궁, 한복 체험 명소"},
    {"name": "명동", "lat": 37.5635, "lng": 126.9846, "desc": "쇼핑과 길거리 음식의 메카, 외국인 방문율 1위"},
    {"name": "남산서울타워", "lat": 37.5512, "lng": 126.9882, "desc": "서울 시내를 한눈에 내려다보는 대표 랜드마크"},
    {"name": "북촌 한옥마을", "lat": 37.5829, "lng": 126.9835, "desc": "실제 주민들이 거주하는 아름다운 전통 한옥 밀집 지역"},
    {"name": "인사동", "lat": 37.5744, "lng": 126.9875, "desc": "한국 전통 골동품, 찻집, 공예품을 만날 수 있는 거리"},
    {"name": "홍대 거리", "lat": 37.5567, "lng": 126.9235, "desc": "젊은 에너지, 버스킹, 트렌디한 밤문화의 중심지"},
    {"name": "동대문디자인플라자 (DDP)", "lat": 37.5668, "lng": 127.0094, "desc": "자하 하디드가 설계한 세계 최대 규모의 3차원 비정형 건축물"},
    {"name": "광장시장", "lat": 37.5701, "lng": 127.0010, "desc": "빈대떡, 육회, 마약김밥 등 K-푸드를 체험하는 전통시장"},
    {"name": "스타필드 코엑스몰 (별마당도서관)", "lat": 37.5118, "lng": 127.0592, "desc": "SNS 인증샷 성지, 거대한 책장이 인상적인 복합 문화공간"},
    {"name": "청계천", "lat": 37.5693, "lng": 126.9787, "desc": "도심 한복판을 흐르는 시민들과 관광객의 도심 속 휴식처"}
]

# 화면을 2개의 구역(왼쪽: 지도, 오른쪽: 리스트 설명)으로 분할
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📍 서울 명소 지도")
    
    # 3. 지도 초기화 (서울 중심부 기준)
    m = folium.Map(location=[37.555, 126.985], zoom_start=12)
    
    # 4. 마커 추가
    for spot in tourist_spots:
        popup_text = f"<b>{spot['name']}</b><br>{spot['desc']}"
        folium.Marker(
            location=[spot['lat'], spot['lng']],
            popup=folium.Popup(popup_text, max_width=300),
            tooltip=spot['name'],
            icon=folium.Icon(color="red", icon="info-sign")
        ).add_to(m)
    
    # 5. 스트림릿 컴포넌트로 지도 렌더링
    st_folium(m, width="100%", height=500, returned_objects=[])

with col2:
    st.subheader("📋 관광지 목록 및 설명")
    for i, spot in enumerate(tourist_spots, 1):
        with st.expander(f"{i}. {spot['name']}"):
            st.write(spot['desc'])
            st.caption(f"위도: {spot['lat']} / 경도: {spot['lng']}")
          streamlit
folium
streamlit-folium
