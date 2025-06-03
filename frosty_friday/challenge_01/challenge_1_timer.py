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

md_text = """
### 🏁 Challenge Goal

You work with raw invoice descriptions like:

- `"Deployment of Snowflake project - Phase 1"`
- `"Data ingestion pipeline optimization"`

Your task is to **classify each description** into a standard category using **Snowflake Cortex's** `CLASSIFY_TEXT()` function in a new bridging table.

---

### 🎯 Requirements

- Use `invoice_line_items` and `service_categories` as dbt sources and models.
- Dynamically pull the full list of categories into an array using `ARRAY_AGG()`.
- Run `AI_CLASSIFY(input, classes)` to classify each line item.

---

### 📥 Output

Your result should include:

- `line_item_id`
- `service_description`
- `predicted_category`

---

### 💡 Hint

You’ll need to use a CTE to first aggregate all category names into an array:  
Then join that into every row using a cross join with `{{ ref('invoice_line_items') }}`.

---

### 🧪 Bonus

Try adding confidence scores using `CLASSIFY_TEXT_PROBABILITIES()`!
"""

st.set_page_config(page_title="⏱ FROSTY_FRIDAY() Timer", layout="centered")

# --- Cached Snowflake connection ---
@st.cache_resource
def get_snowflake_connection():
    session = get_active_session()
    return session.connection

# --- Ensure leaderboard table exists ---
def ensure_leaderboard_table_exists(cursor):
    create_table_query = """
    CREATE TABLE IF NOT EXISTS public.leaderboard_table (
        user_name STRING,
        correct INTEGER,
        duration STRING
    )
    """
    cursor.execute(create_table_query)

# --- Initialize ---
conn = get_snowflake_connection()
cursor = conn.cursor()
ensure_leaderboard_table_exists(cursor)

st.image(logo)
st.title("🥶 Challenge 1")
st.subheader("AI-Powered Text Classification with Cortex")
st.markdown("Start the timer and stop it as quickly as you can!")

# --- Start Screen: Enter Name and Start ---
if "timer_started" not in st.session_state:
    user_name = st.text_input("Enter your name:")
    if st.button("Start Timer") and user_name:
        st.session_state["user_name"] = user_name
        st.session_state["start_time"] = time.time()
        st.session_state["timer_started"] = True
        st.session_state.pop("end_time", None)
        st.session_state.pop("time_submitted", None)
        st.rerun()
    st.markdown(md_text)
    st.markdown("---")
    st.caption("Made with ❤️ for Frosty Fridays ❄️ Powered by Snowflake 🔷")
    st.stop()

# --- Timer Running ---
if "timer_started" in st.session_state and "end_time" not in st.session_state:
    st.markdown(f"### ⏱️ Timer Running for **{st.session_state['user_name']}**")
    elapsed_sec = time.time() - st.session_state["start_time"]
    st.metric(label="Elapsed Time", value=f"{elapsed_sec:.3f} s")
    if st.button("🛑 Stop Timer"):
        st.session_state["end_time"] = time.time()
        st.rerun()
    time.sleep(1)
    st.markdown(md_text)
    st.markdown("---")
    st.caption("Made with ❤️ for Frosty Fridays ❄️ Powered by Snowflake 🔷")
    st.rerun()

# --- Timer Stopped ---
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

    st.markdown(md_text)
    st.markdown("---")
    st.caption("Made with ❤️ for Frosty Fridays ❄️ Powered by Snowflake 🔷")

# --- Leaderboard ---
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
