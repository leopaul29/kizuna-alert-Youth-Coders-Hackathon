# 絆 Kizuna Alert

**Youth Coders Collective Hackathon 2025**

A community resilience web application for mutual aid during natural disasters in Japan.

## 🎯 Project Objective

Kizuna (絆) means "bond" or "connection" in Japanese. This application connects residents of the same Japanese neighborhood to:
- Receive real-time disaster alerts
- Share resources (water, food, shelter)
- Request help during emergencies
- Signal their safety to neighbors (check-in)
- Strengthen community solidarity

## 🌐 Language & Accessibility

**The entire application interface is now available in English** for broader accessibility and international reach. While maintaining Japanese cultural elements (such as the 絆 kanji and Japanese neighborhood names), all user-facing text, alerts, and messages are presented in clear, professional English to ensure:
- Global accessibility for international users
- Clear communication during emergency situations
- Better demonstration for international hackathon judges
- Easier adoption for non-Japanese speaking communities

## 🌟 Hackathon Alignment

### Social Impact (Social Good)
- **Community Mutual Aid**: Facilitates solidarity between neighbors during crises
- **Resilience**: Strengthens communities' ability to face disasters
- **Inclusion**: Accessible to all neighborhood residents, regardless of age

### Function
- Simulated disaster alerts (earthquakes, typhoons, etc.)
- Neighborhood groups based on Japanese postal codes
- Community chat to share resources and information
- Check-in system to reassure neighbors

### Design
- Japanese **wabi-sabi** aesthetic: minimalist, clean, functional
- Calming color palette: blue, white, grey
- Intuitive and accessible interface
- Clear typography (Roboto)

### Presentation
- Well-commented and structured code
- Fully functional demo-ready application
- Complete documentation

## 🚀 How to Launch the Application on Replit

### Step 1: Open the Project
The project is already configured with all necessary files.

### Step 2: Install Dependencies
Dependencies are automatically installed by Replit (Flask is already configured).

### Step 3: Launch the Application
Click the **Run** button or execute in the terminal:
```bash
python main.py
```

### Step 4: Test the Application
1. Open the application in your browser (use the provided Replit URL)
2. On the homepage, you'll see a simulated earthquake alert
3. Enter a Japanese postal code (e.g., `100-0001` for Chiyoda, Tokyo)
4. Access your neighborhood's community chat
5. View simulated resource-sharing messages
6. Click "I'm Safe" to simulate a safety check-in

## 📁 Project Structure

```
kizuna-alert/
├── main.py              # Flask backend with routes and logic
├── templates/           # HTML templates
│   ├── index.html       # Homepage with alerts and form
│   └── chat.html        # Community chat page
├── static/              # Static files
│   └── style.css        # Minimalist wabi-sabi design
├── README.md            # This file
└── pyproject.toml       # Python dependencies configuration
```

## 🎨 Current Features

### Homepage (`/`)
- **Disaster Alerts**: Simulated earthquake display
- **Postal Code Form**: Join your neighborhood group
- **User Guide**: How the application works
- **Clean Design**: Japanese wabi-sabi aesthetic

### Chat Page (`/chat`)
- **Simulated Community Messages**: 
  - 💧 Resource sharing (water, food)
  - 🆘 Help requests (evacuation, assistance)
  - ✓ Safety check-ins ("I'm safe")
  - ℹ️ Useful information (evacuation centers)
- **Color-coded message types** for easy reading
- **Check-in button** to signal safety
- **Integrated safety tips**

## 🔮 Next Steps (Full Version)

### Phase 2 - Real-time Chat
- [ ] Integrate Firebase or WebSockets for live chat
- [ ] Allow users to send their own messages
- [ ] Push notification system for new alerts

### Phase 3 - Advanced Features
- [ ] User authentication (name, profile)
- [ ] Geolocation for targeted alerts
- [ ] Interactive map showing available resources
- [ ] Integration with real weather alert APIs (JMA - Japan Meteorological Agency)
- [ ] Multilingual support (Japanese/English toggle)

### Phase 4 - Mobile & Accessibility
- [ ] Native mobile application (React Native/Flutter)
- [ ] Offline mode for emergency situations
- [ ] Enhanced accessibility (screen readers, contrast)

## 🛠️ Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, minimal JavaScript
- **Design**: Minimalist wabi-sabi, responsive design
- **Data**: Simulated (Python dictionaries) for demo

## 🎓 Technical Concepts Demonstrated

- **Flask Routing**: Managing multiple pages and forms
- **Sessions**: Temporary storage of user postal code
- **Jinja2 Templates**: Dynamic HTML generation
- **Modern CSS**: Gradients, flexbox, responsive design
- **UX Design**: Clear and intuitive interface for emergency situations

## 🌍 Potential Impact

Japan faces numerous natural disasters (earthquakes, typhoons, tsunamis). **Kizuna Alert** aims to:
- Reduce isolation of elderly people during crises
- Optimize distribution of limited resources
- Strengthen community bonds before, during, and after emergencies
- Complement official alert systems with local mutual aid

## 📝 Demo Notes

For your presentation video:
1. Show the homepage with the active alert
2. Demonstrate entering a postal code
3. Browse through the community chat messages
4. Click the check-in button
5. Explain next steps (real-time chat)

## 👥 Demo Postal Codes

- `100-0001` - Chiyoda Ward, Tokyo (City center)
- `150-0001` - Shibuya Ward, Tokyo (Busy district)
- `160-0001` - Shinjuku Ward, Tokyo (Business center)
- `106-0001` - Minato Ward, Tokyo (Residential area)
- `110-0001` - Taito Ward, Tokyo (Historic district)

## 📧 Contact & Contribution

Created for the **Youth Coders Collective Hackathon 2025**

Theme: **Social Good** + **Japan**

---

**絆** - The bonds that unite us are stronger than the disasters that strike us.
