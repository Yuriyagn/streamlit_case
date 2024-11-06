# coding:utf-8
# @Version  : 1.0
# @Author   : yuri
# @File     : streamlit_app.py
# @Time     : 2024/11/6 17:08
import streamlit as st

name = st.text_input('请输入你的名字')
age = st.slider('请选择你的年龄', 0, 100, 25)
st.write(f'你好，{name}! 你的年龄是{age}岁。')

