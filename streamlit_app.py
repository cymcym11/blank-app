import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import io

st.set_page_config(page_title="학교 성격 테스트", page_icon="🏫")

st.title("🏫 학교에서의 내 이미지 성격 테스트")

# --------------------------
# 질문 데이터
# --------------------------
questions = [
    {
        "q": "1. 쉬는 시간에 나는 보통?",
        "options": {
            "친구들과 떠들며 논다": "star",
            "책을 읽거나 공부한다": "model",
            "친구들한테 장난치며 웃긴다": "funny",
            "그림 그리거나 음악 듣는다": "artist",
            "운동장에서 공을 찬다": "sports",
            "친구 고민을 들어준다": "healer"
        }
    },
    {
        "q": "2. 점심시간, 급식 줄 설 때 나는?",
        "options": {
            "친구랑 신나게 수다": "star",
            "조용히 순서 기다림": "model",
            "앞뒤 친구랑 장난": "funny",
            "노래 흥얼거림": "artist",
            "빨리 먹고 운동장 가야지!": "sports",
            "친구 자리 챙겨줌": "healer"
        }
    },
    {
        "q": "3. 조별 활동할 때 나는?",
        "options": {
            "리더 맡아서 이끌기": "star",
            "성실하게 맡은 일 하기": "model",
            "분위기 띄우는 개그 담당": "funny",
            "아이디어 내는 창의 담당": "artist",
            "힘든 일 척척 해냄": "sports",
            "갈등 조정하고 도와줌": "healer"
        }
    },
    {
        "q": "4. 시험이 끝난 날 나는?",
        "options": {
            "친구들이랑 놀러 나간다": "star",
            "도서관에서 자기계발": "model",
            "친구들 놀리며 농담": "funny",
            "집에서 그림/음악": "artist",
            "운동장에서 땀 빼기": "sports",
            "친구 위로하며 같이 쉼": "healer"
        }
    },
    {
        "q": "5. 친구가 슬퍼할 때 나는?",
        "options": {
            "같이 웃기면서 기분 풀어줌": "funny",
            "따뜻하게 위로해줌": "healer",
            "옆에서 조용히 있어줌": "model",
            "재밌는 곳 같이 가자고 함": "star",
            "그림/노래로 위로함": "artist",
            "운동 같이 하자고 함": "sports"
        }
    },
    {
        "q": "6. 학교 행사에서 나는?",
        "options": {
            "무대에 올라가서 공연": "star",
            "뒤에서 묵묵히 돕기": "model",
            "사회나 진행 맡기": "funny",
            "포스터나 꾸미기 담당": "artist",
            "체육대회 주인공": "sports",
            "도움 필요한 곳 챙김": "healer"
        }
    },
    {
        "q": "7. 친구들이 날 부르는 말은?",
        "options": {
            "핵인싸": "star",
            "모범생": "model",
            "개그맨": "funny",
            "예술가": "artist",
            "운동부": "sports",
            "천사": "healer"
        }
    },
    {
        "q": "8. 가장 좋아하는 수업은?",
        "options": {
            "발표/토론 수업": "star",
            "수학·국어 같은 주요과목": "model",
            "활동 많은 수업": "funny",
            "미술·음악": "artist",
            "체육": "sports",
            "봉사활동·상담": "healer"
        }
    }
]

# --------------------------
# 점수 초기화
# --------------------------
scores = {"star":0, "model":0, "funny":0, "artist":0, "sports":0, "healer":0}

# --------------------------
# 질문 출력
# --------------------------
for q in questions:
    st.subheader(q["q"])
    choice = st.radio("선택하세요:", list(q["options"].keys()), key=q["q"])
    if choice:
        scores[q["options"][choice]] += 1

# --------------------------
# 결과 설명 & 아이콘
# --------------------------
result_texts = {
    "star": ("⭐ 인기스타형!", "친구들과 잘 어울리고 주목받는 인기인입니다."),
    "model": ("📚 모범생형!", "성실하고 조용히 할 일을 해내는 신뢰받는 학생입니다."),
    "funny": ("🎭 개그캐형!", "주변을 즐겁게 만드는 분위기 메이커입니다."),
    "artist": ("🎨 아티스트형!", "개성과 창의력이 돋보이는 특별한 학생입니다."),
    "sports": ("⚽ 운동부 에이스형!", "열정적이고 활발한 스포츠형 학생입니다."),
    "healer": ("🍀 힐러형!", "배려심 많고 친구들을 따뜻하게 챙기는 학생입니다."),
}

result_icons = {
    "star": "https://cdn-icons-png.flaticon.com/512/616/616490.png",
    "model": "https://cdn-icons-png.flaticon.com/512/3135/3135755.png",
    "funny": "https://cdn-icons-png.flaticon.com/512/742/742751.png",
    "artist": "https://cdn-icons-png.flaticon.com/512/4333/4333609.png",
    "sports": "https://cdn-icons-png.flaticon.com/512/1046/1046784.png",
    "healer": "https://cdn-icons-png.flaticon.com/512/3448/3448610.png",
}

# --------------------------
# 결과 보기 버튼
# --------------------------
if st.button("결과 보기"):
    result = max(scores, key=scores.get)
    title, desc = result_texts[result]

    st.image(result_icons[result], width=120)
    st.success(f"{title}\n{desc}")

    # --------------------------
    # 카드뉴스 이미지 생성 함수
    # --------------------------
    def create_card(title, desc):
        img = Image.new("RGB", (600, 800), color=(255, 255, 255))
        draw = ImageDraw.Draw(img)

        try:
            font_title = ImageFont.truetype("arial.ttf", 40)
            font_desc = ImageFont.truetype("arial.ttf", 28)
        except:
            font_title = ImageFont.load_default()
            font_desc = ImageFont.load_default()

        draw.text((50, 100), title, font=font_title, fill=(0, 0, 0))
        draw.text((50, 200), desc, font=font_desc, fill=(50, 50, 50))

        return img

    card_img = create_card(title, desc)

    # 이미지 화면에 표시
    st.image(card_img, caption="📢 공유용 카드뉴스")

    # 다운로드 버튼
    buf = io.BytesIO()
    card_img.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 카드뉴스 이미지 다운로드",
        data=byte_im,
        file_name="school_personality_card.png",
        mime="image/png"
    )
