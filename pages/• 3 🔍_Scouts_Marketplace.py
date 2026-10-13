import streamlit as st

st.set_page_config(layout="wide")

selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

P3_TXT = {
    "🇸🇦 العربية": {
        "title": "🔍 لوحة تحكم الكشافين ووكلاء الأندية المعتمدين وسوق صفقات الانتقال الموحد", 
        "price": "💰 ثمن الاشتراك من الخارج: 50 dollar شهرياً للوصول الكامل لتصفح كل اللاعبين (القسم الأول والثاني)", 
        "commission": "🚨 عمولة المنصة الثابتة: يتم اقتطاع عمولة من 5% إلى 10% تلقائياً من القيمة المالية الإجمالية عند إتمام صفقات البيع النهائي أو الإعارة المؤقتة لمنع تخطي المنصة."
    },
    "English": {
        "title": "🔍 Certified Scouts & Club Agents Dashboard & Transfer Market", 
        "price": "💰 Subscription Price: $50/Month for Full Access to Browse All Players (Section 1 & 2)", 
        "commission": "🚨 Platform Transaction Fee: A 5% to 10% commission is automatically deducted from the total value of any completed Sale or Loan transaction."
    },
    "Français": {
        "title": "🔍 Tableau de Bord des Recruteurs & Agents de Clubs (Marché des Transferts)", 
        "price": "💰 Tarif d'abonnement : 50$ / Mois pour un accès total aux profils des joueurs (Section 1 & 2)", 
        "commission": "🚨 Commission de la plateforme : Une commission de 5% à 10% est prélevée automatiquement sur la valeur totale de toute transaction de Vente ou de Prêt."
    },
    "Italiano": {
        "title": "🔍 Pannello di Controllo Scout, Agenti di Club e Mercato Trasferimenti", 
        "price": "💰 Prezzo di abbonamento: $50/Mese per l'accesso completo a tutti i giocatori (Sezione 1 e 2)", 
        "commission": "🚨 Commissione della Piattaforma: Verrà applicata automaticamente una commissione dal 5% al 10% sul valore totale di ogni Vendita o Prestito completato."
    },
    "Español": {
        "title": "🔍 Panel de Control de Cazatalentos, Agentes de Clubes y Mercado de Fichajes", 
        "price": "💰 Precio de suscripción: $50/Mes para acceso completo a todos los jugadores (Sección 1 y 2)", 
        "commission": "🚨 Comisión de la Plataforma: Se deduce automáticamente una comisión del 5% al 10% del valor total en cada transacción de Venta o Préstamo."
    },
    "🇵🇹 Português": {
        "title": "🔍 Painel de Olheiros, Agentes de Clubes Credenciados e Bolsa de Transferências", 
        "price": "💰 Preço de assinatura: $50/Mês para acesso total e navegação de todos os jogadores (Seção 1 e 2)", 
        "commission": "🚨 Taxa de Comissão da Plataforma: Uma taxa de 5% a 10% é deduzida automaticamente do valor total de transações concluídas de Venda ou Empréstimo."
    }
}

lang_key = selected_lang if selected_lang in P3_TXT else "🇸🇦 العربية"
t = P3_TXT[lang_key]

st.title(t["title"])
st.error(t["price"]) # عرض ثمن باقة الـ 50 دولار علناً من الخارج
st.success(t["commission"]) # إبراز نسبة عمولة البيع والإعارة لضمان أرباح المنصة أمام جهات التمويل

st.write("---")

st.markdown("### 🚀 بورصة الانتقالات والصفقات الحية الموحدة (القسم الأول + القسم الثاني)")
st.selectbox("فلترة فرز وتصفح مجموعات اللاعبين حسب الفئة السنية والمركز:", ["كل اللاعبين في المنظومة", "القسم الأول: الناشئون والقصر (إلى حدود 20 سنة)", "القسم الثاني: اللاعبون الكبار سينيور"])
st.selectbox("تصفح البورصة حسب نوع العقد التجاري المطلوب:", ["كل عقود صفقات اللاعبين", "معروض للبيع النهائي (For Sale)", "متاح للإعارة المؤقتة (For Loan)"])

# بيانات الجدول المحمية والمغبشة للكشافين تماشياً مع طلبك الصارم لغرض الشراء والبيع والإعارة مع تفعيل التغبيش العام
market_data = [
    {"رمز اللاعب المشفر (ID)": "YOUTH_TALENT_#992", "القسم المستهدف": "القسم الأول (15 سنة)", "حالة العقد والطلب في البورصة": "متاح للإعارة المؤقتة (For Loan)", "أقرب تشبيه عالمي مطابق": "Lamine Yamal", "السرعة": "87%", "دقة التمركز والالتحام": "74%", "عنصر التغبيش وحماية المعطيات": "🔒 Blurred (مغشّى)"},
    {"ID المشفر للمحترف": "SENIOR_PRO_#402", "القسم المستهدف": "القسم الثاني (24 سنة)", "حالة العقد والطلب في البورصة": "معروض للبيع الفوري (For Sale)", "أقرب تشبيه عالمي مطابق": "Kylian Mbappé", "السرعة": "94%", "دقة التمركز والالتحام": "88%", "عنصر التغبيش وحماية المعطيات": "🔒 Blurred (مغشّى)"},
    {"ID المشفر للحارس": "YOUTH_GK_#114", "القسم المستهدف": "القسم الأول (17 سنة)", "حالة العقد والطلب في البورصة": "معروض للبيع الفوري (For Sale)", "أقرب تشبيه عالمي مطابق": "Gianluigi Donnarumma", "السرعة": "65%", "دقة التمركز والالتحام": "89%", "عنصر التغبيش وحماية المعطيات": "🔒 Blurred (مغشّى)"}
]

st.write("---")
st.dataframe(market_data, use_container_width=True)

st.markdown("""
<div style="background-color:#2a2a2a; padding:12px; border-radius:8px; margin-top:15px; border-right:4px solid #ffcc00;">
    <p style="color:#ffcc00; font-size:13px; margin:0;">
        📌 <b>تنبيه إداري وأمني للكشافين والوكلاء:</b> وجوه كافة اللاعبين والحراس في القسمين الأول والثاني تظهر بعنصر التغبيش الرقمي التلقائي التام 
        حماية للمعطيات الشخصية الدولية. يتم فك التغبيش رقمياً وبشكل رسمي بمجرد تقديم النادي لعرض مالي جدي وقبوله من اللاعب أو وليه 
        عبر الحساب الآمن لضمان وتوثيق عمولة المنصة المذكورة أعلاه.
    </p>
</div>
""", unsafe_allow_html=True)
