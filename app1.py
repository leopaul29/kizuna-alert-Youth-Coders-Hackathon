"""
Kizuna Alert - Community Mutual Aid Application
Youth Coders Collective Hackathon 2025

A disaster alert and community support application for Japanese neighborhoods.
Focuses on mutual aid and community resilience during emergencies.
"""

import streamlit as st
from datetime import datetime

# Simulated disaster alerts
DISASTER_ALERTS = [
    {
        'type': 'Earthquake',
        'magnitude': '5.0',
        'location': 'Tokyo',
        'time': '14:35 JST',
        'status': 'active'
    }
]

# Simulated neighborhood groups by postal code
NEIGHBORHOOD_GROUPS = {
    '100-0001': 'Chiyoda Ward Community',
    '150-0001': 'Shibuya Ward Community',
    '160-0001': 'Shinjuku Ward Community',
    '106-0001': 'Minato Ward Community',
    '110-0001': 'Taito Ward Community'
}

# Simulated chat messages for each neighborhood
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

# Streamlit page configuration
st.set_page_config(page_title="Kizuna Alert", layout="wide")

# Initialize session state
if 'postal_code' not in st.session_state:
    st.session_state.postal_code = ''
if 'neighborhood' not in st.session_state:
    st.session_state.neighborhood = ''
if 'checked_in' not in st.session_state:
    st.session_state.checked_in = False
if 'user_name' not in st.session_state:
    st.session_state.user_name = 'You'
if 'checkin_time' not in st.session_state:
    st.session_state.checkin_time = ''

# Sidebar navigation
page = st.sidebar.selectbox("Navigate", ["Home", "Community Chat", "Evacuation Centers"])

if page == "Home":
    st.title("Kizuna Alert")
    st.subheader("Community Mutual Aid for Disaster Resilience")

    # Display disaster alerts
    for alert in DISASTER_ALERTS:
        st.warning(f"{alert['type']} Alert - Magnitude: {alert['magnitude']}, Location: {alert['location']}, Time: {alert['time']}")

    # Postal code input
    with st.form("postal_form"):
        postal_code = st.text_input("Enter your postal code (e.g., 100-0001)")
        submitted = st.form_submit_button("Join Community")
        if submitted and postal_code:
            postal_code = postal_code.strip()
            st.session_state.postal_code = postal_code
            st.session_state.neighborhood = NEIGHBORHOOD_GROUPS.get(postal_code, f'Community {postal_code}')
            st.rerun()

elif page == "Community Chat":
    if not st.session_state.postal_code:
        st.error("Please enter a postal code on the Home page.")
        st.stop()

    st.title(f"{st.session_state.neighborhood} Chat")
    st.subheader(f"Postal Code: {st.session_state.postal_code}")

    # Display disaster alerts
    for alert in DISASTER_ALERTS:
        st.warning(f"{alert['type']} Alert - Magnitude: {alert['magnitude']}, Location: {alert['location']}, Time: {alert['time']}")

    # Check-in button
    if not st.session_state.checked_in:
        if st.button("Check In (I'm Safe)"):
            st.session_state.checked_in = True
            st.session_state.checkin_time = datetime.now().strftime('%H:%M')
            st.rerun()

    # Display messages
    messages = CHAT_MESSAGES.get(st.session_state.postal_code, [
        {'user': 'System', 'message': 'Welcome to your community mutual aid group!', 'time': datetime.now().strftime('%H:%M'), 'type': 'info'}
    ]).copy()

    if st.session_state.checked_in:
        messages.append({
            'user': st.session_state.user_name,
            'message': "I'm safe ✓",
            'time': st.session_state.checkin_time,
            'type': 'checkin'
        })

    for msg in messages:
        st.write(f"[{msg['time']}] {msg['user']} ({msg['type']}): {msg['message']}")

    # Leave community button
    if st.button("Leave Community"):
        st.session_state.clear()
        st.rerun()

elif page == "Evacuation Centers":
    st.title("Evacuation Centers and Routes")
    st.subheader(f"Postal Code: {st.session_state.postal_code or 'Not set'}")

    # Display disaster alerts
    for alert in DISASTER_ALERTS:
        st.warning(f"{alert['type']} Alert - Magnitude: {alert['magnitude']}, Location: {alert['location']}, Time: {alert['time']}")

    # Render evacuation.html
    try:
        with open("templates/evacuation.html", "r") as f:
            st.components.v1.html(f.read(), height=600)
    except FileNotFoundError:
        st.error("Evacuation page content not found.")