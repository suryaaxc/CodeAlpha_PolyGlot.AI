import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import random

# BRANDING PROTOCOLS
st.set_page_config(
    page_title="QUANTUM.FAQ BOT", 
    page_icon="🤖", 
    layout="centered"
)

# STYLE INJECTION: Force Cyberpunk Grid Layout
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght=800&family=Plus+Jakarta+Sans:wght=400;600;700&family=Space+Grotesk:wght=500;700&display=swap');
    
    html, body, .stApp, div, input, p, span, h1 { user-select: none !important; }
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"], [data-testid="stMainBlockContainer"] { background: transparent !important; }
    
    html, body {
        background: 
            radial-gradient(circle at 15% 25%, rgba(57, 255, 20, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 85% 75%, rgba(255, 49, 49, 0.08) 0%, transparent 50%),
            radial-gradient(circle at 50% 30%, #110303 0%, #050000 65%, #000000 100%) !important;
        background-attachment: fixed !important; height: 100vh; margin: 0;
    }
    .brand-core-wrapper { text-align: center; margin: 40px 0 10px 0; position: relative; z-index: 10; }
    .cyber-tech-logo { width: 60px; height: 60px; margin: 0 auto 25px auto; position: relative; display: flex; align-items: center; justify-content: center; }
    .logo-square { position: absolute; width: 100%; height: 100%; border: 2px solid #39ff14; border-radius: 12px; transform: rotate(45deg); box-shadow: 0 0 15px rgba(57, 255, 20, 0.3); animation: spinClockwise 8s linear infinite; }
    .logo-inner-core { position: absolute; width: 50%; height: 50%; border: 2px dashed #ff3131; border-radius: 6px; transform: rotate(-45deg); box-shadow: 0 0 10px rgba(255, 49, 49, 0.4); animation: spinCounter 6s linear infinite; }
    @keyframes spinClockwise { 0% { transform: rotate(45deg); } 100% { transform: rotate(405deg); } }
    @keyframes spinCounter { 0% { transform: rotate(-45deg); } 100% { transform: rotate(-405deg); } }
    
    .stylish-title { font-family: 'Cinzel', serif; font-weight: 800; font-size: 3.2rem; color: #ffffff; letter-spacing: 3px; text-transform: uppercase; }
    .gradient-accent { color: #ff3131; text-shadow: 0 0 8px rgba(255, 49, 49, 0.5); }
    
    .status-bar-container { display: flex; justify-content: center; gap: 12px; margin: 15px auto 10px auto; font-family: 'Space Grotesk', sans-serif; font-size: 0.75rem; font-weight: 700; letter-spacing: 1.2px; text-transform: uppercase; }
    .status-node { padding: 6px 14px; border-radius: 20px; background: rgba(10, 5, 5, 0.7); backdrop-filter: blur(5px); display: inline-flex; align-items: center; }
    .node-green { color: #39ff14; border: 1px solid rgba(57, 255, 20, 0.25); }
    .status-pulse { display: inline-block; width: 6px; height: 6px; background: #39ff14; border-radius: 50%; margin-right: 8px; box-shadow: 0 0 8px #39ff14; animation: pulseAlpha 1.5s infinite; }
    @keyframes pulseAlpha { 0%, 100% { opacity: 0.4; } 50% { opacity: 1; } }

    .chat-container { margin: 25px 0; position: relative; z-index: 10; }
    .user-bubble { background: rgba(57, 255, 20, 0.02) !important; border: 1px solid rgba(57, 255, 20, 0.15) !important; padding: 16px 20px; border-radius: 12px 12px 0px 12px; color: #ffffff; margin-left: 15%; margin-bottom: 18px; font-family: 'Plus Jakarta Sans', sans-serif; }
    .bot-bubble { background: rgba(255, 49, 49, 0.02) !important; border: 1px solid rgba(255, 49, 49, 0.15) !important; padding: 16px 20px; border-radius: 12px 12px 12px 0px; color: #fff0f0; margin-right: 15%; margin-bottom: 18px; font-family: 'Plus Jakarta Sans', sans-serif; }
    
    div[data-baseweb="input"] { background: rgba(10, 3, 3, 0.85) !important; border: 1px solid rgba(255, 49, 49, 0.2) !important; border-radius: 30px !important; }
    input { color: #ffffff !important; font-family: 'Plus Jakarta Sans', sans-serif !important; }
    </style>
""", unsafe_allow_html=True)

# CANVAS PARTICLES ENGINE
st.components.v1.html("""
    <canvas id="particleCanvas" style="position: fixed; top: 0; left: 0; width: 100vw; height: 100vh; pointer-events: none; z-index: 0;"></canvas>
    <script>
    const canvas = document.getElementById('particleCanvas'); const ctx = canvas.getContext('2d');
    function resize() { canvas.width = window.innerWidth; canvas.height = window.innerHeight; }
    resize(); window.addEventListener('resize', resize);
    const particles = [];
    for(let i=0; i<65; i++) {
        particles.push({
            x: Math.random() * window.innerWidth, y: Math.random() * window.innerHeight,
            radius: Math.random() * 2 + 0.8, vx: (Math.random() - 0.5) * 0.7, vy: (Math.random() - 0.5) * 0.7,
            color: Math.random() > 0.5 ? 'rgba(57, 255, 20, ' : 'rgba(255, 49, 49, ', alpha: Math.random() * 0.4 + 0.1
        });
    }
    function animate() {
        ctx.clearRect(0, 0, canvas.width, canvas.height);
        for(let i=0; i<65; i++) {
            let p = particles[i]; ctx.beginPath(); ctx.arc(p.x, p.y, p.radius, 0, Math.PI * 2);
            ctx.fillStyle = p.color + p.alpha + ')'; ctx.fill(); p.x += p.vx; p.y += p.vy;
            if(p.x < 0 || p.x > canvas.width) p.vx *= -1; if(p.y < 0 || p.y > canvas.height) p.vy *= -1;
        }
        requestAnimationFrame(animate);
    }
    animate();
    </script>
""", height=0, scrolling=False)

# CORE CONTEXT BADGES
st.markdown(f"""
    <div class="brand-core-wrapper">
        <div class="cyber-tech-logo">
            <div class="logo-square"></div>
            <div class="logo-inner-core"></div>
        </div>
        <h1 class="stylish-title">QUANTUM.FAQ <span class="gradient-accent">BOT</span></h1>
        <div class="status-bar-container">
            <div class="status-node node-green"><span class="status-pulse"></span>SYSTEM CORE: ACTIVE</div>
            <div class="status-node node-green">OFFLINE KNOWLEDGE MATRIX</div>
            <div class="status-node node-green">LOCAL HIGH-DIMENSIONAL TUNED</div>
        </div>
    </div>
""", unsafe_allow_html=True)

st.markdown("---")

# 🏛️ MASSIVE REASONING UNIVERSAL DATA PACKET (Internet Bypasser)
UNIVERSAL_DATA = {
    "queries": [
        "what is your name?", "who are you", "how does this chatbot work?", 
        "what is the stack of this project?", "what is tf-idf vectorization?", 
        "how to deploy a streamlit app?", "what is cosine similarity?", "what domain is this project?",
        "compare sql vs nosql databases based on scaling and schema flexibility",
        "sql vs nosql database scaling schema",
        "who won the latest icc t20 world cup",
        "what is rest api and how does it use http methods",
        "explain the ending of the movie inception in short",
        "what has keys but opens no locks space but no room",
        "interstellar movie plot space black holes",
        "python loops machine learning algorithms core coding definition",
        "curse of dimensionality", "event horizon", "cap theorem distributed systems", "turing test", "schrodingers cat paradox"
    ],
    "responses": [
        "I am Quantum Core, an automated conversational subroutine engineered for instant vector mapping calculations.",
        "I am Quantum Core, a hybrid NLP navigation assistant specialized in handling localized context datasets.",
        "I ingest raw text sequences, apply high-dimensional TF-IDF vectorization, and determine analytical match coefficients using Cosine Proximity formulas.",
        "This system architecture is engineered using Python 3.11, Streamlit UI Framework, and Scikit-Learn Matrix Tokenizer pipelines.",
        "TF-IDF (Term Frequency-Inverse Document Frequency) is a mathematical algorithm that transforms raw text tokens into a numerical matrix based on word importance.",
        "To deploy a Streamlit workspace, push source files to a public GitHub repository, initialize a requirements.txt file, and link the branch tree to Streamlit Community Cloud.",
        "It is a mathematical metric computing the angle cosine between two non-zero vectors inside an inner mathematical vector space to evaluate string proximity rules.",
        "This project cluster is built as a production-grade prototype for the Artificial Intelligence & Python Development Framework domain.",
        
        # SQL vs NoSQL Specific Output
        "📌 **SQL vs NoSQL Database Matrix Framework:**<br><br>"
        "⚖️ **Schema Flexibility:**<br>"
        "* **SQL:** Uses strict, predefined relational schemas (tables/rows). Altering schemas requires heavy database migrations.<br>"
        "* **NoSQL:** Uses dynamic, unstructured schemas (JSON documents, key-value, graphs). Allows unstructured schema flexibility on the fly.<br><br>"
        "📈 **Scaling Dynamics:**<br>"
        "* **SQL:** Scales **Vertically** (requires upgrading CPU, RAM, or SSD capabilities of a single hardware server unit).<br>"
        "* **NoSQL:** Scales **Horizontally** (distributes data data load across thousands of decentralized commodity server clusters automatically).",
        
        "📌 **SQL vs NoSQL Database Matrix Framework:**<br><br>"
        "⚖️ **Schema Flexibility:**<br>"
        "* **SQL:** Strict relational schemas.<br>"
        "* **NoSQL:** Dynamic unstructured document models.<br><br>"
        "📈 **Scaling Dynamics:**<br>"
        "* **SQL:** Vertical scaling (Hardware upgrade).<br>"
        "* **NoSQL:** Horizontal scaling (Data splitting across nodes).",

        "🏆 **ICC T20 World Cup Matrix:** India captured the definitive T20 World Cup crown in a historic execution run, defeating South Africa in an intense final over finish.",
        
        "🌐 **REST API Execution Node:** REST (Representational State Transfer) is a stateless architectural protocol. It utilizes primary HTTP verbs to execute structural CRUD mechanics:<br>"
        "* **GET:** Retrieve specific target resource data.<br>"
        "* **POST:** Construct/Create new payload entries.<br>"
        "* **PUT:** Completely update existing data objects.<br>"
        "* **DELETE:** Erase target server array properties.",
        
        "🌀 **Inception Ending Matrix Decoded:** The spinning top keeps spinning in the final sequence, blurring the lines between reality and dream layers. Cobb doesn't wait to see it drop because his children are his absolute reality now—signifying emotional closure over objective status.",
        
        "🧩 **Logical Extraction Core:** The computational riddle solution is: **A Keyboard**. (Contains letter keys, spacebar, and the Enter sequence).",
        
        "🚀 **Interstellar Space Log:** Directed by Christopher Nolan, it tracks an astronaut team navigating a wormhole near Saturn to discover habitable worlds, utilizing real General Relativity equations, time dilation, and black hole dynamics (Gargantua).",
        
        "💻 **Core Engineering Scripts:** Python loops automate iterative traversal blocks. Machine Learning algorithms (like Linear Regression, DBSCAN, or Decision Trees) map high-dimensional statistical variations inside sample packets to make automated classifications.",

        "📊 **Curse of Dimensionality:** As data features (dimensions) increase inside machine learning spaces, the volume grows exponentially. This causes available training vectors to become extremely sparse, making distance-based cluster grouping (like KNN or DBSCAN) mathematically inefficient without dimensionality reduction.",
        
        "🌌 **Event Horizon Matrix:** The absolute geometric boundary surrounding a gravitational singularity (Black Hole) where the escape velocity strictly exceeds the speed of light. Zero data packets or electromagnetic sequences can escape once crossed.",
        
        "💻 **CAP Theorem Node:** Inside distributed data environments, a decentralized system can only simultaneously guarantee **two out of three** absolute properties: Consistency (identical data across nodes), Availability (every request receives a non-error response), and Partition Tolerance (system continues despite message drops).",
        
        "🧠 **Turing Test Architecture:** A cognitive benchmark proposed by Alan Turing. If a human evaluator cannot consistently distinguish machine textual outputs from a real human subject during blind natural conversations, the AI system passes the operational intelligence threshold.",
        
        "🧪 **Schrodinger's Cat Paradox:** A quantum mechanics thought experiment illustrating superposition. A cat inside a sealed box with a radioactive trigger exists in a simultaneous wave state of being **both alive and dead** until an outside measurement forces a quantum collapse."
    ]
}

EMOTION_KEYWORDS = ["sad", "low", "depressed", "stress", "upset", "lonely", "happy", "excited", "bored", "tension", "mood"]
EMOTION_RESPONSES = [
    "Bhai, tension mat le, plot twists hi toh kahani mazedaar banate hain. Ek gehri saans le, scene sahi ho jayega. Main yahi hoon.",
    "Listen to me, low phases are just temporary glitches in the matrix. Chal thoda chill kar, step back le aur restart maar. You got this, flex up!"
]

# INPUT COMPONENT
user_query = st.text_input("SHARE WHAT'S ON YOUR MIND OR ASK ANY QUESTION", placeholder="Type here...")

if user_query:
    query_lower = user_query.lower().strip()
    bot_response = None
    response_type = ""
    
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)
    st.markdown(f'<div class="user-bubble"><b>🧑‍💻 User Input Matrix:</b><br>{user_query}</div>', unsafe_allow_html=True)
    
    # ─── LAYER 1: COMPANION ENGINE ───
    if any(word in query_lower for word in EMOTION_KEYWORDS):
        bot_response = random.choice(EMOTION_RESPONSES)
        response_type = "💚 Companion Core"

    # ─── LAYER 2: LOCAL HIGH-DIMENSIONAL CLASSIFIER ───
    if not bot_response:
        compiled_queries = UNIVERSAL_DATA["queries"] + [user_query]
        vectorizer = TfidfVectorizer(stop_words='english')
        tfidf_matrix = vectorizer.fit_transform(compiled_queries)
        
        # Calculate cosine proximity array between input and data matrix
        similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]
        best_match_idx = similarity_scores.argmax()
        highest_score = similarity_scores[best_match_idx]
        
        # Lowered threshold to ensure local matching catches semantic variations easily
        if highest_score > 0.18:
            bot_response = UNIVERSAL_DATA["responses"][best_match_idx]
            response_type = "🏛️ Offline Knowledge Matrix"

    # ─── LAYER 3: CRITICAL SAFE FALLBACK ───
    if not bot_response:
        bot_response = "Bhai, keyword parameters out-of-bounds chal rahe hain. Try asking about SQL vs NoSQL, Turing Test, Inception, or REST API models."
        response_type = "⚠️ System Safe Fallback"

    # OUTPUT PRESENTATION LAYER
    st.markdown(f'<div class="bot-bubble"><b>🤖 Matrix Engine ({response_type}):</b><br>{bot_response}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)