import streamlit as st

# إعدادات الصفحة
st.set_page_config(
    page_title="TikTok - النسخة الاحترافية بالذكاء الاصطناعي",
    page_icon="📱",
    layout="centered"
)

# تصميم CSS كامل ومطابق لتيك توك مع نظام الأزرار العلوية والسفلية
st.markdown("""
    <style>
        #MainMenu {visibility: hidden;}
        footer {visibility: hidden;}
        header {visibility: hidden;}
        .stApp { background-color: #000000; color: #ffffff; font-family: sans-serif; }

        /* زرار الصوت العلوي في الكاميرا */
        .sound-btn-box {
            position: absolute;
            top: 20px;
            left: 50%;
            transform: translateX(-50%);
            z-index: 100;
        }

        .user-card {
            background: #121212;
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 10px;
            border: 1px solid #222;
        }
        
        .banned-box {
            background: #ff2c55;
            padding: 15px;
            border-radius: 10px;
            text-align: center;
            color: white;
            font-weight: bold;
        }
    </style>
""", unsafe_allow_html=True)

# إدارة حالة التطبيق (Session State)
if "current_page" not in st.session_state:
    st.session_state.current_page = "الرئيسية"

if "feed_videos" not in st.session_state:
    st.session_state.feed_videos = [
        {"user": "@mohamed_dev", "desc": "أقوى تحدي برمجي بلغة بايثون 🔥 #تيك_توك", "video": "https://www.w3schools.com/html/mov_bbb.mp4", "sound": "🎵 الصوت الأصلي - M.Elmezahy"}
    ]

if "banned_users" not in st.session_state:
    st.session_state.banned_users = ["@bad_user99", "@hacker_x"]

# --- كلمات ممنوعة للرقابة التلقائية وحظر الحسابات المخالفة ---
FORBIDDEN_WORDS = ["عيب", "حاجة وحشة", "إباحي", "18+", "shame", "bad_word", "hentai", "porn"]

def check_content_safety(username, text_desc):
    """دالة فحص المحتوى وحظر الحسابات المخالفة تلقائياً"""
    for word in FORBIDDEN_WORDS:
        if word in text_desc.lower():
            # حظر الحساب فوراً وإضافته لقائمة الحظر
            if username not in st.session_state.banned_users:
                st.session_state.banned_users.append(username)
            return False
    return True

# تحقق مما إذا كان المستخدم الحالي محظوراً
current_user = "@user3413067904409"
if current_user in st.session_state.banned_users:
    st.markdown("""
        <div style='margin-top: 100px;'>
            <div class='banned-box'>
                🚨 عذراً! تم حظر حسابك نهائياً بسبب انتهاك معايير المجتمع والأخلاق العامة.
            </div>
        </div>
    """, unsafe_allow_html=True)
    st.stop()


# --- صفحات التطبيق ---
if st.session_state.current_page == "الرئيسية":
    # الهيدر العلوي
    top_col1, top_col2, top_col3 = st.columns([1, 6, 1])
    with top_col1:
        st.write("🔍")
    with top_col2:
        st.markdown("<div style='text-align: center; color: #fff; font-weight: bold;'>المجتمع &nbsp;|&nbsp; أتابعه &nbsp;|&nbsp; <span style='color: #fe2c55;'>لك</span></div>", unsafe_allow_html=True)
    with top_col3:
        st.write("📺")

    st.markdown("---")
    
    # عرض الفيديوهات المتاحة في الفيد
    for item in st.session_state.feed_videos:
        st.video(item["video"])
        st.markdown(f"**{item['user']}**")
        st.write(item["desc"])
        st.markdown(f"<span style='color: #25f4ee; font-size: 12px;'>{item['sound']}</span>", unsafe_allow_html=True)
        st.markdown("---")

elif st.session_state.current_page == "الأصدقاء":
    st.markdown("<h3 style='text-align: right;'>الأصدقاء</h3>", unsafe_allow_html=True)
    story_cols = st.columns(4)
    with story_cols[0]:
        st.markdown("🔴 **الأعرابي**")
    with story_cols[1]:
        st.markdown("🔵 **BaSOMa**")
    with story_cols[2]:
        st.markdown("💎 **N**")
    with story_cols[3]:
        st.markdown("➕ **إنشاء**")
    st.markdown("---")
    st.info("تابع أصدقاءك وتفاعل مع فيديوهاتهم اليومية مباشرة!")

elif st.session_state.current_page == "إضافة/كاميرا":
    st.markdown("<h3 style='text-align: center; color: #fe2c55;'>كاميرا تيك توك الفورية 🎬</h3>", unsafe_allow_html=True)
    
    # --- زرار إضافة الصوت فوق الكاميرا بالظبط زي التيك توك ---
    selected_sound = st.selectbox(
        "🎵 اختر الصوت أو الأغنية للفيديو:",
        [
            "🎧 تريند مصر الأول - تيك توك 2026",
            "🔥 ريمكس حماسي - رقص وفلاتر",
            "🎸 هدوء وروقان - غيتار تركي",
            "🚀 مهرجان السرعة والأكشن"
        ]
    )

    camera_file = st.camera_input("التقط لقطتك الآن")
    
    video_desc = st.text_input("اكتب وصف الفيديو أو الـ Hashtag:")
    
    if st.button("نشر الفيديو للعامة 🚀"):
        if camera_file:
            # تشغيل نظام الرقابة والفحص الأخلاقي
            is_safe = check_content_safety(current_user, video_desc)
            
            if not is_safe:
                st.error("🚨 تم رفض الفيديو وحظر الحساب! محتواك يحتوي على كلمات أو إيحاءات مخالفة للأخلاق.")
                st.rerun()
            else:
                # إضافة الفيديو بنجاح لو آمن ومحترم
                st.session_state.feed_videos.insert(0, {
                    "user": current_user,
                    "desc": video_desc if video_desc else "فيديو جديد بدون وصف #تيك_توك",
                    "video": "https://www.w3schools.com/html/mov_bbb.mp4",
                    "sound": selected_sound
                })
                st.success("تم نشر الفيديو بنجاح في الصفحة الرئيسية! 🎉")

elif st.session_state.current_page == "صندوق الوارد":
    st.markdown("<h3 style='text-align: right;'>صندوق الوارد 📥</h3>", unsafe_allow_html=True)
    st.markdown("""
    <div class="user-card">
        <b>👥 متابعون جدد</b><br><span style='color: #aaa; font-size: 12px;'>Muhammad بدأ في متابعتك.</span>
    </div>
    <div class="user-card">
        <b>🛡️ نظام الرقابة والسياسة</b><br><span style='color: #25f4ee; font-size: 12px;'>تم حماية المجتمع وحظر الحسابات المخالفة بنجاح.</span>
    </div>
    """, unsafe_allow_html=True)

elif st.session_state.current_page == "الملف الشخصي":
    st.markdown("<h3 style='text-align: center;'>@user3413067904409</h3>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("<div style='text-align: center;'><b>1</b><br>أتابعه</div>", unsafe_allow_html=True)
    with col2:
        st.markdown("<div style='text-align: center;'><b>2</b><br>متابعون</div>", unsafe_allow_html=True)
    with col3:
        st.markdown("<div style='text-align: center;'><b>4</b><br>تسجيلات الإعجاب</div>", unsafe_allow_html=True)
        
    st.info("✏️ نظام الأمان والحماية الذكية مفعل على حسابك.")
    st.markdown("---")
    st.write("📂 الفيديوهات المنشورة الخاصة بك:")
    st.success("حسابك نظيف وآمن تماماً.")

# --- شريط التنقل السفلي الثابت ---
st.markdown("<br><br>", unsafe_allow_html=True)
nav1, nav2, nav3, nav4, nav5 = st.columns(5)

with nav1:
    if st.button("🏠 الرئيسية"):
        st.session_state.current_page = "الرئيسية"
        st.rerun()
with nav2:
    if st.button("👥 أصدقاء"):
        st.session_state.current_page = "الأصدقاء"
        st.rerun()
with nav3:
    if st.button("＋ 🎬"):
        st.session_state.current_page = "إضافة/كاميرا"
        st.rerun()
with nav4:
    if st.button("📥 الوارد"):
        st.session_state.current_page = "صندوق الوارد"
        st.rerun()
with nav5:
    if st.button("👤 الملف الشخصي"):
        st.session_state.current_page = "الملف الشخصي"
        st.rerun()
