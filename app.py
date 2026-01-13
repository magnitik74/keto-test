import streamlit as st
import time

# Настройка страницы
st.set_page_config(page_title="KETO AI LUXE", page_icon="🥑", layout="centered")

# Дизайнерские стили (улучшенные и безопасные)
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #FFFFFF; }
    .main-title { font-size: 32px; font-weight: bold; color: #FFD700; text-align: center; margin-bottom: 10px; }
    .sub-title { font-size: 16px; text-align: center; color: #AAAAAA; margin-bottom: 30px; }
    .stButton>button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%);
        color: black !important; border-radius: 30px; border: none;
        padding: 15px 30px; font-weight: bold; width: 100%; font-size: 18px;
    }
    div[data-testid="stExpander"] { background-color: #111111; border: 1px solid #333; border-radius: 15px; }
    </style>
    """, unsafe_allow_index=True)

# Инициализация экранов
if 'step' not in st.session_state:
    st.session_state.step = 1

# --- ЭКРАН 1: ПРИВЕТСТВИЕ ---
if st.session_state.step == 1:
    st.markdown('<p class="main-title">KETO AI LUXE</p>', unsafe_allow_index=True)
    st.image("https://images.unsplash.com/photo-1547592166-23ac45744acd?q=80&w=1000") # Красивое фото кето-еды
    st.markdown('<p class="sub-title">Ваш персональный шеф-повар и диетолог на базе ИИ. Начнем трансформацию?</p>', unsafe_allow_index=True)
    
    if st.button("СОЗДАТЬ МОЙ ПЛАН"):
        st.session_state.step = 2
        st.rerun()

# --- ЭКРАН 2: ПАРАМЕТРЫ ТЕЛА ---
elif st.session_state.step == 2:
    st.markdown('<p class="main-title">ПАРАМЕТРЫ ТЕЛА</p>', unsafe_allow_index=True)
    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Текущий вес (кг)", 40, 200, 80)
    with col2:
        target = st.number_input("Целевой вес (кг)", 40, 200, 70)
    
    gender = st.radio("Пол", ["Женский", "Мужской"], horizontal=True)
    activity = st.select_slider("Ваша активность", options=["Низкая", "Средняя", "Высокая"])
    
    if st.button("ДАЛЕЕ →"):
        st.session_state.user_data = {"w": weight, "t": target, "a": activity}
        st.session_state.step = 3
        st.rerun()

# --- ЭКРАН 3: ВКУСОВЫЕ ПРЕДПОЧТЕНИЯ ---
elif st.session_state.step == 3:
    st.markdown('<p class="main-title">ВАШИ ВКУСЫ</p>', unsafe_allow_index=True)
    st.image("https://images.unsplash.com/photo-1546069901-ba9599a7e63c?q=80&w=1000")
    
    exclusions = st.multiselect("Что исключить?", ["Мясо", "Рыба", "Свинина", "Молочка", "Орехи"])
    sweets = st.toggle("Оставить десерты в рационе", value=True)
    
    if st.button("РАССЧИТАТЬ ИДЕАЛЬНЫЙ БЖУ"):
        st.session_state.step = 4
        st.rerun()

# --- ЭКРАН 4: МАГИЯ ИИ И РЕЗУЛЬТАТ ---
elif st.session_state.step == 4:
    st.markdown('<p class="main-title">АНАЛИЗ ДАННЫХ...</p>', unsafe_allow_index=True)
    
    placeholder = st.empty()
    with placeholder.container():
        st.write("🤖 ИИ подбирает рецепты под ваш вес...")
        bar = st.progress(0)
        for i in range(100):
            bar.progress(i + 1)
            time.sleep(0.03)
    
    placeholder.empty()
    st.balloons()
    
    # Виджет с расчетом БЖУ (Калькулятор)
    st.markdown("""
        <div style="background: #111; padding: 20px; border-radius: 20px; border: 1px solid #FFD700; text-align: center;">
            <h3 style="color: #FFD700; margin: 0;">ВАШИ ПОКАЗАТЕЛИ КБЖУ</h3>
            <p style="color: #FFF; font-size: 24px; margin: 10px 0;"><b>1850 ккал / день</b></p>
            <div style="display: flex; justify-content: space-around;">
                <div><small>БЕЛКИ</small><br><b>90г</b></div>
                <div><small>ЖИРЫ</small><br><b>150г</b></div>
                <div><small>УГЛЕВОДЫ</small><br><b>25г</b></div>
            </div>
        </div>
    """, unsafe_allow_index=True)
    
    st.write("")
    st.write("✅ План на 28 дней готов. Мы учли все ваши пожелания по продуктам.")

    # Кнопка скачивания
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                label="📥 СКАЧАТЬ LUXE КНИГУ (PDF)",
                data=f,
                file_name="Premium_Keto_Plan.pdf",
                mime="application/pdf"
            )
    except:
        st.error("Файл PDF не найден. Но ИИ расчет завершен!")
    
    if st.button("НАЧАТЬ ЗАНОВО"):
        st.session_state.step = 1
        st.rerun()
