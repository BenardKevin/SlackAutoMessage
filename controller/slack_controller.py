import time
import datetime
import streamlit as st
from slack_sdk.errors import SlackApiError
from model.config import client

def schedule_messages(channel_id, date, messages):
    for msg in messages:
        try:
            dt = datetime.datetime.strptime(f"{date} {msg['time']}", "%Y-%m-%d %H:%M")
            ts = int(time.mktime(dt.timetuple()))
            client.chat_scheduleMessage(channel=channel_id, text=msg["text"], post_at=ts)

            print(f"✅ Message scheduled at {msg['time']}: {msg['text'][:40]}...")
        except SlackApiError as e:
            print(f"❌ Slack API error: {e.response['error']}")
        except Exception as ex:
            print(f"❌ Error: {ex}")

def send_message(channel_id, message, timestamp):
    st.info(f"{datetime.fromtimestamp(timestamp).strftime('%H:%M')} → {channel_id} : {message[:80]}...")

def test_slack_connection(channel_id):
    try:
        response = client.chat_postMessage(
            channel=channel_id,
            text="Connexion Slack réussie depuis l'application !"
        )
        return True, response["ts"]
    except SlackApiError as e:
        return False, e.response["error"]
    except Exception as ex:
        return False, str(ex)