import streamlit as st
import time

# --------------------------------------------------
# PAGE CONFIG
# --------------------------------------------------
st.set_page_config(
    page_title="KETO AI PLATINUM",
    page_icon="💎",
    layout="centered"
)

# --------------------------------------------------
# MOBILE-SAFE PREMIUM CSS
# --------------------------------------------------
st.markdown("""
<style>
/* ===== ОСНОВА ===== */
.stApp {
    background-color: #000;
    color: #fff;
}

.main > div {
    max-width: 420px;
    margin: 0 auto;
    padding: 20px 14px 50px;
}

/* ===== ТЕКСТ (КРУПНЫЙ!) ===== */
h1 {
    font-size: 34px !important;
    color: #FFD700;
    text-align: center;
    text-transform: uppercase;
}
h2, h3 {
    font-size: 28px !important;
    color: #FFD700;
    text-align: center;
}
p, label, div {
    font-size: 20px !important;
    line-height: 1.6;
    text-align: center;
    color: #eee;
}

/* ===== КАРТИНКИ ===== */
img {
    width: 100%;
    border-radius: 18px;
    margin: 12px 0;
}

/* ===== КНОПКИ — ПО ЦЕНТРУ ===== */
.stButton {
    display: flex;
    justify-content: center;
}
.stButton > button {
    width: 100%;
    max-width: 360px;
    height: 4.4em;
    font-size: 22px !important;
    font-weight: 700;
    border-radius: 26px;
    background: linear-gradient(90deg,#FFD700,#B8860B);
    color: black;
    border: none;
    margin: 18px auto;
    box-shadow: 0 6px 22px rgba(255,215,0,.45);
}

/* ===== ПОЛЕ ВВОДА (БОЛЬШОЕ, НЕ ОБРЕЗАНО) ===== */
[data-testid="stTextInput"] {
    width: 100%;
}
[data-testid="stTextInput"] input {
    width: 100% !important;
    height: 4.2em !important;
    font-size: 24px !important;
    text-align: center;
    background-color: #111 !important;
    color: #FFD700 !important;
    border: 4px solid #FFD700 !important;
    border-radius: 18px !important;
}

/* ===== СЛАЙДЕРЫ ===== */
[data-testid="stSlider"] {
    font-size: 20px !important;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# STATE
# --------------------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 1
if "data" not in st.session_state:
    st.session_state.data = {}

def next_step():
    st.session_state.step += 1
    st.rerun()

# --------------------------------------------------
# SCREENS
# --------------------------------------------------

# SCREEN 1 — HERO
if st.session_state.step == 1:
    st.title("KETO AI PLATINUM")
    st.image(
        "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?fm=jpg&q=80&w=800",
        use_container_width=True
    )
    st.write("Персональный кето-план на 28 дней. Создан ИИ специально для вас.")
    if st.button("🚀 НАЧАТЬ ТРАНСФОРМАЦИЮ"):
        next_step()

# SCREEN 2 — NAME
elif st.session_state.step == 2:
    st.header("Как вас звать?")
    st.image(
        "https://images.unsplash.com/photo-1490645935967-10de6ba17061?fm=jpg&q=80&w=800",
        use_container_width=True
    )
    name = st.text_input("", placeholder="Введите имя")
    if st.button("ПРОДОЛЖИТЬ"):
        if len(name.strip()) >= 2:
            st.session_state.data["name"] = name.strip()
            next_step()
        else:
            st.warning("Введите имя")

# SCREEN 3 — GENDER
elif st.session_state.step == 3:
    st.header("Ваш пол")
    st.image(
        "https://images.unsplash.com/photo-1605296867304-46d5465a13f1?fm=jpg&q=80&w=800",
        use_container_width=True
    )
    gender = st.radio("", ["🙋‍♂️ Мужской", "🙋‍♀️ Женский"])
    st.session_state.data["gender"] = gender
    if st.button("ДАЛЕЕ"):
        next_step()

# SCREEN 4 — BODY
elif st.session_state.step == 4:
    st.header("Параметры тела")
    st.image(
        "https://images.unsplash.com/photo-1576673442511-7e39b6545c87?fm=jpg&q=80&w=800",
        use_container_width=True
    )
    height = st.slider("Рост (см)", 140, 220, 170)
    weight = st.slider("Вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ ПЛАН"):
        st.session_state.data.update({"height": height, "weight": weight})
        next_step()

# SCREEN 5 — AI
elif st.session_state.step == 5:
    st.header("ИИ анализирует данные…")
    st.image(
        "https://images.unsplash.com/photo-1518316847866-651fbb917956?fm=jpg&q=80&w=800",
        use_container_width=True
    )
    bar = st.progress(0)
    for i in range(100):
        bar.progress(i + 1)
        time.sleep(0.015)
    next_step()

# SCREEN 6 — RESULT
elif st.session_state.step == 6:
    name = st.session_state.data.get("name", "Чемпион")
    st.balloons()
    st.header(f"{name}, ваш план готов 💎")
    st.image(
        "https://images.unsplash.com/photo-1484723091739-30a097e8f929?fm=jpg&q=80&w=800",
        use_container_width=True
    )

    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                "📥 СКАЧАТЬ МОЙ PDF-ПЛАН",
                data=f,
                file_name=f"Keto_Plan_{name}.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("PDF файл не найден")

    if st.button("🔁 Пройти заново"):
        st.session_state.step = 1
        st.rerun()
