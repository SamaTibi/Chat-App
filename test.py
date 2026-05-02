import streamlit as st
import random

def get_response(text):
    text_lower = text.lower().strip()

    greetings = ["hi", "hello", "hey", "nice to meet you"]
    goodbays = ["bye", "goodbye", "see you later"]
    how_are_you = ["how are you", "whats up", "how do you do"]
    thanks = ["thanks", "thank you", "thx", "welcome"]
    name_q = ["your name", "who are you", "what are you", "what's your name", "whats your name"]
    help_q = ["help", "help me", "i need help", "can you help"]
    topics_q = ["what can you talk about", "what do you know", "talk to me", "tell me something", "what topics", "what can we talk about", "suggest something", "what can you do"]

    if any(w in text_lower for w in greetings):
        return random.choice([
            "hey! nice to see you",
            "hi there, how is your day going?",
            "hello! ready to chat?",
            "hey, what is on your mind today?",
            "hi! i am here if you need anything"
        ])

    if any(w in text_lower for w in goodbays):
        return random.choice([
            "take care!",
            "bye, come back anytime",
            "see you later, hope your day goes well",
            "goodbye! it was nice chatting with you",
            "bye for now"
        ])

    if any(w in text_lower for w in how_are_you):
        return random.choice([
            "i am doing great, thanks for asking. how about you?",
            "i am good and ready to chat with you",
            "all good here. how are you feeling today?",
        ])

    if any(w in text_lower for w in thanks):
        return random.choice([
            "you are very welcome",
            "happy to help anytime",
            "no worries at all",
            "glad i could help you",
        ])

    if any(w in text_lower for w in name_q):
        return random.choice([
            "i am sama's chatbot. nice to meet you",
            "people call me sama assistant",
            "i am your chatbot assistant"
        ])

    if any(w in text_lower for w in help_q):
        return random.choice([
            "of course. what do you need help with?",
            "sure, tell me what is going on",
            "i will do my best. what are you looking for?"
        ])

    if any(w in text_lower for w in topics_q):
        return random.choice([
            "we can talk about palestinian cities like tulkarm, nablus, jenin, gaza, jerusalem, hebron, ramallah, and jericho",
            "you can ask me simple science questions or just chat normally",
            "i can discuss city facts, history, and casual daily topics"
        ])

    if "tulkarm" in text_lower:
        return "tulkarm is a city in the northern west bank known for its agricultural land especially citrus fruits it also has a strong history of resistance and is home to many refugee camps like nur shams and tulkarm camp"

    if "nablus" in text_lower:
        return "nablus is famous for its old city its traditional soap made from olive oil and of course knafeh nablus is considered the home of knafeh and it's known as the mountain of fire for its long history of resistance"

    if "jenin" in text_lower:
        return "jenin is known for its refugee camp which became a symbol of resistance it also has a famous freedom theatre and fertile agricultural lands in the jenin valley"

    if "ramallah" in text_lower:
        return "ramallah is the administrative center of palestine it has a lively cultural scene with cafes theatres and art galleries it's also where the muqata the presidential compound is located"

    if "jerusalem" in text_lower or "al quds" in text_lower:
        return "jerusalem or al quds is the heart of palestine it's home to the al aqsa mosque the dome of the rock the church of the holy sepulchre and one of the oldest old cities in the world it holds deep meaning for muslims christians and jews"

    if "gaza" in text_lower:
        return "gaza is one of the oldest cities in the world it's known for its resilience and resistance its people have faced decades of siege but the city has a rich history of trade culture and crafts like pottery and weaving"

    if "hebron" in text_lower or "khalil" in text_lower:
        return "hebron known in arabic as al khalil is famous for its glassblowing tradition its old market and the ibrahimi mosque it's also known for producing grapes and its strong crafts industry"

    if "jericho" in text_lower:
        return "jericho is considered one of the oldest cities in the world it sits below sea level near the dead sea and is known for its warm climate its dates and bananas and ancient archaeological sites"

    science_q = ["what is", "how does", "why does", "what are", "explain", "define", "science", "physics", "chemistry", "biology", "space", "planet", "atom", "gravity", "evolution", "dna", "cell", "energy", "light", "sound"]
    if any(w in text_lower for w in science_q):
        return random.choice([
            "good science question. i may not have the full answer, but i can try",
            "interesting one. i know a little, but not everything",
            "science questions are great. ask me and i will do my best",
            "i might need to double-check that to give you a perfect answer",
            "that is important, so it is better to verify with a trusted source too"
        ])

    if "?" in text_lower:
        return random.choice([
            "that is a good question. i am not fully sure",
            "i really do not know yet",
            "i wish i had a better answer for you",
            "honestly, i am not sure"
        ])

    if len(text_lower) < 5:
        return random.choice([
            "tell me a bit more, that was short",
            "i'm listening go on"
        ])

    return random.choice([
        "keep going, i am listening",
        "tell me more about that",
        f"so you are saying \"{text}\". that is interesting",
        "i see what you mean"
    ])


st.title("Sama Chat Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ask me anything..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_response(prompt)

    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})
