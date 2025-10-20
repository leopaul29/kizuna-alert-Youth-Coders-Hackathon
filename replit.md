# Kizuna Alert - Project Documentation

## Overview
A Flask-based disaster alert and community mutual aid web application for the Youth Coders Collective Hackathon 2025. Focuses on helping Japanese neighborhoods communicate and share resources during natural disasters.

## Recent Changes (October 20, 2025)
- Initial project setup with Flask backend
- Implemented wabi-sabi inspired minimalist design
- Created homepage with disaster alert simulation
- Built community chat functionality with simulated messages
- Added check-in feature for safety status updates
- Comprehensive README for hackathon submission

## Project Architecture

### Stack
- **Backend**: Flask (Python 3.11)
- **Frontend**: HTML5, CSS3, minimal JavaScript
- **Session Management**: Flask sessions (SESSION_SECRET)
- **Data Storage**: Simulated data using Python dictionaries (for MVP demo)

### File Structure
```
kizuna-alert/
├── main.py              # Flask backend with all routes
├── templates/
│   ├── index.html       # Homepage with alerts and postal code form
│   └── chat.html        # Community chat page
├── static/
│   └── style.css        # Wabi-sabi inspired design
├── README.md            # Hackathon documentation
└── .gitignore          # Python gitignore
```

### Key Routes
- `GET /` - Homepage with disaster alerts and postal code form
- `POST /join` - Submit postal code to join neighborhood group
- `GET /chat` - Community chat page (requires session)
- `POST /checkin` - Safety check-in button
- `GET /leave` - Leave neighborhood group (clears session)

### Design Philosophy
**Wabi-sabi** aesthetics:
- Minimalist and functional
- Color palette: Blues (#667eea, #764ba2), whites, greys
- Clean typography (Roboto)
- Focus on clarity and calm during emergencies

### Simulated Data
- **Alerts**: Earthquake simulation (magnitude 5.0 in Tokyo)
- **Postal Codes**: 5 Tokyo neighborhoods (Chiyoda, Shibuya, Shinjuku, Minato, Taito)
- **Chat Messages**: Pre-written resource sharing, help requests, check-ins, and info

## Development Notes

### Running the Application
```bash
python main.py
```
Server runs on `0.0.0.0:5000` (Replit compatible)

### Session Management
Uses Flask sessions to track:
- `postal_code`: User's neighborhood postal code
- `neighborhood`: Neighborhood display name

### Next Phase Features
1. Real-time chat (Firebase/WebSockets)
2. User authentication
3. Real API integration (JMA weather alerts)
4. Mobile app version
5. Multilingual support (Japanese/English)

## Hackathon Alignment

### Theme: Social Good + Japan
- **Impact**: Community mutual aid during disasters
- **Function**: Alert system + neighborhood chat
- **Design**: Japanese wabi-sabi aesthetics
- **Presentation**: Well-documented, beginner-friendly code

### Judging Criteria Addressed
✅ **Impact** - Strengthens community resilience  
✅ **Function** - Fully working demo with simulated data  
✅ **Design** - Clean, minimalist, intuitive interface  
✅ **Presentation** - Complete README and code comments  

## User Preferences
- **English language interface** (translated from French for better accessibility)
- Beginner-friendly code structure
- Focus on demo-ready functionality
- Clean, well-commented code
- Maintain Japanese cultural elements (絆 kanji, neighborhood names)
