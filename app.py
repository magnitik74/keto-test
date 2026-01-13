import streamlit as st
import time

# 1. НАСТРОЙКИ СТРАНИЦЫ
st.set_page_config(page_title="KETO AI PLATINUM", page_icon="💎", layout="centered")

# 2. ЯДЕРНЫЙ CSS ДЛЯ МОБИЛОК (Центровка и размеры на стероидах)
style = """
<style>
    /* Черный фон */
    .stApp { background-color: #000000; color: #FFFFFF; }

    /* === ПРИНУДИТЕЛЬНАЯ ЦЕНТРОВКА ВСЕГО === */
    /* Это заставляет все блоки внутри приложения выстраиваться по центру */
    [data-testid="stVerticalBlock"] {
        display: flex;
        flex-direction: column;
        align-items: center !important; /* Горизонтальный центр */
        text-align: center;
        width: 100%;
    }
    
    /* Центрируем сами картинки */
    [data-testid="stImage"] {
        display: flex;
        justify-content: center;
        width: 100%;
    }
    .stImage > img {
        border-radius: 20px;
        border: 2px solid #333;
        max-width: 95% !important; /* Чтобы не прилипало к краям */
    }

    /* Заголовки */
    h1 { color: #FFD700 !important; font-size: 32px !important; text-transform: uppercase; margin: 10px 0; }
    h2 { color: #FFD700 !important; font-size: 26px !important; margin: 15px 0; }
    p { font-size: 18px !important; line-height: 1.5; color: #DDD; }

    /* === ОГРОМНЫЕ КНОПКИ ПО ЦЕНТРУ === */
    .stButton { width: 100%; display: flex; justify-content: center; }
    .stButton > button { 
        background: linear-gradient(90deg, #FFD700 0%, #B8860B 100%); 
        color: black !important; 
        border-radius: 25px; 
        font-weight: bold; 
        width: 95% !important; /* Почти во всю ширину */
        height: 4.5em !important; /* Очень высокая */
        border: none;
        font-size: 22px !important; /* Крупный текст */
        box-shadow: 0 6px 25px rgba(255, 215, 0, 0.4);
        margin: 25px auto !important; /* Отступы сверху и снизу */
    }

    /* === ОГРОМНОЕ ПОЛЕ ВВОДА === */
    /* Делаем само поле ввода высоким, ярким и с крупным шрифтом */
    .stTextInput { width: 95% !important; margin
