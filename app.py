import streamlit as st
import time

# 1. СУПЕР-БЕЗОПАСНЫЙ ДИЗАЙН (без многострочных блоков, которые бесят Python 3.13)
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="💎")

# Внедряем стиль одной строкой
style = "<style>@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700&display=swap'); .stApp { background-color: #000000; color: #FFFFFF; font-family: 'Inter', sans-serif; } .stButton>button { background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); color: black !important; border-radius: 30px; border: none; padding: 20px; font-weight: bold; width: 100%; font-size: 20px; box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3); } h1, h2, h3 { color: #FFD700 !important; text-align: center; } div[data-testid='stMarkdownContainer'] p { font-size: 18px; text-align: center; } .stProgress > div > div > div > div { background-color: #FFD700; } </style>"
st.markdown(style, unsafe_allow_index=True)

# Инициализация сессии
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.data = {}

def next_step():
    st.session_state.step += 1
    st.rerun()

# --- ЭКРАНЫ ---

if st.session_state.step == 1:
    st.markdown("<h1>KETO AI PLATINUM</h1>", unsafe_allow_index=True)
    st.image("https://images.unsplash.com/photo-1524182620199-a93f4136efac?q=80&w=1000")
    st.write("Начните путь к идеальному телу с персональным ИИ-анализом.")
    if st.button("НАЧАТЬ АНАЛИЗ"): next_step()

elif st.session_state.step == 2:
    st.header("Как вас зовут?")
    name = st.text_input("", placeholder="Ваше имя")
    if name and st.button("ДАЛЕЕ"):
        st.session_state.data['name'] = name
        next_step()

elif st.session_state.step == 3:
    st.header("Ваш пол")
    gender = st.radio("", ["Мужской", "Женский"], horizontal=True)
    if st.button("ПРОДОЛЖИТЬ"):
        st.session_state.data['gender'] = gender
        next_step()

elif st.session_state.step == 4:
    st.header("Возраст")
    age = st.slider("", 18, 80, 30)
    if st.button("СОХРАНИТЬ"):
        st.session_state.data['age'] = age
        next_step()

elif st.session_state.step == 5:
    st.header("Ваш рост и вес")
    h = st.number_input("Рост (см)", 140, 220, 170)
    w = st.number_input("Вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ"):
        st.session_state.data.update({'h': h, 'w': w})
        next_step()

elif st.session_state.step == 6:
    st.header("Ваша цель")
    goal = st.selectbox("", ["Экстремальное похудение", "Плавное снижение", "Набор массы", "Биохакинг"])
    if st.button("УСТАНОВИТЬ ЦЕЛЬ"):
        next_step()

elif st.session_state.step == 7:
    st.header("Активность")
    act = st.select_slider("", options=["Низкая", "Средняя", "Высокая", "Атлет"])
    if st.button("ДАЛЕЕ →"): next_step()

elif st.session_state.step == 8:
    st.header("Исключения")
    st.write("Что мы не будем добавлять в ваш план?")
    ex = st.multiselect("", ["Мясо", "Рыба", "Молочка", "Орехи", "Яйца", "Свинина"])
    if st.button("АДАПТИРОВАТЬ РЕЦЕПТЫ"):
        st.session_state.data['ex'] = ex
        next_step()

elif st.session_state.step == 9:
    st.header("Сладкое")
    st.write("Нужны ли Кето-десерты в меню?")
    sw = st.radio("", ["Да, обязательно", "Нет, я справлюсь"])
    if st.button("СОХРАНИТЬ"): next_step()

elif st.session_state.step == 10:
    st.header("Время на готовку")
    t = st.radio("", ["До 20 мин", "До 45 мин", "Готов на кулинарные шедевры"])
    if st.button("ПОЧТИ ГОТОВО"): next_step()

elif st.session_state.step == 11:
    st.header("ГЕНЕРАЦИЯ ПЛАНА")
    msg = st.empty()
    bar = st.progress(0)
    texts = ["🤖 Синхронизация с БД рецептов...", "⚖️ Расчет метаболической карты...", "🍳 Исключение запрещенных продуктов...", "📅 Финализация PDF..."]
    for i, t in enumerate(texts):
        msg.write(f"### {t}")
        bar.progress((i+1)*25)
        time.sleep(1.5)
    next_step()

elif st.session_state.step == 12:
    st.balloons()
    st.header("ВАШ ПЛАН ГОТОВ!")
    st.markdown(f"### Результат для {st.session_state.data.get('name', 'клиента')}")
    st.info("Ваша норма: 1900 ккал | Б: 95г | Ж: 160г | У: 20г")
    
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(label="📥 СКАЧАТЬ ПЛАН (PDF)", data=f, file_name="Keto_Platinum_Plan.pdf", mime="application/pdf")
    except:
        st.error("Файл PDF не найден. Убедитесь, что загрузили Personal_Keto_Plan.pdf на GitHub")
    
    if st.button("Пройти заново"):
        st.session_state.step = 1
        st.rerun()
