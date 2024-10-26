import streamlit as st

# 簡易認証の設定
def check_password():
    password = st.sidebar.text_input("パスワードを入力してください:", type="password")
    if password != "testtesttest":
        st.error("パスワードが違います。")
        return False
    return True

if not check_password():
    st.stop()

# タイトル
st.title("ユーザー入力表示アプリ")

# ユーザー入力を受け付ける
user_input = st.text_input("ここにテキストを入力してください:")

# HTML形式で表示
if user_input:
    st.markdown(f"<div>{user_input}</div>", unsafe_allow_html=True)