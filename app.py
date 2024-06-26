import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Ruta a tu archivo JSON de credenciales de Firebase
cred = credentials.Certificate("ayemeter4-firebase-adminsdk-kooi0-dd377e6518.json")
firebase_admin.initialize_app(cred)

# Cliente de Firestore
db = firestore.client()

st.title("AYEMOOD")

# Obtener o inicializar el valor del emoji
doc_ref = db.collection("emojis").document("current_emoji")
doc = doc_ref.get()

if doc.exists:
    emoji = doc.to_dict().get("emoji", "😍")
else:
    emoji = "😍"

# Entrada y botón para actualizar el emoji
new_emoji = st.text_input("Introduce un emoji:", value=emoji)

if st.button("ACTUALIZAR"):
    doc_ref.set({"emoji": new_emoji})
    st.success("Emoji actualizado!")

# Mostrar el emoji actual
st.markdown(f"<div style='text-align: center; font-size: 100px;'>{new_emoji}</div>", unsafe_allow_html=True)
