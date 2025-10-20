# app.py
import streamlit as st

st.set_page_config(page_title="MBTI 진로 추천 🌟", page_icon="🧭")

st.title("MBTI로 골라보는 진로 추천 🎯")
st.write("너의 MBTI를 골라봐! 각 유형에 맞는 **진로 2가지**와 어떤 학과·성격에 어울리는지 알려줄게 😊")

MBTI_LIST = [
    "ISTJ","ISFJ","INFJ","INTJ",
    "ISTP","ISFP","INFP","INTP",
    "ESTP","ESFP","ENFP","ENTP",
    "ESTJ","ESFJ","ENFJ","ENTJ"
]

# 데이터: 각 MBTI에 대해 진로 2개, 각 진로에 대한 학과 및 성격 설명
MBTI_CAREERS = {
    "ISTJ": [
        {"career":"회계사 / 재무 담당자 💼", "majors":"회계학, 경영학, 금융학", "personality":"체계적이고 책임감 강함. 규칙과 절차를 잘 지키는 타입."},
        {"career":"품질관리 / 운영관리 🏭", "majors":"산업공학, 경영학, 화학공학", "personality":"세부사항에 강하고 실무를 꼼꼼히 처리하는 사람에게 적합."}
    ],
    "ISFJ": [
        {"career":"간호사 / 보건복지 관련 🩺", "majors":"간호학, 사회복지학, 보건학", "personality":"배려심 많고 성실함. 사람 돕는 일을 즐기는 편."},
        {"career":"초등교사 / 교육지원 🎒", "majors":"교육학, 유아교육, 특수교육", "personality":"인내심 있고 학생을 세심히 챙겨줄 수 있는 성격."}
    ],
    "INFJ": [
        {"career":"상담심리사 / 임상심리 💬", "majors":"심리학, 상담학, 사회복지학", "personality":"통찰력 있고 공감능력 뛰어남. 깊은 의미를 찾는 경향."},
        {"career":"기획·콘텐츠 전략가 ✍️", "majors":"커뮤니케이션학, 문예창작, 경영학", "personality":"창의적이면서도 사람의 마음을 이해하려는 성향."}
    ],
    "INTJ": [
        {"career":"연구개발(R&D) 과학자 🔬", "majors":"물리/화학/생명공학, 전공 심화", "personality":"전략적이고 논리적. 장기적 계획 세우는 걸 좋아함."},
        {"career":"데이터 사이언티스트 / AI 개발자 🤖", "majors":"컴퓨터공학, 통계학, 전산학", "personality":"분석적이며 독립적으로 문제 해결을 즐기는 타입."}
    ],
    "ISTP": [
        {"career":"기계·설비 엔지니어 🛠️", "majors":"기계공학, 전기공학, 제조공학", "personality":"손재주 좋고 즉각적으로 문제를 해결하는 걸 즐김."},
        {"career":"파일럿 / 소방관 같은 실무형 직업 🚒✈️", "majors":"항공과, 소방안전학, 특성화 교육", "personality":"위기 상황에서 침착하고 행동력이 빠른 편."}
    ],
    "ISFP": [
        {"career":"디자이너 (패션/그래픽) 🎨", "majors":"디자인학, 시각디자인, 패션학", "personality":"감각적이고 미적 감각이 뛰어남. 자유로운 분위기 선호."},
        {"career":"예술치료사 / 공연·음악 분야 🎭🎵", "majors":"예체능 계열, 음악치료, 미술치료", "personality":"감성적이고 다른 사람의 감정을 이해하는 능력 보유."}
    ],
    "INFP": [
        {"career":"작가·편집자 / 콘텐츠 크리에이터 📝", "majors":"문예창작, 국문학, 커뮤니케이션", "personality":"상상력 풍부하고 자기 표현을 중요하게 여김."},
        {"career":"NGO·사회공헌 분야 🌱", "majors":"사회학, 국제관계, 사회복지학", "personality":"가치 지향적이고 공감 능력이 높아 사회문제에 관심 많음."}
    ],
    "INTP": [
        {"career":"연구자 / 소프트웨어 아키텍트 🧠", "majors":"컴퓨터공학, 수학, 물리학", "personality":"호기심이 많고 이론을 탐구하는 데 즐거움을 느낌."},
        {"career":"시스템 설계자 / IT 컨설턴트 🖥️", "majors":"정보시스템, 전산학, 산업공학", "personality":"복잡한 문제 구조를 분석하고 설계하는 데 능함."}
    ],
    "ESTP": [
        {"career":"영업·마케팅 담당자 / 스타트업 운영자 🚀", "majors":"경영학, 광고홍보, 마케팅", "personality":"사교적이고 추진력 강함. 현장에서 성과 내는 타입."},
        {"career":"이벤트 기획 / PR 담당자 🎉", "majors":"광고홍보, 관광경영, 커뮤니케이션", "personality":"빠르게 상황을 파악하고 사람들과 호흡하는 걸 좋아함."}
    ],
    "ESFP": [
        {"career":"방송·연예·퍼포먼스 분야 🎤", "majors":"연기·방송학, 공연예술, 실용음악", "personality":"사교적이고 현장 에너지가 넘침. 주목받는 걸 즐김."},
        {"career":"관광·레저·서비스업 🧳", "majors":"관광학, 호텔경영, 서비스경영", "personality":"사람 대하는 걸 좋아하고 친절함이 무기."}
    ],
    "ENFP": [
        {"career":"광고·콘텐츠 플래너 / 창업가 ✨", "majors":"광고홍보, 미디어학, 경영학", "personality":"창의적이고 아이디어가 풍부. 사람과의 연결을 즐김."},
        {"career":"인사(HR)·교육 기획자 👥", "majors":"심리학, 인사조직, 교육학", "personality":"사람의 가능성을 찾아주는 걸 즐기는 유형."}
    ],
    "ENTP": [
        {"career":"스타트업 창업자 / 제품 기획자 💡", "majors":"경영학, 디자인씽킹, 컴퓨터공학", "personality":"문제 해결을 창의적으로 접근하고 토론을 즐김."},
        {"career":"변호사·정책분석가 (논리 기반 직종) ⚖️", "majors":"법학, 정치외교, 공공정책", "personality":"논쟁을 즐기고 새로운 아이디어로 체계를 흔듦."}
    ],
    "ESTJ": [
        {"career":"관리자·운영 책임자 (매니저) 📋", "majors":"경영학, 법학, 공공관리", "personality":"조직적이고 규칙을 중시. 리더십이 강함."},
        {"career":"회계·감사 담당자 🧾", "majors":"회계학, 경영학, 금융학", "personality":"철저하고 효율적이며 책임감을 중시."}
    ],
    "ESFJ": [
        {"career":"간호·보건·교육 관련 (케어 직군) ❤️", "majors":"간호학, 교육학, 사회복지학", "personality":"협력적이고 타인을 챙기는 걸 좋아함."},
        {"career":"HR·고객서비스 매니저 🤝", "majors":"경영학, 심리학, 커뮤니케이션", "personality":"사람의 감정과 요구를 잘 읽어내는 타입."}
    ],
    "ENFJ": [
        {"career":"교사·멘토·리더십 코치 🌟", "majors":"교육학, 경영학, 상담심리", "personality":"사람을 이끌고 동기부여 하는 능력이 뛰어남."},
        {"career":"PR·커뮤니케이션 디렉터 🗣️", "majors":"커뮤니케이션학, 광고홍보, 미디어학", "personality":"사교적이고 설득력이 좋아서 대중과 소통에 강함."}
    ],
    "ENTJ": [
        {"career":"경영자·컨설턴트 💼", "majors":"경영학, 경제학, 전략경영", "personality":"목표지향적이고 결단력 강함. 조직을 이끄는 스타일."},
        {"career":"프로젝트 매니저 / 전략기획자 📈", "majors":"산업공학, 경영학, 데이터분석", "personality":"전략적으로 자원을 배분하고 사람을 관리하는 데 능함."}
    ],
}

def pretty_career_block(c):
    # returns a formatted string for a career entry
    return f"**{c['career']}**\n\n- **적합 학과:** {c['majors']}\n- **어울리는 성격:** {c['personality']}\n"

# UI
selected = st.selectbox("너의 MBTI를 골라봐 ✨", MBTI_LIST)

st.markdown("---")
st.header(f"{selected} 유형을 위한 추천 진로 🔎")

careers = MBTI_CAREERS.get(selected, [])
if not careers:
    st.write("아직 정보가 없는 유형이야... 😅")
else:
    # Brief intro
    st.write("아래는 이 유형에 잘 맞는 진로 2가지야. 각 항목을 눌러서 자세히 봐봐 👇")
    for i, c in enumerate(careers, start=1):
        with st.expander(f"{i}. {c['career']}"):
            st.markdown(pretty_career_block(c))
            # 친근한 마무리 문장
            st.write("팁: 전공만으로 모든 게 정해지진 않아! 여러 경험(동아리, 인턴, 사이드 프로젝트)을 통해 직접 체험해보는 걸 추천할게 😄")
st.markdown("---")

# 추가 기능: 랜덤 팁 버튼
if st.button("진로 결정 팁 하나 줘 💡"):
    tips = [
        "직접 해봐야 알아. 작은 프로젝트나 체험활동부터 시작해봐!",
        "사소한 호기심도 기록해. 반복되면 그게 힌트야.",
        "사람들과 대화해 봐. 멘토나 선생님과 얘기하면 시야가 확 넓어져.",
        "한 가지에만 매달리지 말고 여러 경험을 해보는 게 좋아!"
    ]
    import random
    st.info(random.choice(tips))

st.write("만약 더 자세한 진로 상담을 원하면, 너의 관심사나 좋아하는 활동을 알려줘. 거기 맞춰서 더 구체적으로 도와줄게 🙌")
