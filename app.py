import streamlit as st
import time

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="🥑", layout="centered")

# 2. ИСПРАВЛЕННЫЙ CSS (С закрытыми кавычками и центровкой)
style = """
<style>
    .stApp { background-color: #000000; color: #FFFFFF; }

    /* Принудительная центровка всех контейнеров */
    [data-testid="stVerticalBlock"] > div {
        display: flex;
        flex-direction: column;
        align-items: center !important;
        justify-content: center !important;
        text-align: center;
        width: 100%;
    }

    /* ОГРОМНОЕ ПОЛЕ ВВОДА */
    .stTextInput { width: 100% !important; }
    .stTextInput > div > div > input {
        min-height: 4.5em !important;
        font-size: 22px !important;
        text-align: center;
        background-color: #111 !important;
        color: #FFD700 !important;
        border: 3px solid #FFD700 !important;
        border-radius: 15px;
    }

    /* ОГРОМНЫЕ КНОПКИ ПО ЦЕНТРУ */
    .stButton { width: 100%; display: flex; justify-content: center; }
    .stButton > button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); 
        color: black !important; 
        border-radius: 20px; 
        font-weight: bold; 
        width: 100% !important; 
        min-width: 280px;
        height: 4em !important; 
        font-size: 20px !important;
        box-shadow: 0 4px 20px rgba(255, 215, 0, 0.4);
        border: none;
        margin-top: 20px;
    }

    /* Адаптивные картинки */
    .stImage > img { 
        border-radius: 20px; 
        border: 1px solid #333; 
        max-width: 100% !important;
    }
    
    h1 { color: #FFD700 !important; text-align: center; font-size: 28px !important; }
    h2 { color: #FFD700 !important; text-align: center; }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# Инициализация состояния
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.data = {}

def next_step():
    st.session_state.step += 1
    st.rerun()

# --- ЭКРАНЫ ОПРОСНИКА ---

if st.session_state.step == 1:
    st.markdown("<h1>KETO AI PLATINUM</h1>", unsafe_allow_html=True)
    # Картинка авокадо (диетическая тематика)
    st.image("https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=800", use_container_width=True)
    st.write("Ваш персональный план похудения на 28 дней, созданный ИИ.")
    if st.button("НАЧАТЬ АНАЛИЗ"): next_step()

elif st.session_state.step == 2:
    st.header("Как вас зовут?")
    st.image("https://images.unsplash.com/photo-1490818387583-1baba5e638af?w=800", use_container_width=True)
    # Поле ввода теперь очень заметное
    name = st.text_input("", placeholder="Введите ваше имя здесь...")
    if st.button("ПРОДОЛЖИТЬ"):
        if name:
            st.session_state.data['name'] = name
            next_step()
        else:
            st.warning("Пожалуйста, введите имя в поле выше")

elif st.session_state.step == 3:
    st.header("Ваши параметры")
    st.image("https://images.unsplash.com/photo-1576673442511-7e39b6545c87?w=800", use_container_width=True)
    h = st.number_input("Рост (см)", 140, 220, 170)
    w = st.number_input("Вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ"):
        st.session_state.data.update({'h': h, 'w': w})
        next_step()

elif st.session_state.step == 4:
    st.header("АНАЛИЗ ДАННЫХ...")
    status = st.empty()
    bar = st.progress(0)
    for i in range(1, 101, 5):
        status.write(f"ИИ подбирает рецепты: {i}%")
        bar.progress(i)
        time.sleep(0.05)
    next_step()

elif st.session_state.step == 5:
    st.balloons()
    st.header("ПЛАН ГОТОВ!")
    st.image("https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=800", use_container_width=True)
    
    # ПРОВЕРКА ФАЙЛА (убедитесь, что имя файла на GitHub совпадает)
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                label="📥 СКАЧАТЬ МОЙ ПЛАН (PDF)",
                data=f,
                file_name="Keto_Platinum_Plan.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.error("Файл плана не найден. Проверьте загрузку на GitHub.")

    if st.button("ПРОЙТИ ЗАНОВО"):
        st.session_state.step = 1
        st.rerun()
