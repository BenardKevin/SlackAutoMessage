import streamlit as st
from message_loader import load_default_messages
from slack_controller import schedule_messages, test_slack_connection
from ui import sidebar_inputs, message_inputs, preview_messages

def main():
    st.title("Slack Auto Message")

    defaults = load_default_messages()
    channel_id, date, course_name = sidebar_inputs(defaults)
    st.markdown("---")
    raw_messages = message_inputs(defaults.get("messages", []))

    for msg in raw_messages:
        msg["text"] = msg["text"].replace("{course}", course_name)

    preview_messages(raw_messages, course_name)
    col1, col2 = st.columns([1, 1])
    with col1:
        if st.button("Test Slack connection"):
            ok, result = test_slack_connection(channel_id)
            if ok:
                print(f"Slack connection successful!")
            else:
                print(f"Connection failure: {result}")
    with col2:
        if st.button("Schedule messages"):
            schedule_messages(channel_id, date, raw_messages)

if __name__ == "__main__":
    main()
