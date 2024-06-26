import streamlit as st
import firebase_admin
from firebase_admin import credentials, firestore

# Inicializa Firebase
cred = credentials.Certificate("ayemeter4-firebase-adminsdk-kooi0-dd377e6518.json")  # Reemplaza con la ruta correcta a tu archivo JSON
firebase_admin.initialize_app(cred)
db = firestore.client()

# Función para obtener el emoji actual desde Firestore
def get_current_emoji():
    doc_ref = db.collection("emojis").document("current")
    doc = doc_ref.get()
    if doc.exists:
        return doc.to_dict().get("emoji", "😃")
    else:
        return "😃"

# Función para actualizar el emoji en Firestore
def update_emoji(new_emoji):
    doc_ref = db.collection("emojis").document("current")
    doc_ref.set({"emoji": new_emoji})

# Interfaz de usuario con Streamlit
st.title("AYEMOOD")

# Obtener el emoji actual desde Firestore
current_emoji = get_current_emoji()

# Mostrar el emoji actual
st.markdown(f"<div style='text-align: center; font-size: 100px;'>{current_emoji}</div>", unsafe_allow_html=True)

# Entrada de texto para el nuevo emoji
new_emoji = st.text_input("Introduce un emoji:", value=current_emoji)

# Botón para actualizar el emoji
if st.button("ACTUALIZAR"):
    update_emoji(new_emoji)
    st.experimental_rerun()  # Recargar la aplicación para reflejar el cambio