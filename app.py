"""
Kizuna Alert - Community Mutual Aid Application
Youth Coders Collective Hackathon 2025

A disaster alert and community support application for Japanese neighborhoods.
Focuses on mutual aid and community resilience during emergencies.
"""

import streamlit as st
from datetime import datetime

# Configuration de la page
st.set_page_config(
    page_title="Kizuna Alert - Community Alert System",
    page_icon="🔗",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé avec fond clair
st.markdown("""
<style>
    /* Force light mode */
    .stApp {
        background-color: #f5f7fa;
    }
    
    /* Headers */
    h1, h2, h3, h4, h5, h6 {
        color: #2c3e50 !important;
    }
    
    /* Paragraphs */
    p, li, span, div {
        color: #2c3e50 !important;
    }
    
    .main-header {
        text-align: center;
        padding: 30px;
        background: linear-gradient(135deg, #2c3e50 0%, #3498db 100%);
        color: white !important;
        border-radius: 15px;
        margin-bottom: 30px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }
    
    .main-header h1, .main-header p {
        color: white !important;
    }
    
    .alert-box {
        background-color: #fee;
        border-left: 5px solid #e74c3c;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #721c24 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .alert-box strong, .alert-box span {
        color: #721c24 !important;
    }
    
    .info-box {
        background-color: #e3f2fd;
        border-left: 5px solid #2196f3;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #0d47a1 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .info-box h3, .info-box p {
        color: #0d47a1 !important;
    }
    
    .success-box {
        background-color: #d4edda;
        border-left: 5px solid #28a745;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #155724 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .success-box strong {
        color: #155724 !important;
    }
    
    .warning-box {
        background-color: #fff3cd;
        border-left: 5px solid #ffc107;
        padding: 20px;
        border-radius: 8px;
        margin-bottom: 20px;
        color: #856404 !important;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    .warning-box strong {
        color: #856404 !important;
    }
    
    .message-box {
        padding: 15px;
        margin: 10px 0;
        border-radius: 10px;
        border-left: 4px solid;
        background-color: white;
        box-shadow: 0 2px 4px rgba(0,0,0,0.05);
    }
    
    .message-box strong, .message-box span {
        color: #2c3e50 !important;
    }
    
    .message-resource {
        border-color: #4caf50;
        background-color: #f1f8f4;
    }
    
    .message-help {
        border-color: #ff9800;
        background-color: #fff8f0;
    }
    
    .message-checkin {
        border-color: #2196f3;
        background-color: #f0f7ff;
    }
    
    .message-info {
        border-color: #9c27b0;
        background-color: #f8f4f9;
    }
    
    .stButton>button {
        background-color: #3498db;
        color: white;
        border: none;
        padding: 10px 20px;
        border-radius: 5px;
        font-weight: 500;
    }
    
    .stButton>button:hover {
        background-color: #2980b9;
    }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #2c3e50;
    }
    
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Input fields */
    .stTextInput input {
        background-color: white !important;
        color: #2c3e50 !important;
    }
    
    /* Emergency badge */
    .emergency-badge {
        background: #e74c3c;
        color: white !important;
        padding: 5px 12px;
        border-radius: 5px;
        margin-left: 10px;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Données simulées
DISASTER_ALERTS = [
    {
        'type': 'Earthquake',
        'magnitude': '5.0',
        'location': 'Tokyo',
        'time': '14:35 JST',
        'status': 'active'
    }
]

NEIGHBORHOOD_GROUPS = {
    '100-0001': 'Chiyoda Ward Community',
    '150-0001': 'Shibuya Ward Community',
    '160-0001': 'Shinjuku Ward Community',
    '106-0001': 'Minato Ward Community',
    '110-0001': 'Taito Ward Community'
}

CHAT_MESSAGES = {
    '100-0001': [
        {'user': 'Yuki S.', 'message': "I have water to share - corner of Marunouchi Street", 'time': '14:42', 'type': 'resource'},
        {'user': 'Kenji T.', 'message': 'Need help with evacuation - elderly person on 3rd floor', 'time': '14:45', 'type': 'help'},
        {'user': 'Aiko M.', 'message': "I'm safe ✓", 'time': '14:47', 'type': 'checkin'},
        {'user': 'Hiroshi N.', 'message': 'Evacuation center open at Chiyoda Elementary School', 'time': '14:50', 'type': 'info'}
    ],
    '150-0001': [
        {'user': 'Sakura I.', 'message': 'Flashlights available at Family Mart convenience store', 'time': '14:40', 'type': 'resource'},
        {'user': 'Takeshi Y.', 'message': "I'm safe ✓", 'time': '14:44', 'type': 'checkin'},
        {'user': 'Mei L.', 'message': 'Does anyone have news about the Yamanote Line?', 'time': '14:48', 'type': 'help'}
    ],
    '160-0001': [
        {'user': 'Ryu K.', 'message': "I'm safe ✓", 'time': '14:43', 'type': 'checkin'},
        {'user': 'Nanami H.', 'message': 'Blankets available - contact me', 'time': '14:46', 'type': 'resource'}
    ],
    '106-0001': [
        {'user': 'Daiki W.', 'message': 'Minato Medical Center open for emergencies', 'time': '14:41', 'type': 'info'},
        {'user': 'Emiko F.', 'message': "I'm safe ✓", 'time': '14:49', 'type': 'checkin'}
    ],
    '110-0001': [
        {'user': 'Kazuo S.', 'message': 'Emergency food available at the temple', 'time': '14:44', 'type': 'resource'},
        {'user': 'Yui A.', 'message': "I'm safe ✓", 'time': '14:51', 'type': 'checkin'}
    ]
}

# Initialisation des variables de session
if 'page' not in st.session_state:
    st.session_state.page = 'home'
if 'postal_code' not in st.session_state:
    st.session_state.postal_code = None
if 'neighborhood' not in st.session_state:
    st.session_state.neighborhood = None
if 'checked_in' not in st.session_state:
    st.session_state.checked_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = 'You'
if 'checkin_time' not in st.session_state:
    st.session_state.checkin_time = None

# Fonctions de navigation
def go_to_home():
    st.session_state.page = 'home'
    st.session_state.postal_code = None
    st.session_state.neighborhood = None
    st.session_state.checked_in = False

def go_to_chat():
    st.session_state.page = 'chat'

def go_to_evacuation():
    st.session_state.page = 'evacuation'

def do_checkin():
    st.session_state.checked_in = True
    st.session_state.checkin_time = datetime.now().strftime('%H:%M')

# Sidebar
with st.sidebar:
    st.markdown("### 🔗 Kizuna Alert")
    st.markdown("---")
    
    if st.session_state.postal_code:
        st.write(f"**Neighborhood:**")
        st.write(f"{st.session_state.neighborhood}")
        st.write(f"**Postal Code:** {st.session_state.postal_code}")
        st.markdown("---")
        
        if st.button("🏠 Home", use_container_width=True):
            go_to_home()
            st.rerun()
        if st.button("💬 Community Chat", use_container_width=True):
            go_to_chat()
            st.rerun()
        if st.button("📍 Evacuation Centers", use_container_width=True):
            go_to_evacuation()
            st.rerun()
        
        st.markdown("---")
        if st.button("🚪 Leave Group", use_container_width=True):
            go_to_home()
            st.rerun()
    
    st.markdown("---")
    st.write("**Youth Coders Collective**")
    st.write("Hackathon 2025")
    st.write("Built with ❤️ for community resilience")

# Page d'accueil
if st.session_state.page == 'home':
    st.markdown('''
    <div class="main-header">
        <h1>🔗 Kizuna Alert</h1>
        <p style="font-size: 1.2em; margin-top: 10px;">Together for Community Resilience</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Alertes actives
    st.markdown("## 🚨 Active Alerts")
    if DISASTER_ALERTS:
        for alert in DISASTER_ALERTS:
            st.markdown(f'''
            <div class="alert-box">
                <strong style="font-size: 1.1em;">{alert['type']}</strong> magnitude <strong>{alert['magnitude']}</strong> 
                detected in <strong>{alert['location']}</strong>
                <span class="emergency-badge">{alert['time']}</span>
                <br><br>
                <span style="font-size: 1.05em;">⚠️ Stay calm and follow safety procedures</span>
            </div>
            ''', unsafe_allow_html=True)
    else:
        st.info("No active alerts at this time.")
    
    # Info box
    st.markdown('''
    <div class="info-box">
        <h3>About Kizuna Alert</h3>
        <p style="line-height: 1.6;">
            Kizuna (絆) means "bond" or "connection" in Japanese. This application connects members of the same 
            neighborhood to share resources and support each other during natural disasters.
        </p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Formulaire
    st.markdown("## Join Your Mutual Aid Group")
    st.write("Enter your Japanese postal code to join your neighborhood's mutual aid group and access the community chat.")
    
    col1, col2 = st.columns([2, 1])
    with col1:
        postal_code = st.text_input(
            "Japanese Postal Code",
            placeholder="Ex: 100-0001 (Chiyoda, Tokyo)",
            help="Examples: 100-0001 (Chiyoda), 150-0001 (Shibuya), 160-0001 (Shinjuku)"
        )
        
        if st.button("Join My Neighborhood", type="primary", use_container_width=True):
            if postal_code:
                st.session_state.postal_code = postal_code
                if postal_code in NEIGHBORHOOD_GROUPS:
                    st.session_state.neighborhood = NEIGHBORHOOD_GROUPS[postal_code]
                else:
                    st.session_state.neighborhood = f'Community {postal_code}'
                go_to_chat()
                st.rerun()
            else:
                st.error("Please enter a postal code")
    
    # Comment ça marche
    st.markdown("## How It Works")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        **1. Join** - Enter your postal code to join your neighborhood group
        
        **2. Communicate** - Share resources and ask for help in the chat
        """)
    with col2:
        st.markdown("""
        **3. Check-in** - Signal that you're safe to reassure your neighbors
        
        **4. Support** - Help your community during emergencies
        """)

# Page de chat
elif st.session_state.page == 'chat':
    st.markdown('''
    <div class="main-header">
        <h1>🔗 Kizuna Alert</h1>
        <p style="font-size: 1.2em; margin-top: 10px;">Community Chat</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Alerte active
    if DISASTER_ALERTS:
        for alert in DISASTER_ALERTS:
            st.markdown(f'''
            <div class="alert-box">
                <strong>⚠️ Active Alert:</strong> {alert['type']} {alert['magnitude']} in {alert['location']} ({alert['time']})
            </div>
            ''', unsafe_allow_html=True)
    
    # En-tête du chat
    st.markdown(f"## {st.session_state.neighborhood}")
    st.markdown(f"**Postal Code:** {st.session_state.postal_code}")
    
    st.markdown("---")
    
    # Actions rapides
    st.markdown("### Quick Actions")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.session_state.checked_in:
            st.button("✓ Checked In", disabled=True, use_container_width=True)
        else:
            if st.button("✓ I'm Safe (Check-in)", type="primary", use_container_width=True):
                do_checkin()
                st.rerun()
    
    with col2:
        if st.button("📍 View Evacuation Centers", use_container_width=True):
            go_to_evacuation()
            st.rerun()
    
    with col3:
        if st.button("🚪 Leave Group", use_container_width=True):
            go_to_home()
            st.rerun()
    
    if st.session_state.checked_in:
        st.markdown('''
        <div class="success-box">
            <strong>✓ Check-in recorded!</strong> Your safety status has been shared with your community.
        </div>
        ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Messages de la communauté
    st.markdown("### Community Messages")
    
    messages = CHAT_MESSAGES.get(st.session_state.postal_code, []).copy()
    
    if st.session_state.checked_in:
        messages.append({
            'user': st.session_state.user_name,
            'message': "I'm safe ✓",
            'time': st.session_state.checkin_time,
            'type': 'checkin'
        })
    
    for msg in messages:
        st.markdown(f'''
        <div class="message-box message-{msg['type']}">
            <strong>{msg['user']}</strong> <span style="float: right; color: #666; font-size: 0.9em;">{msg['time']}</span>
            <br><br>
            {msg['message']}
        </div>
        ''', unsafe_allow_html=True)
    
    if not messages:
        st.info("No messages yet. Be the first to share helpful information!")
    
    # Note
    st.markdown('''
    <div class="warning-box">
        <strong>Note:</strong> In the final version, you'll be able to send your own messages. 
        For this demo, messages are simulated to showcase the functionality.
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    # Conseils de sécurité
    st.markdown("### Safety Tips 安全")
    st.markdown("""
    - Stay calm and follow instructions from authorities
    - Check alerts and community messages regularly
    - Share your resources with those in need
    - Use check-in to reassure your neighbors
    - Keep your phone charged and have a flashlight nearby
    """)

# Page d'évacuation
elif st.session_state.page == 'evacuation':
    st.markdown('''
    <div class="main-header">
        <h1>🔗 Kizuna Alert</h1>
        <p style="font-size: 1.2em; margin-top: 10px;">Evacuation Centers</p>
    </div>
    ''', unsafe_allow_html=True)
    
    # Alerte active
    if DISASTER_ALERTS:
        for alert in DISASTER_ALERTS:
            st.markdown(f'''
            <div class="alert-box">
                <strong>⚠️ Active Alert:</strong> {alert['type']} {alert['magnitude']} in {alert['location']} ({alert['time']})
            </div>
            ''', unsafe_allow_html=True)
    
    st.markdown("## 📍 Nearest Evacuation Center")
    st.markdown("### Route to Chiyoda Gym Evacuation Center")
    
    # Information sur le centre
    st.markdown('''
    <div class="info-box">
        <h3>🏢 Chiyoda Gym (千代田体育館)</h3>
        <p><strong>Address:</strong> 1-1 Uchikanda, Chiyoda-ku, Tokyo 101-0047</p>
        <p><strong>Distance:</strong> 1.2 km (approximately 15 minutes walk)</p>
        <p><strong>Capacity:</strong> 500 people</p>
        <p><strong>Facilities:</strong> First aid station, water supply, emergency blankets, 
        wheelchair accessible, multilingual staff</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.info("📌 Map would be displayed here showing the evacuation route from your location to Chiyoda Gym")
    
    st.markdown("---")
    
    # Instructions d'évacuation
    st.markdown("## 🚶 Evacuation Instructions")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("""
        1. **Stay calm** - Take a moment to assess your situation
        2. **Grab essentials** - Water, medications, phone, flashlight, and important documents
        3. **Follow the route** - Use the map above for the safest walking path
        """)
    with col2:
        st.markdown("""
        4. **Help others** - Assist elderly neighbors or those with mobility challenges
        5. **Check in** - Once you arrive safely, use the check-in feature to notify your community
        6. **Follow instructions** - Listen to evacuation center staff for further guidance
        """)
    
    st.markdown("---")
    
    # Centres alternatifs
    st.markdown("### 📋 Alternative Evacuation Centers")
    st.markdown("""
    - **Chiyoda Elementary School** - 0.8 km east, 300 capacity
    - **Kanda Community Center** - 1.5 km north, 400 capacity
    - **Hibiya Park Shelter** - 2.0 km south, 600 capacity
    
    *Choose the nearest available center. Check with local authorities for real-time capacity updates.*
    """)
    
    st.markdown("---")
    
    # Contacts d'urgence
    st.markdown('''
    <div class="alert-box">
        <h3>🚨 Emergency Contacts</h3>
        <p><strong>Emergency Services:</strong> 119 (Fire/Ambulance), 110 (Police)</p>
        <p><strong>Tokyo Disaster Hotline:</strong> 03-5320-7777</p>
        <p><strong>English Support:</strong> 03-5285-8181</p>
    </div>
    ''', unsafe_allow_html=True)
    
    st.markdown("---")
    
    if st.button("← Back to Community Chat", use_container_width=True):
        go_to_chat()
        st.rerun()