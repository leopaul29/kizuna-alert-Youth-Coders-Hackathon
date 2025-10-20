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
        'type': 'Séisme',
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
        {'user': 'Yuki S.', 'message': "J'ai de l'eau à partager - coins des rues Marunouchi", 'time': '14:42', 'type': 'resource'},
        {'user': 'Kenji T.', 'message': 'Besoin d\'aide pour évacuation - personne âgée au 3ème étage', 'time': '14:45', 'type': 'help'},
        {'user': 'Aiko M.', 'message': 'Je vais bien ✓', 'time': '14:47', 'type': 'checkin'},
        {'user': 'Hiroshi N.', 'message': 'Centre d\'évacuation ouvert à l\'école primaire Chiyoda', 'time': '14:50', 'type': 'info'}
    ],
    '150-0001': [
        {'user': 'Sakura I.', 'message': 'Lampes de poche disponibles au konbini familial', 'time': '14:40', 'type': 'resource'},
        {'user': 'Takeshi Y.', 'message': 'Je vais bien ✓', 'time': '14:44', 'type': 'checkin'},
        {'user': 'Mei L.', 'message': 'Quelqu\'un a des nouvelles de la ligne Yamanote?', 'time': '14:48', 'type': 'help'}
    ],
    '160-0001': [
        {'user': 'Ryu K.', 'message': 'Je vais bien ✓', 'time': '14:43', 'type': 'checkin'},
        {'user': 'Nanami H.', 'message': 'Couvertures disponibles - contactez-moi', 'time': '14:46', 'type': 'resource'}
    ],
    '106-0001': [
        {'user': 'Daiki W.', 'message': 'Centre médical Minato ouvert pour urgences', 'time': '14:41', 'type': 'info'},
        {'user': 'Emiko F.', 'message': 'Je vais bien ✓', 'time': '14:49', 'type': 'checkin'}
    ],
    '110-0001': [
        {'user': 'Kazuo S.', 'message': 'Nourriture d\'urgence disponible au temple', 'time': '14:44', 'type': 'resource'},
        {'user': 'Yui A.', 'message': 'Je vais bien ✓', 'time': '14:51', 'type': 'checkin'}
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
        session['neighborhood'] = f'Communauté {postal_code}'
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
        {'user': 'Système', 'message': 'Bienvenue dans votre groupe d\'entraide communautaire!', 'time': datetime.now().strftime('%H:%M'), 'type': 'info'}
    ]).copy()
    
    # Add user's check-in message if they have checked in
    if session.get('checked_in'):
        user_name = session.get('user_name', 'Vous')
        checkin_time = session.get('checkin_time', datetime.now().strftime('%H:%M'))
        messages.append({
            'user': user_name,
            'message': 'Je vais bien ✓',
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
        session['user_name'] = 'Vous'
    
    return redirect(url_for('chat'))


@app.route('/leave')
def leave():
    """Leave the neighborhood group"""
    session.clear()
    return redirect(url_for('index'))


if __name__ == '__main__':
    # Run on 0.0.0.0:5000 for Replit compatibility
    app.run(host='0.0.0.0', port=5000, debug=True)
