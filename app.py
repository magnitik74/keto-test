import streamlit as st
import time

# 1. СТАБИЛЬНЫЙ ПРЕМИУМ ДИЗАЙН
CSS = """
<style>
    .stApp { background-color: #050505; color: #FFFFFF; font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; }
    h1, h2, h3 { color: #FFD700 !important; text-align: center; text-transform: uppercase; letter-spacing: 2px; }
    .stButton>button { 
        background: linear-gradient(145deg, #FFD700 0%, #B8860B 100%);
        color: black !important; border-radius: 50px; border: none;
        padding: 20px; font-weight: bold; width: 100%; font-size: 20px;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3); transition: 0.3s;
    }
    .stButton>button:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(255, 215, 0, 0.5); }
    .stProgress > div > div > div > div { background-image: linear-gradient(to right, #B8860B, #FFD700); }
    div[data-testid="stMarkdownContainer"] p { font-size: 18px; text-align: center; color: #CCCCCC; }
    .card { background: #111111; padding: 25px; border-radius: 20px; border: 1px solid #222; margin-bottom: 20px; }
</style>
"""

st.set_page_config(page_title="KETO AI PLATINUM", page_icon="💎", layout="centered")
st.markdown(CSS, unsafe_allow_index=True)

# Инициализация системы экранов
if 'step' not in st.session_state:
    st.session_state.step = 1
    st.session_state.data = {}

def next_step():
    st.session_state.step += 1
    st.rerun()

# --- ЛОГИКА ЭКРАНОВ ---

# ЭКРАН 1: ИНТРО
if st.session_state.step == 1:
    st.markdown("<h1>KETO AI <br>PLATINUM EDITION</h1>", unsafe_allow_index=True)
    st.image("https://images.unsplash.com/photo-1524182620199-a93f4136efac?q=80&w=1000") # Роскошный завтрак
    st.write("Добро пожаловать в закрытый клуб персонального здоровья. Наш ИИ создаст для вас план, который изменит всё.")
    if st.button("НАЧАТЬ АНАЛИЗ МЕТАБОЛИЗМА"):
        next_step()

# ЭКРАН 2: ИМЯ И ПОЛ
elif st.session_state.step == 2:
    st.header("Шаг 1: Знакомство")
    name = st.text_input("Как к вам обращаться?", placeholder="Ваше имя")
    gender = st.radio("Ваш пол", ["Мужской", "Женский"], horizontal=True)
    if name and st.button("ПРОДОЛЖИТЬ"):
        st.session_state.data['name'] = name
        next_step()

# ЭКРАН 3: ВОЗРАСТ
elif st.session_state.step == 3:
    st.header("Шаг 2: Возраст")
    st.write("Возраст влияет на скорость метаболизма и усвоение кетонов.")
    age = st.slider("Сколько вам полных лет?", 18, 80, 30)
    if st.button("ЗАФИКСИРОВАТЬ ВОЗРАСТ"):
        st.session_state.data['age'] = age
        next_step()

# ЭКРАН 4: РОСТ/ВЕС
elif st.session_state.step == 4:
    st.header("Шаг 3: Антропометрия")
    h = st.number_input("Ваш рост (см)", 140, 220, 170)
    w = st.number_input("Текущий вес (кг)", 40, 200, 85)
    if st.button("РАССЧИТАТЬ ИМТ"):
        st.session_state.data['height'] = h
        st.session_state.data['weight'] = w
        next_step()

# ЭКРАН 5: ЦЕЛЬ
elif st.session_state.step == 5:
    st.header("Шаг 4: Главная цель")
    goal = st.selectbox("Чего мы хотим достичь?", 
                        ["Экстремальное похудение", "Плавное снижение веса", "Рельеф и мышцы", "Энергия и биохакинг"])
    target_w = st.number_input("Желаемый вес (кг)", 40, 150, 70)
    if st.button("УСТАНОВИТЬ ЦЕЛЬ"):
        st.session_state.data['target'] = target_w
        next_step()

# ЭКРАН 6: ФИЗИЧЕСКАЯ АКТИВНОСТЬ
elif st.session_state.step == 6:
    st.header("Шаг 5: Энергозатраты")
    act = st.select_slider("Ваш уровень активности", 
                           options=["Сидячий (офис)", "Легкие прогулки", "Тренировки 3 раза в неделю", "Профи спорт"])
    if st.button("УЧЕСТЬ НАГРУЗКИ"):
        st.session_state.data['activity'] = act
        next_step()

# ЭКРАН 7: ИСКЛЮЧЕНИЯ (МЯСО/РЫБА)
elif st.session_state.step == 7:
    st.header("Шаг 6: Пищевые привычки")
    st.image("https://images.unsplash.com/photo-1544022613-e87ca75a784a?q=80&w=1000") # Стейк
    excl = st.multiselect("Что мы убираем из рациона?", 
                          ["Свинина", "Говядина", "Рыба", "Морепродукты", "Молочные продукты", "Яйца", "Орехи"])
    if st.button("АДАПТИРОВАТЬ МЕНЮ"):
        st.session_state.data['exclusions'] = excl
        next_step()

# ЭКРАН 8: СЛАДКОЕЖКА
elif st.session_state.step == 8:
    st.header("Шаг 7: Сладости")
    sweet = st.radio("Сложно ли вам отказаться от сладкого?", 
                     ["Да, нужен полезный десерт", "Нет, я кремень"])
    if st.button("СОХРАНИТЬ ПРЕДПОЧТЕНИЯ"):
        st.session_state.data['sweets'] = sweet
        next_step()

# ЭКРАН 9: ВРЕМЯ НА ГОТОВКУ
elif st.session_state.step == 9:
    st.header("Шаг 8: Время")
    cook = st.radio("Сколько вы готовы тратить на готовку?", 
                    ["До 30 минут (быстрые рецепты)", "Люблю готовить сложные блюда"])
    if st.button("ПОДОБРАТЬ РЕЦЕПТЫ"):
        next_step()

# ЭКРАН 10: СТОП-ФАКТОРЫ
elif st.session_state.step == 10:
    st.header("Шаг 9: Здоровье")
    st.write("Есть ли у вас аллергии или хронические заболевания?")
    health = st.text_area("Напишите кратко или оставьте пустым", placeholder="Например: аллергия на лактозу")
    if st.button("ПОСЛЕДНИЙ ШАГ"):
        next_step()

# ЭКРАН 11: МАГИЯ ИИ (ОЖИДАНИЕ)
elif st.session_state.step == 11:
    st.header("ГЕНЕРАЦИЯ ПЛАНА...")
    placeholder = st.empty()
    bar = st.progress(0)
    
    messages = [
        "🤖 Анализирую метаболический профиль...",
        "⚖️ Рассчитываю идеальный дефицит калорий...",
        "🍳 Подбираю рецепты из базы (2500+ блюд)...",
        "🍰 Адаптирую десерты под КБЖУ...",
        "📅 Формирую список покупок на 4 недели...",
        "✨ Финализирую вашу Platinum книгу..."
    ]
    
    for i, msg in enumerate(messages):
        placeholder.markdown(f"<h3>{msg}</h3>", unsafe_allow_index=True)
        bar.progress((i + 1) * 16)
        time.sleep(1.8)
    
    st.session_state.step = 12
    st.rerun()

# ЭКРАН 12: РЕЗУЛЬТАТ И СКАЧИВАНИЕ
elif st.session_state.step == 12:
    st.balloons()
    st.markdown("<h1>ВАШ ПЛАН ГОТОВ!</h1>", unsafe_allow_index=True)
    
    # Блок БЖУ
    st.markdown(f"""
    <div class="card">
        <p style="color:#FFD700; font-size: 22px;"><b>РЕЗУЛЬТАТ ДЛЯ {st.session_state.data['name'].upper()}</b></p>
        <p>Ваша дневная норма: <b>1920 ккал</b></p>
        <hr style="border-color: #333;">
        <div style="display: flex; justify-content: space-around;">
            <div>БЕЛКИ<br><b style="color:white">95г</b></div>
            <div>ЖИРЫ<br><b style="color:white">155г</b></div>
            <div>УГЛЕВОДЫ<br><b style="color:white">22г</b></div>
        </div>
    </div>
    """, unsafe_allow_index=True)
    
    st.write("На основе ваших параметров (цель: " + str(st.session_state.data['target']) + " кг) ИИ сформировал книгу рецептов на 28 дней.")

    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                label="📥 СКАЧАТЬ ПЕРСОНАЛЬНЫЙ ПЛАН (PDF)",
                data=f,
                file_name=f"Keto_Plan_{st.session_state.data['name']}.pdf",
                mime="application/pdf"
            )
    except:
        st.error("Файл PDF не найден. Проверьте имя файла на GitHub.")
    
    if st.button("ПРОЙТИ ЗАНОВО"):
        st.session_state.step = 1
        st.rerun()
