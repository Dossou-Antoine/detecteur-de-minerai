import streamlit as st

st.set_page_config(page_title="Detecteur de Minerai - Antoine DOSSOU", layout="centered")

st.title("⛏️ DÉTECTEUR DE MINERAI")
st.subheader("Par Antoine DOSSOU | Or - Chrome - Lithium - Nickel")
st.markdown("**Méthode 100% Terrain :** Résistivimètre + Magnétomètre + Observation géologique")
st.divider()

st.header("1. Entrez les mesures du terrain")

resistivite = st.slider("Résistivité (Ohm.m) - Résistivimètre", 5, 500, 150)
magnetisme = st.slider("Magnétisme (nT) - Magnétomètre", 0, 800, 50)
quartz = st.slider("Indice de Veines de Quartz (0 à 10) - Observation à l'oeil", 0, 10, 1)

if st.button("🔍 ANALYSER LE TERRAIN", type="primary"):
    st.divider()
    st.header("2. Résultat")
    resultat = "AUCUN MINERAI"
    confiance = 50.0
    explication = "Aucune anomalie."
    reco = "Changer de zone."
    if resistivite > 200 and magnetisme < 150:
        resultat = "🔋 LITHIUM DÉTECTÉ"
        confiance = min(92, 55 + (resistivite-200)/10)
        explication = f"Résistivité très haute ({resistivite} Ohm.m) + Magnétisme bas = Pegmatite à Lithium."
        reco = "Faire un sondage carotté."
    elif magnetisme > 450 and resistivite < 60:
        resultat = "⚫ CHROME DÉTECTÉ"
        confiance = min(92, 55 + (magnetisme-450)/20)
        explication = f"Magnétisme très fort ({magnetisme} nT) + Résistivité très basse = Chromite."
        reco = "Cartographie magnétique détaillée."
    elif quartz >= 6 and resistivite < 120 and magnetisme < 150:
        resultat = "🟡 OR DÉTECTÉ"
        confiance = min(92, 55 + quartz*3)
        explication = f"Beaucoup de Quartz ({quartz}/10) + Résistivité basse + Magnétisme bas = Signature de l'Or."
        reco = "Faire un forage de confirmation."
    elif magnetisme > 250 and resistivite < 80 and quartz < 5:
        resultat = "🟢 NICKEL DÉTECTÉ"
        confiance = min(90, 55 + (magnetisme-250)/20)
        explication = f"Magnétisme haut + Résistivité basse + Peu de Quartz = Nickel."
        reco = "Analyse géochimique Nickel-Cobalt."
    if resultat != "AUCUN MINERAI":
        st.success(f"### {resultat}")
    else:
        st.warning(f"### {resultat}")
    st.metric("Confiance", f"{confiance:.1f} %")
    st.info(f"**Pourquoi ?** {explication}")
    st.warning(f"**Recommandation :** {reco}")

st.divider()
st.caption("DÉTECTEUR DE MINERAI - Par Antoine DOSSOU - Prototype IA")
