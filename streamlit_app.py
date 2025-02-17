import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import time

# Заголовок приложения
st.title("Интерактивная анимация в Streamlit")

# Кнопка запуска анимации
if st.button("Запустить анимацию"):
    progress_bar = st.progress(0)
    status_text = st.empty()
    
    fig, ax = plt.subplots()
    x = np.linspace(0, 2*np.pi, 100)
    
    for i in range(100):
        y = np.sin(x + i * 0.1)
        ax.clear()
        ax.plot(x, y, color='royalblue')
        ax.set_ylim([-1, 1])
        st.pyplot(fig)
        progress_bar.progress(i + 1)
        status_text.text(f"Процесс: {i+1}%")
        time.sleep(0.05)
    
    st.success("Анимация завершена!")
