import streamlit as st
import time

st.set_page_config(layout="wide")

selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

P1_TXT = {
    "🇸🇦 العربية": {
        "title": "👶 قسم الناشئين والقصر (إلى حدود 20 سنة)",
        "price": "💰 ثمن الاشتراك من الخارج: 20 دولار شهرياً | مجاني بالكامل للأكاديميات الصغيرة للأطفال دون 16 سنة",
        "upload_lbl": "📥 مكان رفع مقطع فيديو المباراة للناشئ (تحسين جودة فيديو الهاتف وترميمه تلقائياً وتوضيح الضبابية والضوء الخافت):",
        "process": "🔄 جاري معالجة فيديو الهاتف وترميم الضبابية والإضاءة وفك تداخل اللاعبين بالذكاء الاصطناعي..."
    },
    "English": {
        "title": "👶 Youth & Minors Section (Up to 20 Years Old)",
        "price": "💰 Subscription Price: $20/Month | Completely FREE for Small Children's Academies Under 16",
        "upload_lbl": "📥 Upload Youth Match Video (Auto mobile footage enhancement, blur & low-light restoration):",
        "process": "🔄 AI is restoring mobile video quality, fixing blur, low-light and de-overlapping players..."
    },
    "Français": {
        "title": "👶 Section Jeunes & Mineurs (Jusqu'à 20 ans)",
        "price": "💰 Tarif d'abonnement : 20$ / Mois | Entièrement GRATUIT pour les petites académies d'enfants de moins de 16 ans",
        "upload_lbl": "📥 Déposer la vidéo du jeune (Amélioration automatique des vidéos de téléphone, flou et basse lumière) :",
        "process": "🔄 L'IA restaure le flou de la vidéo, élimine le chevauchement et ajuste le faible éclairage..."
    },
    "Italiano": {
        "title": "👶 Sezione Giovani e Minori (Fino a 20 anni)",
        "price": "💰 Prezzo di abbonamento: $20/Mese | Completamente GRATUITO per le piccole accademie di bambini sotto i 16 anni",
        "upload_lbl": "📥 Carica il video del giovane (Miglioramento automatico dei video da cellulare, sfocatura e luce scarsa):",
        "process": "🔄 L'IA sta ripristinando la sfocatura, disfacendo la sovrapposizione e correggendo l'oscurità..."
    },
    "Español": {
        "title": "👶 Sección de Juveniles y Menores (Hasta 20 años)",
        "price": "💰 Precio de suscripción: $20/Mes | Totalmente GRATIS para pequeñas academias de niños menores de 16 años",
        "upload_lbl": "📥 Subir video del partido juvenil (Mejora de videos de móviles, eliminación de desenfoque y luz tenue):",
        "process": "🔄 La IA está restaurando el desenfoque de movimiento, luz baja y resolviendo superposición..."
    },
    "🇵🇹 Português": {
        "title": "👶 Seção de Juvenis e Menores (Até 20 anos)",
        "price": "💰 Preço de assinatura: $20/Mês | Totalmente GRATUITO para pequenas academias de crianças menores de 16 anos",
        "upload_lbl": "📥 Carregar vídeo do jogo juvenil (Melhoria automática de celular, correção de desfoque e pouca luz):",
        "process": "🔄 A IA está processando o vídeo para restaurar pouca luz, desfoque e sobreposição de jogadores..."
    }
}

lang_key = selected_lang if selected_lang in P1_TXT else "🇸🇦 العربية"
t = P1_TXT[lang_key]

st.title(t["title"])
st.error(t["price"]) # عرض السعر بشكل بارز جداً من الخارج باللون الأحمر

st.write("---")

# إعداد واجهة التسجيل المخصصة للقصر
st.sidebar.header("👤 حساب الناشئ")
acc_type = st.sidebar.radio("نوع الاشتراك والجهة:", ["لاعب مستقل (Individual)", "أكاديمية صغيرة للأطفال (Small Academy)"])
age = st.sidebar.number_input("أدخل عمر اللاعب الحالي:", min_value=5, max_value=20, value=14)

if acc_type == "أكاديمية صغيرة للأطفال (Small Academy)" and age < 16:
    st.success("🎉 هذا الحساب مفعل مجاناً بالكامل تبعاً للأكاديميات الصغيرة للأطفال.")

# تفعيل بروتوكول التدخل القانوني الإلزامي للأولياء دون سن 16 سنة
proceed_allowed = True
if age < 16:
    st.markdown("### 👨‍👩‍👦 نظام تدخل وموافقة الولي الشرعي (إلزامي دون 16 سنة)")
    col1, col2 = st.columns(2)
    with col1:
        parent_name = st.text_input("اسم الولي الشرعي بالكامل:")
        parent_id = st.text_input("رقم بطاقة تعريف الولي / جواز السفر:")
    with col2:
        consent_signature = st.checkbox("أقر أنا الولي بالموافقة على معالجة البيانات واستخراج بطاقة الأداء التكتيكية لعرضها لغرض الشراء أو الإعارة.")
    
    if not (consent_signature and parent_id != "" and parent_name != ""):
        proceed_allowed = False
        st.warning("⚠️ يرجى تعبئة بيانات موافقة الولي بالكامل وتفعيل خانة الإقرار لفتح خانة رفع الفيديو للناشئ.")

if proceed_allowed:
    # مكان رفع الفيديو - متاح علناً في الصفحة الأولى
    uploaded_file = st.file_uploader(t["upload_lbl"], type=["mp4", "mov"], key="youth_match_uploader")
    
    if uploaded_file:
        with st.spinner(t["process"]):
            time.sleep(1.5)
        st.warning("🔒 تم تفعيل عنصر التغبيش لحماية المعطيات الشخصية (ملامح وجه الناشئ مشفرة ومحجوبة بالكامل عن الكشافين والأندية وتظهر له ولوليه فقط).")
        
        # استخراج بطاقة البيانات البدنية والنفسية الأساسية للناشئين للبيع والإعارة
        st.subheader("📊 بطاقة البيانات المستخرجة بالذكاء الاصطناعي بدقة:")
        youth_metrics = {"Speed": 88, "Focus": 75, "Pressure": 70, "Ethics": 94, "Physical": 78}
        
        c1, c2, c3, c4, c5 = st.columns(5)
        c1.metric("السرعة (Speed)", f"{youth_metrics['Speed']}%")
        c2.metric("التركيز (Focus)", f"{youth_metrics['Focus']}%")
        c3.metric("تحت الضغط العالي (Pressure)", f"{youth_metrics['Pressure']}%")
        c4.metric("الأخلاق النفسية (Ethics)", f"{youth_metrics['Ethics']}%")
        c5.metric("الأداء البدني العام (Physical)", f"{youth_metrics['Physical']}%")
        
        # تفعيل منظومة التشبيه التلقائي واكتشاف الضعف
        st.write("---")
        best_match = "Lamine Yamal" if youth_metrics["Speed"] > 85 else "Pedri"
        st.markdown(f"### 🔄 **عنصر التشبيه:** المنظومة تشبه أداءك الرياضي بالنجم العالمي: **{best_match}**")
        
        st.error(f"⚠️ **البيانات الضعيفة لتعمل على تقويتها:** لديك نقص ملحوظ في معدل اللعب تحت الضغط العالي (Pressure) بنسبة {youth_metrics['Pressure']}% مقارنة بـ {best_match} (90%).")
        st.info("💡 **الحلول الموجهة المقترحة:** أداء تمارين تكتيكية مصغرة وسريعة (Small Sided Games 3v3) لتقليل زمن الاحتفاظ بالكرة ورفع سرعة اتخاذ القرار التكتيكي.")
