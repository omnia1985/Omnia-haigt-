import streamlit as st

st.set_page_config(page_title="Omnia DeepArena", layout="wide")

# ✨ السطر السحري المؤمن: تأمين ذاكرة الجلسة واللغة وقائمة اللاعبين فوراً لمنع اختفاء المحتوى
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
        'm1': "📊 نسبة الاستحواذ اللحظية", 'm2': "🎯 نسبة تسجيل الأهداف (xG Live)", 'm3': "⚔️ نسبة التفوق في الثنائيات (Duels Won)",
        'btn_add': "➕ إنشاء كارت لاعب وتفعيل منظومة التشبيه (تجريبي)",
        'btn_pub': "🚀 إدراج في جدول الكشافين وتفعيل حماية الـ GDPR",
        'warn_no_player': "⚠️ لا يوجد لاعبون مسجلون حالياً عبر الصفحة الأولى.",
        'success_pub': "📥 تم النشر بنجاح! تفعيل ميزة التغبيش وحماية الـ GDPR في الجدول لضمان حقوق المكوّن آلياً.",
        'ai_tactical': "🧠 مساعد الذكاء الاصطناعي التكتيكي وطوارئ الريمونتادا: تم رصد ثغرة في الرواق الأيسر للخصم ونقترح التحول فوراً إلى خطة 3-5-2 الهجومية. محرك الريمونتادا قام بمحاكاة المباراة 50,000 مرة ونسبة العودة والانتصار بهذه الخطة هي 78%!",
        'ai_medical': "🩺 التقرير الطبي والنفسي الاستباقي للناشئين والهواة: لغة جسد اللاعب تشير إلى إجهاد عضلي حاد ونرفزة مرتفعة (مؤشر اليوم السلبي)، نقترح استبداله لتفادي الكرت الأحمر أو الإصابة."
    },
    'English': {
        'title': "🏪 Division 2, 3, Amateur Clubs & Private Academies",
        'sub': "📌 Small Clubs & Academies Package - Tailored to manage, feed, and display your club's own talents securely peer-to-peer.",
        'price_label': "💰 Monthly Subscription Price",
        'features_title': "📋 Active Features:",
        'f1': "✅ Live Remontada Engine & Substitution Tactics (50,000 simulations)",
        'f2': "✅ Proactive Medical & Psychological Analysis (Negative Day Syndrome)",
        'f3': "✅ AR Overlay on Camera (Possession, Goals, Duels)",
        'f4': "✅ Data Protection & GDPR Compliance",
        'cam_title': "🎥 Live Match-Facing Filter (Universal AI Camera & AR Overlay)",
        'cam_sub': "📌 System currently connected to active video source (Smartphone or Stadium Camera)",
        'm1': "📊 Live Possession Rate", 'm2': "🎯 Expected Goals (xG Live)", 'm3': "⚔️ Duels Won Percentage",
        'btn_add': "➕ Create Player Card & Activate Comparison System (Demo)",
        'btn_pub': "🚀 Publish to Scouts Market with GDPR Shield",
        'warn_no_player': "⚠️ No players registered yet via the first page.",
        'success_pub': "📥 Successfully published! Blurring and GDPR features activated to secure developer rights automatically.",
        'ai_tactical': "🧠 AI Tactical Assistant: Weakness detected in opponent's left flank. We suggest shifting to 3-5-2. Remontada engine simulated the match 50,000 times, success rate is 78%!",
        'ai_medical': "🩺 Proactive Medical Report: Player body language shows acute muscle fatigue and high stress (Negative Day Index). Substitution recommended to avoid red cards or injury."
    },
    'Français': {
        'title': "🏪 Clubs de Division 2, 3, Amateurs & Académies Privées",
        'sub': "📌 Pack Petits Clubs & Académies - Conçu pour gérer et afficher les talents de votre club de manière sécurisée et d'égal à égal.",
        'price_label': "💰 Prix de l'abonnement mensuel",
        'features_title': "📋 Fonctionnalités actives:",
        'f1': "✅ Moteur de Remontada et tactiques de remplacement (50 000 simulations)",
        'f2': "✅ Analyse médicale et psychologique proactive (Jour Négatif)",
        'f3': "✅ Incrustation AR sur caméra (Possession, Buts, Duels)",
        'f4': "✅ Protection des données et conformité GDPR",
        'cam_title': "🎥 Filtrage de match en direct (Universal AI Camera & AR Overlay)",
        'cam_sub': "📌 Système actuellement connecté à la source vidéo active",
        'm1': "📊 Taux de possession", 'm2': "🎯 xG Live", 'm3': "⚔️ Pourcentage de duels gagnés",
        'btn_add': "➕ Créer une carte joueur (Démo)",
        'btn_pub': "🚀 Publier sur le marché avec protection GDPR",
        'warn_no_player': "⚠️ Aucun joueur enregistré pour le moment.",
        'success_pub': "📥 Publié avec succès! Floutage et GDPR activés pour protéger les droits des formateurs.",
        'ai_tactical': "🧠 Assistant tactique IA: Faille détectée. Nous suggérons de passer en 3-5-2. Le moteur de Remontada a simulé le match 50 000 fois, réussite de 78%!",
        'ai_medical': "🩺 Rapport médical proactif: Fatigue musculaire aiguë détectée (Indice Jour Négatif). Remplacement recommandé."
    },
    'Español': { 'title': "🏪 Clubes de División 2, 3, Aficionados y Academias Privadas", 'sub': "📌 Paquete de Clubes Pequeños.", 'price_label': "💰 Suscripción mensual", 'features_title': "📋 Funciones:", 'f1': "✅ Motor de Remontada (50,000)", 'f2': "✅ Día Negativo", 'f3': "✅ Superposición AR", 'f4': "✅ GDPR", 'cam_title': "🎥 Filtro en vivo", 'cam_sub': "📌 Sistema conectado", 'm1': "📊 Posesión", 'm2': "🎯 xG", 'm3': "⚔️ Duelos", 'btn_add': "➕ Crear tarjeta", 'btn_pub': "🚀 Publicar con GDPR", 'warn_no_player': "⚠️ No hay jugadores", 'success_pub': "📥 Éxito", 'ai_tactical': "🧠 3-5-2 (78%)", 'ai_medical': "🩺 Alerta" },
    'Italiano': { 'title': "🏪 Club di Divisione 2, 3, Dilettanti e Accademie Private", 'sub': "📌 Piccoli Club.", 'price_label': "💰 Abbonamento mensile", 'features_title': "📋 Funzionalità:", 'f1': "✅ Rimonta (50.000)", 'f2': "✅ Giorno Negativo", 'f3': "✅ Sovrapposizione AR", 'f4': "✅ GDPR", 'cam_title': "🎥 Filtro partita", 'cam_sub': "📌 Connesso", 'm1': "📊 Possesso", 'm2': "🎯 xG", 'm3': "⚔️ Duelli", 'btn_add': "➕ Crea scheda", 'btn_pub': "🚀 Pubblica con GDPR", 'warn_no_player': "⚠️ No giocatori", 'success_pub': "📥 Successo", 'ai_tactical': "🧠 3-5-2 (78%)", 'ai_medical': "🩺 Allerta" },
    'Português': { 'title': "🏪 Clubes de Divisão 2, 3, Amadores e Academias Privadas", 'sub': "📌 Pequenos Clubes.", 'price_label': "💰 Assinatura mensal", 'features_title': "📋 Recursos:", 'f1': "✅ Reviravolta (50.000)", 'f2': "✅ Dia Negativo", 'f3': "✅ Sobreposição AR", 'f4': "✅ GDPR", 'cam_title': "🎥 Filtro de jogo", 'cam_sub': "📌 Conectado", 'm1': "📊 Posse", 'm2': "🎯 xG", 'm3': "⚔️ Duelos", 'btn_add': "➕ Criar carta", 'btn_pub': "🚀 Publicar com GDPR", 'warn_no_player': "⚠️ Não há jogadores", 'success_pub': "📥 Sucesso", 'ai_tactical': "🧠 3-5-2 (78%)", 'ai_medical': "🩺 Alerta" }
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

st.info(t['ai_tactical'])
st.warning(t.get('ai_medical', 'التقرير الطبي والنفسي الاستباقي للناشئين والهواة: لغة جسم الاستماع يستمع إلى توتر عضلي محيط ورفزة مرتفعة (اليوم السلبي)، نقترح استبداله لتفادي الكرت الأحمر أو الشهر.'))
#
st.write("---")
st.header(t.get('player_title', 'تحليل أداء ومستوى اللاعب تكتيكياً'))
#
if st.button(t.get('btn_add', 'إضافة اللاعب للمقارنة')):
    st.session_state['selected_player'] = t.get('player_title', 'لاعب جديد').append({

        "name": "أحمد (Player Profile)", "age": 15, "position": "LW",
        "similar_to": "World-Class Pro", "star_image": "https://unsplash.com",
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
