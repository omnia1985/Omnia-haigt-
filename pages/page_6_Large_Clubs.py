import streamlit as st

st.set_page_config(page_title="Omnia DeepArena - Large Clubs", layout="wide")

# استقبال اللغة النشطة تلقائياً عبر ذاكرة الجلسة المشتركة من الصفحة الرئيسية
if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'

lang = st.session_state['language']

translations = {
    'العربية': {
        'title': "🏰 أندية البطولات والكؤوس الكبرى",
        'price_label': "💰 اشتراك الباقة الشهري",
        'features_title': "📋 الحماية الفائقة والسيادة النشطة:",
        'f1': "✅ معالجة فورية للملاعب الذكية وحواسيبها ببث فوري Ultra HD (صفر تأخير)",
        'f2': "✅ مستشار الذكاء الاصطناعي لإدارة أزمات غرف الملابس والضغط الإعلامي وجماهيري",
        'f3': "✅ بيئة سيبرانية معزولة ومحمية بالكامل لحماية عمليات الإسقاط والامتثال للـ GDPR"
    },
    'English': {
        'title': "🏰 Major Championship & Cup Clubs",
        'price_label': "💰 Monthly Subscription Price",
        'features_title': "📋 Premium Security & Sovereignty:",
        'f1': "✅ Real-time smart stadium processing with Ultra HD live feed (Zero latency)",
        'f2': "✅ AI consultant to manage locker room behavioral crises and media/fan pressure",
        'f3': "✅ Fully isolated sandbox environment protecting tactical projections and GDPR compliance"
    },
    'Français': {
        'title': "🏰 Grands Clubs de Championnats & Coupes",
        'price_label': "💰 Prix de l'abonnement mensuel",
        'features_title': "📋 Sécurité Premium & Souveraineté:",
        'f1': "✅ Traitement des stades intelligents en temps réel avec flux Ultra HD (Zéro latence)",
        'f2': "✅ Consultant IA pour gérer les crises de vestiaire et la pression médiatique",
        'f3': "✅ Environnement sandbox isolé protégeant les projections tactiques et la conformité GDPR"
    },
    'Español': { 
        'title': "🏰 Grandes Clubes de Campeonatos y Copas", 
        'price_label': "💰 Suscripción mensual", 
        'features_title': "📋 Seguridad Premium y Soberanía:", 
        'f1': "✅ Procesamiento en tiempo real Ultra HD", 
        'f2': "✅ Consultor de IA para gestionar crisis", 
        'f3': "✅ Entorno de sandbox aislado y GDPR" 
    },
    'Italiano': { 
        'title': "🏰 Grandi Club di Campionati e Coppe", 
        'price_label': "💰 Abbonamento mensile", 
        'features_title': "📋 Sicurezza Premium e Sovranità:", 
        'f1': "✅ Elaborazione in tempo reale Ultra HD", 
        'f2': "✅ Consulente IA per gestire crisi", 
        'f3': "✅ Sandbox isolato e GDPR" 
    },
    'Português': { 
        'title': "🏰 Grandes Clubes de Campeonatos e Copas", 
        'price_label': "💰 Assinatura mensal", 
        'features_title': "📋 Segurança Premium e Soberania:", 
        'f1': "✅ Processamento em tempo real Ultra HD", 
        'f2': "✅ Consultor de IA para gerenciar crises", 
        'f3': "✅ Ambiente sandbox isolado e GDPR" 
    }
}

t = translations.get(lang, translations['English'])

# عرض السعر المالي الثابت بشكل بارز في الجانب بكل اللغات لزوار المنصة
st.sidebar.metric(label=t['price_label'], value="1500 USD")
st.sidebar.markdown(f"### {t['features_title']}")
st.sidebar.write(t['f1'])
st.sidebar.write(t['f2'])
st.sidebar.write(t['f3'])

# العنوان الرئيسي المحدث بكلمة كبرى لترجمته ديناميكياً في أعلى الشاشة
st.title(t['title'])
st.write("---")
