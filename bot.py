import datetime
import random
import time
import requests
import streamlit as st

# --- API & TELEGRAM CONFIGURATION ---
TELEGRAM_API_KEY = "8309364556:AAGZZM4B0hmAQU-7jYd9x6e1w1wVzyGg-Ck"
TELEGRAM_CHAT_ID = "-1004405838356"


def send_telegram_alert(message):
  """Sends notification updates to the specified Telegram chat."""
  url = f"https://api.telegram.org/bot{TELEGRAM_API_KEY}/sendMessage"
  payload = {"chat_id": TELEGRAM_CHAT_ID, "text": message, "parse_mode": "HTML"}
  try:
    requests.post(url, json=payload, timeout=5)
  except Exception:
    pass


# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="ROHIT • 2-LEVEL PATTERN ENGINE",
    page_icon="👑",
    layout="centered",
)

# --- THEME STYLING CONFIGURATIONS ---
THEMES = {
    "👑 Royal Gold": {
        "bg": "#0a0a1a",
        "logo": "#FFD700",
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
   <div style="font-size: 10px; background: rgba(0,0,0,0.4); padding: 4px 12px; border-radius: 20px; display: inline-block; color: {theme['logo']}; border: 1px solid {theme['logo']};">{st.session_state.level}</div>
   <div style="font-size: 75px; font-weight: 900; margin: 10px 0; color: {theme['logo']}; text-shadow: 0 0 20px {theme['logo']};">{st.session_state.current_pred}</div>
   <div style="font-size: 35px; font-weight: 900; background: radial-gradient(circle, {theme['card_bg']}, {theme['bg']}); width: 70px; height: 70px; line-height: 70px; border-radius: 50%; margin: 0 auto; border: 4px solid {theme['logo']}; color: {theme['logo']};">{st.session_state.current_num}</div>
   <div style="margin-top: 15px; font-size: 12px; color: #aaa;">
    Confidence Accuracy: <strong style="color: {theme['accent']};">{st.session_state.confidence}%</strong>
   </div>
  </div>
  """, unsafe_allow_html=True, ) st.markdown("
  <br>
  ", unsafe_allow_html=True) # --- STATS BAR --- total_games = st.session_state.wins + st.session_state.losses win_rate = ( (st.session_state.wins / total_games * 100) if total_games &gt; 0 else 100.0 ) col_s1, col_s2, col_s3, col_s4 = st.columns(4) col_s1.metric("Wins", st.session_state.wins) col_s2.metric("Losses", st.session_state.losses) col_s3.metric("Jackpots", st.session_state.jackpots) col_s4.metric("Win Rate", f"{win_rate:.1f}%") st.markdown("---") # --- SESSION HISTORY TABLE --- st.markdown("### 📊 Live Session Logs") if st.session_state.history: for h in st.session_state.history[:10]: color = ( "#00FF88" if h["status"] == "WIN" else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500") ) st.markdown( f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result:" f" <span style="color: {color}; font-weight:&quot;
        f&quot; 900;">{h['status']}</span>", unsafe_allow_html=True, ) else: st.info("Waiting for the first period cycle to log history results...") # --- AUTO-REFRESH TRIGGER --- time.sleep(1) st.rerun() _s4.metric("Win Rate", f"{win_rate:.1f}%") st.markdown("---") # --- SESSION HISTORY TABLE --- st.markdown("### 📊 Live Session Logs") if st.session_state.history: for h in st.session_state.history[:10]: color = ( "#00FF88" if h["status"] == "WIN" else ("#FFD700" if h["status"] == "JACKPOT" else "#FF4500") ) st.markdown( f"🔹 Period: **{h['period']}** | Prediction: **{h['pred']}** | Result:" f" <span style="color: {color}; font-weight:&quot;
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
