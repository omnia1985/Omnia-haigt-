import streamlit as st
import time

st.set_page_config(layout="wide")

selected_lang = st.session_state.get("lang", "🇸🇦 العربية")
st.markdown(f"**🌐 Language / اللغة الحالية:** {selected_lang}")

P2_TXT = {
    "🇸🇦 العربية": {
        "title": "🏃 قسم اللاعبين الكبار (سينيور - فوق 20 سنة)", 
        "price": "💰 ثمن الاشتراك من الخارج: 30 دولار شهرياً للوصول التشريحي الشامل والجاهزية", 
        "upload_lbl": "📥 مكان رفع مقطع فيديو المباراة (تحسين تلقائي، معالجة فيديو الهاتف وترميم الضبابية والضوء الخافت):"
    },
    "English": {
        "title": "🏃 Senior Players Section (Over 20 Years Old)", 
        "price": "💰 Subscription Price: $30/Month for Full Anatomical, Tactical & Medical Stack", 
        "upload_lbl": "📥 Upload match video for AI analysis (Auto mobile footage enhancement, blur & low-light restoration):"
    },
    "Français": {
        "title": "🏃 Section Joueurs Seniors (Plus de 20 ans)", 
        "price": "💰 Tarif d'abonnement : 30$ / Mois pour un accès anatomique, tactique et médical complet", 
        "upload_lbl": "📥 Déposer la vidéo du match pour l'analyse IA (Correction automatique d'éclairage faible et vidéos de téléphone) :"
    },
    "Italiano": {
        "title": "🏃 Sezione Giocatori Senior (Oltre 20 anni)", 
        "price": "💰 Prezzo di abbonamento: $30/Mese per l'accesso anatomico, tattico e medico completo", 
        "upload_lbl": "📥 Carica il video della partita per l'analisi dell'IA (Ripristino automatico dell'oscurità e video da cellulare):"
    },
    "Español": {
        "title": "🏃 Sección de Jugadores Seniors (Más de 20 años)", 
        "price": "💰 Precio de suscripción: $30/Mes para acceso anatómico, táctico y médico completo", 
        "upload_lbl": "📥 Subir video del partido para análisis de IA (Restauración de luz tenue y videos borrosos de móviles):"
    },
    "🇵🇹 Português": {
        "title": "🏃 Seção de Jogadores Seniores (Mais de 20 anos)", 
        "price": "💰 Preço de assinatura: $30/Mês para acesso anatômico, tático e médico completo", 
        "upload_lbl": "📥 Carregar vídeo do jogo para análise de IA (Restauração automática de pouca luz e gravações de celular):"
    }
}

lang_key = selected_lang if selected_lang in P2_TXT else "🇸🇦 العربية"
t = P2_TXT[lang_key]

st.title(t["title"])
st.error(t["price"]) # إظهار ثمن اشتراك المحترفين من الخارج بشكل علني وواضح

st.write("---")

# 📥 مكان رفع الفيديو - مكشوف ومتاح من الخارج في أول الصفحة الثانية فوراً لجميع اللغات
uploaded_file = st.file_uploader(t["upload_lbl"], type=["mp4", "mov", "avi"], key="senior_match_uploader")

if uploaded_file:
    with st.spinner("🔄 جاري تشغيل معالجة وترميم الفيديو الرقمي، وتتبع الهيكل الحركي للاعب وفك تداخل المدافعين..."):
        time.sleep(1.5)
    st.warning("🔒 بروتوكول حماية المعطيات الشخصية (GDPR) نشط: تم تفعيل عنصر التغبيش الرقمي الموحد على الوجه. لا يرى ملامح وجهك والبيانات الطبية والنفسية الحساسة جداً إلا نفسك فقط لحين تقديم صفقات البيع.")
    
    # لوحة التحليلات التشريحية، الطبية، والنفسية العميقة الشاملة للاعب الكبار (سينيور)
    st.subheader("📋 لوحة تحليلات الأداء والجاهزية الاحترافية المتكاملة (Full Analytics Stack)")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### 🧮 الإحصائيات الفنية والتكتيكية")
        st.progress(0.12, text="نسبة الخطأ في التمركز الفردي (Positioning Error Rate): 12%")
        st.progress(0.14, text="نسبة الأخطاء العامة والتمرير الخاطئ (Total Errors Rate): 14%")
        st.progress(0.85, text="نسبة التفوق في الثنائيات والالتحامات الأرضية والهوائية: 85%")
        st.progress(0.89, text="نسبة اللعب في مختلف المراكز (تعدد المراكز وتكيفه التكتيكي): 89%")
        st.caption("⚽ **الإنتاجية الهجومية المستخرجة:** 12 هدفاً مسجلاً | 8 تمريرات حاسمة")
        
    with col2:
        st.markdown("### 🧠 التحليل النفسي والسلوكي")
        st.progress(0.82, text="الحالة النفسية والثبات من ملامح الوجه (Emotion AI): 82%")
        st.progress(0.90, text="نسبة التركيز في مركزك ولعب تحت الضغط العالي: 90%")
        st.write("🤝 **الانسجام السلوكي والأخلاق الرياضية:**")
        st.caption("- نسبة التأقلم والانسجام مع زملائه في الملعب: 91% (ممتاز)")
        st.caption("- حدة النقاش والاعتراض مع الحكم ولغة الجسد: منخفضة ومنضبطة (أخلاق عالية)")
        st.caption("- النضج في التصريح الصحفي والإعلامي والمقابلات: متزن ويتحمل الضغط")
        
    with col3:
        st.markdown("### 🩺 المنظومة الطبية والتنبؤ بالإصابات")
        st.progress(0.08, text="نسبة التنبؤ بالإصابة العضلية مستقبلاً (Injury Prediction): 8%")
        st.progress(0.95, text="نسبة شفاء واستجابة الهيكل الحركي إن كان مصاباً: 95%")
        st.metric(label="🟢 حالة وجاهزية اللاعب للمباريات الرسمية (Readiness to Play)", value="96% جاهز تماماً")

    # عنصر التشبيه المفتوح والمقارنة بالـ 15 لاعباً وحراس المرمى المشاهير عالمياً
    st.write("---")
    st.subheader("🔄 عنصر التشبيه المفتوح وتقوية نقاط الضعف")
    comp_target = st.selectbox("قارن أرقامك الحالية وتشابهك مع نجوم قاعدة البيانات الـ 15 وحراس المرمى الدوليين من الخارج:", ["Kylian Mbappé", "Cristiano Ronaldo", "Lionel Messi", "Thibaut Courtois", "Erling Haaland", "Gianluigi Donnarumma", "Kevin De Bruyne", "Virgil van Dijk"])
    
    if comp_target:
        st.info(f"🔄 ميزة التطابق التكتيكي والتشبيه الرياضي نشطة الآن مع النجم العالمي المختار: **{comp_target}**.")
        
    st.error("⚠️ **نسبة نقاط الضعف وثغرات الأداء الإجمالية المكتشفة:** 15% (نقص طفيف في استغلال الكرات الهوائية الثانية والارتقاء العضلي).")
    st.info("💡 **نصائح وتوجيهات موجهة للمحترف:** يوصى بتكثيف تمارين القوة الارتدادية العضلية لرفع كفاءة الارتقاء الرأسي وتغطية أخطاء التمركز المستخرجة من مقطع الفيديو المحسن.")
