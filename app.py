import streamlit as st
import time

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="💎")

# 2. КОРРЕКТНЫЙ ДИЗАЙН (Исправлен параметр на unsafe_allow_html)
style = """
<style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    .stButton>button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); 
        color: black !important; 
        border-radius: 30px; 
        font-weight: bold; 
        width: 100%; 
        height: 3.5em; 
        border: none; 
    }
    h1, h2, h3 { color: #FFD700 !important; text-align: center; }
    .stProgress > div > div > div > div { background-color: #FFD700; }
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

# --- ЦИКЛ ОПРОСНИКА (12 ЭКРАНОВ) ---

if st.session_state.step == 1:
    st.markdown("<h1>KETO AI PLATINUM</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1524182620199-a93f4136efac?q=80&w=1000")
    st.write("Начните трансформацию с персональным ИИ-анализом на 28 дней.")
    if st.button("НАЧАТЬ АНАЛИЗ"): next_step()

elif st.session_state.step == 2:
    st.header("Как к вам обращаться?")
    name = st.text_input("", placeholder="Ваше имя")
    if name and st.button("ДАЛЕЕ"):
        st.session_state.data['name'] = name
        next_step()

elif st.session_state.step == 3:
    st.header("Ваш пол")
    st.session_state.data['gender'] = st.radio("", ["Мужской", "Женский"], horizontal=True)
    if st.button("ПРОДОЛЖИТЬ"): next_step()

elif st.session_state.step == 4:
    st.header("Ваш возраст")
    st.session_state.data['age'] = st.slider("", 18, 80, 30)
    if st.button("СОХРАНИТЬ"): next_step()

elif st.session_state.step == 5:
    st.header("Рост и вес")
    h = st.number_input("Рост (см)", 140, 220, 170)
    w = st.number_input("Текущий вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ ИМТ"):
        st.session_state.data.update({'h': h, 'w': w})
        next_step()

elif st.session_state.step == 6:
    st.header("Цель")
    st.session_state.data['goal'] = st.selectbox("", ["Сбросить вес", "Рельеф", "Энергия"])
    if st.button("УСТАНОВИТЬ"): next_step()

elif st.session_state.step == 7:
    st.header("Активность")
    st.session_state.data['act'] = st.select_slider("", options=["Низкая", "Средняя", "Высокая"])
    if st.button("ДАЛЕЕ"): next_step()

elif st.session_state.step == 8:
    st.header("Исключения")
    ex = st.multiselect("Что не добавлять в меню?", ["Мясо", "Рыба", "Молочка", "Орехи"])
    st.session_state.data['ex'] = ex
    if st.button("ПРИМЕНИТЬ"): next_step()

elif st.session_state.step == 9:
    st.header("Сладости")
    st.session_state.data['sweets'] = st.radio("Оставить десерты?", ["Да", "Нет"])
    if st.button("OK"): next_step()

elif st.session_state.step == 10:
    st.header("Время готовки")
    st.radio("Сколько времени есть?", ["20 мин", "40 мин", "Час+"])
    if st.button("ФИНАЛИЗИРОВАТЬ"): next_step()

elif st.session_state.step == 11:
    st.header("ГЕНЕРАЦИЯ ПЛАНА...")
    status = st.empty()
    bar = st.progress(0)
    msgs = ["Анализ метаболизма...", "Сборка рецептов...", "Генерация PDF..."]
    for i, m in enumerate(msgs):
        status.write(f"### {m}")
        bar.progress((i+1)*33)
        time.sleep(1.5)
    next_step()

elif st.session_state.step == 12:
    st.balloons()
    st.header("ГОТОВО!")
    name = st.session_state.data.get('name', 'друг')
    st.success(f"{name}, ваш план на 28 дней сформирован!")
    st.info("Норма: 1850 ккал | Б: 90г | Ж: 150г | У: 25г")
    
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                label="📥 СКАЧАТЬ КНИГУ (PDF)",
                data=f,
                file_name="Keto_Platinum_Plan.pdf",
                mime="application/pdf"
            )
    except:
        st.error("Файл PDF не найден. Проверьте имя на GitHub.")
    
    if st.button("В НАЧАЛО"):
        st.session_state.step = 1
        st.rerun()
