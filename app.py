import streamlit as st
import time

# --------------------------------------------------
# 1. НАСТРОЙКИ СТРАНИЦЫ (MOBILE FIRST)
# --------------------------------------------------
st.set_page_config(
    page_title="KETO AI PLATINUM",
    page_icon="💎",
    layout="centered"
)

# --------------------------------------------------
# 2. MOBILE-FIRST CSS (АККУРАТНО, БЕЗ ПЕРЕБОРА)
# --------------------------------------------------
st.markdown("""
<style>
.stApp {
    background-color: #000;
    color: #fff;
}

/* Ограничиваем ширину — как мобильный экран */
.main > div {
    max-width: 420px;
    margin: auto;
    padding-bottom: 40px;
}

/* Заголовки */
h1 {
    color: #FFD700;
    font-size: 30px;
    text-align: center;
    text-transform: uppercase;
}
h2, h3 {
    color: #FFD700;
    text-align: center;
}

/* Текст */
p, label {
    font-size: 17px;
    text-align: center;
    color: #ddd;
}

/* Картинки */
img {
    border-radius: 18px;
}

/* КНОПКИ — БОЛЬШИЕ, ПАЛЬЦЕОРИЕНТИРОВАННЫЕ */
.stButton > button {
    width: 100%;
    height: 4em;
    font-size: 20px;
    font-weight: bold;
    border-radius: 25px;
    background: linear-gradient(90deg,#FFD700,#B8860B);
    color: black;
    border: none;
    box-shadow: 0 6px 20px rgba(255,215,0,.35);
}

/* ПОЛЯ ВВОДА */
input {
    font-size: 22px !important;
    text-align: center;
    background-color: #111 !important;
    color: #FFD700 !important;
    border: 3px solid #FFD700 !important;
    border-radius: 14px !important;
    height: 3.5em;
}
</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# 3. СОСТОЯНИЕ
# --------------------------------------------------
if "step" not in st.session_state:
    st.session_state.step = 1
if "data" not in st.session_state:
    st.session_state.data = {}

def next_step():
    st.session_state.step += 1
    st.rerun()

# --------------------------------------------------
# 4. ЭКРАНЫ
# --------------------------------------------------

# === ЭКРАН 1 ===
if st.session_state.step == 1:
    st.title("KETO AI PLATINUM")
    st.image(
        "https://images.unsplash.com/photo-1482049016688-2d3e1b311543?w=800",
        use_container_width=True
    )
    st.write("Персональный кето-план на 28 дней. Создан ИИ.")
    if st.button("🚀 НАЧАТЬ ТРАНСФОРМАЦИЮ"):
        next_step()

# === ЭКРАН 2 ===
elif st.session_state.step == 2:
    st.header("Как вас называть?")
    name = st.text_input(
        "",
        placeholder="Введите имя"
    )
    if st.button("ПРОДОЛЖИТЬ"):
        if len(name.strip()) >= 2:
            st.session_state.data["name"] = name.strip()
            next_step()
        else:
            st.warning("Введите имя")

# === ЭКРАН 3 ===
elif st.session_state.step == 3:
    st.header("Ваш пол")
    gender = st.radio(
        "",
        ["🙋‍♂️ Мужской", "🙋‍♀️ Женский"]
    )
    st.session_state.data["gender"] = gender
    if st.button("ДАЛЕЕ"):
        next_step()

# === ЭКРАН 4 ===
elif st.session_state.step == 4:
    st.header("Параметры тела")
    height = st.slider("Рост (см)", 140, 220, 170)
    weight = st.slider("Вес (кг)", 40, 200, 80)

    if st.button("РАССЧИТАТЬ ПЛАН"):
        st.session_state.data.update({
            "height": height,
            "weight": weight
        })
        next_step()

# === ЭКРАН 5 ===
elif st.session_state.step == 5:
    st.header("ИИ анализирует данные…")
    progress = st.progress(0)
    for i in range(100):
        progress.progress(i + 1)
        time.sleep(0.015)
    next_step()

# === ЭКРАН 6 ===
elif st.session_state.step == 6:
    name = st.session_state.data.get("name", "Чемпион")
    st.balloons()
    st.header(f"{name}, ваш план готов 💎")

    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                "📥 СКАЧАТЬ МОЙ PDF-ПЛАН",
                data=f,
                file_name=f"Keto_Plan_{name}.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("PDF файл не найден в репозитории")

    if st.button("🔁 Пройти заново"):
        st.session_state.step = 1
        st.rerun()
