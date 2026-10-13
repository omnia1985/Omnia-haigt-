import streamlit as st

st.set_page_config(page_title="Omnia DeepArena IA", layout="wide")

# القاموس المركزي لست لغات والأعلام لجميع الصفحات والباقات علناً من الخارج
LANG_DATA = {
    "🇸🇦 العربية": {
        "welcome": "⚽ مرحباً بك في منصة Omnia DeepArena الرقمية الموحدة لكشافي الملاعب وسوق الانتقالات العالمية",
        "info": "← يرجى تصفح الأقسام والانتقال بين الصفحات الثلاث المتاحة عبر القائمة الجانبية (Sidebar) على هاتفك.",
        "headline": "🏟️ باقات الاشتراك المتاحة علناً من الخارج (Pricing Plans):",
        "p1_nav": "1️⃣ الصفحة الأولى: باقة الناشئين والأطفال (20 دولار شهرياً / مجاناً للأكاديميات الصغيرة للأطفال دون 16 سنة)",
        "p2_nav": "2️⃣ الصفحة الثانية: باقة اللاعبين الكبار وسينيور (30 دولار شهرياً للوصول التشريحي الشامل)",
        "p3_nav": "3️⃣ الصفحة الثالثة: باقة الكشافين ووكلاء الأندية وسوق الانتقالات (50 دولار شهرياً مع عمولات صفقات البيع والإعارة)"
    },
    "🇬🇧 English": {
        "welcome": "⚽ Welcome to Omnia DeepArena Unified Scouting & Global Transfer Marketplace Platform",
        "info": "← Please navigate through the 3 available pages via the Sidebar on your phone.",
        "headline": "🏟️ Public Subscription Plans & Pricing (Visible from Outside):",
        "p1_nav": "1️⃣ Page 1: Youth & Minors Package ($20/Month / Fully FREE for Small Children's Academies Under 16)",
        "p2_nav": "2️⃣ Page 2: Senior Players Package ($30/Month for Full Anatomical & Tactical Stack)",
        "p3_nav": "3️⃣ Page 3: Certified Scouts, Club Agents & Transfer Market ($50/Month with Sale/Loan Commissions)"
    },
    "🇫🇷 Français": {
        "welcome": "⚽ Bienvenue sur la plateforme unifiée de recrutement mondial Omnia DeepArena",
        "info": "← Veuillez naviguer à travers les 3 pages disponibles via le menu latéral de votre téléphone.",
        "headline": "🏟️ Tarifs et Offres d'Abonnement Publics (Visibles de l'extérieur) :",
        "p1_nav": "1️⃣ Page 1: Offre Jeunes & Mineurs (20$ / Mois / Entièrement GRATUIT pour les petites académies d'enfants < 16 ans)",
        "p2_nav": "2️⃣ Page 2: Offre Joueurs Seniors (30$ / Mois pour un accès anatomique et tactique complet)",
        "p3_nav": "3️⃣ Page 3: Offre Recruteurs, Agents & Marché des Transferts (50$ / Mois avec commissions sur Ventes/Prêts)"
    },
    "🇮🇹 Italiano": {
        "welcome": "⚽ Benvenuto sulla piattaforma unificata di scouting mondiale Omnia DeepArena",
        "info": "← Si prega di navigare attraverso le 3 pagine disponibili tramite il menu laterale sul telefono.",
        "headline": "🏟️ Piani di Abbonamento Pubblici e Prezzi (Visibili dall'esterno):",
        "p1_nav": "1️⃣ Pagina 1: Pacchetto Giovani e Minori ($20/Mese / Completamente GRATUITO per piccole accademie sotto i 16 anni)",
        "p2_nav": "2️⃣ Pagina 2: Pacchetto Giocatori Senior ($30/Mese per l'accesso anatomico e tattico completo)",
        "p3_nav": "3️⃣ Pagina 3: Pacchetto Scout, Agenti e Mercato dei Trasferimenti ($50/Mese con commissioni su Vendite/Prestiti)"
    },
    "🇪🇸 Español": {
        "welcome": "⚽ Bienvenido a la plataforma unificada de ojeadores globales Omnia DeepArena",
        "info": "← Por favor, navegue a través de las 3 páginas disponibles via el menú lateral en su teléfono.",
        "headline": "🏟️ Planes de Suscripción Públicos y Tarifas (Visibles desde el exterior):",
        "p1_nav": "1️⃣ Página 1: Paquete Juvenil y Menores ($20/Mes / Totalmente GRATIS para pequeñas academias de niños < 16 años)",
        "p2_nav": "2️⃣ Página 2: Paquete Jugadores Seniors ($30/Mes para acceso anatómico y táctico completo)",
        "p3_nav": "3️⃣ Página 3: Paquete Cazatalentos, Agentes y Mercado de Fichajes ($50/Mes con comisiones de Venta/Préstamo)"
    },
    "🇵🇹 Português": {
        "welcome": "⚽ Bem-vindo à plataforma unificada de olheiros globais Omnia DeepArena",
        "info": "← Por favor, navegue pelas 3 páginas disponíveis através do menu lateral no seu telefone.",
        "headline": "🏟️ Planos de Assinatura Públicos e Preços (Visíveis do exterior):",
        "p1_nav": "1️⃣ Página 1: Pacote Juvenil e Menores ($20/Mês / Totalmente GRATUITO para pequenas academias de crianças < 16 anos)",
        "p2_nav": "2️⃣ Página 2: Pacote Jogadores Seniores ($30/Mês para acesso anatômico e tático completo)",
        "p3_nav": "3️⃣ Página 3: Pacote Olheiros, Agentes e Mercado de Transferências ($50/Mês com comissões de Venda/Empréstimo)"
    }
}

# شريط اختيار اللغة والأعلام العلوي العام والموحد لجميع شاشات التطبيق
st.markdown("### 🌐 Select Language / اختر اللغة")
selected_lang = st.selectbox("", list(LANG_DATA.keys()), label_visibility="collapsed")

# حفظ الاختيار في الجلسة لضمان التزامن الكامل عبر الصفحات الفرعية
st.session_state["lang"] = selected_lang

tx = LANG_DATA[selected_lang]

# تصميم الواجهة الرئيسية الجميلة والبارزة
st.title(tx["welcome"])
st.info(tx["info"])
st.write("---")

st.markdown(f"### {tx['headline']}")
st.success(tx["p1_nav"])
st.info(tx["p2_nav"])
st.warning(tx["p3_nav"])

st.markdown("""
<div style="background-color:#1e1e1e; padding:15px; border-radius:10px; border-left:5px solid #00ffcc; margin-top:20px;">
    <h4 style="color:#00ffcc; margin:0;">💡 ملاحظة استثمارية للمستثمرين (VMS / Brinc / BTS):</h4>
    <p style="color:#ffffff; font-size:14px; margin-top:5px;">
        تعتمد المنصة على نظام حماية المعطيات الشخصية الصارم بتفعيل عنصر التغبيش الرقمي لوجوه جميع اللاعبين، 
        مع معالجة متطورة لترميم الفيديوهات الرديئة وضبط الضوء الخافت وفيديو الهاتف لضمان دقة التحليل الفني والنفسي والطبي.
    </p>
</div>
""", unsafe_allow_html=True)
