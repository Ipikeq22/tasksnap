import streamlit as st

# ---------------------
# 頁面基本設定
# ---------------------
st.set_page_config(
    page_title="互動小遊戲體驗｜Tasksnap",
    page_icon="🍪",
    layout="wide"
)

# ---------------------
# 自訂 CSS
# ---------------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(135deg, #de6262 0%, #ffb88c 100%);
    background-attachment: fixed;
}

div[data-testid="stMarkdownContainer"] h1 {
    text-align: center;
    color: #3E2723;
    font-size: 3rem;
    margin: 2rem 0;
}


</style>
""", unsafe_allow_html=True)

# ---------------------
# 標題
# ---------------------
st.markdown("# 🍪 互動小遊戲體驗")

# ---------------------
# 內容
# ---------------------
st.markdown("""
<div style="
    background: rgba(255, 255, 255, 0.95);
    border-radius: 20px;
    padding: 2rem;
    margin: 2rem auto;
    max-width: 700px;
    text-align: center;
    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
    font-size: 1.2rem;
    line-height: 1.8;
">
    <strong>感謝您認真觀看我們網站！</strong> 🎉<br><br>
    這是我們精心設計的一個<strong>可愛互動小遊戲</strong>，邀請您一起來體驗這個充滿驚喜的幸運餅乾機 🎮<br><br>
    <strong>Have a nice day!</strong> ☀️
</div>
""", unsafe_allow_html=True)

# ---------------------
# 遊戲按鈕
# ---------------------
st.markdown("""
<style>
.learn-more {
  position: relative;
  display: inline-block;
  cursor: pointer;
  outline: none;
  border: 0;
  vertical-align: middle;
  text-decoration: none;
  font-family: inherit;
  font-size: 18px;
  font-weight: 700;
  color: white !important;
  padding: 15px 40px;
  background: linear-gradient(45deg, #FF8C00, #FF7F00);
  border: 3px solid #CC5500;
  border-radius: 12px;
  box-shadow: 0 6px 0 #CC5500, 0 8px 15px rgba(0,0,0,0.3);
  transform-style: preserve-3d;
  transition: all 150ms ease;
}

.learn-more:hover {
  background: linear-gradient(45deg, #FF7F00, #FF8C00);
  transform: translateY(-2px);
  box-shadow: 0 8px 0 #CC5500, 0 10px 20px rgba(0,0,0,0.4);
}

.learn-more:active {
  background: linear-gradient(45deg, #CC5500, #B8860B);
  transform: translateY(4px);
  box-shadow: 0 2px 0 #CC5500, 0 4px 8px rgba(0,0,0,0.2);
}
</style>

<div style="text-align: center; margin: 2rem 0;">
    <a href="https://ipikeq22.github.io/tasksnap_Sweet_Cookie_Bite_Game/" target="_blank" class="learn-more">
        🎮 開始遊戲
    </a>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 遊戲玩法介紹
# ---------------------
st.markdown("""
<div style="text-align: center; color: #3E2723; font-size: 2.5rem; font-weight: 700; margin: 3rem 0 2rem 0;">
🎯 遊戲玩法介紹
</div>
""", unsafe_allow_html=True)

# 步驟1
st.image("1.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>步驟 1：點擊「開始遊戲」</strong><br>
點擊上方的橙色按鈕開始你的幸運之旅
</div>
""", unsafe_allow_html=True)

# 步驟2
st.image("2.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>步驟 2：點擊「給我好運」按鈕</strong><br>
進入遊戲後，點擊畫面中的「給我好運」按鈕
</div>
""", unsafe_allow_html=True)

# 步驟3
st.image("3.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>步驟 3：機器開始晃動</strong><br>
幸運餅乾機會開始晃動，準備掉出神秘的幸運餅乾
</div>
""", unsafe_allow_html=True)

# 步驟4
st.image("4.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>步驟 4：得到幸運籤文</strong><br>
餅乾會展開並顯示你的專屬幸運訊息，也可以點「再來一次」得到不同主題的幸運籤
</div>
""", unsafe_allow_html=True)

# 步驟5
st.image("5.png", use_container_width=True)
st.markdown("""
<div style="background: rgba(255,255,255,0.9); padding: 1rem; border-radius: 10px; margin: 1rem 0; text-align: center; font-size: 1.2rem;">
<strong>步驟 5：分享給朋友</strong><br>
抽到喜歡的籤，可以點擊「分享」，內容會自動複製，你可以把它貼給你的家人朋友們分享
</div>
""", unsafe_allow_html=True)

# ---------------------
# 製作初心
# ---------------------
st.markdown("""
<div style="text-align: center; color: #3E2723; font-size: 2.5rem; font-weight: 700; margin: 3rem 0 2rem 0;">
❤️ 製作初心
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: #011F26; font-size: 1.1rem; line-height: 1.8; text-align: left; max-width: 90%; margin: 2rem auto; font-family: serif; font-weight: bold;">
在這個快節奏繁忙的世界裡，我們希望能做出一款能帶給人們笑容與片刻溫暖的遊戲。就像打開一塊幸運餅乾，裡面藏著一張驚喜小紙條，那種簡單卻真實的快樂，讓人心裡充滿期待。
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: #011F26; font-size: 1.1rem; line-height: 1.8; text-align: left; max-width: 90%; margin: 1rem auto; font-family: serif; font-weight: bold;">
Lucky Cookie Bite 的誕生，就是想把這樣的感覺傳遞給每一位玩家。無論是小朋友還是大人，都能在遊戲裡輕鬆拽取屬於自己的幸運，在繽紛的餅乾世界裡，找到一點點童心與快樂。
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: #011F26; font-size: 1.1rem; line-height: 1.8; text-align: left; max-width: 90%; margin: 1rem auto; font-family: serif; font-weight: bold;">
如果你能在遊戲中，因為一個小小的幸運而展露笑容，那就是我們製作這款遊戲最初、也是最真誠的願望。
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style="color: #011F26; font-size: 1.1rem; text-align: right; max-width: 90%; margin: 2rem auto 0 auto; font-family: serif; font-weight: 600;">
Tasksnap團隊敬上
</div>
""", unsafe_allow_html=True)

# ---------------------
# 頁尾
# ---------------------
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: rgba(255,255,255,0.8); margin-top: 2rem;">
© 2025 Tasksnap App | 互動小遊戲體驗 🍪
</div>
""", unsafe_allow_html=True)