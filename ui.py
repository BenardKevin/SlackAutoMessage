import streamlit as st

def sidebar_inputs(defaults):
    with st.sidebar:
        st.header("Settings")
        channel_id = st.text_input("Channel Slack", value=defaults.get("channel_id", ""))
        date = st.date_input("Date", value=defaults.get("date", "2025-07-23"))
        course_name = st.text_input("Course Name", value=defaults.get("course_name", ""))
    return channel_id, date, course_name

def message_inputs(defaults):
    messages = []
    with st.expander("Edit messages to schedule", expanded=False):
        st.header("Messages to schedule")
        for i, msg in enumerate(defaults):
            col1, col2 = st.columns([1, 5])
            with col1:
                time = st.text_input(f"Hour {i+1}", value=msg["time"], key=f"time_{i}")
            with col2:
                text = st.text_area(f"Content {i+1}", value=msg["text"], height=100, key=f"text_{i}")
            messages.append({"time": time, "text": text})
    return messages

def preview_messages(messages, course_name):
    st.markdown("### Preview of personalized messages")
    for i, msg in enumerate(messages):
        formatted = msg["text"].replace("[course_name]", course_name)
        st.markdown(f"**[{msg['time']}]**")
        st.markdown(f"<pre>{formatted}</pre>", unsafe_allow_html=True)
        st.markdown("---")
