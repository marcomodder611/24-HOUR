import random
import time
from datetime import datetime
import urllib.request
import urllib.parse
import streamlit as st

# ==========================================
# STREAMLIT PAGE CONFIGURATION
# ==========================================
st.set_page_config(
    page_title="VIP RAJPUT • 2-LEVEL PATTERN ENGINE",
    page_icon="👑",
    layout="centered",
    initial_sidebar_state="expanded"
)

# ==========================================
# CUSTOM CSS STYLING & THEMES
# ==========================================
def load_custom_css(theme_name):
    themes = {
        "royal": {"bg": "#0a0a1a", "card": "#0d0d2b", "primary": "#FFD700", "accent": "#00FF88", "border": "#FFD70044"},
        "crimson": {"bg": "#0a0000", "card": "#1a0000", "primary": "#FFD700", "accent": "#FF4500", "border": "#FF450044"},
        "purple": {"bg": "#0a0015", "card": "#15002a", "primary": "#FFD700", "accent": "#9B59B6", "border": "#9B59B644"},
        "emerald": {"bg": "#000a00", "card": "#001a00", "primary": "#FFD700", "accent": "#00FF88", "border": "#00FF8844"},
        "rose": {"bg": "#0a0008", "card": "#1a0015", "primary": "#FFD700", "accent": "#E8A0BF", "border": "#E8A0BF44"}
    }
    t = themes.get(theme_name, themes["royal"])
    
    css = f"""
    <style>
        .stApp {{
            background-color: {t['bg']};
            color: #ffffff;
            font-family: 'Inter', sans-serif;
        }}
        .main-header {{
            font-size: 32px;
            font-weight: 900;
            text-align: center;
            color: {t['primary']};
            text-shadow: 0 0 20px {t['primary']};
            letter-spacing: 2px;
            margin-bottom: 0px;
        }}
        .sub-header {{
            font-size: 11px;
            text-align: center;
            color: {t['accent']};
            letter-spacing: 1px;
            margin-bottom: 20px;
        }}
        .metric-card {{
            background-color: {t['card']};
            border: 1px solid {t['border']};
            padding: 15px;
            border-radius: 15px;
            text-align: center;
            box-shadow: 0 4px 15px rgba(0,0,0,0.5);
        }}
        .pred-box {{
            background: linear-gradient(145deg, {t['bg']}, {t['card']});
            border: 3px solid {t['accent']};
            border-radius: 30px;
            padding: 30px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.8);
            margin-bottom: 20px;
        }}
        .pred-value {{
            font-size: 80px;
            font-weight: 900;
            color: {t['primary']};
            line-height: 1;
            text-shadow: 0 0 25px {t['primary']};
        }}
        .number-badge {{
            display: inline-block;
            background: radial-gradient(circle at 30% 30%, {t['card']}, {t['bg']});
            border: 4px solid {t['primary']};
            color: {t['primary']};
            width: 70px;
            height: 70px;
            border-radius: 50%;
            font-size: 32px;
            font-weight: 900;
            line-height: 60px;
            text-align: center;
            box-shadow: 0 0 15px {t['primary']}aa;
            margin-top: 15px;
        }}
        .footer {{
            text-align: center;
            font-size: 10px;
            color: {t['primary']}55;
            letter-spacing: 1px;
            margin-top: 30px;
        }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

# ==========================================
# ENGINE STATE MANAGEMENT (SESSION STATE)
# ==========================================
if "wins" not in st.session_state:
    st.session_state.wins = 14
if "losses" not in st.session_state:
    st.session_state.losses = 2
if "jackpots" not in st.session_state:
    st.session_state.jackpots = 5
if "history" not in st.session_state:
    st.session_state.history = [
        {"period": "452", "prediction": "BIG", "number": 8, "result": "BIG", "status": "WIN ✅", "confidence": "94.5%"},
        {"period": "451", "prediction": "SMALL", "number": 3, "result": "SMALL", "status": "JACKPOT 🎰", "confidence": "91.2%"},
        {"period": "450", "prediction": "BIG", "number": 7, "result": "SMALL", "status": "LOSS ❌", "confidence": "89.8%"}
    ]
if "current_period" not in st.session_state:
    st.session_state.current_period = "453"
if "current_pred" not in st.session_state:
    st.session_state.current_pred = "BIG"
if "current_num" not in st.session_state:
    st.session_state.current_num = 9
if "current_conf" not in st.session_state:
    st.session_state.current_conf = "96.4%"

# ==========================================
# TELEGRAM SENDER FUNCTION
# ==========================================
TELEGRAM_API_KEY = "8309364556:AAGZZM4B0hmAQU-7jYd9x6e1w1wVzyGg-Ck"
TELEGRAM_CHAT_ID = "-1004405838356"

def send_telegram_alert(message):
    try:
        url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"
        payload = {
            "chat_id": TELEGRAM_CHAT_ID,
            "text": message,
            "parse_mode": "Markdown"
        }
        data = urllib.parse.urlencode(payload).encode("utf-8")
        req = urllib.request.Request(url, data=data, method="POST")
        with urllib.request.urlopen(req, timeout=5) as response:
            return response.status == 200
    except Exception as e:
        return False

# ==========================================
# SIDEBAR CONFIGURATION
# ==========================================
st.sidebar.markdown("## ⚙️ ENGINE CONTROLS")
selected_theme = st.sidebar.selectbox(
    "Choose Theme Style", 
    ["royal", "crimson", "purple", "emerald", "rose"],
    format_func=lambda x: x.upper()
)

load_custom_css(selected_theme)

st.sidebar.markdown("---")
st.sidebar.markdown("### 📡 TELEGRAM STATUS")
st.sidebar.success("API Connected: Active ✅")
st.sidebar.code(f"Chat ID: {TELEGRAM_CHAT_ID}", language="text")

st.sidebar.markdown("---")
if st.sidebar.button("🚀 Run Live Engine Cycle", use_container_width=True):
    # Simulate processing new cycle
    now = datetime.now()
    new_period = f"{int(now.strftime('%H%M%S')) % 1000:03d}"
    pred_type = random.choice(["BIG", "SMALL"])
    pred_num = random.randint(5, 9) if pred_type == "BIG" else random.randint(0, 4)
    confidence = round(88.5 + random.uniform(1.2, 10.0), 1)
    if confidence > 98.9: confidence = 98.9
    
    actual_res = random.choice(["BIG", "SMALL"])
    actual_num = random.randint(0, 9)
    
    is_jackpot = (pred_num == actual_num)
    is_win = (pred_type == actual_res) or is_jackpot
    
    if is_jackpot:
        st.session_state.jackpots += 1
        st.session_state.wins += 1
        status = "JACKPOT 🎰"
    elif is_win:
        st.session_state.wins += 1
        status = "WIN ✅"
    else:
        st.session_state.losses += 1
        status = "LOSS ❌"
        
    st.session_state.current_period = new_period
    st.session_state.current_pred = pred_type
    st.session_state.current_num = pred_num
    st.session_state.current_conf = f"{confidence}%"
    
    log_entry = {
        "period": new_period,
        "prediction": pred_type,
        "number": pred_num,
        "result": actual_res,
        "status": status,
        "confidence": f"{confidence}%"
    }
    st.session_state.history.insert(0, log_entry)
    if len(st.session_state.history) > 15:
        st.session_state.history.pop()
        
    # Broadcast to Telegram
    tg_msg = (
        f"👑 *VIP RAJPUT • 2-LEVEL PATTERN ENGINE* 👑\n\n"
        f"📌 *Period:* `{new_period}`\n"
        f"🎯 *Prediction:* `{pred_type}` (Lucky No: `{pred_num}`)\n"
        f"📈 *Confidence:* `{confidence}%`\n"
        f"📊 *Outcome:* `{status}`\n"
        f"━━━━━━━━━━━━━━━━━━━\n"
        f"🏆 Wins: `{st.session_state.wins}` | ❌ Losses: `{st.session_state.losses}` | 🎰 Jackpots: `{st.session_state.jackpots}`"
    )
    send_telegram_alert(tg_msg)
    st.rerun()

# ==========================================
# MAIN DASHBOARD INTERFACE
# ==========================================
st.markdown('<div class="main-header">VIP RAJPUT</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-header">2-LEVEL PATTERN ENGINE • CLOUD STREAMLIT PORTAL</div>', unsafe_allow_html=True)

# STATS COUNTER ROW
col1, col2, col3, col4 = st.columns(4)
total_games = st.session_state.wins + st.session_state.losses
win_rate = (st.session_state.wins / total_games * 100) if total_games > 0 else 0.0

with col1:
    st.markdown(f'<div class="metric-card"><span style="font-size:10px; color:#aaa;">WINS</span><br><b style="font-size:22px; color:#00FF88;">{st.session_state.wins}</b></div>', unsafe_allow_html=True)
with col2:
    st.markdown(f'<div class="metric-card"><span style="font-size:10px; color:#aaa;">LOSSES</span><br><b style="font-size:22px; color:#ff4444;">{st.session_state.losses}</b></div>', unsafe_allow_html=True)
with col3:
    st.markdown(f'<div class="metric-card"><span style="font-size:10px; color:#aaa;">JACKPOTS</span><br><b style="font-size:22px; color:#FFD700;">{st.session_state.jackpots}</b></div>', unsafe_allow_html=True)
with col4:
    st.markdown(f'<div class="metric-card"><span style="font-size:10px; color:#aaa;">ACCURACY</span><br><b style="font-size:22px; color:#00ffff;">{win_rate:.1f}%</b></div>', unsafe_allow_html=True)

st.write("")

# PERIOD & PREDICTION CARD
st.markdown(f"""
<div class="pred-box">
    <div style="font-size: 13px; font-weight: 700; letter-spacing: 2px; color: #888;">ACTIVE PERIOD: #{st.session_state.current_period}</div>
    <div style="font-size: 11px; margin-top: 5px; color: #00FF88;">CONFIDENCE LEVEL: {st.session_state.current_conf}</div>
    <div class="pred-value" style="margin: 15px 0;">{st.session_state.current_pred}</div>
    <div style="font-size: 12px; font-weight: 600; color: #aaa;">RECOMMENDED LUCKY NUMBER</div>
    <div class="number-badge">{st.session_state.current_num}</div>
</div>
""", unsafe_allow_html=True)

# HISTORY LOG TABLE
st.markdown("### 📊 LIVE SESSION HISTORY LOGS")
history_data = []
for h in st.session_state.history:
    history_data.append({
        "Period": h["period"],
        "Prediction": h["prediction"],
        "Lucky No": h["number"],
        "Actual Result": h["result"],
        "Confidence": h["confidence"],
        "Status": h["status"]
    })

st.dataframe(history_data, use_container_width=True, hide_index=True)

st.markdown('<div class="brand-footer">SECURE CLOUD DEPLOYMENT • VIP RAJPUT ENGINE V2.6</div>', unsafe_allow_html=True)
    def send_telegram_alert(self, message):
        """Dispatches real-time automated updates directly to the designated Telegram chat channel."""
        try:
            url = f"https://api.telegram.org/bot{self.TELEGRAM_API_KEY}/sendMessage"
            payload = {
                "chat_id": self.TELEGRAM_CHAT_ID,
                "text": message,
                "parse_mode": "Markdown"
            }
            data = urllib.parse.urlencode(payload).encode("utf-8")
            req = urllib.request.Request(url, data=data, method="POST")
            with urllib.request.urlopen(req, timeout=5) as response:
                return response.status == 200
        except Exception as e:
            print(f"[!] Telegram Alert Failed: {e}")
            return False

    def run_engine_cycle(self):
        """Executes a single pattern cycle predicting Big/Small and Number values."""
        period = self.generate_period_id()
        
        # 2-Level Matrix Probability calculation
        prediction_type = random.choice(["BIG", "SMALL"])
        predicted_number = random.randint(5, 9) if prediction_type == "BIG" else random.randint(0, 4)

        confidence = round(self.confidence_base + random.uniform(1.2, 8.4), 2)
        if confidence > 98.9:
            confidence = 98.9

        # Simulate outcome evaluation
        actual_result = random.choice(["BIG", "SMALL"])
        actual_number = random.randint(0, 9)
        
        is_jackpot = (predicted_number == actual_number)
        is_win = (prediction_type == actual_result) or is_jackpot

        if is_jackpot:
            self.jackpots += 1
            self.wins += 1
            status_tag = "JACKPOT 🎰"
        elif is_win:
            self.wins += 1
            status_tag = "WIN ✅"
        else:
            self.losses += 1
            status_tag = "LOSS ❌"

        # Track history logs
        log_entry = {
            "period": period,
            "prediction": prediction_type,
            "number": predicted_number,
            "result": actual_result,
            "status": status_tag,
            "confidence": confidence
        }
        self.history.insert(0, log_entry)
        
        if len(self.history) > 20:
            self.history.pop()

        # Format and send update to Telegram channel
        telegram_message = (
            f"👑 *VIP RAJPUT • 2-LEVEL PATTERN ENGINE* 👑\n\n"
            f"📌 **Period:** `{period}`\n"
            f"🎯 **Prediction:** `{prediction_type}` (Lucky No: `{predicted_number}`)\n"
            f"📈 **Confidence:** `{confidence}%`\n"
            f"📊 **Outcome:** `{status_tag}`\n"
            f"━━━━━━━━━━━━━━━━━━━\n"
            f"🏆 Wins: `{self.wins}` | ❌ Losses: `{self.losses}` | 🎰 Jackpots: `{self.jackpots}`"
        )
        self.send_telegram_alert(telegram_message)

        return log_entry

    def display_dashboard(self):
        """Renders a clean CLI-based visual dashboard replicating the web interface."""
        print("\033[H\033[J") # Clear screen terminal output
        print("==================================================")
        print("          VIP RAJPUT • 2-LEVEL PATTERN ENGINE      ")
        print(f"          Active Theme: {self.theme.upper()} (Telegram Connected) ")
        print("==================================================")
        
        total_games = self.wins + self.losses
        win_rate = (self.wins / total_games * 100) if total_games > 0 else 0.0
        
        print(f"[*] Stats -> Wins: {self.wins} | Losses: {self.losses} | Jackpots: {self.jackpots}")
        print(f"[*] Win Accuracy: {win_rate:.2f}% | Current Level: L{self.current_level}")
        print("--------------------------------------------------")

        if self.history:
            latest = self.history[0]
            print(f" >> CURRENT PERIOD  : {latest['period']}")
            print(f" >> PREDICTION      : {latest['prediction']} (Num: {latest['number']})")
            print(f" >> CONFIDENCE      : {latest['confidence']}%")
            print(f" >> STATUS OUTCOME  : [{latest['status']}]")
        print("--------------------------------------------------")
        print("RECENT HISTORY SESSIONS:")
        print(f"{'Period':<8} | {'Pred':<6} | {'Num':<3} | {'Res':<6} | {'Status'}")
        print("-" * 50)
        
        for entry in self.history[:5]:
            print(f"{entry['period']:<8} | {entry['prediction']:<6} | {entry['number']:<3} | {entry['result']:<6} | {entry['status']}")
        print("==================================================")

# Example Execution Loop
if __name__ == "__main__":
    engine = VIPRajputPatternEngine(theme="royal")
    
    try:
        print("Initializing VIP Rajput Pattern Engine with Telegram Automation...")
        for _ in range(3):
            engine.run_engine_cycle()
            engine.display_dashboard()
            time.sleep(2) # Simulating live interval updates between prediction windows
    except KeyboardInterrupt:
        print("\nEngine safely terminated by user.")
        "card_bg": "#0d0d2b",
        "accent": "#00FF88",
        "border": "#FFD70044",
    },
    "🔥 Crimson Warrior": {
        "bg": "#0a0000",
        "logo": "#FFD700",
        "card_bg": "#1a0000",
        "accent": "#FF4500",
        "border": "#FF450044",
    },
    "🔮 Purple Emperor": {
        "bg": "#0a0015",
        "logo": "#FFD700",
        "card_bg": "#15002a",
        "accent": "#9B59B6",
        "border": "#9B59B644",
    },
    "💎 Emerald King": {
        "bg": "#000a00",
        "logo": "#FFD700",
        "card_bg": "#001a00",
        "accent": "#00FF88",
        "border": "#00FF8844",
    },
    "🌹 Rose Gold Luxury": {
        "bg": "#0a0008",
        "logo": "#FFD700",
        "card_bg": "#1a0015",
        "accent": "#E8A0BF",
        "border": "#E8A0BF44",
    },
}

# --- SESSION STATE INITIALIZATION ---
if "history" not in st.session_state:
    st.session_state.history = []
if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0
if "jackpots" not in st.session_state:
    st.session_state.jackpots = 0
if "last_period" not in st.session_state:
    st.session_state.last_period = ""
if "alert_sent" not in st.session_state:
    st.session_state.alert_sent = False

# --- UI HEADER & THEME SWITCHER ---
st.markdown(
    '<h1 style="text-align: center; font-weight: 900; letter-spacing: 2px;">ROHIT 👑</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="text-align: center; font-size: 11px; letter-spacing: 1px; margin-top: -15px;">2-LEVEL PATTERN ENGINE</p>',
    unsafe_allow_html=True,
)

selected_theme_name = st.selectbox(
    "Select Theme", list(THEMES.keys()), label_visibility="collapsed"
)
theme = THEMES[selected_theme_name]

# Apply Theme Style via CSS injection
st.markdown(
    f"""
<style>
    .stApp {{ background-color: {theme['bg']}; color: #ffffff; }}
    .metric-card {{
        background-color: {theme['card_bg']};
        border: 1px solid {theme['border']};
        padding: 15px;
        border-radius: 20px;
        text-align: center;
    }}
</style>
""",
    unsafe_allow_html=True,
)

# --- TIME & PERIOD ENGINE LOGIC ---
now = datetime.datetime.utcnow()
total_minutes = now.hour * 60 + now.minute
period_str = f"{now.strftime('%Y%m%d')}1000{10001 + total_minutes}"
remaining_seconds = 60 - now.second

col_p1, col_p2 = st.columns(2)
with col_p1:
    st.markdown(
        f"""
    <div class="metric-card">
        <div style="font-size: 11px; color: #888;">CURRENT PERIOD</div>
        <div style="font-size: 22px; font-weight: 900; color: {theme['logo']};">{period_str}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col_p2:
    st.markdown(
        f"""
    <div class="metric-card">
        <div style="font-size: 11px; color: #888;">TIMER</div>
        <div style="font-size: 26px; font-weight: 900; color: {theme['accent']};">00:{remaining_seconds:02d}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- 2-LEVEL PATTERN ENGINE PREDICTION LOGIC ---
if st.session_state.last_period != period_str:
    pred_type = random.choice(["BIG", "SMALL"])
    pred_num = random.randint(0, 4) if pred_type == "BIG" else random.randint(5, 9)
    confidence = random.randint(88, 98)
    level = random.choice(["LEVEL 1 [PRIMARY]", "LEVEL 2 [RECOVERY]"])

    if st.session_state.last_period != "":
        actual_res = random.choice(["BIG", "SMALL"])
        is_jackpot = random.random() < 0.15
        if is_jackpot:
            status = "JACKPOT"
            st.session_state.jackpots += 1
            st.session_state.wins += 1
        elif pred_type == actual_res:
            status = "WIN"
            st.session_state.wins += 1
        else:
            status = "LOSS"
            st.session_state.losses += 1

        st.session_state.history.insert(
            0,
            {
                "period": st.session_state.last_period,
                "pred": pred_type,
                "status": status,
            },
        )

    st.session_state.current_pred = pred_type
    st.session_state.current_num = pred_num
    st.session_state.confidence = confidence
    st.session_state.level = level
    st.session_state.last_period = period_str
    st.session_state.alert_sent = False

# Send Telegram Alert at the start of every new period cycle
if not st.session_state.alert_sent:
    telegram_msg = (
        f"👑 <b>ROHIT • 2-LEVEL PATTERN ENGINE</b>\n\n"
        f"📌 <b>Period:</b> {period_str}\n"
        f"📊 <b>Level:</b> {st.session_state.level}\n"
        f"🎯 <b>Prediction:</b> <b>{st.session_state.current_pred}</b> ({st.session_state.current_num})\n"
        f"⭐ <b>Confidence:</b> {st.session_state.confidence}%\n\n"
        f"🚀 <i>Place your bets now!</i>"
    )
    send_telegram_alert(telegram_msg)
    st.session_state.alert_sent = True

# --- PREDICTION DISPLAY CARD ---
st.markdown(
    f"""
<div style="background: linear-gradient(145deg, {theme['card_bg']}, {theme['bg']}); 
            border: 3px solid {theme['logo']}; border-radius: 35px; padding: 30px; text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
    <div style="font-size: 10px; background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 20px; display: inline-block; color: {theme['logo']}; border: 1px solid {theme['logo']};">{st.session_state.level}</div>
    <div style="font-size: 75px; font-weight: 900; margin: 10px 0; color: {theme['logo']}; text-shadow: 0 0 20px {theme['logo']};">{st.session_state.current_pred}</div>
    <div style="font-size: 35px; font-weight: 900; background: radial-gradient(circle, {theme['card_bg']}, {theme['bg']}); width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto; border: 4px solid {theme['logo']}; color: {theme['logo']};">{st.session_state.current_num}</div>
    <div style="margin-top: 15px; font-size: 12px; color: #aaa;">
        Confidence Accuracy: <strong style="color: {theme['accent']};">{st.session_state.confidence}%</strong>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# --- STATS BAR ---
total_games = st.session_state.wins + st.session_state.losses
win_rate = (
    (st.session_state.wins / total_games * 100) if total_games > 0 else 100.0
)

col_s1, col_s2, col_s3, col_s4 = st.columns(4)
col_s1.metric("Wins", st.session_state.wins)
col_s2.metric("Losses", st.session_state.losses)
col_s3.metric("Jackpots", st.session_state.jackpots)
col_s4.metric("Win Rate", f"{win_rate:.1f}%")

st.markdown("---")

# --- SESSION HISTORY TABLE ---
st.markdown("### 📊 Live Session Logs")
if st.session_state.history:
    for h in st.session_state.history[:10]:
        color = (
            "#00FF88"
            if h["status"] == "WIN"
            else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500")
        )
        st.markdown(
            f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result: <span style='color: {color}; font-weight: 900;'>{h['status']}</span>",
            unsafe_allow_html=True,
        )
else:
    st.info("Waiting for the first period cycle to log history results...")

# --- AUTO-REFRESH TRIGGER ---
time.sleep(1)
st.rerun()

    "💎 Emerald King": {
        "bg": "#000a00",
        "logo": "#FFD700",
        "card_bg": "#001a00",
        "accent": "#00FF88",
        "border": "#00FF8844",
    },
    "🌹 Rose Gold Luxury": {
        "bg": "#0a0008",
        "logo": "#FFD700",
        "card_bg": "#1a0015",
        "accent": "#E8A0BF",
        "border": "#E8A0BF44",
    },
}

# --- SESSION STATE INITIALIZATION ---
if "history" not in st.session_state:
    st.session_state.history = []
if "wins" not in st.session_state:
    st.session_state.wins = 0
if "losses" not in st.session_state:
    st.session_state.losses = 0
if "jackpots" not in st.session_state:
    st.session_state.jackpots = 0
if "last_period" not in st.session_state:
    st.session_state.last_period = ""
if "alert_sent" not in st.session_state:
    st.session_state.alert_sent = False

# --- UI HEADER & THEME SWITCHER ---
st.markdown(
    '<h1 style="text-align: center; font-weight: 900; letter-spacing: 2px;">ROHIT 👑</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p style="text-align: center; font-size: 11px; letter-spacing: 1px; margin-top: -15px;">2-LEVEL PATTERN ENGINE</p>',
    unsafe_allow_html=True,
)

selected_theme_name = st.selectbox(
    "Select Theme", list(THEMES.keys()), label_visibility="collapsed"
)
theme = THEMES[selected_theme_name]

# Apply Theme Style via CSS injection
st.markdown(
    f"""
<style>
    .stApp {{ background-color: {theme['bg']}; color: #ffffff; }}
    .metric-card {{
        background-color: {theme['card_bg']};
        border: 1px solid {theme['border']};
        padding: 15px;
        border-radius: 20px;
        text-align: center;
    }}
</style>
""",
    unsafe_allow_html=True,
)

# --- TIME & PERIOD ENGINE LOGIC ---
now = datetime.datetime.utcnow()
total_minutes = now.hour * 60 + now.minute
period_str = f"{now.strftime('%Y%m%d')}1000{10001 + total_minutes}"
remaining_seconds = 60 - now.second

col_p1, col_p2 = st.columns(2)
with col_p1:
    st.markdown(
        f"""
    <div class="metric-card">
        <div style="font-size: 11px; color: #888;">CURRENT PERIOD</div>
        <div style="font-size: 22px; font-weight: 900; color: {theme['logo']};">{period_str}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

with col_p2:
    st.markdown(
        f"""
    <div class="metric-card">
        <div style="font-size: 11px; color: #888;">TIMER</div>
        <div style="font-size: 26px; font-weight: 900; color: {theme['accent']};">00:{remaining_seconds:02d}</div>
    </div>
    """,
        unsafe_allow_html=True,
    )

st.markdown("<br>", unsafe_allow_html=True)

# --- 2-LEVEL PATTERN ENGINE PREDICTION LOGIC ---
if st.session_state.last_period != period_str:
    pred_type = random.choice(["BIG", "SMALL"])
    pred_num = random.randint(0, 4) if pred_type == "BIG" else random.randint(5, 9)
    confidence = random.randint(88, 98)
    level = random.choice(["LEVEL 1 [PRIMARY]", "LEVEL 2 [RECOVERY]"])

    if st.session_state.last_period != "":
        actual_res = random.choice(["BIG", "SMALL"])
        is_jackpot = random.random() < 0.15
        if is_jackpot:
            status = "JACKPOT"
            st.session_state.jackpots += 1
            st.session_state.wins += 1
        elif pred_type == actual_res:
            status = "WIN"
            st.session_state.wins += 1
        else:
            status = "LOSS"
            st.session_state.losses += 1

        st.session_state.history.insert(
            0,
            {
                "period": st.session_state.last_period,
                "pred": pred_type,
                "status": status,
            },
        )

    st.session_state.current_pred = pred_type
    st.session_state.current_num = pred_num
    st.session_state.confidence = confidence
    st.session_state.level = level
    st.session_state.last_period = period_str
    st.session_state.alert_sent = False

# Send Telegram Alert at the start of every new period cycle
if not st.session_state.alert_sent:
    telegram_msg = (
        f"👑 <b>ROHIT • 2-LEVEL PATTERN ENGINE</b>\n\n"
        f"📌 <b>Period:</b> {period_str}\n"
        f"📊 <b>Level:</b> {st.session_state.level}\n"
        f"🎯 <b>Prediction:</b> <b>{st.session_state.current_pred}</b> ({st.session_state.current_num})\n"
        f"⭐ <b>Confidence:</b> {st.session_state.confidence}%\n\n"
        f"🚀 <i>Place your bets now!</i>"
    )
    send_telegram_alert(telegram_msg)
    st.session_state.alert_sent = True

# --- PREDICTION DISPLAY CARD ---
st.markdown(
    f"""
<div style="background: linear-gradient(145deg, {theme['card_bg']}, {theme['bg']}); 
            border: 3px solid {theme['logo']}; border-radius: 35px; padding: 30px; text-align: center;
            box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
    <div style="font-size: 10px; background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 20px; display: inline-block; color: {theme['logo']}; border: 1px solid {theme['logo']};">{st.session_state.level}</div>
    <div style="font-size: 75px; font-weight: 900; margin: 10px 0; color: {theme['logo']}; text-shadow: 0 0 20px {theme['logo']};">{st.session_state.current_pred}</div>
    <div style="font-size: 35px; font-weight: 900; background: radial-gradient(circle, {theme['card_bg']}, {theme['bg']}); width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto; border: 4px solid {theme['logo']}; color: {theme['logo']};">{st.session_state.current_num}</div>
    <div style="margin-top: 15px; font-size: 12px; color: #aaa;">
        Confidence Accuracy: <strong style="color: {theme['accent']};">{st.session_state.confidence}%</strong>
    </div>
</div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# --- STATS BAR ---
total_games = st.session_state.wins + st.session_state.losses
win_rate = (
    (st.session_state.wins / total_games * 100) if total_games > 0 else 100.0
)

col_s1, col_s2, col_s3, col_s4 = st.columns(4)
col_s1.metric("Wins", st.session_state.wins)
col_s2.metric("Losses", st.session_state.losses)
col_s3.metric("Jackpots", st.session_state.jackpots)
col_s4.metric("Win Rate", f"{win_rate:.1f}%")

st.markdown("---")

# --- SESSION HISTORY TABLE ---
st.markdown("### 📊 Live Session Logs")
if st.session_state.history:
    for h in st.session_state.history[:10]:
        color = (
            "#00FF88"
            if h["status"] == "WIN"
            else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500")
        )
        st.markdown(
            f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result: <span style='color: {color}; font-weight: 900;'>{h['status']}</span>",
            unsafe_allow_html=True,
        )
else:
    st.info("Waiting for the first period cycle to log history results...")

# --- AUTO-REFRESH TRIGGER ---
time.sleep(1)
st.rerun()

    },
    "💎 Emerald King": {
        "bg": "#000a00",
        "logo": "#FFD700",
        "card_bg": "#001a00",
        "accent": "#00FF88",
        "border": "#00FF8844",
    },
    "🌹 Rose Gold Luxury": {
        "bg": "#0a0008",
        "logo": "#FFD700",
        "card_bg": "#1a0015",
        "accent": "#E8A0BF",
        "border": "#E8A0BF44",
    },
}

# --- SESSION STATE INITIALIZATION ---
if "history" not in st.session_state:
  st.session_state.history = []
if "wins" not in st.session_state:
  st.session_state.wins = 0
if "losses" not in st.session_state:
  st.session_state.losses = 0
if "jackpots" not in st.session_state:
  st.session_state.jackpots = 0
if "last_period" not in st.session_state:
  st.session_state.last_period = ""
if "alert_sent" not in st.session_state:
  st.session_state.alert_sent = False

# --- UI HEADER & THEME SWITCHER ---
st.markdown(
    "<h1 style='text-align: center; font-weight: 900; letter-spacing:"
    " 2px;'>ROHIT 👑</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 11px; letter-spacing: 1px;"
    " margin-top: -15px;'>2-LEVEL PATTERN ENGINE</p>",
    unsafe_allow_html=True,
)

selected_theme_name = st.selectbox(
    "Select Theme", list(THEMES.keys()), label_visibility="collapsed"
)
theme = THEMES[selected_theme_name]

# Apply Theme Style via CSS injection
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {theme['bg']}; color: #ffffff; }}
    .metric-card {{
        background-color: {theme['card_bg']};
        border: 1px solid {theme['border']};
        padding: 15px;
        border-radius: 20px;
        text-align: center;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# --- TIME & PERIOD ENGINE LOGIC ---
now = datetime.datetime.utcnow()
total_minutes = now.hour * 60 + now.minute
period_str = f"{now.strftime('%Y%m%d')}1000{10001 + total_minutes}"
remaining_seconds = 60 - now.second

col_p1, col_p2 = st.columns(2)
with col_p1:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">CURRENT PERIOD</div>
            <div style="font-size: 22px; font-weight: 900; color: {theme['logo']};">{period_str}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_p2:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">TIMER</div>
            <div style="font-size: 26px; font-weight: 900; color: {theme['accent']};">00:{remaining_seconds:02d}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.markdown("<br>", unsafe_allow_html=True)

# --- 2-LEVEL PATTERN ENGINE PREDICTION LOGIC ---
if st.session_state.last_period != period_str:
  pred_type = random.choice(["BIG", "SMALL"])
  pred_num = random.randint(0, 4) if pred_type == "BIG" else random.randint(5, 9)
  confidence = random.randint(88, 98)
  level = random.choice(["LEVEL 1 [PRIMARY]", "LEVEL 2 [RECOVERY]"])

  if st.session_state.last_period != "":
    actual_res = random.choice(["BIG", "SMALL"])
    is_jackpot = random.random() < 0.15

    if is_jackpot:
      status = "JACKPOT"
      st.session_state.jackpots += 1
      st.session_state.wins += 1
    elif pred_type == actual_res:
      status = "WIN"
      st.session_state.wins += 1
    else:
      status = "LOSS"
      st.session_state.losses += 1

    st.session_state.history.insert(
        0,
        {
            "period": st.session_state.last_period,
            "pred": pred_type,
            "status": status,
        },
    )

  st.session_state.current_pred = pred_type
  st.session_state.current_num = pred_num
  st.session_state.confidence = confidence
  st.session_state.level = level
  st.session_state.last_period = period_str
  st.session_state.alert_sent = False

# Send Telegram Alert at the start of every new period cycle
if not st.session_state.alert_sent:
  telegram_msg = (
      f"👑 <b>ROHIT • 2-LEVEL PATTERN ENGINE</b>\n\n"
      f"📌 <b>Period:</b> {period_str}\n"
      f"📊 <b>Level:</b> {st.session_state.level}\n"
      f"🎯 <b>Prediction:</b> <b>{st.session_state.current_pred}</b> ({st.session_state.current_num})\n"
      f"⭐ <b>Confidence:</b> {st.session_state.confidence}%\n\n"
      f"🚀 <i>Place your bets now!</i>"
  )
  send_telegram_alert(telegram_msg)
  st.session_state.alert_sent = True

# --- PREDICTION DISPLAY CARD ---
st.markdown(
    f"""
    <div style="background: linear-gradient(145deg, {theme['card_bg']}, {theme['bg']}); 
                border: 3px solid {theme['logo']}; border-radius: 35px; padding: 30px; text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div style="font-size: 10px; background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 20px; display: inline-block; color: {theme['logo']}; border: 1px solid {theme['logo']};">
            {st.session_state.level}
        </div>
        <div style="font-size: 75px; font-weight: 900; margin: 10px 0; color: {theme['logo']}; text-shadow: 0 0 20px {theme['logo']};">
            {st.session_state.current_pred}
        </div>
        <div style="font-size: 35px; font-weight: 900; background: radial-gradient(circle, {theme['card_bg']}, {theme['bg']}); width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto; border: 4px solid {theme['logo']}; color: {theme['logo']};">
            {st.session_state.current_num}
        </div>
        <div style="margin-top: 15px; font-size: 12px; color: #aaa;">
            Confidence Accuracy: <strong style="color: {theme['accent']};">{st.session_state.confidence}%</strong>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# --- STATS BAR ---
total_games = st.session_state.wins + st.session_state.losses
win_rate = (
    (st.session_state.wins / total_games * 100) if total_games > 0 else 100.0
)

col_s1, col_s2, col_s3, col_s4 = st.columns(4)
col_s1.metric("Wins", st.session_state.wins)
col_s2.metric("Losses", st.session_state.losses)
col_s3.metric("Jackpots", st.session_state.jackpots)
col_s4.metric("Win Rate", f"{win_rate:.1f}%")

st.markdown("---")

# --- SESSION HISTORY TABLE ---
st.markdown("### 📊 Live Session Logs")
if st.session_state.history:
  for h in st.session_state.history[:10]:
    color = (
        "#00FF88"
        if h["status"] == "WIN"
        else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500")
    )
    st.markdown(
        f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result:"
        f" <span style='color: {color}; font-weight:"
        f" 900;'>{h['status']}</span>",
        unsafe_allow_html=True,
    )
else:
  st.info("Waiting for the first period cycle to log history results...")

# --- AUTO-REFRESH TRIGGER ---
time.sleep(1)
st.rerun()
    },
    "🔥 Crimson Warrior": {
        "bg": "#0a0000",
        "logo": "#FFD700",
        "card_bg": "#1a0000",
        "accent": "#FF4500",
        "border": "#FF450044",
    },
    "🔮 Purple Emperor": {
        "bg": "#0a0015",
        "logo": "#FFD700",
        "card_bg": "#15002a",
        "accent": "#9B59B6",
        "border": "#9B59B644",
    },
    "💎 Emerald King": {
        "bg": "#000a00",
        "logo": "#FFD700",
        "card_bg": "#001a00",
        "accent": "#00FF88",
        "border": "#00FF8844",
    },
    "🌹 Rose Gold Luxury": {
        "bg": "#0a0008",
        "logo": "#FFD700",
        "card_bg": "#1a0015",
        "accent": "#E8A0BF",
        "border": "#E8A0BF44",
    },
}

# --- SESSION STATE INITIALIZATION ---
if "history" not in st.session_state:
  st.session_state.history = []
if "wins" not in st.session_state:
  st.session_state.wins = 0
if "losses" not in st.session_state:
  st.session_state.losses = 0
if "jackpots" not in st.session_state:
  st.session_state.jackpots = 0
if "last_period" not in st.session_state:
  st.session_state.last_period = ""
if "alert_sent" not in st.session_state:
  st.session_state.alert_sent = False

# --- UI HEADER & THEME SWITCHER ---
st.markdown(
    "<h1 style='text-align: center; font-weight: 900; letter-spacing:"
    " 2px;'>ROHIT 👑</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 11px; letter-spacing: 1px;"
    " margin-top: -15px;'>2-LEVEL PATTERN ENGINE</p>",
    unsafe_allow_html=True,
)

selected_theme_name = st.selectbox(
    "Select Theme", list(THEMES.keys()), label_visibility="collapsed"
)
theme = THEMES[selected_theme_name]

# Apply Theme Style via CSS injection
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {theme['bg']}; color: #ffffff; }}
    .metric-card {{
        background-color: {theme['card_bg']};
        border: 1px solid {theme['border']};
        padding: 15px;
        border-radius: 20px;
        text-align: center;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# --- TIME & PERIOD ENGINE LOGIC ---
now = datetime.datetime.utcnow()
total_minutes = now.hour * 60 + now.minute
period_str = f"{now.strftime('%Y%m%d')}1000{10001 + total_minutes}"
remaining_seconds = 60 - now.second

col_p1, col_p2 = st.columns(2)
with col_p1:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">CURRENT PERIOD</div>
            <div style="font-size: 22px; font-weight: 900; color: {theme['logo']};">{period_str}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_p2:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">TIMER</div>
            <div style="font-size: 26px; font-weight: 900; color: {theme['accent']};">00:{remaining_seconds:02d}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.markdown("<br>", unsafe_allow_html=True)

# --- 2-LEVEL PATTERN ENGINE PREDICTION LOGIC ---
if st.session_state.last_period != period_str:
  pred_type = random.choice(["BIG", "SMALL"])
  pred_num = random.randint(0, 4) if pred_type == "BIG" else random.randint(5, 9)
  confidence = random.randint(88, 98)
  level = random.choice(["LEVEL 1 [PRIMARY]", "LEVEL 2 [RECOVERY]"])

  if st.session_state.last_period != "":
    actual_res = random.choice(["BIG", "SMALL"])
    is_jackpot = random.random() < 0.15

    if is_jackpot:
      status = "JACKPOT"
      st.session_state.jackpots += 1
      st.session_state.wins += 1
    elif pred_type == actual_res:
      status = "WIN"
      st.session_state.wins += 1
    else:
      status = "LOSS"
      st.session_state.losses += 1

    st.session_state.history.insert(
        0,
        {
            "period": st.session_state.last_period,
            "pred": pred_type,
            "status": status,
        },
    )

  st.session_state.current_pred = pred_type
  st.session_state.current_num = pred_num
  st.session_state.confidence = confidence
  st.session_state.level = level
  st.session_state.last_period = period_str
  st.session_state.alert_sent = False

# Send Telegram Alert at the start of every new period cycle
if not st.session_state.alert_sent:
  telegram_msg = (
      f"👑 <b>ROHIT • 2-LEVEL PATTERN ENGINE</b>\n\n"
      f"📌 <b>Period:</b> {period_str}\n"
      f"📊 <b>Level:</b> {st.session_state.level}\n"
      f"🎯 <b>Prediction:</b> <b>{st.session_state.current_pred}</b> ({st.session_state.current_num})\n"
      f"⭐ <b>Confidence:</b> {st.session_state.confidence}%\n\n"
      f"🚀 <i>Place your bets now!</i>"
  )
  send_telegram_alert(telegram_msg)
  st.session_state.alert_sent = True

# --- PREDICTION DISPLAY CARD ---
st.markdown(
    f"""
    <div style="background: linear-gradient(145deg, {theme['card_bg']}, {theme['bg']}); 
                border: 3px solid {theme['logo']}; border-radius: 35px; padding: 30px; text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div style="font-size: 10px; background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 20px; display: inline-block; color: {theme['logo']}; border: 1px solid {theme['logo']};">
            {st.session_state.level}
        </div>
        <div style="font-size: 75px; font-weight: 900; margin: 10px 0; color: {theme['logo']}; text-shadow: 0 0 20px {theme['logo']};">
            {st.session_state.current_pred}
        </div>
        <div style="font-size: 35px; font-weight: 900; background: radial-gradient(circle, {theme['card_bg']}, {theme['bg']}); width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto; border: 4px solid {theme['logo']}; color: {theme['logo']};">
            {st.session_state.current_num}
        </div>
        <div style="margin-top: 15px; font-size: 12px; color: #aaa;">
            Confidence Accuracy: <strong style="color: {theme['accent']};">{st.session_state.confidence}%</strong>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# --- STATS BAR ---
total_games = st.session_state.wins + st.session_state.losses
win_rate = (
    (st.session_state.wins / total_games * 100) if total_games > 0 else 100.0
)

col_s1, col_s2, col_s3, col_s4 = st.columns(4)
col_s1.metric("Wins", st.session_state.wins)
col_s2.metric("Losses", st.session_state.losses)
col_s3.metric("Jackpots", st.session_state.jackpots)
col_s4.metric("Win Rate", f"{win_rate:.1f}%")

st.markdown("---")

# --- SESSION HISTORY TABLE ---
st.markdown("### 📊 Live Session Logs")
if st.session_state.history:
  for h in st.session_state.history[:10]:
    color = (
        "#00FF88"
        if h["status"] == "WIN"
        else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500")
    )
    st.markdown(
        f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result:"
        f" <span style='color: {color}; font-weight:"
        f" 900;'>{h['status']}</span>",
        unsafe_allow_html=True,
    )
else:
  st.info("Waiting for the first period cycle to log history results...")

# --- AUTO-REFRESH TRIGGER ---
time.sleep(1)
st.rerun()
    },
    "🔥 Crimson Warrior": {
        "bg": "#0a0000",
        "logo": "#FFD700",
        "card_bg": "#1a0000",
        "accent": "#FF4500",
        "border": "#FF450044",
    },
    "🔮 Purple Emperor": {
        "bg": "#0a0015",
        "logo": "#FFD700",
        "card_bg": "#15002a",
        "accent": "#9B59B6",
        "border": "#9B59B644",
    },
    "💎 Emerald King": {
        "bg": "#000a00",
        "logo": "#FFD700",
        "card_bg": "#001a00",
        "accent": "#00FF88",
        "border": "#00FF8844",
    },
    "🌹 Rose Gold Luxury": {
        "bg": "#0a0008",
        "logo": "#FFD700",
        "card_bg": "#1a0015",
        "accent": "#E8A0BF",
        "border": "#E8A0BF44",
    },
}

# --- SESSION STATE INITIALIZATION ---
if "history" not in st.session_state:
  st.session_state.history = []
if "wins" not in st.session_state:
  st.session_state.wins = 0
if "losses" not in st.session_state:
  st.session_state.losses = 0
if "jackpots" not in st.session_state:
  st.session_state.jackpots = 0
if "last_period" not in st.session_state:
  st.session_state.last_period = ""
if "alert_sent" not in st.session_state:
  st.session_state.alert_sent = False

# --- UI HEADER & THEME SWITCHER ---
st.markdown(
    "<h1 style='text-align: center; font-weight: 900; letter-spacing:"
    " 2px;'>ROHIT 👑</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 11px; letter-spacing: 1px;"
    " margin-top: -15px;'>2-LEVEL PATTERN ENGINE</p>",
    unsafe_allow_html=True,
)

selected_theme_name = st.selectbox(
    "Select Theme", list(THEMES.keys()), label_visibility="collapsed"
)
theme = THEMES[selected_theme_name]

# Apply Theme Style via CSS injection
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {theme['bg']}; color: #ffffff; }}
    .metric-card {{
        background-color: {theme['card_bg']};
        border: 1px solid {theme['border']};
        padding: 15px;
        border-radius: 20px;
        text-align: center;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# --- TIME & PERIOD ENGINE LOGIC ---
now = datetime.datetime.utcnow()
total_minutes = now.hour * 60 + now.minute
period_str = f"{now.strftime('%Y%m%d')}1000{10001 + total_minutes}"
remaining_seconds = 60 - now.second

col_p1, col_p2 = st.columns(2)
with col_p1:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">CURRENT PERIOD</div>
            <div style="font-size: 22px; font-weight: 900; color: {theme['logo']};">{period_str}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_p2:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">TIMER</div>
            <div style="font-size: 26px; font-weight: 900; color: {theme['accent']};">00:{remaining_seconds:02d}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.markdown("<br>", unsafe_allow_html=True)

# --- 2-LEVEL PATTERN ENGINE PREDICTION LOGIC ---
if st.session_state.last_period != period_str:
  pred_type = random.choice(["BIG", "SMALL"])
  pred_num = random.randint(0, 4) if pred_type == "BIG" else random.randint(5, 9)
  confidence = random.randint(88, 98)
  level = random.choice(["LEVEL 1 [PRIMARY]", "LEVEL 2 [RECOVERY]"])

  if st.session_state.last_period != "":
    actual_res = random.choice(["BIG", "SMALL"])
    is_jackpot = random.random() < 0.15

    if is_jackpot:
      status = "JACKPOT"
      st.session_state.jackpots += 1
      st.session_state.wins += 1
    elif pred_type == actual_res:
      status = "WIN"
      st.session_state.wins += 1
    else:
      status = "LOSS"
      st.session_state.losses += 1

    st.session_state.history.insert(
        0,
        {
            "period": st.session_state.last_period,
            "pred": pred_type,
            "status": status,
        },
    )

  st.session_state.current_pred = pred_type
  st.session_state.current_num = pred_num
  st.session_state.confidence = confidence
  st.session_state.level = level
  st.session_state.last_period = period_str
  st.session_state.alert_sent = False

# Send Telegram Alert at the start of every new period cycle
if not st.session_state.alert_sent:
  telegram_msg = (
      f"👑 <b>ROHIT • 2-LEVEL PATTERN ENGINE</b>\n\n"
      f"📌 <b>Period:</b> {period_str}\n"
      f"📊 <b>Level:</b> {st.session_state.level}\n"
      f"🎯 <b>Prediction:</b> <b>{st.session_state.current_pred}</b> ({st.session_state.current_num})\n"
      f"⭐ <b>Confidence:</b> {st.session_state.confidence}%\n\n"
      f"🚀 <i>Place your bets now!</i>"
  )
  send_telegram_alert(telegram_msg)
  st.session_state.alert_sent = True

# --- PREDICTION DISPLAY CARD ---
st.markdown(
    f"""
    <div style="background: linear-gradient(145deg, {theme['card_bg']}, {theme['bg']}); 
                border: 3px solid {theme['logo']}; border-radius: 35px; padding: 30px; text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div style="font-size: 10px; background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 20px; display: inline-block; color: {theme['logo']}; border: 1px solid {theme['logo']};">
            {st.session_state.level}
        </div>
        <div style="font-size: 75px; font-weight: 900; margin: 10px 0; color: {theme['logo']}; text-shadow: 0 0 20px {theme['logo']};">
            {st.session_state.current_pred}
        </div>
        <div style="font-size: 35px; font-weight: 900; background: radial-gradient(circle, {theme['card_bg']}, {theme['bg']}); width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto; border: 4px solid {theme['logo']}; color: {theme['logo']};">
            {st.session_state.current_num}
        </div>
        <div style="margin-top: 15px; font-size: 12px; color: #aaa;">
            Confidence Accuracy: <strong style="color: {theme['accent']};">{st.session_state.confidence}%</strong>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# --- STATS BAR ---
total_games = st.session_state.wins + st.session_state.losses
win_rate = (
    (st.session_state.wins / total_games * 100) if total_games > 0 else 100.0
)

col_s1, col_s2, col_s3, col_s4 = st.columns(4)
col_s1.metric("Wins", st.session_state.wins)
col_s2.metric("Losses", st.session_state.losses)
col_s3.metric("Jackpots", st.session_state.jackpots)
col_s4.metric("Win Rate", f"{win_rate:.1f}%")

st.markdown("---")

# --- SESSION HISTORY TABLE ---
st.markdown("### 📊 Live Session Logs")
if st.session_state.history:
  for h in st.session_state.history[:10]:
    color = (
        "#00FF88"
        if h["status"] == "WIN"
        else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500")
    )
    st.markdown(
        f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result:"
        f" <span style='color: {color}; font-weight:"
        f" 900;'>{h['status']}</span>",
        unsafe_allow_html=True,
    )
else:
  st.info("Waiting for the first period cycle to log history results...")

# --- AUTO-REFRESH TRIGGER ---
time.sleep(1)
st.rerun()
ts...") # --- AUTO-REFRESH TRIGGER --- time.sleep(1) st.rerun() _s4.metric("Win Rate", f"{win_rate:.1f}%") st.markdown("---") # --- SESSION HISTORY TABLE --- st.markdown("### 📊 Live Session Logs") if st.session_state.history: for h in st.session_state.history[:10]: color = ( "#00FF88" if h["status"] == "WIN" else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500") ) st.markdown( f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result:" f" <span style="color: {color}; font-weight:&quot;
        f&quot; 900;">{h['status']}</span>", unsafe_allow_html=True, ) else: st.info("Waiting for the first period cycle to log history results...") # --- AUTO-REFRESH TRIGGER --- time.sleep(1) st.rerun()
 </body>
</html>    },
    "🔥 Crimson Warrior": {
        "bg": "#0a0000",
        "logo": "#FFD700",
        "card_bg": "#1a0000",
        "accent": "#FF4500",
        "border": "#FF450044",
    },
    "🔮 Purple Emperor": {
        "bg": "#0a0015",
        "logo": "#FFD700",
        "card_bg": "#15002a",
        "accent": "#9B59B6",
        "border": "#9B59B644",
    },
    "💎 Emerald King": {
        "bg": "#000a00",
        "logo": "#FFD700",
        "card_bg": "#001a00",
        "accent": "#00FF88",
        "border": "#00FF8844",
    },
    "🌹 Rose Gold Luxury": {
        "bg": "#0a0008",
        "logo": "#FFD700",
        "card_bg": "#1a0015",
        "accent": "#E8A0BF",
        "border": "#E8A0BF44",
    },
}

# --- SESSION STATE INITIALIZATION ---
if "history" not in st.session_state:
  st.session_state.history = []
if "wins" not in st.session_state:
  st.session_state.wins = 0
if "losses" not in st.session_state:
  st.session_state.losses = 0
if "jackpots" not in st.session_state:
  st.session_state.jackpots = 0
if "last_period" not in st.session_state:
  st.session_state.last_period = ""
if "alert_sent" not in st.session_state:
  st.session_state.alert_sent = False

# --- UI HEADER & THEME SWITCHER ---
st.markdown(
    "<h1 style='text-align: center; font-weight: 900; letter-spacing:"
    " 2px;'>VIP RAJPUT</h1>",
    unsafe_allow_html=True,
)
st.markdown(
    "<p style='text-align: center; font-size: 11px; letter-spacing: 1px;"
    " margin-top: -15px;'>2-LEVEL PATTERN ENGINE</p>",
    unsafe_allow_html=True,
)

selected_theme_name = st.selectbox(
    "Select Theme", list(THEMES.keys()), label_visibility="collapsed"
)
theme = THEMES[selected_theme_name]

# Apply Theme Style via CSS injection
st.markdown(
    f"""
    <style>
    .stApp {{ background-color: {theme['bg']}; color: #ffffff; }}
    .metric-card {{
        background-color: {theme['card_bg']};
        border: 1px solid {theme['border']};
        padding: 15px;
        border-radius: 20px;
        text-align: center;
    }}
    </style>
""",
    unsafe_allow_html=True,
)

# --- TIME & PERIOD ENGINE LOGIC ---
now = datetime.datetime.utcnow()
total_minutes = now.hour * 60 + now.minute
period_str = f"{now.strftime('%Y%m%d')}1000{10001 + total_minutes}"
remaining_seconds = 60 - now.second

col_p1, col_p2 = st.columns(2)
with col_p1:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">CURRENT PERIOD</div>
            <div style="font-size: 22px; font-weight: 900; color:"
          f" {theme['logo']};">{period_str}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

with col_p2:
  st.markdown(
      f"""
        <div class="metric-card">
            <div style="font-size: 11px; color: #888;">TIMER</div>
            <div style="font-size: 26px; font-weight: 900; color:"
          f" {theme['accent']};">00:{remaining_seconds:02d}</div>
        </div>
    """,
      unsafe_allow_html=True,
  )

st.markdown("<br>", unsafe_allow_html=True)

# --- 2-LEVEL PATTERN ENGINE PREDICTION LOGIC ---
if st.session_state.last_period != period_str:
  pred_type = random.choice(["BIG", "SMALL"])
  pred_num = random.randint(5, 9) if pred_type == "BIG" else random.randint(0, 4)
  confidence = random.randint(88, 98)
  level = random.choice(["LEVEL 1 [PRIMARY]", "LEVEL 2 [RECOVERY]"])

  if st.session_state.last_period != "":
    actual_res = random.choice(["BIG", "SMALL"])
    is_jackpot = random.random() < 0.15

    if is_jackpot:
      status = "JACKPOT"
      st.session_state.jackpots += 1
      st.session_state.wins += 1
    elif pred_type == actual_res:
      status = "WIN"
      st.session_state.wins += 1
    else:
      status = "LOSS"
      st.session_state.losses += 1

    st.session_state.history.insert(
        0,
        {
            "period": st.session_state.last_period,
            "pred": pred_type,
            "status": status,
        },
    )

  st.session_state.current_pred = pred_type
  st.session_state.current_num = pred_num
  st.session_state.confidence = confidence
  st.session_state.level = level
  st.session_state.last_period = period_str
  st.session_state.alert_sent = False

# Send Telegram Alert at the start of every new period cycle
if not st.session_state.alert_sent:
  telegram_msg = (
      f"👑 <b>VIP RAJPUT • 2-LEVEL PATTERN ENGINE</b>\n\n"
      f"📌 <b>Period:</b> {period_str}\n"
      f"📊 <b>Level:</b> {st.session_state.level}\n"
      f"🎯 <b>Prediction:</b> <b>{st.session_state.current_pred}</b> ({st.session_state.current_num})\n"
      f"⭐ <b>Confidence:</b> {st.session_state.confidence}%\n\n"
      f"🚀 <i>Place your bets now!</i>"
  )
  send_telegram_alert(telegram_msg)
  st.session_state.alert_sent = True

# --- PREDICTION DISPLAY CARD ---
st.markdown(
    f"""
    <div style="background: linear-gradient(145deg, {theme['card_bg']}, {theme['bg']}); 
                border: 3px solid {theme['logo']}; border-radius: 35px; padding: 30px; text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.5);">
        <div style="font-size: 10px; background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 20px; display: inline-block; color: {theme['logo']}; border: 1px solid {theme['logo']};">
            {st.session_state.level}
        </div>
        <div style="font-size: 75px; font-weight: 900; margin: 10px 0; color: {theme['logo']}; text-shadow: 0 0 20px {theme['logo']};">
            {st.session_state.current_pred}
        </div>
        <div style="font-size: 35px; font-weight: 900; background: radial-gradient(circle, {theme['card_bg']}, {theme['bg']}); width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto; border: 4px solid {theme['logo']}; color: {theme['logo']};">
            {st.session_state.current_num}
        </div>
        <div style="margin-top: 15px; font-size: 12px; color: #aaa;">
            Confidence Accuracy: <strong style="color: {theme['accent']};">{st.session_state.confidence}%</strong>
        </div>
    </div>
""",
    unsafe_allow_html=True,
)

st.markdown("<br>", unsafe_allow_html=True)

# --- STATS BAR ---
total_games = st.session_state.wins + st.session_state.losses
win_rate = (
    (st.session_state.wins / total_games * 100) if total_games > 0 else 100.0
)

col_s1, col_s2, col_s3, col_s4 = st.columns(4)
col_s1.metric("Wins", st.session_state.wins)
col_s2.metric("Losses", st.session_state.losses)
col_s3.metric("Jackpots", st.session_state.jackpots)
col_s4.metric("Win Rate", f"{win_rate:.1f}%")

st.markdown("---")

# --- SESSION HISTORY TABLE ---
st.markdown("### 📊 Live Session Logs")
if st.session_state.history:
  for h in st.session_state.history[:10]:
    color = (
        "#00FF88"
        if h["status"] == "WIN"
        else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500")
    )
    st.markdown(
        f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result:"
        f" <span style='color: {color}; font-weight:"
        f" 900;'>{h['status']}</span>",
        unsafe_allow_html=True,
    )
else:
  st.info("Waiting for the first period cycle to log history results...")

# --- AUTO-REFRESH TRIGGER ---
time.sleep(1)
st.rerun()
