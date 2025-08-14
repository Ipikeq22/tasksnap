import streamlit as st

# ---------------------
# 頁面基本設定
# ---------------------
st.set_page_config(
    page_title="常見問題｜Tasksnap",
    page_icon="❓",
    layout="wide"
)

# ---------------------
# 自訂 CSS
# ---------------------
st.markdown("""
    <style>
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
    }
    .category-title {
        text-align: center;
        color: #0055A5;
        font-size: 28px;
        font-weight: 800;
        margin-top: 48px;
        margin-bottom: 18px;
        letter-spacing: 2px;
    }
    .faq-item {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 15px;
        box-shadow: 0 8px 25px rgba(0,0,0,0.08);
        padding: 25px;
        margin: 15px 0;
        border-left: 4px solid #FF9900;
        transition: all 0.3s ease;
    }
    .faq-item:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 35px rgba(0,0,0,0.12);
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .faq-question {
        font-size: 18px;
        font-weight: 700;
        color: #003366;
        margin-bottom: 10px;
    }
    .faq-answer {
        font-size: 16px;
        color: #234;
        line-height: 1.7;
    }
    .contact-box {
        background: linear-gradient(135deg, #ffffff, #fff8f0);
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1);
        padding: 30px;
        text-align: center;
        margin: 30px 0;
        border: 2px solid #FF9900;
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
st.markdown("<div class='main-title'>❓ 常見問題</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>找不到答案？歡迎聯絡我們的客服團隊</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------
# 帳號相關問題
# ---------------------
st.markdown("<div class='category-title'>👤 帳號相關</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 如何註冊 Tasksnap 帳號？</div>
    <div class='faq-answer'>A: 您可以使用學校信箱註冊，我們會發送驗證郵件到您的信箱。完成驗證後，需要上傳學生證進行身分驗證，確保平台使用者都是真實的學生。</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 忘記密碼怎麼辦？</div>
    <div class='faq-answer'>A: 點擊登入頁面的「忘記密碼」，輸入您的註冊信箱，系統會發送重設密碼的連結到您的信箱。</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 可以修改個人資料嗎？</div>
    <div class='faq-answer'>A: 可以！登入後進入「個人設定」頁面，您可以修改暱稱、自我介紹、技能標籤等資訊。但學校和科系資訊需要重新驗證才能修改。</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 接案相關問題
# ---------------------
st.markdown("<div class='category-title'>💼 接案相關</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 如何開始接案？</div>
    <div class='faq-answer'>A: 完成身分驗證考核後，您可以在「接案模式」中瀏覽可接的案件，或在「個人檔案」中展示您的技能或曾經的作品，讓發案者主動聯繫您。</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 接案後如何收款？</div>
    <div class='faq-answer'>A: 我們使用第三方金流系統確保交易安全。案件完成並經發案者確認後，款項會在3-5個工作天內匯入您指定的銀行帳戶。</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 如果遇到糾紛怎麼辦？</div>
    <div class='faq-answer'>A: 平台提供糾紛調解服務。您可以在「客服中心」提出申訴，我們會在24小時內回應，並協助雙方達成共識。</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 發案相關問題
# ---------------------
st.markdown("<div class='category-title'>📋 發案相關</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 如何發布案件？</div>
    <div class='faq-answer'>A: 切換到「發案模式」，點擊「發布新案件」，填寫案件詳情、預算、時程等資訊。案件發布後會經過平台審核，通過後即可開始接收應徵。</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 發案需要付費嗎？</div>
    <div class='faq-answer'>A: 發布案件免費，但成功媒合後會收取少量的平台服務費（約案件金額的5%），用於維護平台運作和提供客服支援。</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 接案/發案功能流程介紹圖
# ---------------------
st.markdown("<div class='category-title'>📊 接案/發案功能流程介紹圖</div>", unsafe_allow_html=True)
st.image("接案發案功能介紹圖.png", caption="接案/發案功能流程介紹圖", use_container_width=True)

# ---------------------
# 代幣相關問題
# ---------------------
st.markdown("<div class='category-title'> 代幣相關</div>", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 如何獲得代幣？</div>
    <div class='faq-answer'>A: 您可以透過完成案件、玩小遊戲、參與社群活動、邀請朋友註冊等方式獲得代幣。每日登入也會獲得簽到獎勵。</div>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class='faq-item'>
    <div class='faq-question'>Q: 代幣可以兌換什麼？</div>
    <div class='faq-answer'>A: 代幣可以兌換平台內的虛擬物品、合作商家的優惠券、或是提升個人檔案的曝光度。我們也會定期推出限時兌換活動。</div>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 聯絡我們
# ---------------------
st.markdown("""
<div class='contact-box'>
    <h3 style="color:#FF9900; margin-bottom:15px;">🤝 還有其他問題？</h3>
    <p style="color:#234; margin-bottom:20px;">我們的客服團隊隨時為您服務</p>
    <div style="display:flex; justify-content:center; gap:30px; flex-wrap:wrap;">
        <div style="text-align:center;">
            <div style="font-size:24px; margin-bottom:5px;">📧</div>
            <div style="font-weight:600; color:#0055A5;">尚無</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:24px; margin-bottom:5px;">💬</div>
            <div style="font-weight:600; color:#0055A5;">線上客服 (9:00-18:00)</div>
        </div>
        <div style="text-align:center;">
            <div style="font-size:24px; margin-bottom:5px;">📱</div>
            <div style="font-weight:600; color:#0055A5;">官方 LINE:尚無</div>
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------
# 頁尾
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | 常見問題</div>",
    unsafe_allow_html=True
)
