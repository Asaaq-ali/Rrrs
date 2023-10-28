import pyrogram

app = pyrogram.Client(
    "session_name",
    23308690,
    "0a64b7fb353afea42c8847bd5ae5c744",
    in_memory=True
)

app.start()

string_session = app.export_session_string()

app.send_message("me", f"`{string_session}`")

print("\n\nCHECK SAVED MESSAGES")
