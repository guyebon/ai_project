import streamlit as st

# 1. 페이지 설정
st.set_page_config(page_title="MBTI 진로 추천 서비스", page_icon="🚀")

# 2. MBTI 데이터 구성 (특징 및 추천 진로 2가지)
mbti_data = {
    "ISTJ": {"desc": "책임감이 강하고 현실적인 관리자", "careers": ["회계사", "공무원"]},
    "ISFJ": {"desc": "타인을 돕는 성실한 수호자", "careers": ["간호사", "초등교사"]},
    "INFJ": {"desc": "통찰력 있는 이상주의적 조언자", "careers": ["심리상담사", "작가"]},
    "INTJ": {"desc": "전략을 세우는 독립적인 설계자", "careers": ["데이터 분석가", "소프트웨어 개발자"]},
    "ISTP": {"desc": "기술적인 문제 해결에 능한 장인", "careers": ["엔지니어", "파일럿"]},
    "ISFP": {"desc": "예술적 감각이 있는 성인군자", "careers": ["디자이너", "작곡가"]},
    "INFP": {"desc": "가치를 중시하는 열정적인 중재자", "careers": ["예술가", "사회복지사"]},
    "INTP": {"desc": "논리적인 비판을 즐기는 전략가", "careers": ["교수/연구원", "프로그래머"]},
    "ESTP": {"desc": "행동력이 빠른 활동가", "careers": ["기업가", "스포츠 매니저"]},
    "ESFP": {"desc": "에너지가 넘치는 분위기 메이커", "careers": ["연예인", "이벤트 기획자"]},
    "ENFP": {"desc": "창의적이고 자유로운 영혼", "careers": ["홍보 전문가", "카피라이터"]},
    "ENTP": {"desc": "새로운 도전을 즐기는 발명가", "careers": ["변호사", "마케팅 디렉터"]},
    "ESTJ": {"desc": "체계적으로 이끄는 엄격한 관리자", "careers": ["경영자", "은행원"]},
    "ESFJ": {"desc": "친절하고 사교적인 협력자", "careers": ["호텔리어", "승무원"]},
    "ENFJ": {"desc": "사람들을 이끄는 카리스마 리더", "careers": ["아나운서", "취업 컨설턴트"]},
    "ENTJ": {"desc": "목표를 향해 나아가는 통솔자", "careers": ["경영 컨설턴트", "정치인"]}
}

# 3. UI 구성
st.title("✨ MBTI별 맞춤 진로 추천")
st.write("자신의 MBTI를 선택하면 어울리는 진로를 추천해 드립니다.")

# 4. 사용자 선택
mbti_list = list(mbti_data.keys())
selected_mbti = st.selectbox("당신의 MBTI는 무엇인가요?", mbti_list)

# 5. 결과 출력
if selected_mbti:
    info = mbti_data[selected_mbti]
    
    st.divider()
    st.subheader(f"🔍 {selected_mbti} 유형 결과")
    st.info(f"**특징:** {info['desc']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.success(f"**추천 진로 1:** {info['careers'][0]}")
    with col2:
        st.success(f"**추천 진로 2:** {info['careers'][1]}")
    
    st.balloons() # 축하 효과
