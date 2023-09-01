import streamlit as st
import streamlit_calendar as st_calendar
import webbrowser

st.set_page_config(layout="wide")

st.warning('このページは工事中です。まだ動作しません', icon="⚠️")

hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("""<style>
            .title {
              padding: 20px;
              background-color:rgb(11,42,90);
              color:rgb(235,236,240)}
            .stButton {
              text-align: right
            }
            </style>""", unsafe_allow_html=True)


st.markdown("<h3 class='title'>Ms Planning</h3>", unsafe_allow_html=True)
st.markdown('---')
st.markdown("<h1 class='title' style='text-align: center;'>私たちについて</h1>", unsafe_allow_html=True)
st.markdown("<p class='title'><font size='3'>ご訪問いただき、ありがとうございます。Ms Planningは、あなたの大事な予定までに準備しなければいけないことを考えます。何をいつまでに、どうやって準備するか詳細に教えることができます。あなたは以下の項目に回答するだけです。さあ、一緒に始めましょう。</font></p>", unsafe_allow_html=True)

st.markdown("  ")
st.markdown("  ")
st.markdown("  ")
st.markdown("<h1 style='text-align: center;'>予定の準備を計画しましょう！</h1>", unsafe_allow_html=True)
d = st.date_input('予定の日にち')
event = st.text_input('予定のタイトル', placeholder='結婚式、遠足など')
place = st.text_input('予定の場所')
detail = st.text_area('予定の内容')

if 'plan' not in st.session_state:
  st.session_state['plan'] = False
if 'question' not in st.session_state:
  st.session_state['question'] = False

if st.button('準備計画を作成する'):
  st.session_state['plan'] = True

if st.session_state['plan']:
  st.markdown("  ")
  st.markdown("  ")
  st.markdown("<h1 style='text-align: center;'>計画が作成されました！</h1>", unsafe_allow_html=True)
  st.markdown("  ")
  st.markdown("  ")
  st_calendar.calendar()
  st.info('ここに作成された計画が記載されます')
  option = st.text_area('追加の要望')
  st.button('要望を送信する')
  question = st.text_area('システムに質問する')
  if st.button('質問を送信する'):
    st.session_state['question'] = True
  if st.session_state['question']:
    st.info('ここにシステムからの返答が記載されます')

  if st.button('Googleカレンダーに予定を記入する'):
    webbrowser.open_new_tab('https://calendar.google.com')