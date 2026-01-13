import streamlit as st
import time

# 1. МОБИЛЬНАЯ ВЕРСТКА И ДИЗАЙН
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="💎", layout="centered")

# Адаптивный CSS для смартфонов
style = """
<style>
    /* Черный фон для всего приложения */
    .stApp { background-color: #000000; color: #FFFFFF; }
    
    /* Делаем заголовки крупными и золотыми */
    h1 { color: #FFD700 !important; font-size: 28px !important; text-align: center; text-transform: uppercase; }
    h2, h3 { color: #FFD700 !important; font-size: 22px !important; text-align: center; }
    
    /* Огромные кнопки для удобного нажатия пальцем */
    .stButton>button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); 
        color: black !important; 
        border-radius: 15px; 
        font-weight: bold; 
        width: 100%; 
        height: 4em; 
        border: none;
        font-size: 18px !important;
        margin-top: 20px;
    }
    
    /* Центрируем обычный текст */
    div[data-testid="stMarkdownContainer"] p { 
        text-align: center; 
        font-size: 16px; 
        color: #DDDDDD;
    }

    /* Настройка полей ввода для мобилок */
    .stTextInput input, .stNumberInput input {
        background-color: #111111 !important;
        color: white !important;
        border: 1px solid #333 !important;
    }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# Инициализация шагов
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.data = {}

def next_step():
    st.session_state.step += 1
    st.rerun()

# --- ЦИКЛ ОПРОСНИКА ---

if st.session_state.step == 1:
    st.markdown("<h1>KETO AI<br>PLATINUM</h1>", unsafe_allow_html=True)
    # use_container_width=True заставляет картинку подстраиваться под ширину телефона
    st.image("https://images.unsplash.com/photo-1524182620199-a93f4136efac?q=80&w=1000", use_container_width=True)
    st.write("Получите ваш персональный план питания на 28 дней, созданный искусственным интеллектом.")
    if st.button("НАЧАТЬ АНАЛИЗ"): next_step()

elif st.session_state.step == 2:
    st.header("Ваше имя")
    name = st.text_input("", placeholder="Введите ваше имя")
    if name and st.button("ПРОДОЛЖИТЬ"):
        st.session_state.data['name'] = name
        next_step()

elif st.session_state.step == 3:
    st.header("Ваш пол")
    st.session_state.data['gender'] = st.radio("", ["Мужской", "Женский"], horizontal=True)
    if st.button("ДАЛЕЕ"): next_step()

elif st.session_state.step == 4:
    st.header("Ваш возраст")
    st.session_state.data['age'] = st.slider("", 18, 80, 30)
    if st.button("ДАЛЕЕ"): next_step()

elif st.session_state.step == 5:
    st.header("Параметры")
    h = st.number_input("Рост (см)", 140, 220, 170)
    w = st.number_input("Вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ"):
        st.session_state.data.update({'h': h, 'w': w})
        next_step()

elif st.session_state.step == 6:
    st.header("Ваша цель")
    st.session_state.data['goal'] = st.selectbox("", ["Сбросить вес", "Рельеф", "Энергия"])
    if st.button("ВЫБРАТЬ"): next_step()

elif st.session_state.step == 7:
    st.header("Активность")
    st.session_state.data['act'] = st.select_slider("", options=["Низкая", "Средняя", "Высокая"])
    if st.button("ПРОДОЛЖИТЬ"): next_step()

elif st.session_state.step == 8:
    st.header("Исключения")
    st.image("https://images.unsplash.com/photo-1544022613-e87ca75a784a?q=80&w=1000", use_container_width=True)
    ex = st.multiselect("Что не добавлять в меню?", ["Мясо", "Рыба", "Молочка", "Орехи"])
    st.session_state.data['ex'] = ex
    if st.button("АДАПТИРОВАТЬ"): next_step()

elif st.session_state.step == 9:
    st.header("Сладости")
    st.session_state.data['sweets'] = st.radio("Оставить десерты?", ["Да, обязательно", "Нет"], horizontal=True)
    if st.button("СОХРАНИТЬ"): next_step()

elif st.session_state.step == 10:
    st.header("Время готовки")
    st.radio("Сколько есть времени?", ["До 20 мин", "До 45 мин", "Без ограничений"])
    if st.button("ФИНАЛИЗИРОВАТЬ"): next_step()

elif st.session_state.step == 11:
    st.header("ИДЕТ АНАЛИЗ...")
    status = st.empty()
    bar = st.progress(0)
    msgs = ["Анализ метаболизма...", "Подбор рецептов...", "Генерация PDF..."]
    for i, m in enumerate(msgs):
        status.write(f"**{m}**")
        bar.progress((i+1)*33)
        time.sleep(1.5)
    next_step()

elif st.session_state.step == 12:
    st.balloons()
    st.header("ВАШ ПЛАН ГОТОВ!")
    name = st.session_state.data.get('name', '')
    st.write(f"**{name}**, расчет окончен. Мы подготовили для вас идеальное Кето-меню.")
    st.info("Норма: 1850 ккал | Б: 90г | Ж: 150г | У: 25г")
    
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                label="📥 СКАЧАТЬ ПЛАН (PDF)",
                data=f,
                file_name="Keto_Platinum_Plan.pdf",
                mime="application/pdf"
            )
    except:
        st.error("Файл PDF не найден. Загрузите его на GitHub!")
    
    if st.button("ПРОЙТИ ЗАНОВО"):
        st.session_state.step = 1
        st.rerun()
