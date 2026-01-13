import streamlit as st
import time

# --- НАСТРОЙКИ СТРАНИЦЫ ---
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="🥑", layout="centered")

# --- АДАПТИВНЫЙ LUXE ДИЗАЙН ---
style = """
<style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    h1 { color: #FFD700 !important; font-size: 28px !important; text-align: center; text-transform: uppercase; margin-bottom: 5px; margin-top: 0px;}
    h2 { color: #FFD700 !important; font-size: 22px !important; text-align: center; margin-bottom: 10px; }
    
    /* Кнопка для пальца - БОЛЬШАЯ И ПО ЦЕНТРУ */
    .stButton>button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); 
        color: black !important; border-radius: 15px; font-weight: bold; 
        width: 100%; height: 3.8em; border: none; font-size: 18px !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
        margin-top: 15px; /* Отступ сверху */
    }
    
    div[data-testid="stMarkdownContainer"] p { 
        text-align: center; font-size: 16px; line-height: 1.4; color: #EEEEEE;
    }
    
    /* Красивые картинки с рамкой */
    .stImage > img { border-radius: 15px; border: 1px solid #333; margin-bottom: 10px; }
    
    /* Поля ввода */
    .stTextInput input, .stNumberInput input { background-color: #111; color: white; border: 1px solid #333; }
</style>
"""
st.markdown(style, unsafe_allow_html=True)

# Инициализация
if 'step' not in st.session_state: st.session_state.step = 1
if 'data' not in st.session_state: st.session_state.data = {}
def next_step(): st.session_state.step += 1; st.rerun()

# ================= ЦИКЛ ОПРОСНИКА С КАРТИНКАМИ =================

# ЭКРАН 1: ГЛАВНЫЙ (Авокадо и Кето-набор)
if st.session_state.step == 1:
    st.markdown("<h1>KETO AI<br>PLATINUM</h1>", unsafe_allow_html=True)
    st.image("https://images.unsplash.com/photo-1547592166-23ac45744acd?w=800&auto=format&fit=crop", use_container_width=True)
    st.write("Ваш персональный план трансформации тела на 28 дней. Разработано ИИ.")
    if st.button("НАЧАТЬ АНАЛИЗ"): next_step()

# ЭКРАН 2: ИМЯ (Свежие продукты)
elif st.session_state.step == 2:
    st.header("Знакомство")
    st.image("https://images.unsplash.com/photo-1490474504059-bf6208b606f4?w=800&auto=format&fit=crop", use_container_width=True)
    name = st.text_input("", placeholder="Как вас зовут?")
    if name and st.button("ПРОДОЛЖИТЬ"):
        st.session_state.data['name'] = name
        next_step()

# ЭКРАН 3: ПОЛ (Сбалансированная тарелка)
elif st.session_state.step == 3:
    st.header("Ваш пол")
    st.image("https://images.unsplash.com/photo-1579613832111-ac7dfcc7723f?w=800&auto=format&fit=crop", use_container_width=True)
    st.session_state.data['gender'] = st.radio("", ["Мужской", "Женский"], horizontal=True)
    if st.button("ДАЛЕЕ"): next_step()

# ЭКРАН 4: ВОЗРАСТ (Зеленый салат - здоровье)
elif st.session_state.step == 4:
    st.header("Возраст")
    st.image("https://images.unsplash.com/photo-1512621776951-a57141f2eefd?w=800&auto=format&fit=crop", use_container_width=True)
    st.session_state.data['age'] = st.slider("", 18, 80, 30)
    if st.button("ДАЛЕЕ"): next_step()

# ЭКРАН 5: ЗАМЕРЫ (Измерительная лента и еда)
elif st.session_state.step == 5:
    st.header("Текущие параметры")
    st.image("https://images.unsplash.com/photo-1576673442511-7e39b6545c87?w=800&auto=format&fit=crop", use_container_width=True)
    h = st.number_input("Рост (см)", 140, 220, 170)
    w = st.number_input("Вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ ИМТ"):
        st.session_state.data.update({'h': h, 'w': w})
        next_step()

# ЭКРАН 6: ЦЕЛЬ (Яркий результат)
elif st.session_state.step == 6:
    st.header("Ваша главная цель")
    st.image("https://images.unsplash.com/photo-1507919909716-c8262e491cde?w=800&auto=format&fit=crop", use_container_width=True)
    st.session_state.data['goal'] = st.selectbox("", ["Быстрое похудение", "Рельеф и сушка", "Здоровье и энергия"])
    if st.button("УСТАНОВИТЬ ЦЕЛЬ"): next_step()

# ЭКРАН 7: АКТИВНОСТЬ (Энергия/Спортпит)
elif st.session_state.step == 7:
    st.header("Уровень активности")
    st.image("https://images.unsplash.com/photo-1606923829579-0cb981a83e2e?w=800&auto=format&fit=crop", use_container_width=True)
    st.session_state.data['act'] = st.select_slider("", options=["Низкая", "Средняя", "Высокая"])
    if st.button("ПРОДОЛЖИТЬ"): next_step()

# ЭКРАН 8: ИСКЛЮЧЕНИЯ (Мясное ассорти)
elif st.session_state.step == 8:
    st.header("Предпочтения")
    st.image("https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=800&auto=format&fit=crop", use_container_width=True)
    ex = st.multiselect("Что исключить из меню?", ["Мясо", "Рыба", "Свинина", "Молочка", "Орехи"])
    st.session_state.data['ex'] = ex
    if st.button("АДАПТИРОВАТЬ"): next_step()

# ЭКРАН 9: СЛАДОСТИ (Кето-ягоды и шоколад)
elif st.session_state.step == 9:
    st.header("Десерты")
    st.image("https://images.unsplash.com/photo-1601004890684-d8cbf643f5f2?w=800&auto=format&fit=crop", use_container_width=True)
    st.session_state.data['sweets'] = st.radio("Нужны ли полезные сладости?", ["Да", "Нет"], horizontal=True)
    if st.button("СОХРАНИТЬ"): next_step()

# ЭКРАН 10: ВРЕМЯ (Контейнеры с едой)
elif st.session_state.step == 10:
    st.header("Время на готовку")
    st.image("https://images.unsplash.com/photo-1505253716362-afaea1d3d1af?w=800&auto=format&fit=crop", use_container_width=True)
    st.radio("", ["Быстро (до 20 мин)", "Средне (до 40 мин)", "Люблю готовить"])
    if st.button("ФИНАЛИЗИРОВАТЬ"): next_step()

# ЭКРАН 11: АНАЛИЗ (Без картинки, только процесс)
elif st.session_state.step == 11:
    st.header("АНАЛИЗ ДАННЫХ...")
    status = st.empty(); bar = st.progress(0)
    msgs = ["Синхронизация с базой рецептов...", "Расчет дефицита калорий...", "Генерация персональной книги..."]
    for i, m in enumerate(msgs):
        status.write(f"**{m}**"); bar.progress((i+1)*33); time.sleep(1.3)
    next_step()

# ЭКРАН 12: ФИНАЛ (Праздничный кето-стол)
elif st.session_state.step == 12:
    st.balloons()
    st.header("ВАШ ПЛАН ГОТОВ!")
    st.image("https://images.unsplash.com/photo-1565299624946-b28f40a0ae38?w=800&auto=format&fit=crop", use_container_width=True)
    name = st.session_state.data.get('name', 'Чемпион')
    st.write(f"✅ **{name}**, ИИ сформировал для вас идеальное меню.")
    
    st.markdown("""
    <div style="background: #111; padding: 15px; border-radius: 15px; border: 1px solid #FFD700; margin: 15px 0;">
        <p style="margin:0; color:#FFD700; font-size: 14px;">ВАША ЦЕЛЬ НА ДЕНЬ:</p>
        <p style="margin:5px 0; font-size: 18px; font-weight: bold;">1850 ккал</p>
        <p style="margin:0; font-size: 14px; color: #CCC;">Б: 90г | Ж: 150г | У: 25г</p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(label="📥 СКАЧАТЬ PDF ПЛАН", data=f, file_name=f"Keto_Plan_{name}.pdf", mime="application/pdf")
    except: st.error("Файл PDF не найден на GitHub.")
    
    if st.button("ПРОЙТИ ЗАНОВО"): st.session_state.step = 1; st.rerun()
