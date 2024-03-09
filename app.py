import streamlit as st

# ダークモードのヘッダー表示
st.markdown("<h1 style='text-align: center; color: black; background-color: #0e1117; padding: 10px;'>ストリームリット テストアプリ</h1>", unsafe_allow_html=True)

# カスタムスタイルのタイトル表示
st.markdown("<h2 style='text-align: center; color: white; background-color: #1e2022; padding: 10px;'>Webアプリ開発進行中</h2>", unsafe_allow_html=True)

# スタイリッシュなテキスト表示
st.markdown("<p style='text-align: center; color: #adb5bd;'>生活向上アプリ</p>", unsafe_allow_html=True)

# スライダー（カスタムスタイルで0~100）
st.markdown("## スライダー")
weight = st.slider("今日の体重は？", 0, 100, 50)
st.markdown(f"<h3 style='text-align: center; color: #adb5bd;'>今の体重は {weight}kgです</h3>", unsafe_allow_html=True)

# カスタムボタン
st.markdown("## 今日の天気は？")
if st.button("晴れ"):
    st.success("今日も元気に！")
elif st.button("雨"):
    st.error("傘を忘れずに！")

# テキスト入力（スタイリッシュ）
st.markdown("## やることリスト")
task = st.text_input("今日やること", key="do")
if task:
    st.markdown(f"<p style='color: #adb5bd;'>今日のタスク: {task}</p>", unsafe_allow_html=True)

# チェックボックス（カスタムスタイル）
st.markdown("## ごみ捨てチェックリスト")
is_agree = st.checkbox("ごみ捨てた？")
if is_agree:
    st.success("お疲れ様！")
else:
    st.warning("忘れずに！")
