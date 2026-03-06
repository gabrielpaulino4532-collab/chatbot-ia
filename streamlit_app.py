import streamlit as st
from groq import Groq

modelo_ia = Groq(api_key="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")

st.write("# Chatbot com IA")

if not "lista_mensagens" in st.session_state:
    st.session_state["lista_mensagens"] = []

texto_usuario = st.chat_input("Digite sua mensagem aqui...")

for mensagem in st.session_state["lista_mensagens"]:
    role = mensagem["role"]
    content = mensagem["content"]
    st.chat_message(role).write(content)

if texto_usuario:
    print(texto_usuario)
    st.chat_message("user").write(texto_usuario)
    mensagem_usuario = {"role": "user", "content": texto_usuario}
    st.session_state["lista_mensagens"].append(mensagem_usuario)
    # Nome
    # User (usuário normal)
    # Assistant (assistente, o chatbot)

    resposta_ia = modelo_ia.chat.completions.create(
        messages=[
            {"role": "system", "content": "Você é um assistente útil e amigável."},
            *st.session_state["lista_mensagens"]
    ],
        model="openai/gpt-oss-120b"
    )
    texto_reposta_ia = resposta_ia.choices[0].message.content
    
    st.chat_message("assistant").write(texto_reposta_ia)
    mensagem_ia = {"role": "assistant", "content": texto_reposta_ia}
    st.session_state["lista_mensagens"].append(mensagem_ia)
