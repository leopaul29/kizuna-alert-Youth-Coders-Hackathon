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
│   ├── chat.html        # Community chat page
│   └── evacuation.html  # Evacuation centers with map
├── static/              # Static files
│   ├── style.css        # Enhanced wabi-sabi design
│   └── images/          # Image assets
│       └── evacuation_map.png  # Route to evacuation center
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
- **Evacuation center access** with route maps
- **Integrated safety tips**

### Evacuation Centers Page (`/evacuation`)
- **Interactive route map** showing path to nearest evacuation center
- **Detailed facility information** (capacity, facilities, accessibility)
- **Step-by-step evacuation instructions**
- **Alternative center listings** for flexibility
- **Emergency contact information**

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
- **Design**: Enhanced wabi-sabi aesthetic with CSS animations
- **Data**: Simulated (Python dictionaries) for demo

## 🎨 Design Choices

### Wabi-Sabi Philosophy
Our design embodies the Japanese aesthetic of **wabi-sabi** — finding beauty in imperfection, simplicity, and naturalness. This philosophy is particularly appropriate for disaster response applications because it:
- **Promotes calmness** during stressful emergencies through understated design
- **Emphasizes functionality** over decoration, ensuring clear communication
- **Embraces simplicity** to reduce cognitive load when users need information quickly

### Color Palette
We carefully selected colors that reflect wabi-sabi principles while maintaining usability:

| Color | Purpose | Psychological Impact |
|-------|---------|---------------------|
| **Navy Blue (#1a2332)** | Primary background, headers | Trust, stability, authority - reassuring during crises |
| **Off-White (#f8f9fa)** | Content backgrounds | Clean, neutral canvas that doesn't strain eyes |
| **Soft Gray (#94a3b8)** | Secondary elements, borders | Gentle contrast without harshness |
| **Accent Red (#dc2626)** | Alerts, warnings | Immediate attention for critical information |
| **Accent Green (#16a34a)** | Safety confirmations, resources | Reassurance, positive actions |
| **Accent Blue (#2563eb)** | Interactive elements, information | Clarity, trust, navigation |

### Typography
- **Font Family**: Roboto with Japanese fallback (Noto Sans JP)
- **Font Weights**: 200-500 range for subtle hierarchy
- **Line Height**: 1.6-1.8 for comfortable reading during stress
- **Letter Spacing**: Increased for headers to create breathing room

### Subtle Animations
Animations are designed to be **gentle and purposeful**, never distracting:
- **Button hover effects**: Slight elevation and glow to confirm interactivity
- **Ripple effect**: Subtle feedback on button clicks
- **Fade-in transitions**: Smooth 0.6s ease-in for page loads
- **Slide-in messages**: 0.4s animation for chat messages
- **Transform on hover**: 2-3px translateY for depth perception

All animations respect **prefers-reduced-motion** settings for accessibility.

### Responsive Design
- **Mobile-first approach**: Optimized for phones (primary device during emergencies)
- **Breakpoint at 768px**: Seamless transition between mobile and desktop
- **Touch-friendly targets**: Minimum 44px tap areas for buttons
- **Flexible layouts**: Content adapts gracefully to all screen sizes

## ♿ Accessibility Features

### WCAG 2.1 Compliance
Kizuna Alert follows **WCAG 2.1 Level AA** guidelines for accessibility:

#### Visual Accessibility
- **Color Contrast**: All text meets minimum 4.5:1 contrast ratio
- **Focus Indicators**: 3px visible outline on all interactive elements
- **Text Scaling**: Design remains functional up to 200% zoom
- **Non-color Indicators**: Icons and text labels accompany color-coding

#### Keyboard Navigation
- **Full keyboard support**: All features accessible via keyboard
- **Logical tab order**: Follows visual flow of content
- **Skip links**: (Planned) Jump to main content
- **Focus management**: Clear visual focus states

#### Screen Reader Support
- **Semantic HTML**: Proper heading hierarchy (h1-h3)
- **ARIA labels**: Meaningful labels for interactive elements
- **Alt text**: Descriptive alternative text for images
- **Language declaration**: `lang="en"` attribute for proper pronunciation

#### Motor Accessibility
- **Large click targets**: Minimum 44x44px touch areas
- **No time limits**: Users can take their time to read and act
- **Error prevention**: Form validation with clear messages
- **Undo actions**: "Leave Group" option allows reversal

#### Cognitive Accessibility
- **Simple language**: Clear, direct communication
- **Consistent layout**: Familiar patterns across pages
- **Visual hierarchy**: Important information stands out
- **Iconography**: Visual symbols support text
- **Progress indicators**: Users know where they are

### Accessibility Testing Checklist
- [x] Color contrast verified with WCAG tools
- [x] Keyboard navigation tested
- [x] Semantic HTML structure validated
- [x] Focus states clearly visible
- [x] Responsive at 200% zoom
- [x] Reduced motion preferences respected
- [x] High contrast mode compatible
- [ ] Screen reader testing (pending)
- [ ] User testing with disabilities (planned)

### Emergency-Specific Accessibility
- **Panic-friendly design**: Large fonts, clear buttons
- **Multilingual considerations**: English interface with Japanese cultural elements
- **Low-bandwidth optimization**: Minimal images, efficient CSS
- **Offline capability**: (Planned) Service worker for offline access

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
