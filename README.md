# 絆 Kizuna Alert

**Youth Coders Collective Hackathon 2025**

Une application web de résilience communautaire pour l'entraide lors de catastrophes naturelles au Japon.

## 🎯 Objectif du Projet

Kizuna (絆) signifie "lien" ou "connexion" en japonais. Cette application connecte les résidents d'un même quartier japonais pour:
- Recevoir des alertes de catastrophes en temps réel
- Partager des ressources (eau, nourriture, abri)
- Demander de l'aide lors d'urgences
- Signaler leur sécurité à leurs voisins (check-in)
- Renforcer la solidarité communautaire

## 🌟 Alignement avec le Hackathon

### Impact Social (Social Good)
- **Entraide communautaire**: Facilite la solidarité entre voisins lors de crises
- **Résilience**: Renforce la capacité des communautés à faire face aux catastrophes
- **Inclusion**: Accessible à tous les résidents d'un quartier, peu importe leur âge

### Fonction
- Alertes de catastrophes simulées (séismes, typhons, etc.)
- Groupes de quartier basés sur les codes postaux japonais
- Chat communautaire pour partager ressources et informations
- Système de check-in pour rassurer ses voisins

### Design
- Esthétique **wabi-sabi** japonaise: minimaliste, épurée, fonctionnelle
- Palette de couleurs apaisantes: bleu, blanc, gris
- Interface intuitive et accessible
- Typography claire (Roboto)

### Présentation
- Code bien commenté et structuré
- Application fonctionnelle prête pour démo
- Documentation complète

## 🚀 Comment Lancer l'Application sur Replit

### Étape 1: Ouvrir le Projet
Le projet est déjà configuré avec tous les fichiers nécessaires.

### Étape 2: Installer les Dépendances
Les dépendances sont automatiquement installées par Replit (Flask est déjà configuré).

### Étape 3: Lancer l'Application
Cliquez sur le bouton **Run** ou exécutez dans le terminal:
```bash
python main.py
```

### Étape 4: Tester l'Application
1. Ouvrez l'application dans votre navigateur (utilisez l'URL Replit fournie)
2. Sur la page d'accueil, vous verrez une alerte de séisme simulée
3. Entrez un code postal japonais (ex: `100-0001` pour Chiyoda, Tokyo)
4. Accédez au chat communautaire de votre quartier
5. Voyez les messages simulés de partage de ressources
6. Cliquez sur "Je Vais Bien" pour simuler un check-in de sécurité

## 📁 Structure du Projet

```
kizuna-alert/
├── main.py              # Backend Flask avec routes et logique
├── templates/           # Templates HTML
│   ├── index.html       # Page d'accueil avec alertes et formulaire
│   └── chat.html        # Page de chat communautaire
├── static/              # Fichiers statiques
│   └── style.css        # Design wabi-sabi minimaliste
├── README.md            # Ce fichier
└── pyproject.toml       # Configuration des dépendances Python
```

## 🎨 Fonctionnalités Actuelles

### Page d'Accueil (`/`)
- **Alertes de catastrophe**: Affichage simulé de séisme
- **Formulaire de code postal**: Rejoindre son groupe de quartier
- **Guide d'utilisation**: Comment fonctionne l'application
- **Design épuré**: Esthétique wabi-sabi japonaise

### Page de Chat (`/chat`)
- **Messages communautaires simulés**: 
  - 💧 Partage de ressources (eau, nourriture)
  - 🆘 Demandes d'aide (évacuation, assistance)
  - ✓ Check-ins de sécurité ("Je vais bien")
  - ℹ️ Informations utiles (centres d'évacuation)
- **Types de messages codés par couleur** pour faciliter la lecture
- **Bouton check-in** pour signaler sa sécurité
- **Conseils de sécurité** intégrés

## 🔮 Prochaines Étapes (Version Complète)

### Phase 2 - Chat en Temps Réel
- [ ] Intégrer Firebase ou WebSockets pour un chat en direct
- [ ] Permettre aux utilisateurs d'envoyer leurs propres messages
- [ ] Système de notifications push pour nouvelles alertes

### Phase 3 - Fonctionnalités Avancées
- [ ] Authentification utilisateur (nom, profil)
- [ ] Géolocalisation pour alertes ciblées
- [ ] Carte interactive montrant ressources disponibles
- [ ] Intégration avec vraies APIs d'alertes météo (JMA - Japan Meteorological Agency)
- [ ] Support multilingue (japonais/anglais)

### Phase 4 - Mobile & Accessibilité
- [ ] Application mobile native (React Native/Flutter)
- [ ] Mode hors-ligne pour situations d'urgence
- [ ] Accessibilité améliorée (lecteurs d'écran, contraste)

## 🛠️ Technologies Utilisées

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript minimal
- **Design**: Wabi-sabi minimaliste, design responsive
- **Données**: Simulées (dictionnaires Python) pour la démo

## 🎓 Concepts Techniques Démontrés

- **Routing Flask**: Gestion de plusieurs pages et formulaires
- **Sessions**: Stockage temporaire du code postal utilisateur
- **Templates Jinja2**: Génération dynamique de HTML
- **CSS Moderne**: Gradients, flexbox, design responsive
- **UX Design**: Interface claire et intuitive pour situations d'urgence

## 🌍 Impact Potentiel

Le Japon fait face à de nombreuses catastrophes naturelles (séismes, typhons, tsunamis). **Kizuna Alert** vise à:
- Réduire l'isolement des personnes âgées lors de crises
- Optimiser la distribution de ressources limitées
- Renforcer les liens communautaires avant, pendant et après les urgences
- Compléter les systèmes d'alerte officiels avec l'entraide de proximité

## 📝 Notes pour la Démo

Pour votre vidéo de présentation:
1. Montrez la page d'accueil avec l'alerte active
2. Démontrez l'entrée d'un code postal
3. Parcourez les messages du chat communautaire
4. Cliquez sur le bouton check-in
5. Expliquez les prochaines étapes (chat en temps réel)

## 👥 Codes Postaux de Démonstration

- `100-0001` - Chiyoda Ward, Tokyo (Centre ville)
- `150-0001` - Shibuya Ward, Tokyo (Quartier animé)
- `160-0001` - Shinjuku Ward, Tokyo (Centre d'affaires)
- `106-0001` - Minato Ward, Tokyo (Zone résidentielle)
- `110-0001` - Taito Ward, Tokyo (Quartier historique)

## 📧 Contact & Contribution

Créé pour le **Youth Coders Collective Hackathon 2025**

Thème: **Social Good** + **Japon**

---

**絆** - Les liens qui nous unissent sont plus forts que les catastrophes qui nous frappent.
