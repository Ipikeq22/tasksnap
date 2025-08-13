import streamlit as st

# ---------------------
# 頁面基本設定
# ---------------------
st.set_page_config(
    page_title="人才招募｜Tasksnap",
    page_icon="🚀",
    layout="wide"
)

# ---------------------
# 自訂 CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes slideInLeft {
        from { opacity: 0; transform: translateX(-50px); }
        to { opacity: 1; transform: translateX(0); }
    }
    @keyframes bounce {
        0%, 20%, 50%, 80%, 100% { transform: translateY(0); }
        40% { transform: translateY(-10px); }
        60% { transform: translateY(-5px); }
    }
    @keyframes rainbow {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    body {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
        background-attachment: fixed;
    }
    .stApp {
        background: linear-gradient(135deg, #f0f8ff 0%, #e6f3ff 50%, #fff5e6 100%);
    }
    .main-title {
        text-align: center;
        font-size: 54px;
        color: #003366;
        font-weight: 900;
        letter-spacing: 4px;
        margin-bottom: 8px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .subtitle {
        text-align: center;
        font-size: 20px;
        color: #234;
        margin-bottom: 36px;
        margin-top: 8px;
        font-weight: 500;
        letter-spacing: 1.5px;
        line-height: 1.8;
    }
    .section-title {
        text-align: center;
        color: #0055A5;
        font-size: 28px;
        font-weight: 800;
        margin-top: 48px;
        margin-bottom: 18px;
        letter-spacing: 2px;
    }
    .card-list {
        display: flex;
        flex-direction: column;
        align-items: center;
        margin: 0 auto 40px auto;
        background: linear-gradient(135deg, #ffffff, #f8fbff, #fff8f0);
        border-radius: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.12), 0 8px 20px rgba(0,85,165,0.15);
        padding: 45px 40px 30px 40px;
        max-width: 580px;
        border: 2px solid transparent;
        background-clip: padding-box;
        transition: all 0.4s ease;
        animation: slideInLeft 1s ease-out;
    }
    .card-list:hover {
        transform: translateY(-5px);
        box-shadow: 0 30px 70px rgba(0,0,0,0.18), 0 12px 30px rgba(0,85,165,0.2), 0 0 40px rgba(255,153,0,0.1);
    }
    .card-item {
        width: 100%;
        margin-bottom: 28px;
        background: linear-gradient(135deg, #f7faff, #ffffff);
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,85,165,0.1), 0 3px 10px rgba(0,0,0,0.05);
        padding: 25px 28px 18px 28px;
        text-align: left;
        border-left: 4px solid #FF9900;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
        position: relative;
        overflow: hidden;
    }
    .card-item::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 2px;
        background: linear-gradient(90deg, #FF9900, #0055A5);
        transform: scaleX(0);
        transition: transform 0.4s ease;
    }
    .card-item:hover {
        transform: translateX(8px) scale(1.02);
        box-shadow: 0 15px 40px rgba(0,85,165,0.15), 0 5px 15px rgba(255,153,0,0.2);
        border-left-width: 6px;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .card-item:hover::before {
        transform: scaleX(1);
    }
    .card-title {
        font-size: 20px;
        color: #FF9900;
        font-weight: bold;
        margin-bottom: 6px;
        letter-spacing: 1px;
    }
    .card-desc {
        font-size: 16px;
        color: #234;
        margin-left: 8px;
        margin-bottom: 2px;
        line-height: 1.7;
    }
    .offer-list {
        margin-top: 0;
        margin-bottom: 32px;
        padding: 28px 36px 18px 36px;
    }
    .offer-item {
        font-size: 17px;
        color: #003366;
        margin-bottom: 10px;
        text-align: left;
        width: 100%;
        padding-left: 8px;
        position: relative;
    }
    .offer-item:before {
        content: "•";
        color: #FF9900;
        font-size: 22px;
        position: absolute;
        left: -14px;
        top: -2px;
    }
    .join-block {
        text-align: center;
        font-size: 18px;
        line-height: 2;
        margin-bottom: 32px;
        margin-top: 12px;
    }
    .cta-block {
        text-align: center;
        font-size: 20px;
        margin-top: 40px;
        margin-bottom: 24px;
        font-weight: 600;
        letter-spacing: 1.5px;
    }
    .cta-block:hover {
        transform: perspective(1000px) rotateX(5deg) scale(1.05) !important;
        box-shadow: 0 25px 60px rgba(102,126,234,0.7), 0 10px 30px rgba(0,0,0,0.2), 0 0 50px rgba(240,147,251,0.6) !important;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 40px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# 標題
# ---------------------
st.markdown("<div class='main-title'>🚀 人才招募</div>", unsafe_allow_html=True)
st.markdown("""
<div class='subtitle'>
我們相信，<b>每個好點子，都需要一群有熱情的夥伴一起實現。</b><br><br>
Tasksnap由一群大學生自主開發，<br>
我們期待更多志同道合的夥伴一起加入，<br>
從校園出發，打造最安全、最有保障的接案環境！
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------
# 招募職缺說明（美化卡片式）
# ---------------------
st.markdown("<div class='section-title'>🔍 我們正在尋找的角色</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card-list'>
    <div class='card-item'>
        <div class='card-title'>✅ UI/UX 設計師</div>
        <div class='card-desc'>- 協助進階優化平台介面與使用者流程</div>
        <div class='card-desc'>- 熟悉 Figma 尤佳</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ 前端工程師</div>
        <div class='card-desc'>- 熟悉 HTML / CSS / JavaScript</div>
        <div class='card-desc'>- 若有開發經驗更好</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ 後端開發人員</div>
        <div class='card-desc'>- 熟悉 Python / Firebase / Google Sheets API</div>
        <div class='card-desc'>- 能協助接入金流、會員系統</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ 行銷企劃 / 校園大使</div>
        <div class='card-desc'>- 擅長社群經營、文案撰寫</div>
        <div class='card-desc'>- 協助推廣平台與媒合更多使用者</div>
    </div>
    <div class='card-item'>
        <div class='card-title'>✅ 遊戲製作人員</div>
        <div class='card-desc'>- 擅長 Unity 操作</div>
        <div class='card-desc'>- 製作跨平台遊戲</div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 福利說明（美化卡片式）
# ---------------------
st.markdown("<div class='section-title'>🌱 我們提供什麼？</div>", unsafe_allow_html=True)
st.markdown("""
<div class='card-list offer-list'>
    <div class='offer-item'>彈性、自由的遠端合作環境</div>
    <div class='offer-item'>實際產品開發經驗，強化履歷</div>
    <div class='offer-item'>參與跨校、跨科系合作，擴展人脈</div>
    <div class='offer-item'>共同見證校園接案新模式的誕生</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 如何加入
# ---------------------
st.markdown("<div class='section-title'>📩 如何加入我們？</div>", unsafe_allow_html=True)
st.markdown("""
<div class='join-block'>
如果你熱愛創造、喜歡挑戰，<br>
請將 <b>履歷或作品集</b> 寄至：<br>
<b>campusfreelance@example.com</b><br>
我們會盡快與你聯繫，安排進一步討論！
</div>
""", unsafe_allow_html=True)

# ---------------------
# 行動號召
# ---------------------
st.markdown("""
<div class='cta-block' style="
    background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
    border-radius: 25px;
    box-shadow: 0 15px 35px rgba(102,126,234,0.4), 0 5px 15px rgba(0,0,0,0.1);
    padding: 40px 20px 35px 20px;
    margin: 0 auto 32px auto;
    max-width: 600px;
    text-align: center;
    font-size: 22px;
    font-weight: 700;
    letter-spacing: 1.5px;
    color: #ffffff;
    position: relative;
    overflow: hidden;
    animation: pulse-glow 3s ease-in-out infinite;
    transform: perspective(1000px) rotateX(5deg);
    transition: all 0.3s ease;
">
    一起用行動改變校園接案生態，<br>
    <span style="color:#ffffff; font-size:24px; text-shadow: 0 0 10px rgba(255,255,255,0.5);"><b>讓每個學生的努力都被看見，並得到應有的保障。</b></span><br>
    <span style="font-size:28px; color:#ffffff; text-shadow: 0 0 15px rgba(255,255,255,0.7);">🚀 加入我們，從現在開始！</span>
</div>
<style>
@keyframes pulse-glow {
    0%, 100% { 
        box-shadow: 0 15px 35px rgba(102,126,234,0.4), 0 5px 15px rgba(0,0,0,0.1), 0 0 20px rgba(102,126,234,0.3);
        transform: perspective(1000px) rotateX(5deg) scale(1);
    }
    50% { 
        box-shadow: 0 20px 50px rgba(102,126,234,0.6), 0 8px 25px rgba(0,0,0,0.15), 0 0 40px rgba(240,147,251,0.5);
        transform: perspective(1000px) rotateX(5deg) scale(1.02);
    }
}
</style>
""", unsafe_allow_html=True)

# ---------------------
# 團隊文化區塊
# ---------------------
st.markdown("<div class='section-title'>🌈 團隊文化</div>", unsafe_allow_html=True)
culture1, culture2, culture3 = st.columns(3)
with culture1:
    st.markdown("""
    <div style="text-align:center; padding:25px 20px; background:linear-gradient(135deg, #ffffff, #f0f8ff); border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <div style="font-size:50px; margin-bottom:15px;">🚀</div>
        <h4 style="color:#0055A5; margin-bottom:10px;">創新至上</h4>
        <p style="color:#666; font-size:14px; line-height:1.6;">鼓勵創新思維，每個想法都值得被討論和實現</p>
    </div>
    """, unsafe_allow_html=True)
with culture2:
    st.markdown("""
    <div style="text-align:center; padding:25px 20px; background:linear-gradient(135deg, #ffffff, #fff8f0); border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <div style="font-size:50px; margin-bottom:15px;">🤝</div>
        <h4 style="color:#FF9900; margin-bottom:10px;">協作共贏</h4>
        <p style="color:#666; font-size:14px; line-height:1.6;">跨領域合作，互相學習，共同成長</p>
    </div>
    """, unsafe_allow_html=True)
with culture3:
    st.markdown("""
    <div style="text-align:center; padding:25px 20px; background:linear-gradient(135deg, #ffffff, #f0fff0); border-radius:18px; box-shadow:0 10px 30px rgba(0,0,0,0.08); margin:15px 0;">
        <div style="font-size:50px; margin-bottom:15px;">⚖️</div>
        <h4 style="color:#4CAF50; margin-bottom:10px;">工作平衡</h4>
        <p style="color:#666; font-size:14px; line-height:1.6;">彈性時間，重視效率而非時長</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# ---------------------
# 頁尾
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | 人才招募</div>",
    unsafe_allow_html=True
)
