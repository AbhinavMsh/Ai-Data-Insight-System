import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Data Insight System",
    page_icon="🧠",
    layout="centered"
)
# Custom CSS styling
st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;600;700&family=Syne:wght@700;800&display=swap');

        html, body, [class*="css"] {
            font-family: 'Space Grotesk', sans-serif;
        }

        .stApp {
            background: linear-gradient(135deg, #0a0a0f 0%, #0f0f1a 50%, #0a0f1a 100%);
            min-height: 100vh;
        }

        /* Animated background grid */
        .stApp::before {
            content: '';
            position: fixed;
            top: 0; left: 0; right: 0; bottom: 0;
            background-image:
                linear-gradient(rgba(0,200,255,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(0,200,255,0.03) 1px, transparent 1px);
            background-size: 40px 40px;
            pointer-events: none;
            z-index: 0;
        }

        /* Main heading */
        .main-heading {
            font-family: 'Syne', sans-serif;
            font-size: clamp(2rem, 5vw, 3.6rem);
            font-weight: 800;
            text-align: center;
            letter-spacing: -1px;
            line-height: 1.1;
            margin: 2.5rem 0 0.5rem;
            background: linear-gradient(90deg, #00c8ff 0%, #7b61ff 50%, #00ffc3 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            filter: drop-shadow(0 0 30px rgba(0,200,255,0.25));
        }

        .accent-bar {
            display: block;
            width: 400px;
            height: 4px;
            background: linear-gradient(90deg, #00c8ff, #7b61ff);
            border-radius: 2px;
            margin: 0.6rem auto 1.2rem;
        }

        /* Description */
        .description {
            font-size: 1.05rem;
            color: #8899bb;
            text-align: center;
            max-width: 520px;
            margin: 0 auto 2.5rem;
            line-height: 1.7;
            font-weight: 300;
        }

        .description span {
            color: #00c8ff;
            font-weight: 600;
        }

        /* Upload section card */
        .upload-card {
            background: rgba(255,255,255,0.03);
            border: 1px solid rgba(0,200,255,0.12);
            border-radius: 20px;
            padding: 2.5rem 2rem;
            max-width: 560px;
            margin: 0 auto;
            box-shadow:
                0 0 40px rgba(0,200,255,0.05),
                inset 0 1px 0 rgba(255,255,255,0.05);
            backdrop-filter: blur(12px);
        }

        .upload-label {
            font-size: 0.78rem;
            letter-spacing: 0.14em;
            text-transform: uppercase;
            color: #00c8ff;
            font-weight: 600;
            margin-bottom: 0.8rem;
            display: block;
        }

        /* Streamlit file uploader override */
        [data-testid="stFileUploader"] {
            background: rgba(0,200,255,0.04) !important;
            border: 2px dashed rgba(0,200,255,0.25) !important;
            border-radius: 14px !important;
            padding: 1.2rem !important;
            transition: all 0.3s ease !important;
        }
        [data-testid="stFileUploader"]:hover {
            border-color: rgba(0,200,255,0.55) !important;
            background: rgba(0,200,255,0.07) !important;
        }

        /* Upload icon/text */
        [data-testid="stFileUploadDropzone"] p {
            color: #7b93bb !important;
            font-size: 0.92rem !important;
        }

        /* Submit button */
        .stButton > button {
            width: 100%;
            margin-top: 1.2rem;
            padding: 0.85rem 2rem;
            background: linear-gradient(90deg, #00c8ff, #7b61ff);
            color: #fff;
            font-family: 'Space Grotesk', sans-serif;
            font-weight: 700;
            font-size: 1rem;
            letter-spacing: 0.06em;
            border: none;
            border-radius: 12px;
            cursor: pointer;
            transition: all 0.25s ease;
            box-shadow: 0 4px 24px rgba(0,200,255,0.25);
        }
        .stButton > button:hover {
            transform: translateY(-2px);
            box-shadow: 0 8px 32px rgba(0,200,255,0.4);
            filter: brightness(1.08);
        }
        .stButton > button:active {
            transform: translateY(0);
        }

        /* Success/info messages */
        .file-info {
            margin-top: 1rem;
            padding: 0.8rem 1rem;
            background: rgba(0,255,195,0.07);
            border: 1px solid rgba(0,255,195,0.2);
            border-radius: 10px;
            color: #00ffc3;
            font-size: 0.88rem;
            display: flex;
            align-items: center;
            gap: 0.5rem;
        }

        /* Footer */
        .footer {
            text-align: center;
            margin-top: 3rem;
            color: #3a4a6a;
            font-size: 0.78rem;
            letter-spacing: 0.08em;
        }

        /* Hide Streamlit default elements */
        #MainMenu, footer, header { visibility: hidden; }
        .block-container { padding-top: 0 !important; }
    </style>
""", unsafe_allow_html=True)

# --- HEADING ---
st.markdown('<h1 class="main-heading">AI DATA INSIGHT SYSTEM</h1>', unsafe_allow_html=True)
st.markdown('<span class="accent-bar"></span>', unsafe_allow_html=True)

# --- DESCRIPTION ---
st.markdown("""
    <p class="description">
        Upload your dataset and let our <span>AI-powered engine</span> extract patterns,
        generate insights, and surface the intelligence hidden within your data — instantly.
    </p>
""", unsafe_allow_html=True)

# --- UPLOAD CARD ---

st.markdown('<span class="upload-label">📂 &nbsp;Upload Your Data File</span>', unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    label="",
    type=["csv", "xlsx", "xls"],
    label_visibility="collapsed"
)

if uploaded_file:
    st.markdown(f"""
        <div class="file-info">
            ✅ &nbsp;<strong>{uploaded_file.name}</strong> &nbsp;·&nbsp; {round(uploaded_file.size / 1024, 1)} KB
        </div>
    """, unsafe_allow_html=True)

submit = st.button("⚡  Analyze with AI")

st.markdown('</div>', unsafe_allow_html=True)

# --- SUBMIT LOGIC ---
if submit:
    if uploaded_file is None:
        st.warning("⚠️ Please upload a file before submitting.")
    else:
        with st.spinner("Running AI analysis..."):
            import time
            time.sleep(1.5)  # Placeholder for real processing
        st.success(f"✅ File **{uploaded_file.name}** submitted successfully! Analysis in progress.")

# --- FOOTER ---
st.markdown('<p class="footer">AI DATA INSIGHT SYSTEM &nbsp;·&nbsp; Powered by Advanced Analytics</p>', unsafe_allow_html=True)