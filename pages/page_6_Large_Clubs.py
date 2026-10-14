import streamlit as st

st.set_page_config(page_title="Omnia DeepArena", layout="wide")

# ✨ السطر السحري المؤمن: تأمين ذاكرة الجلسة واللغة فوراً لمنع اختفاء المحتوى
if 'language' not in st.session_state:
    st.session_state['language'] = 'العربية'

lang = st.session_state['language']

translations = {
    'العربية': {
        'title': "🏰 أندية البطولات والكؤوس الكبرى",
        'sub': "📌 خاص بالأندية الكبرى والمنافسة على ألقاب البطولات المحلية، الكؤوس، والمسابقات الكبرى بصفة عامة في المشهد الكروي ند لند.",
        'price_label': "💰 اشتراك الباقة الشهري",
        'features_title': "📋 الحماية الفائقة والسيادة النشطة:",
        'f1': "✅ معالجة فورية للملاعب الذكية وحواسيبها ببث فوري Ultra HD (صفر تأخير)",
        'f2': "✅ مستشار الذكاء الاصطناعي لإدارة أزمات غرف الملابس والضغط الإعلامي وجماهيري",
        'f3': "✅ بيئة سيبرانية معزولة ومحمية بالكامل لحماية عمليات الإسقاط والامتثال للـ GDPR",
        'crisis_title': "🔥 مستشار إدارة الأزمات الافتراضي ومحاكي الضغط الإعلامي (AI Crisis Simulator)",
        'shield_title': "🛡️ نظام عزل رادارات الاستقطاب وتشفير عمليات الإسقاط التكتيكي",
        'shield_success': "🔒 جدار الحماية والسرية والفصل التام للمعطيات (GDPR) نشط: جميع عمليات الإسقاط التكتيكي ومحاكاة الـ 10,000 مباراة التي تقومون بها معزولة تماماً في بيئة مستقلة لمنع التجسس التكتيكي، ويستحيل على أي نادٍ منافس معرفة رادارات كشافتكم السريّة لحمايتكم بالكامل أثناء التنافس الشامل على الألقاب والمسابقات كقوة سيادية مكافئة لغيرها ند لند.",
        'err_msg': "🚨 تنبيه أزمة سلوكية محتملة: رصد مؤشر سلبي مرتفع في لغة جسد اللاعب وتراجع تواصله اللفظي نتيجة ضغوطات إعلامية وجماهيرية شرسة.",
        'info_msg': "📋 خطة احتواء الأزمة المقترحة من الـ AI: نقترح منحه راحة إعلامية كاملة وتفعيل محاكاة الضغط الإعلامي الافتراضي لتهيئته ذهنياً لضمان تفوقه الكامل في الثنائيات والاستحواذ."
    },
    'English': {
        'title': "🏰 Major Championship & Cup Clubs",
        'sub': "📌 Exclusively for large clubs competing for domestic titles, cups, and major competitions peer-to-peer.",
        'price_label': "💰 Monthly Subscription Price",
        'features_title': "📋 Premium Security & Sovereignty:",
        'f1': "✅ Real-time smart stadium processing with Ultra HD live feed (Zero latency)",
        'f2': "✅ AI consultant to manage locker room behavioral crises and media/fan pressure",
        'f3': "✅ Fully isolated sandbox environment protecting tactical projections and GDPR compliance",
        'crisis_title': "🔥 AI Crisis & Media Simulator Room",
        'shield_title': "🛡️ Scouting Radar Isolation & Encrypted Tactical Projections",
        'shield_success': "🔒 Military-Grade Shield & GDPR Isolation Active: All tactical projections and 10,000-match simulations you run are entirely isolated.",
        'err_msg': "🚨 Potential Behavioral Crisis Warning: High negative index detected.",
        'info_msg': "📋 AI Crisis Containment Plan: Complete media isolation recommended."
    },
    'Français': { 'title': "🏰 Grands Clubs de Championnats & Coupes", 'sub': "📌 Pour les grands clubs en compétition d'égal à égal.", 'price_label': "💰 Prix mensuel", 'features_title': "📋 Sécurité Premium:", 'f1': "✅ Traitement (Zéro latence)", 'f2': "✅ Consultant IA (Crises)", 'f3': "✅ Sandbox & GDPR", 'crisis_title': "🔥 Simulateur de Crise IA", 'shield_title': "🛡️ Isolation des Radars", 'shield_success': "🔒 Protection Active", 'err_msg': "🚨 Alerte Crise", 'info_msg': "📋 Plan IA" },
    'Español': { 'title': "🏰 Grandes Clubes de Campeonatos y Copas", 'sub': "📌 Títulos y copas.", 'price_label': "💰 Suscripción", 'features_title': "📋 Seguridad:", 'f1': "✅ Ultra HD", 'f2': "✅ Consultor IA", 'f3': "✅ GDPR", 'crisis_title': "🔥 Crisis", 'shield_title': "🛡️ Radar", 'shield_success': "🔒 Escudo militar", 'err_msg': "🚨 Alerta", 'info_msg': "📋 Plan" },
    'Italiano': { 'title': "🏰 Grandi Club di Campionati e Coppe", 'sub': "📌 Titoli e coppe.", 'price_label': "💰 Abbonamento", 'features_title': "📋 Sicurezza:", 'f1': "✅ Ultra HD", 'f2': "✅ Consulente IA", 'f3': "✅ GDPR", 'crisis_title': "🔥 Crisi", 'shield_title': "🛡️ Isolamento", 'shield_success': "🔒 Scudo", 'err_msg': "🚨 Allerta", 'info_msg': "📋 Piano" },
    'Português': { 'title': "🏰 Grandes Clubes de Campeonatos e Copas", 'sub': "📌 Títulos e copas.", 'price_label': "💰 Assinatura", 'features_title': "📋 Segurança:", 'f1': "✅ Real-time Ultra HD", 'f2': "✅ Consultor IA", 'f3': "✅ GDPR", 'crisis_title': "🔥 Crise", 'shield_title': "🛡️ Radar", 'shield_success': "🔒 Escudo", 'err_msg': "🚨 Alerta", 'info_msg': "📋 Plano" }
}

t = translations.get(lang, translations['English'])

st.sidebar.metric(label=t['price_label'], value="1500 USD")
st.sidebar.markdown(f"### {t['features_title']}")
st.sidebar.write(t['f1'])
st.sidebar.write(t['f2'])
st.sidebar.write(t['f3'])

st.title(t['title'])
st.write(t['sub'])
st.write("---")

st.header(t['crisis_title'])
st.error(t['err_msg'])
st.info(t['info_msg'])

st.write("---")
st.header(t['shield_title'])
st.success(t['shield_success'])
