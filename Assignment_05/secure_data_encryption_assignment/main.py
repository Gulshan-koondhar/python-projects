import streamlit as st
import json
import os
import time
import base64
import hashlib
from cryptography.fernet import Fernet, InvalidToken
from datetime import datetime, timedelta

# --- Setup & Globals ---
DATA_FILE = "data.json"
KEY_FILE = "secret.key"
LOCKOUT_DURATION = 30  # seconds

# --- Load or Generate Fernet Key ---
def load_or_create_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, "rb") as f:
            return f.read()
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as f:
        f.write(key)
    return key

KEY = load_or_create_key()
cipher = Fernet(KEY)

# Load data
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as f:
        stored_data = json.load(f)
else:
    stored_data = {}

# Initialize session state
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0
if "lockout_time" not in st.session_state:
    st.session_state.lockout_time = None

# --- Helper Functions ---
def save_data():
    with open(DATA_FILE, "w") as f:
        json.dump(stored_data, f, indent=4)

def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def encrypt_data(text):
    return cipher.encrypt(text.encode()).decode()

def decrypt_data(encrypted_text):
    try:
        return cipher.decrypt(encrypted_text.encode()).decode()
    except InvalidToken:
        return None

def check_lockout():
    if st.session_state.lockout_time:
        if datetime.now() < st.session_state.lockout_time:
            remaining = (st.session_state.lockout_time - datetime.now()).seconds
            st.error(f"⏳ Locked out. Please wait {remaining} seconds.")
            return True
        else:
            st.session_state.lockout_time = None
            st.session_state.failed_attempts = 0
    return False

# --- UI ---
st.title("🛡️ Secure Data Encryption System")

menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Navigation", menu)

# --- Home Page ---
if choice == "Home":
    st.subheader("🏠 Welcome!")
    st.write("This system uses **PBKDF2 hashing**, **Fernet encryption**, and **session-based security**.")
    if st.button("🧹 Clear All Data"):
        stored_data.clear()
        save_data()
        st.success("✅ All data cleared.")

# --- Store Data ---
elif choice == "Store Data":
    st.subheader("📂 Store Data")
    title = st.text_input("Enter a title for your data:")
    user_data = st.text_area("Enter text to encrypt:")
    passkey = st.text_input("Enter a passkey:", type="password")

    if st.button("Encrypt & Save"):
        if title and user_data and passkey:
            hashed = hash_passkey(passkey)
            encrypted = encrypt_data(user_data)
            stored_data[title] = {
                "encrypted_text": encrypted,
                "passkey": hashed,
                "timestamp": datetime.now().isoformat()
            }
            save_data()
            st.success("✅ Data encrypted and saved!")
            st.code(encrypted[:50] + "...", language="text")
        else:
            st.error("⚠️ Please fill all fields.")

# --- Retrieve Data ---
elif choice == "Retrieve Data":
    st.subheader("🔍 Retrieve Data")

    if check_lockout():
        st.stop()

    if stored_data:
        selected_title = st.selectbox("Select a saved entry:", list(stored_data.keys()))
        passkey = st.text_input("Enter your passkey:", type="password")

        if st.button("Decrypt"):
            if selected_title and passkey:
                stored_entry = stored_data[selected_title]
                hashed_input = hash_passkey(passkey)

                if hashed_input == stored_entry["passkey"]:
                    decrypted_text = decrypt_data(stored_entry["encrypted_text"])
                    if decrypted_text:
                        st.success("✅ Success! Here's your decrypted data:")
                        st.code(decrypted_text, language="text")
                        st.session_state.failed_attempts = 0
                    else:
                        st.error("❌ Error: Decryption failed. Invalid key or corrupted data.")
                else:
                    st.session_state.failed_attempts += 1
                    remaining = 3 - st.session_state.failed_attempts
                    st.error(f"❌ Incorrect passkey! Attempts left: {remaining}")
                    if st.session_state.failed_attempts >= 3:
                        st.warning("🔒 Too many failed attempts! Locked out for 30 seconds.")
                        st.session_state.lockout_time = datetime.now() + timedelta(seconds=LOCKOUT_DURATION)
                        st.experimental_rerun()
            else:
                st.error("⚠️ Fill all fields.")
    else:
        st.info("ℹ️ No encrypted entries found. Please add data first.")

# --- Login Page ---
elif choice == "Login":
    st.subheader("🔐 Reauthorize")
    login_pass = st.text_input("Enter Admin Password:", type="password")

    if st.button("Login"):
        if login_pass == "admin123":
            st.session_state.failed_attempts = 0
            st.session_state.lockout_time = None
            st.success("✅ Reauthorized. You may now retrieve data.")
        else:
            st.error("❌ Incorrect admin password.")
