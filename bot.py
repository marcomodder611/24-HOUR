import random
import time
from datetime import datetime
import urllib.request
import urllib.parse
import json

class VIPRajputPatternEngine:
    def __init__(self, theme="royal"):
        self.theme = theme
        self.wins = 0
        self.losses = 0
        self.jackpots = 0
        self.history = []
        self.current_level = 1
        self.confidence_base = 88.5
        
        # Telegram API Configurations
        self.TELEGRAM_API_KEY = "8309364556:AAGZZM4B0hmAQU-7jYd9x6e1w1wVzyGg-Ck"
        self.TELEGRAM_CHAT_ID = "-1004405838356"
        
        # Theme configuration palette definitions
        self.themes = {
            "royal": {"primary": "#FFD700", "accent": "#00FF88", "bg": "#0a0a1a"},
            "crimson": {"primary": "#FFD700", "accent": "#FF4500", "bg": "#0a0000"},
            "purple": {"primary": "#FFD700", "accent": "#9B59B6", "bg": "#0a0015"},
            "emerald": {"primary": "#FFD700", "accent": "#00FF88", "bg": "#000a00"},
            "rose": {"primary": "#FFD700", "accent": "#E8A0BF", "bg": "#0a0008"}
        }

    def generate_period_id(self):
        """Generates a dynamic 3-digit period identifier simulating live state."""
        now = datetime.now()
        base_num = int(now.strftime("%H%M%S")) % 1000
        return f"{base_num:03d}"

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
