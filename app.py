import streamlit as st
import time

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="🥑", layout="centered")

# 2. УЛУЧШЕННЫЙ CSS (Центровка, большие кнопки и видимые поля)
style = """
<style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    
    /* Центрируем все блоки */
    [data-testid="stVerticalBlock"] > div {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    h1 { color: #FFD700 !important; font-size: 30px !important; text-transform: uppercase; margin-bottom: 10px; }
    h2 { color: #FFD700 !important; font-size: 24px !important; margin-bottom: 20px; }
    
    /* ОГРОМНАЯ КНОПКА ПО ЦЕНТРУ */
    .stButton > button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); 
        color: black !important; 
        border-radius: 20px; 
        font-weight: bold; 
        width: 90% !important; /* Почти на всю ширину экрана */
        height: 4em; 
        border: none;
        font-size: 20px !important;
        box-shadow: 0 4px 20px rgba(255, 215, 0, 0.4);
        margin: 20px auto;
        display: block;
    }
    
    /* ВИДИМОЕ ПОЛЕ ВВОДА */
    .stTextInput > div > div > input {
        background-color: #111 !important;
        color: white !important;
        border: 2px solid #FFD700 !important; /* Золотая рамка */
        border-radius: 10px;
        height: 3.5em;
        text-align: center;
        font-size: 18px;
    }

    .stImage > img { border-radius: 20px; border: 1px solid #333; }
</style>
"""
# ОШИБКА ИСПРАВЛЕНА: используем unsafe_allow_html=True
st.markdown(style, unsafe_allow_html=True)

# Инициализация
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}
def next_step(): st.session_state.step += 1; st.rerun()

# --- ЭКРАНЫ ---

if st.session_state.step == 1:
    st.markdown("<h1>KETO AI PLATINUM</h1>", unsafe_allow_html=True)
    # Сочное авокадо вместо девушки
    st.image("https://images.unsplash.com/photo-1523049673857-eb18f1d7b578?w=800", use_container_width=True)
    st.write("Создайте идеальное тело с помощью персонального ИИ-плана.")
    if st.button("НАЧАТЬ АНАЛИЗ"): next_step()

elif st.session_state.step == 2:
    st.header("Как вас зовут?")
    st.image("https://images.unsplash.com/photo-1490818387583-1baba5e638af?w=800", use_container_width=True)
    # Поле ввода теперь с рамкой и кнопка сразу под ним
    name = st.text_input("Введите имя:", placeholder="Ваше имя...")
    if st.button("ДАЛЕЕ"):
        if name:
            st.session_state.data['name'] = name
            next_step()
        else:
            st.warning("Пожалуйста, введите имя")

elif st.session_state.step == 3:
    st.header("Ваш пол")
    st.image("https://images.unsplash.com/photo-1584263347416-85a696b4eda7?w=800", use_container_width=True)
    st.session_state.data['gender'] = st.radio("", ["Мужской", "Женский"], horizontal=True)
    if st.button("ПРОДОЛЖИТЬ"): next_step()

elif st.session_state.step == 4:
    st.header("Параметры тела")
    st.image("https://images.unsplash.com/photo-1576673442511-7e39b6545c87?w=800", use_container_width=True)
    h = st.number_input("Рост (см)", 140, 220, 170)
    w = st.number_input("Вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ"):
        st.session_state.data.update({'h': h, 'w': w})
        next_step()

elif st.session_state.step == 5:
    st.header("ГЕНЕРАЦИЯ ПЛАНА...")
    status = st.empty()
    bar = st.progress(0)
    msgs = ["Анализ метаболизма...", "Сборка рецептов...", "Генерация PDF..."]
    for i, m in enumerate(msgs):
        status.write(f"### {m}")
        bar.progress((i+1)*33)
        time.sleep(1.5)
    next_step()

elif st.session_state.step == 6:
    st.balloons()
    st.header("ГОТОВО!")
    st.image("https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=800", use_container_width=True)
    name = st.session_state.data.get('name', 'Чемпион')
    st.success(f"{name}, ваш план сформирован!")
    
    # ПРОВЕРЬ ИМЯ ФАЙЛА НА GITHUB! Если там Personal_Keto_Plan.pdf.pdf, исправь код ниже
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(label="📥 СКАЧАТЬ ПЛАН (PDF)", data=f, file_name="Keto_Plan.pdf", mime="application/pdf")
    except:
        st.error("Файл не найден. Проверьте, что загрузили PDF в репозиторий без двойного расширения.")
    
    if st.button("В НАЧАЛО"):
        st.session_state.step = 1
        st.rerun()
