import os
from dotenv import load_dotenv
import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.schema import SystemMessage, HumanMessage, AIMessage
load_dotenv()

os.environ["GOOGLE_API_KEY"] = os.getenv("GOOGLE_API_KEY")

def main():

    llm = ChatGoogleGenerativeAI(
        model="models/gemini-1.5-flash")

    st.set_page_config(
        page_title="Sample ChatApp with Streamlit",
        page_icon="😎"
    )
    st.header("Sample ChatApp with Streamlit")


    # チャット履歴初期化
    if "messages" not in st.session_state:
        st.session_state.messages = [
            SystemMessage(content="あなたはとても優秀なアシスタントです。")
        ]

    # チャット入力
    if user_input := st.chat_input("質問を入力してくださいね！"):
        st.session_state.messages.append(HumanMessage(content=user_input))
        response = llm.invoke(st.session_state.messages)
        st.session_state.messages.append(AIMessage(content=response.content))

    # チャット履歴表示
    messages = st.session_state.get("messages", [])
    for message in messages:
        if isinstance(message, AIMessage):
            st.markdown(message.content)
        elif isinstance(message, HumanMessage):
            st.text_area("あなた", value=message.content, height=100)
        else:
            st.write(f"システム: {message.content}")


if __name__ == '__main__':
    main()