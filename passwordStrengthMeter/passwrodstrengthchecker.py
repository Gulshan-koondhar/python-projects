import streamlit as st
import string
import random
import re

def password_checker(password):
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        st.error("❌ Password should be at least 8 characters long.")
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:   
        st.error("❌ Include both uppercase and lowercase letters.")
    if re.search(r"\d", password):
        score += 1
    else:
        st.error("❌ Add at least one number (0-9).")
    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        st.error("❌ Include at least one special character (!@#$%^&*).")

    if score == 4:
        st.success("✅ Strong Password!")
        st.progress(score/4)
    elif score == 3:
        st.warning("⚠️ Moderate Password - Consider adding more security features.")
        st.progress(score/4)
    elif score == 2:
        st.error("⚠️ Weak Password - Needs improvement.")
        st.progress(score/4)
    else:
        st.error("❌ Very Weak Password - Improve it using the suggestions above.")
        st.progress(score/4)
    

st.title("🔐 Password Strength Checker")
password = st.text_input("Enter your password:")
password_checker(password)

def generate_password(length):
    characters = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(characters) for i in range(length))

if st.button("Generate Strong Password"):
    st.success(generate_password(random.randint(8, 12)))