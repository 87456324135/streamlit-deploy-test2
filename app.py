import streamlit as st   
from ment import ment
import random

st.title("오늘의 한마디")

random_ment = random.choice(ment)
text1 = st.text_input("이름을 입력해주세요.")

if st.button("확인") and text1:
    st.success(f"{text1}님 {random_ment}")