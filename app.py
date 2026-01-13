import streamlit as st
import time

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="💎", layout="centered")

# Адаптивный CSS для мобилок (исправленный и чистый)
style = """
<style>
    .stApp { background-color: #000000; color: #FFFFFF; }
    h1 { color: #FFD700 !important; font-size: 32px !important; text-align: center; text-transform: uppercase; margin-bottom: 0px; }
    h2, h3 { color: #FFD700 !important; text-align: center; }
    
    /* Огромная кнопка для пальца */
    .stButton>button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); 
        color: black !important; 
        border-radius: 15px; 
        font-weight: bold; 
        width: 100%; 
        height: 3.8em; 
        border: none;
        font-size: 18px !important;
        box-shadow: 0 4px 15px rgba(255, 215, 0, 0.3);
    }
    
    div[data-testid="stMarkdownContainer"] p { 
        text-align: center; 
        font-size: 16px; 
        line-height: 1.5;
        color: #EEEEEE;
    }
    
    /* Убираем лишние отступы у картинок */
    .stImage > img { border-radius: 20px; border: 1px solid #222; }
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
    # Заменил ссылку на более стабильную (прямой линк на сочное кето-блюдо)
    st.image("https://images.unsplash.com/photo-1544022613-e87ca75a784a?w=800&auto=format&fit=crop", use_container_width=True)
    st.write("Ваш персональный план трансформации на 28 дней. Разработано ИИ специально под ваши параметры.")
    if st.button("НАЧАТЬ АНАЛИЗ"): next_step()

elif st.session_state.step == 2:
    st.header("Как вас зовут?")
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
    st.header("Параметры тела")
    h = st.number_input("Рост (см)", 140, 220, 170)
    w = st.number_input("Текущий вес (кг)", 40, 200, 80)
    if st.button("РАССЧИТАТЬ"):
        st.session_state.data.update({'h': h, 'w': w})
        next_step()

elif st.session_state.step == 6:
    st.header("Ваша цель")
    st.session_state.data['goal'] = st.selectbox("", ["Сбросить вес", "Рельеф и мышцы", "Энергия и фокус"])
    if st.button("ВЫБРАТЬ"): next_step()

elif st.session_state.step == 7:
    st.header("Активность")
    st.session_state.data['act'] = st.select_slider("", options=["Минимальная", "Средняя", "Высокая", "Спортсмен"])
    if st.button("ПРОДОЛЖИТЬ"): next_step()

elif st.session_state.step == 8:
    st.header("Исключения")
    # Еще одна стабильная картинка (стейк)
    st.image("https://images.unsplash.com/photo-1555939594-58d7cb561ad1?w=800&auto=format&fit=crop", use_container_width=True)
    ex = st.multiselect("Что исключить из меню?", ["Мясо", "Рыба", "Молочка", "Орехи", "Свинина"])
    st.session_state.data['ex'] = ex
    if st.button("АДАПТИРОВАТЬ"): next_step()

elif st.session_state.step == 9:
    st.header("Сладости")
    st.session_state.data['sweets'] = st.radio("Нужны ли кето-десерты?", ["Да, обязательно", "Нет, я кремень"], horizontal=True)
    if st.button("СОХРАНИТЬ"): next_step()

elif st.session_state.step == 10:
    st.header("Готовка")
    st.write("Сколько времени вы готовы тратить?")
    st.radio("", ["До 20 мин", "До 45 мин", "Готов творить шедевры"])
    if st.button("ПОСЛЕДНИЙ ШАГ"): next_step()

elif st.session_state.step == 11:
    st.header("АНАЛИЗ ДАННЫХ...")
    status = st.empty()
    bar = st.progress(0)
    msgs = ["Синхронизация с базой рецептов...", "Расчет дефицита калорий...", "Генерация персональной книги..."]
    for i, m in enumerate(msgs):
        status.write(f"**{m}**")
        bar.progress((i+1)*33)
        time.sleep(1.5)
    next_step()

elif st.session_state.step == 12:
    st.balloons()
    st.header("ВАШ ПЛАН ГОТОВ!")
    name = st.session_state.data.get('name', 'друг')
    st.write(f"✅ **{name}**, ваш Platinum-план на 28 дней успешно сформирован.")
    
    st.markdown("""
    <div style="background: #111; padding: 20px; border-radius: 15px; border: 1px solid #FFD700; margin-bottom: 20px;">
        <p style="margin:0; color:#FFD700;"><b>ВАШИ ПОКАЗАТЕЛИ КБЖУ:</b></p>
        <p style="margin:10px 0; font-size: 20px;"><b>1890 ккал | Б: 95г | Ж: 160г | У: 25г</b></p>
    </div>
    """, unsafe_allow_html=True)
    
    try:
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                label="📥 СКАЧАТЬ LUXE-ПЛАН (PDF)",
                data=f,
                file_name=f"Keto_Platinum_{name}.pdf",
                mime="application/pdf"
            )
    except:
        st.error("Файл PDF не найден. Проверьте, что он загружен на GitHub!")
    
    if st.button("ПРОЙТИ ЗАНОВО"):
        st.session_state.step = 1
        st.rerun()
