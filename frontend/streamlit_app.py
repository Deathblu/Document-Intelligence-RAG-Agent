import streamlit as st
import requests


# =========================================================
# PAGE CONFIG
# =========================================================

st.set_page_config(
    page_title="Document Intelligence RAG Agent",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)


# =========================================================
# SESSION STATE
# =========================================================

if "messages" not in st.session_state:
    st.session_state.messages = []

if "pdf_uploaded" not in st.session_state:
    st.session_state.pdf_uploaded = False


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown("""
<style>

/* =========================================================
GLOBAL
========================================================= */

html, body, [class*="css"]  {

    font-family: "Inter", sans-serif;
}


/* =========================================================
APP BACKGROUND
========================================================= */

.stApp {

    background:
    radial-gradient(circle at top left, rgba(59,130,246,0.18), transparent 30%),
    radial-gradient(circle at bottom right, rgba(139,92,246,0.18), transparent 30%),
    linear-gradient(
        135deg,
        #020617 0%,
        #0F172A 40%,
        #111827 70%,
        #1E1B4B 100%
    );

    color: #F8FAFC;
}


/* =========================================================
STREAMLIT HEADER
========================================================= */

header[data-testid="stHeader"] {

    background: rgba(2,6,23,0.45);

    backdrop-filter: blur(18px);

    border-bottom: 1px solid rgba(255,255,255,0.06);
}


/* =========================================================
MAIN AREA
========================================================= */

.main,
.block-container,
section.main {

    background: transparent !important;
}

.block-container {

    max-width: 1100px;

    padding-top: 2rem;

    padding-bottom: 5rem;
}


/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        rgba(2,6,23,0.96),
        rgba(15,23,42,0.96)
    );

    border-right: 1px solid rgba(255,255,255,0.06);

    box-shadow:
        4px 0 30px rgba(0,0,0,0.35);
}

[data-testid="stSidebar"] * {

    color: #F8FAFC;
}


/* =========================================================
SIDEBAR TEXT
========================================================= */

.sidebar-title {

    font-size: 34px;

    font-weight: 800;

    margin-top: 8px;

    margin-bottom: 8px;

    letter-spacing: -1px;
}

.sidebar-subtitle {

    color: #94A3B8;

    font-size: 15px;

    line-height: 1.8;

    margin-bottom: 28px;
}

.sidebar-bottom-text {

    color: #94A3B8;

    font-size: 14px;

    line-height: 1.9;

    margin-top: 25px;
}


/* =========================================================
UPLOAD BOX
========================================================= */

section[data-testid="stFileUploader"] {

    background: rgba(15,23,42,0.70);

    border: 1px solid rgba(255,255,255,0.08);

    border-radius: 24px;

    padding: 16px;

    backdrop-filter: blur(16px);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.22);
}


/* DROPZONE */

[data-testid="stFileUploaderDropzone"] {

    background: rgba(2,6,23,0.78) !important;

    border: 1px dashed rgba(255,255,255,0.12) !important;

    border-radius: 18px !important;

    padding: 22px !important;
}


/* UPLOADER TEXT */

[data-testid="stFileUploaderDropzone"] * {

    color: #F8FAFC !important;
}


/* BUTTON */

[data-testid="stFileUploaderDropzone"] button {

    background:
    linear-gradient(
        135deg,
        #2563EB,
        #7C3AED
    ) !important;

    border: none !important;

    color: white !important;

    border-radius: 14px !important;

    padding: 10px 20px !important;

    font-weight: 700 !important;

    transition: 0.25s ease;
}

[data-testid="stFileUploaderDropzone"] button:hover {

    transform: translateY(-2px);

    box-shadow:
        0 10px 24px rgba(59,130,246,0.35);
}


/* =========================================================
HERO SECTION
========================================================= */

.hero-title {

    font-size: 72px;

    font-weight: 900;

    line-height: 1;

    letter-spacing: -3px;

    margin-top: 40px;

    margin-bottom: 18px;

    color: white;
}

.hero-subtitle {

    color: #94A3B8;

    font-size: 22px;

    line-height: 1.8;

    margin-bottom: 40px;
}


/* =========================================================
CHAT MESSAGE
========================================================= */

.stChatMessage {

    background: rgba(15,23,42,0.55);

    border: 1px solid rgba(255,255,255,0.06);

    border-radius: 24px;

    padding: 18px;

    margin-bottom: 18px;

    backdrop-filter: blur(18px);

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}

.stChatMessage p {

    color: #F8FAFC !important;

    line-height: 1.9;
}


/* =========================================================
CHAT INPUT
========================================================= */

.stChatInputContainer {

    background: transparent !important;

    border: none !important;
}

.stChatInputContainer > div {

    background: rgba(15,23,42,0.72) !important;

    border: 1px solid rgba(255,255,255,0.08) !important;

    border-radius: 24px !important;

    padding: 10px 18px !important;

    backdrop-filter: blur(18px);

    box-shadow:
        0 8px 30px rgba(0,0,0,0.12);
}

.stChatInput input {

    color: #F8FAFC !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stChatInput input::placeholder {

    color: #94A3B8 !important;
}


/* =========================================================
INFO BOX
========================================================= */

.stInfo {

    background: rgba(37,99,235,0.14);

    border: 1px solid rgba(59,130,246,0.22);

    border-radius: 20px;
}


/* =========================================================
SUCCESS
========================================================= */

.stSuccess {

    background: rgba(16,185,129,0.14);

    border: 1px solid rgba(16,185,129,0.24);

    border-radius: 18px;
}


/* =========================================================
FOOTER
========================================================= */

.footer {

    text-align: center;

    margin-top: 40px;

    margin-bottom: 10px;

    color: rgba(255,255,255,0.55);

    font-size: 13px;
}


/* =========================================================
SCROLLBAR
========================================================= */

::-webkit-scrollbar {

    width: 10px;
}

::-webkit-scrollbar-track {

    background: transparent;
}

::-webkit-scrollbar-thumb {

    background: rgba(255,255,255,0.12);

    border-radius: 20px;
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# SIDEBAR
# =========================================================

with st.sidebar:

    st.markdown(
        """
        <div class="sidebar-title">
            🤖 RAG Agent
        </div>

        <div class="sidebar-subtitle">
            AI-powered document understanding and conversational retrieval.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown("---")

    st.markdown("### 📄 Upload Document")

    uploaded_file = st.file_uploader(
        "Upload PDF",
        type=["pdf"],
        label_visibility="collapsed"
    )

    if uploaded_file is not None:

        with st.spinner("Processing PDF..."):

            files = {
                "file": uploaded_file
            }

            response = requests.post(
                "http://127.0.0.1:8000/upload",
                files=files
            )

            if response.status_code == 200:

                st.session_state.pdf_uploaded = True

                st.success("PDF indexed successfully")

            else:

                st.error("Upload failed")

    st.markdown("---")

    st.markdown(
        """
        <div class="sidebar-bottom-text">
            Semantic retrieval • Context-aware AI answers • Conversational document analysis.
        </div>
        """,
        unsafe_allow_html=True
    )


# =========================================================
# HERO
# =========================================================

st.markdown(
    """
    <div class="hero-title">
        Document Intelligence
    </div>

    <div class="hero-subtitle">
        Understand documents through conversational AI.
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# CHAT HISTORY
# =========================================================

for message in st.session_state.messages:

    with st.chat_message(message["role"]):

        st.markdown(message["content"])


# =========================================================
# CHAT INPUT
# =========================================================

if st.session_state.pdf_uploaded:

    prompt = st.chat_input(
        "Ask something about your document..."
    )

    if prompt:

        st.session_state.messages.append(
            {
                "role": "user",
                "content": prompt
            }
        )

        with st.chat_message("user"):

            st.markdown(prompt)

        with st.chat_message("assistant"):

            with st.spinner("Thinking..."):

                try:

                    response = requests.get(
                        "http://127.0.0.1:8000/ask",
                        params={"query": prompt}
                    )

                    answer = response.json()["answer"]

                    st.markdown(answer)

                    st.session_state.messages.append(
                        {
                            "role": "assistant",
                            "content": answer
                        }
                    )

                except Exception:

                    st.error("Failed to connect to backend")

else:

    st.info("👉 Upload a PDF from the sidebar to begin.")


# =========================================================
# FOOTER
# =========================================================

st.markdown(
    """
    <div class="footer">
        Built with ❤️ using LangChain • ChromaDB • Groq • FastAPI • Streamlit
    </div>
    """,
    unsafe_allow_html=True
)