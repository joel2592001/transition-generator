
import streamlit as st
import openai

openai.api_key = st.secrets["openai_api_key"]

st.title("🧠 Transition Generator (GPT-4)")
st.markdown("Enter two paragraphs separated by the keyword `TRANSITION`. The app will generate a natural connector between them.")

input_text = st.text_area("✍️ Enter full text (use TRANSITION to separate)", height=250)

if st.button("✨ Generate Transition"):
    if "TRANSITION" not in input_text:
        st.error("Please include the keyword TRANSITION between the two paragraphs.")
    else:
        messages = [
            {"role": "system", "content": "You are a French news assistant that replaces the word TRANSITION with a short, natural and context-aware phrase (5–10 words) that logically connects two paragraphs."},
            {"role": "user", "content": "Le club de tennis de Rennes a organisé un tournoi pour les jeunes.\nTRANSITION\nUn incendie s’est déclaré dans un entrepôt du centre-ville."},
            {"role": "assistant", "content": "Dans l’actualité locale plus dramatique, un"},
            {"role": "user", "content": "Le marché de Noël d’Arras a accueilli des milliers de visiteurs.\nTRANSITION\nLe conseil municipal a débattu d’un plan pour les transports publics."},
            {"role": "assistant", "content": "Sur le plan politique local, le"},
            {"role": "user", "content": input_text}
        ]

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=messages,
                temperature=0.7,
                max_tokens=20
            )
            st.success("✅ Suggested Transition:")
            st.markdown(f"**{response.choices[0].message.content.strip()}**")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
