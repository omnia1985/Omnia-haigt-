import streamlit as st

st.set_page_config(page_title="Omnia DeepArena - Small Clubs", layout="wide")

# استقبال اللغة النشطة من حساب المستخدم أو الصفحة الرئيسية تلقائياً
if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'

lang = st.session_state['language']

translations = {
    'العربية': {
        'title': "🏪 أندية الدرجة 2 و3، أندية الهواة، والأكاديميات الخاصة",
        'price_label': "💰 اشتراك الباقة الشهري",
        'features_title': "📋 الميزات النشطة:",
        'f1': "✅ محرك الريمونتادا والخطط التبديلية الحية (50,000 محاكاة)",
        'f2': "✅ التحليل الطبي والنفسي الاستباقي (متلازمة اليوم السلبي)",
        'f3': "✅ العرض فوق الكاميرا للثنائيات والاستحواذ",
        'f4': "✅ حماية المعطيات والامتثال لمنظومة GDPR"
    },
    'English': {
        'title': "🏪 Division 2, 3, Amateur Clubs & Private Academies",
        'price_label': "💰 Monthly Subscription Price",
        'features_title': "📋 Active Features:",
        'f1': "✅ Live Remontada Engine & Substitution Tactics (50,000 simulations)",
        'f2': "✅ Proactive Medical & Psychological Analysis (Negative Day Syndrome)",
        'f3': "✅ AR Overlay on Camera (Possession, Goals, Duels)",
        'f4': "✅ Data Protection & GDPR Compliance"
    },
    'Français': {
        'title': "🏪 Clubs de Division 2, 3, Amateurs & Académies Privées",
        'price_label': "💰 Prix de l'abonnement mensuel",
        'features_title': "📋 Fonctionnalités actives:",
        'f1': "✅ Moteur de Remontada et tactiques de remplacement en direct (50 000 simulations)",
        'f2': "✅ Analyse médicale et psychologique proactive (Syndrome du Jour Négatif)",
        'f3': "✅ Incrustation AR sur caméra (Possession, Buts, Duels)",
        'f4': "✅ Protection des données et conformité GDPR"
    },
    'Español': { 'title': "🏪 Clubes de División 2, 3, Aficionados y Academias Privadas", 'price_label': "💰 Precio de suscripción mensual", 'features_title': "📋 Funciones activas:", 'f1': "✅ Motor de Remontada en vivo (50,000 simulaciones)", 'f2': "✅ Análisis médico proactivo (Día Negativo)", 'f3': "✅ Superposición AR en cámara", 'f4': "✅ Protección de datos GDPR" },
    'Italiano': { 'title': "🏪 Club di Divisione 2, 3, Dilettanti e Accademie Private", 'price_label': "💰 Prezzo dell'abbonamento mensile", 'features_title': "📋 Funzionalità attive:", 'f1': "✅ Rimonta in diretta (50.000 simulazioni)", 'f2': "✅ Analisi medica proattiva (Giorno Negativo)", 'f3': "✅ Sovrapposizione AR su telecamera", 'f4': "✅ Protezione dei dati GDPR" },
    'Português': { 'title': "🏪 Clubes de Divisão 2, 3, Amadores e Academias Privadas", 'price_label': "💰 Preço da assinatura mensal", 'features_title': "📋 Recursos ativos:", 'f1': "✅ Motor de Reviravolta ao vivo (50.000 simulações)", 'f2': "✅ Análise médica proativa (Dia Negativo)", 'f3': "✅ Sobreposição AR na câmera", 'f4': "✅ Proteção de dados GDPR" }
}

t = translations.get(lang, translations['English'])

# إظهار مبلغ الاشتراك والميزات في الجانب بوضوح تلبية لطلبك
st.sidebar.metric(label=t['price_label'], value="150 USD")
st.sidebar.markdown(f"### {t['features_title']}")
st.sidebar.write(t['f1'])
st.sidebar.write(t['f2'])
st.sidebar.write(t['f3'])
st.sidebar.write(t['f4'])

# العنوان المترجم تلقائياً في أعلى الصفحة حسب المستخدم
st.title(t['title'])
st.write("---")
