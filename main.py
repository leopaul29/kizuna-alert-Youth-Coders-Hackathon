"""
Kizuna Alert - Community Mutual Aid Application
Youth Coders Collective Hackathon 2025

A disaster alert and community support application for Japanese neighborhoods.
Focuses on mutual aid and community resilience during emergencies.
"""

from flask import Flask, render_template, request, redirect, url_for, session
import os
from datetime import datetime

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'dev-secret-key-change-in-production')

# Simulated disaster alerts (in a real app, this would come from an API)
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


@app.route('/')
def index():
    """Homepage with disaster alert and postal code form"""
    return render_template('index.html', alerts=DISASTER_ALERTS)


@app.route('/join', methods=['POST'])
def join_neighborhood():
    """Handle postal code submission and redirect to chat"""
    postal_code = request.form.get('postal_code', '').strip()
    
    # Validate postal code format (simple validation)
    if postal_code in NEIGHBORHOOD_GROUPS:
        session['postal_code'] = postal_code
        session['neighborhood'] = NEIGHBORHOOD_GROUPS[postal_code]
        return redirect(url_for('chat'))
    else:
        # For demo purposes, accept any postal code and use a default group
        session['postal_code'] = postal_code
        session['neighborhood'] = f'Community {postal_code}'
        return redirect(url_for('chat'))


@app.route('/chat')
def chat():
    """Community chat page"""
    if 'postal_code' not in session:
        return redirect(url_for('index'))
    
    postal_code = session.get('postal_code', '')
    neighborhood = session.get('neighborhood', '')
    
    # Get base messages for this neighborhood
    messages = CHAT_MESSAGES.get(postal_code, [
        {'user': 'System', 'message': 'Welcome to your community mutual aid group!', 'time': datetime.now().strftime('%H:%M'), 'type': 'info'}
    ]).copy()
    
    # Add user's check-in message if they have checked in
    if session.get('checked_in'):
        user_name = session.get('user_name', 'You')
        checkin_time = session.get('checkin_time', datetime.now().strftime('%H:%M'))
        messages.append({
            'user': user_name,
            'message': "I'm safe ✓",
            'time': checkin_time,
            'type': 'checkin'
        })
    
    return render_template('chat.html', 
                         neighborhood=neighborhood, 
                         postal_code=postal_code,
                         messages=messages,
                         alerts=DISASTER_ALERTS,
                         checked_in=session.get('checked_in', False))


@app.route('/checkin', methods=['POST'])
def checkin():
    """Handle safety check-in"""
    if 'postal_code' not in session:
        return redirect(url_for('index'))
    
    # Store check-in status in session
    session['checked_in'] = True
    session['checkin_time'] = datetime.now().strftime('%H:%M')
    
    # Set a default user name if not already set
    if 'user_name' not in session:
        session['user_name'] = 'You'
    
    return redirect(url_for('chat'))


@app.route('/leave')
def leave():
    """Leave the neighborhood group"""
    session.clear()
    return redirect(url_for('index'))


@app.route('/evacuation')
def evacuation():
    """Evacuation centers and route map"""
    # Get postal code from session if available
    postal_code = session.get('postal_code', '')
    
    return render_template('evacuation.html', 
                         alerts=DISASTER_ALERTS,
                         postal_code=postal_code)


# if __name__ == '__main__':
#     # Run on 0.0.0.0:5000 for Replit compatibility
#     app.run(host='0.0.0.0', port=5000, debug=True)
