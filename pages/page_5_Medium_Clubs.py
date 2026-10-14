import streamlit as st

st.set_page_config(page_title="Omnia DeepArena - Medium Clubs", layout="wide")

if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'

lang = st.session_state['language']

translations = {
    'العربية': {
        'title': "🏢 الأندية المتوسطة من الدرجة الأولى",
        'price_label': "💰 اشتراك الباقة الشهري",
        'features_title': "📋 الميزات النشطة الباقة:",
        'f1': "✅ كل ميزات باقة ديمقراطية التكنولوجيا (الرمونتادا والثنائيات والطبي والـ GDPR)",
        'f2': "✅ دمج كاميرات البث المحترفة وتصوير الدرون (Drone Integration)",
        'f3': "✅ تصفح كامل لسوق المواهب العالمي وعمل إسقاط تكتيكي للمشتري"
    },
    'English': {
        'title': "🏢 Medium Clubs from Division 1",
        'price_label': "💰 Monthly Subscription Price",
        'features_title': "📋 Active Features:",
        'f1': "✅ All tech democratization features (Remontada, Duels, Medical & GDPR)",
        'f2': "✅ Integration with professional broadcast cameras and drones",
        'f3': "✅ Full access to browse global talents and perform buyer tactical projections"
    },
    'Français': {
        'title': "🏢 Clubs Moyens de Première Division",
        'price_label': "💰 Prix de l'abonnement mensuel",
        'features_title': "📋 Fonctionnalités actives:",
        'f1': "✅ Toutes les fonctions de démocratisation (Remontada, Duels, Médical & GDPR)",
        'f2': "✅ Intégration de caméras de diffusion professionnelles et de drones",
        'f3': "✅ Accès complet pour parcourir les talents mondiaux et faire des projections tactiques"
    },
    'Español': { 'title': "🏢 Clubes Medianos de Primera División", 'price_label': "💰 Suscripción mensual", 'features_title': "📋 Funciones activas:", 'f1': "✅ Todas las funciones de democratización", 'f2': "✅ Integración con cámaras profesionales y drones", 'f3': "✅ Acceso completo para buscar talentos globales" },
    'Italiano': { 'title': "🏢 Club Medi di Prima Divisione", 'price_label': "💰 Abbonamento mensile", 'features_title': "📋 Funzionalità attive:", 'f1': "✅ Tutte le funzioni di democratizzazione", 'f2': "✅ Integrazione con telecamere professionali e droni", 'f3': "✅ Accesso completo ai talenti globali" },
    'Português': { 'title': "🏢 Clubes Médios da Primeira Divisão", 'price_label': "💰 Assinatura mensal", 'features_title': "📋 Recursos ativos:", 'f1': "✅ Todos os recursos de democratização", 'f2': "✅ Integração com câmeras profissionais e drones", 'f3': "✅ Acesso total para buscar talentos globais" }
}

t = translations.get(lang, translations['English'])

st.sidebar.metric(label=t['price_label'], value="500 USD")
st.sidebar.markdown(f"### {t['features_title']}")
st.sidebar.write(t['f1'])
st.sidebar.write(t['f2'])
st.sidebar.write(t['f3'])

# العنوان المترجم تلقائياً في أعلى الصفحة حسب المستخدم
st.title(t['title'])
st.write("---")
