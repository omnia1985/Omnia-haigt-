import streamlit as st

st.set_page_config(page_title="Omnia DeepArena", layout="wide")

# ✨ السطر السحري المؤمن: تأمين ذاكرة الجلسة واللغة فوراً لمنع اختفاء المحتوى
if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'

lang = st.session_state['language']

translations = {
    'العربية': {
        'title': "🏢 الأندية المتوسطة من الدرجة الأولى",
        'sub': "📌 إذا كان ناديك ينتمي إلى الدرجة الأولى ويمتلك ميزانية ذكية، فهذا هو المكان الصحيح للاشتراك وتفعيل حسابك.",
        'price_label': "💰 اشتراك الباقة الشهري",
        'features_title': "📋 الميزات النشطة في الباقة:",
        'f1': "✅ كل ميزات باقة ديمقراطية التكنولوجيا (الرمونتادا والثنائيات والطبي والـ GDPR)",
        'f2': "✅ دمج كاميرات البث المحترفة وتصوير الدرون (Drone Integration)",
        'f3': "✅ تصفح كامل لسوق المواهب العالمي وعمل إسقاط تكتيكي للمشتري",
        'market_title': "🔍 محرك الاستكشاف المفتوح وسوق الانتقالات العالمي المشترك",
        'market_sub': "📌 تتيح لك هذه الباقة تصفح مواهب الصفحتين 1 و2 وعمل إسقاط تكتيكي فوري لهم لمعرفة مدى انسجامهم قبل الشراء.",
        'btn_drop': "🔬 عمل إسقاط تكتيكي في خطة نادينا (10,000 مباراة)",
        'btn_buy': "💼 بدء تفاوض رسمي وشراء العقد",
        'success_drop': "📊 نتيجة محاكاة الإسقاط التكتيكي الموحد: هذا اللاعب يمتلك نسبة تأقلم تكتيكي وبدني 89% ونسبة تفوق في الثنائيات تصل لـ 72% بناءً على قوالب المباريات التاريخية.",
        'info_buy': "⚖️ امتثال المعاملات وعقود الانتقال وحماية الـ GDPR: تم فتح قناة المعاملات المشفرة، وسيتم حساب واقتطاع حقوق التكوين والتضامن وعمولة المنصة آلياً فور توقيع الأطراف لضمان حقوق المكوّن."
    },
    'English': {
        'title': "🏢 Medium Clubs from Division 1",
        'sub': "📌 If your club belongs to the top division with a smart budget, this is the right place to subscribe and activate your account.",
        'price_label': "💰 Monthly Subscription Price",
        'features_title': "📋 Active Features:",
        'f1': "✅ All tech democratization features (Remontada, Duels, Medical & GDPR)",
        'f2': "✅ Integration with professional broadcast cameras and drones",
        'f3': "✅ Full access to browse global talents and perform buyer tactical projections",
        'market_title': "🔍 Open Scouting Engine & Global Unified Transfer Market",
        'market_sub': "📌 This package allows you to browse talents from pages 1 and 2 and run instant tactical projections to check adaptation before buying.",
        'btn_drop': "🔬 Run Tactical Projection in Our System (10,000 matches)",
        'btn_buy': "💼 Start Official Negotiation & Buy Contract",
        'success_drop': "📊 Tactical Projection Result: This player has an 89% tactical and physical adaptation rate, and a 72% success rate in duels.",
        'info_buy': "⚖️ Transaction Compliance & GDPR Protection: Encrypted channel opened. Solidarity mechanisms and platform commission calculated automatically."
    },
    'Français': {
        'title': "🏢 Clubs Moyens de Première Division",
        'sub': "📌 Si votre club appartient à la première division avec un budget intelligent, c'est le bon endroit pour vous abonner.",
        'price_label': "💰 Prix de l'abonnement mensuel",
        'features_title': "📋 Fonctionnalités actives:",
        'f1': "✅ Toutes les fonctions de démocratisation (Remontada, Duels, Médical & GDPR)",
        'f2': "✅ Intégration de caméras de diffusion professionnelles et de drones",
        'f3': "✅ Accès complet pour parcourir les talents mondiaux et faire des projections tactiques",
        'market_title': "🔍 Moteur de recherche ouvert & Marché mondial unifié des transferts",
        'market_sub': "📌 Ce pack vous permet de parcourir les talents des pages 1 et 2 et de lancer des projections tactiques.",
        'btn_drop': "🔬 Lancer une projection tactique (10 000 matchs)",
        'btn_buy': "💼 Négociation officielle & Acheter le contrat",
        'success_drop': "📊 Résultat de la projection: Adaptation de 89% et 72% de réussite dans los duels.",
        'info_buy': "⚖️ Conformité & Protection GDPR: Canal chiffré ouvert. Calcul automatique des commissions."
    },
    'Español': { 'title': "🏢 Clubes Medianos de Primera División", 'sub': "📌 Presupuesto inteligente.", 'price_label': "💰 Suscripción mensual", 'features_title': "📋 Funciones:", 'f1': "✅ Democratización", 'f2': "✅ Cámaras", 'f3': "✅ Acceso completo", 'market_title': "🔍 Mercado global", 'market_sub': "📌 Explorar talentos.", 'btn_drop': "🔬 Proyección", 'btn_buy': "💼 Comprar", 'success_drop': "📊 89% Éxito", 'info_buy': "⚖️ GDPR" },
    'Italiano': { 'title': "🏢 Club Medi di Prima Divisione", 'sub': "📌 Budget intelligente.", 'price_label': "💰 Abbonamento", 'features_title': "📋 Funzionalità:", 'f1': "✅ Democratizzazione", 'f2': "✅ Telecamere", 'f3': "✅ Accesso completo", 'market_title': "🔍 Mercato globale", 'market_sub': "📌 Sfoglia i talenti.", 'btn_drop': "🔬 Proiezione", 'btn_buy': "💼 Acquista", 'success_drop': "📊 89% Successo", 'info_buy': "⚖️ GDPR" },
    'Português': { 'title': "🏢 Clubes Médios da Primeira Divisão", 'sub': "📌 Orçamento inteligente.", 'price_label': "💰 Assinatura", 'features_title': "📋 Recursos:", 'f1': "✅ Democratização", 'f2': "✅ Câmeras", 'f3': "✅ Acesso total", 'market_title': "🔍 Mercado global", 'market_sub': "📌 Navegar pelos talentos.", 'btn_drop': "🔬 Projeção", 'btn_buy': "💼 Comprar", 'success_drop': "📊 89% Sucesso", 'info_buy': "⚖️ GDPR" }
}

t = translations.get(lang, translations['English'])

st.sidebar.metric(label=t['price_label'], value="500 USD")
st.sidebar.markdown(f"### {t['features_title']}")
st.sidebar.write(t['f1'])
st.sidebar.write(t['f2'])
st.sidebar.write(t['f3'])

st.title(t['title'])
st.write(t['sub'])
st.write("---")

st.header(t['market_title'])
st.write(t['market_sub'])

# محاكاة تفاعلية للجدول الموحد والإسقاط
c_btn1, c_btn2 = st.columns(2)
with c_btn1:
    if st.button(t['btn_drop']): st.success(t['success_drop'])
with c_btn2:
    if st.button(t['btn_buy']): st.info(t['info_buy'])
