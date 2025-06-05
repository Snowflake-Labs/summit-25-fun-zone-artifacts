import streamlit as st
import time
import snowflake.connector
from snowflake.snowpark.context import get_active_session

session = get_active_session()

logo = session.file.get_stream(
    "@CHALLENGE_001_DB.CHALLENGE_001_SETUP.ASSETS/cropped-Screenshot-2024-05-31-at-09.08.06.png", 
    decompress=False
).read()

qr_code = session.file.get_stream(
    "@CHALLENGE_001_DB.CHALLENGE_001_SETUP.ASSETS/frostyfriday_qr_no_logo.png",
    decompress=False
).read()

md_text_one = """
### 🌍 Challenge 03: Multilingual Feedback Classification

Use **Snowflake Cortex** to translate and summarize international customer reviews in various languages.

---

### 🎯 Objective

Analyze a single combined dataset (`customer_feedback_combined`) containing reviews in **English, Spanish, French, German, and Japanese**.
"""

md_text_two = """
### ✅ Result:

1. Translate all reviews in English
2. Summarize them all
"""

st.set_page_config(page_title="⏱ FROSTY_FRIDAY() Timer", layout="wide")

feedback_table = session.table('challenge_003_db.challenge_003_setup.customer_feedback_combined')
answer = session.table('challenge_003_db.challenge_003_setup.answer')

@st.cache_resource
def get_snowflake_connection():
    session = get_active_session()
    return session.connection

def ensure_leaderboard_table_exists(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS public.leaderboard_table (
        user_name STRING,
        correct INTEGER,
        duration STRING
    )
    """
    cursor.execute(create_table_query)

def instructions():
    st.markdown(md_text_one)
    st.dataframe(feedback_table)
    st.markdown(md_text_two)
    st.dataframe(answer)
    st.markdown("---")
    st.caption("Made with ❤️ for Frosty Fridays ❄️ Powered by Snowflake 🔷")

conn = get_snowflake_connection()
cursor = conn.cursor()
ensure_leaderboard_table_exists(cursor)

st.image(logo)
st.title("🥶 Challenge 3")
st.subheader("Multilingual Entity Sentiment with Cortex")
st.markdown("Start the timer and stop it as quickly as you can!")

if "timer_started" not in st.session_state:
    user_name = st.text_input("Enter your name:")
    if st.button("Start Timer") and user_name:
        st.session_state["user_name"] = user_name
        st.session_state["start_time"] = time.time()
        st.session_state["timer_started"] = True
        st.session_state.pop("end_time", None)
        st.session_state.pop("time_submitted", None)
        st.rerun()
    instructions()
    st.stop()

if "timer_started" in st.session_state and "end_time" not in st.session_state:
    st.markdown(f"### ⏱️ Timer Running for **{st.session_state['user_name']}**")
    elapsed_sec = time.time() - st.session_state["start_time"]
    st.metric(label="Elapsed Time", value=f"{elapsed_sec:.3f} s")
    if st.button("🛑 Stop Timer"):
        st.session_state["end_time"] = time.time()
        st.rerun()
    time.sleep(1)
    instructions()
    st.rerun()

if "end_time" in st.session_state:
    duration_sec = st.session_state["end_time"] - st.session_state["start_time"]
    duration_str = f"{duration_sec:.3f}"
    st.success(f"✅ Time recorded for **{st.session_state['user_name']}**: **{duration_str} seconds**")

    if "time_submitted" not in st.session_state:
        safe_name = st.session_state["user_name"].replace("'", "''")
        insert_query = f"""
            INSERT INTO public.leaderboard_table (user_name, correct, duration)
            VALUES ('{safe_name}', NULL, '{duration_str}')
        """
        cursor.execute(insert_query)
        st.session_state["time_submitted"] = True

    if st.button("🔄 New Timer"):
        for key in ["timer_started", "start_time", "end_time", "user_name", "time_submitted"]:
            st.session_state.pop(key, None)
        st.rerun()

    instructions()

with st.sidebar:
    st.markdown("## 👨‍💻 Join the Community!")
    st.markdown("[https://frostyfriday.org](https://frostyfriday.org)")
    st.image(qr_code)
    st.divider()
    st.markdown("## 🏆 Leaderboard")
    try:
        select_query = """
            SELECT user_name, correct, duration 
            FROM leaderboard_table 
            ORDER BY 
                CASE WHEN correct IS NULL THEN 0 ELSE correct END DESC, 
                TRY_TO_NUMBER(duration) ASC
            LIMIT 10
        """
        cursor.execute(select_query)
        leaderboard = cursor.fetchall()
        if leaderboard:
            for idx, row in enumerate(leaderboard, start=1):
                score_display = f"{row[1]}/?" if row[1] is not None else "N/A"
                emoji = "🥇" if idx == 1 else "🥈" if idx == 2 else "🥉" if idx == 3 else ""
                st.write(f"{emoji} **{row[0]}** — Score: {score_display} | Time: ⏱️ {row[2]} s")
        else:
            st.info("No leaderboard entries yet.")
    except Exception as e:
        st.error(e)
