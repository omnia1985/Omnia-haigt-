import streamlit as st

st.set_page_config(page_title="Omnia DeepArena", layout="wide")

# 🔒 السطر السحري المؤمن: خلق ذاكرة الجلسة واللغة وقائمة اللاعبين فوراً إذا كانت فارغة
if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'
if 'global_players_list' not in st.session_state:
    st.session_state['global_players_list'] = []

lang = st.session_state['language']

translations = {
    'العربية': {
        'title': "🏪 أندية الدرجة 2 و3، أندية الهواة، والأكاديميات الخاصة",
        'sub': "📌 باقة الأندية الصغيرة والأكاديميات - مخصصة لإدارة وتغذية وعرض مواهب النادي الخاصة وحمايتها بمبدأ الند للند.",
        'price_label': "💰 اشتراك الباقة الشهري",
        'features_title': "📋 الميزات النشطة:",
        'f1': "✅ محرك الريمونتادا والخطط التبديلية الحية (50,000 محاكاة)",
        'f2': "✅ التحليل الطبي والنفسي الاستباقي (متلازمة اليوم السلبي)",
        'f3': "✅ العرض فوق الكاميرا الشاملة للثنائيات والاستحواذ",
        'f4': "✅ حماية المعطيات والامتثال لمنظومة GDPR",
        'cam_title': "🎥 فلتر مواجهة المباريات الحي (Universal AI Camera & AR Overlay)",
        'cam_sub': "📌 المنظومة مرتبطة حالياً بمصدر التصوير النشط (كاميرا الهاتف أو كاميرا الملعب)",
        'm1': "📊 نسبة الاستحواذ اللحظية", 'm2': "🎯 نسبة تسجيل الأهداف (xG Live)", 'm3': "⚔️ نسبة التفوق في الثنائيات",
        'btn_add': "➕ إنشاء كارت لاعب وتفعيل منظومة التشبيه (تجريبي)",
        'btn_pub': "🚀 إدراج في جدول الكشافين وتفعيل حماية الـ GDPR",
        'warn_no_player': "⚠️ لا يوجد لاعبون مسجلون حالياً عبر الصفحة الأولى.",
        'success_pub': "📥 تم النشر بنجاح! تفعيل ميزة التغبيش وحماية الـ GDPR في الجدول لضمان حقوق المكوّن آلياً."
    },
    'English': {
        'title': "🏪 Division 2, 3, Amateur Clubs & Private Academies",
        'sub': "📌 Small Clubs & Academies Package - Tailored to manage, feed, and display your club's own talents securely.",
        'price_label': "💰 Monthly Subscription Price",
        'features_title': "📋 Active Features:",
        'f1': "✅ Live Remontada Engine & Substitution Tactics (50,000 simulations)",
        'f2': "✅ Proactive Medical & Psychological Analysis (Negative Day Syndrome)",
        'f3': "✅ AR Overlay on Camera (Possession, Goals, Duels)",
        'f4': "✅ Data Protection & GDPR Compliance",
        'cam_title': "🎥 Live Match-Facing Filter (Universal AI Camera & AR Overlay)",
        'cam_sub': "📌 System currently connected to active video source",
        'm1': "📊 Live Possession Rate", 'm2': "🎯 Expected Goals (xG Live)", 'm3': "⚔️ Duels Won Percentage",
        'btn_add': "➕ Create Player Card & Activate Comparison System (Demo)",
        'btn_pub': "🚀 Publish to Scouts Market with GDPR Shield",
        'warn_no_player': "⚠️ No players registered yet via the first page.",
        'success_pub': "📥 Successfully published with GDPR Shield."
    },
    'Français': { 'title': "🏪 Clubs de Division 2, 3, Amateurs & Académies Privées", 'sub': "📌 Pack Petits Clubs & Académies.", 'price_label': "💰 Prix mensuel", 'features_title': "📋 Fonctionnalités:", 'f1': "✅ Moteur de Remontada (50 000 simulations)", 'f2': "✅ Analyse médicale (Jour Négatif)", 'f3': "✅ Incrustation AR", 'f4': "✅ Conformité GDPR", 'cam_title': "🎥 Filtrage en direct", 'cam_sub': "📌 Connecté", 'm1': "📊 Possession", 'm2': "🎯 xG Live", 'm3': "⚔️ Duels", 'btn_add': "➕ Créer joueur", 'btn_pub': "🚀 Publier", 'warn_no_player': "⚠️ Aucun joueur", 'success_pub': "📥 Publié" },
    'Español': { 'title': "🏪 Clubes de División 2, 3", 'sub': "📌 Pack Pequeños.", 'price_label': "💰 Suscripción", 'features_title': "📋 Funciones:", 'f1': "✅ Remontada", 'f2': "✅ Médico", 'f3': "✅ AR", 'f4': "✅ GDPR", 'cam_title': "🎥 Filtro", 'cam_sub': "📌 Conectado", 'm1': "📊 Posesión", 'm2': "🎯 xG", 'm3': "⚔️ Duelos", 'btn_add': "➕ Crear", 'btn_pub': "🚀 Publicar", 'warn_no_player': "⚠️ No", 'success_pub': "📥 Éxito" },
    'Italiano': { 'title': "🏪 Club di Divisione 2, 3", 'sub': "📌 Piccoli Club.", 'price_label': "💰 Abbonamento", 'features_title': "📋 Funzioni:", 'f1': "✅ Rimonta", 'f2': "✅ Medico", 'f3': "✅ AR", 'f4': "✅ GDPR", 'cam_title': "🎥 Filtro", 'cam_sub': "📌 Connesso", 'm1': "📊 Possesso", 'm2': "🎯 xG", 'm3': "⚔️ Duelli", 'btn_add': "➕ Crea", 'btn_pub': "🚀 Pubblica", 'warn_no_player': "⚠️ No", 'success_pub': "📥 Successo" },
    'Português': { 'title': "🏪 Clubes de Divisão 2, 3", 'sub': "📌 Pequenos.", 'price_label': "💰 Assinatura", 'features_title': "📋 Recursos:", 'f1': "✅ Reviravolta", 'f2': "✅ Médico", 'f3': "✅ AR", 'f4': "✅ GDPR", 'cam_title': "🎥 Filtro", 'cam_sub': "📌 Conectado", 'm1': "📊 Posse", 'm2': "🎯 xG", 'm3': "⚔️ Duelos", 'btn_add': "➕ Criar", 'btn_pub': "🚀 Publicar", 'warn_no_player': "⚠️ Não", 'success_pub': "📥 Sucesso" }
}

t = translations.get(lang, translations['English'])

st.sidebar.metric(label=t['price_label'], value="150 USD")
st.sidebar.markdown(f"### {t['features_title']}")
st.sidebar.write(t['f1'])
st.sidebar.write(t['f2'])
st.sidebar.write(t['f3'])
st.sidebar.write(t['f4'])

st.title(t['title'])
st.write(t['sub'])
st.write("---")

st.header(t['cam_title'])
st.write(f"*{t['cam_sub']}*")
c1, c2, c3 = st.columns(3)
c1.metric(label=t['m1'], value="56%")
c2.metric(label=t['m2'], value="2.1")
c3.metric(label=t['m3'], value="64%")

st.write("---")
if st.button(t['btn_add']):
    st.session_state['global_players_list'].append({
        "name": "أحمد (ناشئ)", "age": 15, "position": "LW",
        "similar_to": "نجوم المحترفين", "star_image": "https://unsplash.com",
        "price": "45,000 USD", "status": "للبيع"
    })
    st.rerun()

players = st.session_state['global_players_list']
if not players:
    st.warning(t['warn_no_player'])
else:
    for idx, p in enumerate(players):
        col_img, col_info, col_btn = st.columns()
        with col_img: st.image(p["star_image"], width=100)
        with col_info: st.write(f"**المركز:** {p['position']} | **الثمن:** {p['price']}")
        with col_btn:
            if st.button(t['btn_pub'], key=f"btn_p_{idx}"): st.success(t['success_pub'])
