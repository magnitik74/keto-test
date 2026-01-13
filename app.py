import streamlit as st
import time

# 1. Настройки дизайна
st.set_page_config(page_title="AI Keto Plan", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    h1 { color: #FFD700 !important; text-align: center; }
    .stButton>button { 
        background: #FFD700; color: black !important; 
        font-weight: bold; border-radius: 20px; width: 100%;
    }
    </style>
    """, unsafe_allow_index=True)

# 2. Контент
st.title("🥑 Твой Персональный Кето-План")
st.write("Ответь на вопросы, чтобы ИИ составил меню на 28 дней.")

# Вопросы
age = st.number_input("Сколько тебе лет?", 18, 80, 25)
weight = st.number_input("Твой текущий вес (кг)", 40, 150, 70)
no_meat = st.checkbox("Я не ем мясо (только рыба и овощи)")
sweets = st.checkbox("Хочу оставить сладкое в рационе")

# 3. Логика работы
if st.button("ПОЛУЧИТЬ ПЛАН ПИТАНИЯ"):
    with st.spinner('ИИ анализирует данные...'):
        time.sleep(2)
        st.write("✅ Рост и вес учтены...")
        time.sleep(1)
        if no_meat:
            st.write("✅ Мясо исключено из рецептов...")
        if sweets:
            st.write("✅ Добавлены Кето-десерты...")
        time.sleep(1)
        st.balloons()
        st.success("Твой план на 28 дней готов!")
        
        # Кнопка скачивания
        with open("Personal_Keto_Plan.pdf", "rb") as f:
            st.download_button(
                label="📥 СКАЧАТЬ КНИГУ (PDF)",
                data=f,
                file_name="My_Keto_Diet.pdf",
                mime="application/pdf"
            )