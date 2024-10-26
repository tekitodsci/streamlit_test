import streamlit as st

# タイトル
st.title("ユーザー入力表示アプリ")

# ユーザー入力を受け付ける
user_input = st.text_input("ここにテキストを入力してください:")

# HTML形式で表示
if user_input:
    st.markdown(f"<div>{user_input}</div>", unsafe_allow_html=True)