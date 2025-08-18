import streamlit as st

# ---------------------
# 頁面基本設定
# ---------------------
st.set_page_config(
    page_title="贊助我們｜Tasksnap",
    page_icon="💖",
    layout="wide"
)

# ---------------------
# 自訂 CSS
# ---------------------
st.markdown("""
    <style>
    @keyframes heartbeat {
        0% { transform: scale(1); }
        14% { transform: scale(1.1); }
        28% { transform: scale(1); }
        42% { transform: scale(1.1); }
        70% { transform: scale(1); }
    }
    @keyframes sparkle {
        0%, 100% { opacity: 0; transform: scale(0); }
        50% { opacity: 1; transform: scale(1); }
    }
    @keyframes slideInRight {
        from { opacity: 0; transform: translateX(50px); }
        to { opacity: 1; transform: translateX(0); }
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
        font-size: 60px;
        color: #003366;
        font-weight: 900;
        letter-spacing: 4px;
        margin-bottom: 12px;
        font-family: "Noto Sans TC", "Microsoft JhengHei", "Arial Rounded MT Bold", "Arial", sans-serif;
        text-shadow: 1px 2px 8px rgba(0,0,0,0.08);
    }
    .intro-text {
        text-align: center;
        font-size: 24px;
        line-height: 2;
        color: #234;
        margin-bottom: 40px;
        margin-top: 20px;
        font-weight: 500;
        background: linear-gradient(135deg, #ffffff, #fff0f5);
        padding: 35px;
        border-radius: 20px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.08), 0 5px 15px rgba(255,105,180,0.1);
        border-left: 5px solid #FF9900;
        position: relative;
    }
    .sponsor-card {
        background: linear-gradient(135deg, #ffffff, #fff0f5, #f0f8ff);
        border-radius: 25px;
        box-shadow: 0 20px 50px rgba(0,0,0,0.12), 0 8px 20px rgba(255,105,180,0.15);
        padding: 45px 35px 40px 35px;
        margin: 0 auto 30px auto;
        max-width: 580px;
        text-align: center;
        border: 3px solid transparent;
        background-clip: padding-box;
        transition: all 0.4s ease;
        position: relative;
        overflow: hidden;
        animation: slideInRight 1s ease-out;
    }
    .sponsor-card::before {
        content: '';
        position: absolute;
        top: 0;
        left: 0;
        right: 0;
        height: 4px;
        background: linear-gradient(90deg, #FF69B4, #FF1493, #DC143C, #FF6347);
        border-radius: 25px 25px 0 0;
    }
    .sponsor-card:hover {
        transform: translateY(-8px) scale(1.02);
        box-shadow: 0 30px 70px rgba(0,0,0,0.18), 0 12px 30px rgba(255,105,180,0.25), 0 0 40px rgba(255,20,147,0.2);
        border-color: #FF1493;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .qr-title, .form-title {
        text-align: center;
        font-size: 26px;
        color: #0055A5;
        font-weight: 800;
        margin-bottom: 18px;
        letter-spacing: 2px;
    }
    .contact-block {
        text-align: center;
        margin-top: 48px;
        margin-bottom: 12px;
    }
    .contact-block h3 {
        color: #003366;
        font-size: 24px;
        margin-bottom: 8px;
        font-weight: 800;
    }
    .contact-block b {
        color: #0055A5;
        font-size: 18px;
        letter-spacing: 1px;
    }
    .footer {
        text-align: center;
        color: #888;
        font-size: 15px;
        margin-top: 40px;
        margin-bottom: 8px;
        letter-spacing: 1px;
    }
    .stForm {
        background: linear-gradient(135deg, #ffffff, #f8fbff);
        border-radius: 20px;
        padding: 30px;
        box-shadow: 0 15px 40px rgba(0,0,0,0.1), 0 5px 15px rgba(0,85,165,0.1);
        border: 2px solid rgba(0,85,165,0.1);
    }
    .stTextInput > div > div > input {
        border-radius: 12px;
        border: 2px solid #e0e7ef;
        padding: 12px 16px;
        font-size: 16px;
        transition: all 0.3s ease;
        background: #ffffff;
    }
    .stTextInput > div > div > input:focus {
        border-color: #0055A5;
        box-shadow: 0 0 15px rgba(0,85,165,0.2);
        outline: none;
    }
    .stSelectbox > div > div > div {
        border-radius: 12px;
        border: 2px solid #e0e7ef;
        background: #ffffff;
        transition: all 0.3s ease;
    }
    .stSelectbox > div > div > div:hover {
        border-color: #0055A5;
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    .stTextArea > div > div > textarea {
        border-radius: 12px;
        border: 2px solid #e0e7ef;
        padding: 12px 16px;
        font-size: 16px;
        transition: all 0.3s ease;
        background: #ffffff;
        min-height: 100px;
    }
    .stTextArea > div > div > textarea:focus {
        border-color: #0055A5;
        box-shadow: 0 0 15px rgba(0,85,165,0.2);
        outline: none;
    }
    .stButton > button {
        background: linear-gradient(45deg, #0055A5, #003366);
        border: none;
        border-radius: 12px;
        color: white;
        font-weight: 700;
        font-size: 16px;
        padding: 12px 30px;
        transition: all 0.3s ease;
        box-shadow: 0 8px 20px rgba(0,85,165,0.3);
        width: 100%;
    }
    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 30px rgba(0,85,165,0.4);
        background-image: linear-gradient(120deg, rgba(137, 247, 254, 0.06) 0%, rgba(102, 166, 255, 0.06) 100%);
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------
# 標題
# ---------------------
st.markdown("<div class='main-title'>💖 贊助我們</div>", unsafe_allow_html=True)
st.write("---")

# ---------------------
# 贊助介紹文字
# ---------------------
st.markdown("""
<div class='intro-text'>
我們是一群正在努力開發安全、信任的接案平台的大學生團隊。<br>
為了持續優化功能、維護伺服器以及推廣更多學生安全接案管道，<br>
我們需要您的支持與鼓勵！<br><br>
不論是一杯咖啡的金額或企業合作，都能幫助我們走得更遠 💪
</div>
""", unsafe_allow_html=True)
st.write("---")

# ---------------------
# 兩欄：左 QR Code，右 表單
# ---------------------
col1, col2 = st.columns([1.2, 1])

with col1:
    st.markdown("<div class='qr-title'>📱 掃描 QR Code 贊助</div>", unsafe_allow_html=True)
    st.image("簡報.png", width=550, caption="掃描 QR Code 贊助我們")

with col2:
    st.markdown("<div class='form-title'>📝 贊助資料填寫</div>", unsafe_allow_html=True)
    with st.form("sponsor_form"):
        name = st.text_input("您的姓名")
        email = st.text_input("聯絡 Email")
        amount = st.selectbox("贊助金額", ["☕ 小額支持｜一杯咖啡", "🍱 核心支持｜一份大餐", "🏢 品牌支持｜企業方案", "其他"])
        amount_way = st.selectbox("贊助方式", ["線上轉帳", "超商轉帳", "現金捐款"])
        message = st.text_area("留言給我們（選填）")
        submitted = st.form_submit_button("送出資料")
        if submitted:
            st.success(f"感謝您的支持，{name}！我們已收到您的贊助資料 ❤️")

# ---------------------
# 贊助方案區塊
# ---------------------
st.markdown("<div style='text-align:center; margin-top:48px; margin-bottom:36px;'><h3>💖 贊助方案</h3></div>", unsafe_allow_html=True)
st.markdown("""
<div style="overflow-x:auto; margin:20px 0;">
<table style="width:100%; border-collapse:collapse; background:linear-gradient(135deg, #ffffff, #f8fbff); border-radius:15px; box-shadow:0 15px 40px rgba(0,0,0,0.1); overflow:hidden;">
    <thead>
        <tr style="background:linear-gradient(135deg, #0055A5, #003366); color:white;">
            <th style="padding:20px; text-align:left; font-size:18px; font-weight:700;">贊助金額</th>
            <th style="padding:20px; text-align:left; font-size:18px; font-weight:700;">適合對象</th>
            <th style="padding:20px; text-align:left; font-size:18px; font-weight:700;">方案內容</th>
        </tr>
    </thead>
    <tbody>
        <tr style="border-bottom:1px solid #e0e7ef;">
            <td style="padding:25px 20px; vertical-align:top;">
                <div style="font-size:24px; margin-bottom:8px;">☕ <strong>小額支持｜一杯咖啡</strong></div>
                <div style="font-size:20px; font-weight:700; color:#0055A5;">NT$ 150</div>
            </td>
            <td style="padding:25px 20px; vertical-align:top; color:#666; font-size:16px;">一般使用者、學生</td>
            <td style="padding:25px 20px; vertical-align:top;">
                <ul style="margin:0; padding-left:20px; color:#333; font-size:15px; line-height:1.8;">
                    <li>支援基本伺服器營運</li>
                    <li>感謝卡（數位版）</li>
                    <li>Tasksnap 限定贊助者徽章（實體）</li>
                    <li>加入官方 Discord 社群</li>
                </ul>
            </td>
        </tr>
        <tr style="border-bottom:1px solid #e0e7ef; background:rgba(255,153,0,0.05);">
            <td style="padding:25px 20px; vertical-align:top;">
                <div style="font-size:24px; margin-bottom:8px;">🍱 <strong>核心支持｜一份大餐</strong></div>
                <div style="font-size:20px; font-weight:700; color:#FF9900;">NT$ 800</div>
            </td>
            <td style="padding:25px 20px; vertical-align:top; color:#666; font-size:16px;">熱愛本平台的使用者或開發支持者</td>
            <td style="padding:25px 20px; vertical-align:top;">
                <ul style="margin:0; padding-left:20px; color:#333; font-size:15px; line-height:1.8;">
                    <li>支援新功能開發</li>
                    <li>優先體驗封測版本功能</li>
                    <li>Tasksnap 限量 插圖+梗圖 套組</li>
                    <li>加入官方 Discord 贊助者Vip社群</li>
                    <li>折扣獲得限量週邊（T-shirt、貼紙等）</li>
                </ul>
            </td>
        </tr>
        <tr>
            <td style="padding:25px 20px; vertical-align:top;">
                <div style="font-size:24px; margin-bottom:8px;">🏢 <strong>品牌支持｜企業方案</strong></div>
                <div style="font-size:20px; font-weight:700; color:#4CAF50;">NT$ 5000+（可議）</div>
            </td>
            <td style="padding:25px 20px; vertical-align:top; color:#666; font-size:16px;">教育單位、合作企業、品牌推廣</td>
            <td style="padding:25px 20px; vertical-align:top;">
                <ul style="margin:0; padding-left:20px; color:#333; font-size:15px; line-height:1.8;">
                    <li>掛名官方合作夥伴</li>
                    <li>官方網站／活動露出品牌 Logo</li>
                    <li>客製合作服務（如校園活動、介面置入）</li>
                    <li>Vip外包折扣</li>
                </ul>
            </td>
        </tr>
    </tbody>
</table>
</div>
""", unsafe_allow_html=True)

st.write("---")

# ---------------------
# 聯絡方式
# ---------------------
st.markdown("""
<div class='contact-block'>
    <h3>📩 聯絡我們</h3>
    如需開立收據或企業合作洽詢，請寄信至：<br>
    <b>campusfreelance@example.com</b>
</div>
""", unsafe_allow_html=True)

# ---------------------
# 頁尾
# ---------------------
st.markdown(
    "<div class='footer'>© 2025 Tasksnap App | 感謝您的支持與愛心 💖</div>",
    unsafe_allow_html=True
)
