# Kizuna Alert - Project Documentation

## Overview
A Flask-based disaster alert and community mutual aid web application for the Youth Coders Collective Hackathon 2025. Focuses on helping Japanese neighborhoods communicate and share resources during natural disasters.

## Recent Changes (October 20, 2025)
- Enhanced CSS with wabi-sabi colors (navy blue #1a2332, off-white #f8f9fa, soft gray #94a3b8)
- Added subtle button animations (hover effects, transforms, box-shadows)
- Generated Google Maps-style evacuation route map for Chiyoda Gym, Tokyo
- Created evacuation centers page with route map, facility info, and safety instructions
- Updated README with comprehensive Design Choices and Accessibility sections
- Integrated evacuation page link in community chat for easy access
- Added responsive design with mobile breakpoints (768px)
- Implemented color-coded message types in chat (green=resource, orange=help, blue=info)

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
│   ├── chat.html        # Community chat page
│   └── evacuation.html  # Evacuation centers with route map
├── static/
│   ├── style.css        # Enhanced wabi-sabi design with animations
│   └── images/
│       └── evacuation_map.png  # Google Maps-style route to Chiyoda Gym
├── README.md            # Comprehensive hackathon documentation
└── .gitignore          # Python gitignore
```

### Key Routes
- `GET /` - Homepage with disaster alerts and postal code form
- `POST /join` - Submit postal code to join neighborhood group
- `GET /chat` - Community chat page (requires session)
- `POST /checkin` - Safety check-in button
- `GET /evacuation` - Evacuation centers page with route map
- `GET /leave` - Leave neighborhood group (clears session)

### Design Philosophy
**Enhanced Wabi-sabi** aesthetics:
- Minimalist and functional with subtle animations
- Color palette: Navy blue (#1a2332), off-white (#f8f9fa), soft gray (#94a3b8)
- Accent colors: Red (#dc2626) for alerts, green (#16a34a) for safety, blue (#2563eb) for info
- Clean typography (Roboto with Noto Sans JP fallback)
- Subtle button hover effects with transform and box-shadow
- Focus on clarity and calm during emergencies
- WCAG 2.1 Level AA accessibility compliance

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
