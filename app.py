import streamlit as st
from deep_translator import GoogleTranslator

# 1. Page Configuration
st.set_page_config(
    page_title="PolyGlot.AI", 
    page_icon="🧬", 
    layout="centered"
)

# Advanced Global Network & Realistic Animated Matrix CSS
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;800&family=Space+Grotesk:wght@500;700&display=swap');

    /* Premium Deep Space Matrix Background */
    .stApp {
        background: radial-gradient(circle at 50% 20%, #0d0a21 0%, #05040d 60%, #010103 100%);
        overflow: hidden;
    }
    
    /* Background Cyber Grid Lines and Nodes Effect */
    .cyber-grid {
        position: fixed;
        top: 0; left: 0; width: 100%; height: 100%;
        background-image: 
            linear-gradient(rgba(0, 242, 254, 0.03) 1px, transparent 1px),
            linear-gradient(90deg, rgba(0, 242, 254, 0.03) 1px, transparent 1px);
        background-size: 40px 40px;
        pointer-events: none;
        z-index: 0;
    }

    /* Header Typography */
    .main-title {
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-weight: 800;
        font-size: 3.2rem;
        color: #ffffff;
        text-align: center;
        margin-bottom: 5px;
        letter-spacing: -1.5px;
        text-transform: uppercase;
    }
    .gradient-text {
        background: linear-gradient(135deg, #00f2fe 0%, #4facfe 50%, #ff007f 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }
    
    /* Interactive Translation Containers */
    div[data-baseweb="textarea"] {
        background: rgba(13, 10, 33, 0.7) !important;
        border: 1px solid rgba(0, 242, 254, 0.2) !important;
        border-radius: 14px !important;
        backdrop-filter: blur(16px);
        transition: all 0.3s ease;
    }
    div[data-baseweb="textarea"]:focus-within {
        border-color: #00f2fe !important;
        box-shadow: 0 0 20px rgba(0, 242, 254, 0.3) !important;
    }
    textarea {
        color: #ffffff !important;
        font-family: 'Plus Jakarta Sans', sans-serif !important;
    }
    
    /* Clean Terminal Output Box */
    .output-box {
        background: rgba(255, 0, 127, 0.03);
        border: 1px solid rgba(255, 0, 127, 0.2);
        padding: 22px;
        border-radius: 14px;
        color: #e2e0ff;
        font-family: 'Plus Jakarta Sans', sans-serif;
        font-size: 1.1rem;
        min-height: 120px;
        line-height: 1.6;
        backdrop-filter: blur(16px);
        box-shadow: inset 0 0 20px rgba(255, 0, 127, 0.05);
    }
    
    /* Sleek Custom Select Fields */
    div[data-baseweb="select"] {
        background-color: #0d0a21 !important;
        border: 1px solid rgba(0, 242, 254, 0.15) !important;
        border-radius: 10px !important;
    }
    div[data-baseweb="select"] * {
        color: #ffffff !important;
        font-family: 'Space Grotesk', sans-serif;
    }
    label {
        color: #00f2fe !important;
        font-family: 'Space Grotesk', sans-serif !important;
        letter-spacing: 1px;
        font-size: 0.85rem !important;
    }
    </style>

    <div class="cyber-grid"></div>
""", unsafe_allow_html=True)

# 2. Advanced Realistic Core Logo Injection (Canvas Based Kinetic Design)
logo_html = """
<div style="display: flex; justify-content: center; align-items: center; margin-bottom: 5px;">
    <canvas id="neuralCanvas" width="100" height="100" style="filter: drop-shadow(0px 0px 12px rgba(0, 242, 254, 0.8));"></canvas>
</div>
<script>
    const canvas = document.getElementById('neuralCanvas');
    const ctx = canvas.getContext('2d');
    let angle = 0;

    function drawLogo() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        const cx = canvas.width / 2;
        const cy = canvas.height / 2;
        
        // Dynamic Outer Intersecting Language Arc 1
        ctx.beginPath();
        ctx.ellipse(cx, cy, 38, 14, angle, 0, Math.PI * 2);
        ctx.strokeStyle = '#00f2fe';
        ctx.lineWidth = 2;
        ctx.stroke();

        // Dynamic Outer Intersecting Language Arc 2
        ctx.beginPath();
        ctx.ellipse(cx, cy, 38, 14, -angle - (Math.PI / 4), 0, Math.PI * 2);
        ctx.strokeStyle = '#ff007f';
        ctx.lineWidth = 2;
        ctx.stroke();
        
        // Quantum Neural Core Node
        ctx.beginPath();
        ctx.arc(cx, cy, 10, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff';
        ctx.shadowColor = '#00f2fe';
        ctx.shadowBlur = 15;
        ctx.fill();
        ctx.shadowBlur = 0; // reset
        
        angle += 0.02;
        requestAnimationFrame(drawLogo);
    }
    drawLogo();
</script>
"""
st.components.v1.html(logo_html, height=110)

# Branding Layout
st.markdown('<h1 class="main-title">POLYGLOT.<span class="gradient-text">AI</span></h1>', unsafe_allow_html=True)

# Glowing Custom Badges
st.markdown("""
    <div style="text-align: center; margin-bottom: 2.5rem;">
        <span style="
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            padding: 6px 16px;
            background: rgba(0, 242, 254, 0.05);
            border: 1px solid rgba(0, 242, 254, 0.3);
            border-radius: 30px;
            color: #00f2fe;
            text-shadow: 0 0 12px rgba(0, 242, 254, 0.6);
            display: inline-block;
        ">
            ⚡ INSTANT MULTI-LANGUAGE TRANSLATOR
        </span>
        <span style="
            font-family: 'Space Grotesk', sans-serif;
            font-size: 0.95rem;
            font-weight: 700;
            letter-spacing: 2px;
            text-transform: uppercase;
            padding: 6px 16px;
            background: rgba(255, 0, 127, 0.05);
            border: 1px solid rgba(255, 0, 127, 0.3);
            border-radius: 30px;
            color: #ff007f;
            text-shadow: 0 0 12px rgba(255, 0, 127, 0.6);
            display: inline-block;
            margin-left: 8px;
        ">
            NEURAL ENGINE 🧠
        </span>
    </div>
""", unsafe_allow_html=True)

# 3. Supported Languages Mapping
SUPPORTED_LANGUAGES = {
    "English": "en",
    "Hindi": "hi",
    "Spanish": "es",
    "French": "fr",
    "German": "de",
    "Japanese": "ja",
    "Mandarin (Chinese)": "zh-CN",
    "Arabic": "ar",
    "Russian": "ru",
    "Italian": "it"
}

# 4. Multi-lingual Layer Inputs
col1, col2 = st.columns(2)

with col1:
    source_lang_name = st.selectbox("SOURCE NODE", list(SUPPORTED_LANGUAGES.keys()), index=0)
    source_lang_code = SUPPORTED_LANGUAGES[source_lang_name]

with col2:
    target_lang_name = st.selectbox("TARGET INSTANCE", list(SUPPORTED_LANGUAGES.keys()), index=1)
    target_lang_code = SUPPORTED_LANGUAGES[target_lang_name]

st.markdown("<br>", unsafe_allow_html=True)

# 5. Core Interface Input Text Area
source_text = st.text_area(
    label="Source Text Input:",
    placeholder="Ingest raw text strings for multi-node compilation...", 
    height=140,
    label_visibility="collapsed"
)

st.markdown("<br>", unsafe_allow_html=True)

# 6. Execution Loop Trigger
if st.button("EXECUTE NEURAL COMPILATION", type="primary", use_container_width=True):
    if not source_text.strip():
        st.warning("⚠️ Source node buffer empty. Please provide input.")
    else:
        with st.spinner("Decoding language vectors..."):
            try:
                # Backend Layer Trigger
                translator = GoogleTranslator(source=source_lang_code, target=target_lang_code)
                translated_result = translator.translate(source_text)
                
                # Render Clean Custom Output Card
                st.markdown("<h5 style='color:#ff007f; font-family:\"Space Grotesk\"; letter-spacing: 1px;'>SYNTHESIZED MATRIX OUTPUT</h5>", unsafe_allow_html=True)
                st.markdown(f'<div class="output-box">{translated_result}</div>', unsafe_allow_html=True)
                st.markdown("<br>", unsafe_allow_html=True)
                
                # 7. Cyan-to-Blue Audio Injection Button
                safe_js_text = translated_result.replace("'", "\\'").replace("\n", " ")
                
                tts_html_script = f"""
                <script>
                    function playTTS() {{
                        if ('speechSynthesis' in window) {{
                            var speech = new SpeechSynthesisUtterance('{safe_js_text}');
                            speech.lang = '{target_lang_code}';
                            window.speechSynthesis.speak(speech);
                        }} else {{
                            alert("Speech engine initialization failed.");
                        }}
                    }}
                </script>
                <div style="text-align: center;">
                    <button onclick="playTTS()" style="background: linear-gradient(135deg, #00f2fe 0%, #4facfe 100%); color: #0d0a21; border: none; padding: 14px 45px; border-radius: 30px; cursor: pointer; font-size: 15px; font-family: 'Space Grotesk', sans-serif; font-weight: bold; box-shadow: 0 0 25px rgba(0, 242, 254, 0.5); transition: all 0.3s ease; text-transform: uppercase; letter-spacing: 1px;">
                        🔊 Stream Audio Manifest
                    </button>
                </div>
                """
                st.components.v1.html(tts_html_script, height=70)

            except Exception as e:
                st.error(f"Matrix Synthesis Error: {e}")