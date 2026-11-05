"""
build_team_roles_deck.py
Generates a dedicated, highly polished PowerPoint presentation
explaining the 5 team roles and task breakdown for the Tawazon graduation project.
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE

# ── Color Palette ─────────────────────────────────────────────────────────────
C_BG_DARK     = RGBColor(15, 23, 42)      # #0f172a
C_CARD_DARK   = RGBColor(30, 41, 59)      # #1e293b
C_BG_LIGHT    = RGBColor(248, 250, 252)   # #f8fafc
C_CARD_WHITE  = RGBColor(255, 255, 255)   # #ffffff
C_BORDER      = RGBColor(226, 232, 240)   # #e2e8f0
C_TEXT_DARK   = RGBColor(15, 23, 42)      # #0f172a
C_TEXT_MUTED  = RGBColor(100, 116, 139)   # #64748b

# Role Identity Colors
C_ROLE1_BLUE   = RGBColor(37, 99, 235)     # ML & Data
C_ROLE2_PURPLE = RGBColor(124, 58, 237)    # XAI & Risk Engine
C_ROLE3_GREEN  = RGBColor(5, 150, 105)     # Backend & Security
C_ROLE4_AMBER  = RGBColor(217, 119, 6)     # Frontend & Localization
C_ROLE5_CYAN   = RGBColor(8, 145, 178)     # Analytics & QA

SLIDE_W = Inches(13.333)
SLIDE_H = Inches(7.5)
FONT_NAME = "Calibri"

def create_presentation():
    prs = Presentation()
    prs.slide_width = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs

def blank_slide(prs):
    return prs.slides.add_slide(prs.slide_layouts[6])

def add_rect(slide, left, top, width, height, fill_color=None, line_color=None, line_width=Pt(1)):
    shape = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, left, top, width, height)
    shape.line.width = line_width
    if fill_color:
        shape.fill.solid()
        shape.fill.fore_color.rgb = fill_color
    else:
        shape.fill.background()
    if line_color:
        shape.line.color.rgb = line_color
    else:
        shape.line.fill.background()
    return shape

def add_header(slide, title_ar, title_en, page_num, total_pages=9, accent_color=C_ROLE1_BLUE):
    add_rect(slide, 0, 0, SLIDE_W, Inches(1.15), fill_color=C_BG_DARK, line_color=None)
    add_rect(slide, 0, Inches(1.11), SLIDE_W, Inches(0.04), fill_color=accent_color, line_color=None)
    
    tb = slide.shapes.add_textbox(Inches(0.6), Inches(0.12), Inches(10.5), Inches(0.95))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.margin_left = tf.margin_top = tf.margin_right = tf.margin_bottom = 0
    
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.LEFT
    r = p.add_run()
    r.text = title_ar
    r.font.name = FONT_NAME
    r.font.size = Pt(25)
    r.font.bold = True
    r.font.color.rgb = RGBColor(255, 255, 255)
    
    p2 = tf.add_paragraph()
    p2.alignment = PP_ALIGN.LEFT
    r2 = p2.add_run()
    r2.text = title_en
    r2.font.name = FONT_NAME
    r2.font.size = Pt(13)
    r2.font.color.rgb = RGBColor(148, 163, 184)
    
    # Page indicator pill
    pill = add_rect(slide, Inches(11.5), Inches(0.35), Inches(1.3), Inches(0.42),
                    fill_color=RGBColor(30, 41, 59), line_color=RGBColor(51, 65, 85))
    tb_pg = slide.shapes.add_textbox(Inches(11.5), Inches(0.38), Inches(1.3), Inches(0.35))
    tf_pg = tb_pg.text_frame
    tf_pg.margin_left = tf_pg.margin_top = tf_pg.margin_right = tf_pg.margin_bottom = 0
    p_pg = tf_pg.paragraphs[0]
    p_pg.alignment = PP_ALIGN.CENTER
    r_pg = p_pg.add_run()
    r_pg.text = f"{page_num} / {total_pages}"
    r_pg.font.name = FONT_NAME
    r_pg.font.size = Pt(13)
    r_pg.font.bold = True
    r_pg.font.color.rgb = RGBColor(226, 232, 240)
    
    # Slide base background
    add_rect(slide, 0, Inches(1.15), SLIDE_W, SLIDE_H - Inches(1.15), fill_color=C_BG_LIGHT, line_color=None)
    
    # Footer
    add_rect(slide, 0, SLIDE_H - Inches(0.38), SLIDE_W, Inches(0.38), fill_color=C_CARD_WHITE, line_color=C_BORDER)
    tb_foot = slide.shapes.add_textbox(Inches(0.6), SLIDE_H - Inches(0.35), Inches(12.13), Inches(0.3))
    tf_foot = tb_foot.text_frame
    tf_foot.margin_left = tf_foot.margin_top = tf_foot.margin_right = tf_foot.margin_bottom = 0
    p_foot = tf_foot.paragraphs[0]
    p_foot.alignment = PP_ALIGN.LEFT
    r_foot = p_foot.add_run()
    r_foot.text = "Tawazon Graduation Project  •  دليل التوزيع المعياري لمهام الفريق وشرح الأكواد البرمجية للمناقشة"
    r_foot.font.name = FONT_NAME
    r_foot.font.size = Pt(10)
    r_foot.font.color.rgb = C_TEXT_MUTED

# ── SLIDE 1: COVER ────────────────────────────────────────────────────────────
def build_slide_1(prs):
    sl = blank_slide(prs)
    add_rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_color=C_BG_DARK, line_color=None)
    
    add_rect(sl, Inches(1.2), Inches(1.2), Inches(0.12), Inches(4.8), fill_color=C_ROLE1_BLUE, line_color=None)
    add_rect(sl, Inches(1.2), Inches(1.2), Inches(1.5), Inches(0.08), fill_color=C_ROLE1_BLUE, line_color=None)
    
    tb_tag = sl.shapes.add_textbox(Inches(1.6), Inches(1.2), Inches(10), Inches(0.45))
    tf_tag = tb_tag.text_frame
    p_tag = tf_tag.paragraphs[0]
    r_tag = p_tag.add_run()
    r_tag.text = "TAWAZON PROJECT  •  TEAM ROLES & RESPONSIBILITIES ARCHITECTURE"
    r_tag.font.name = FONT_NAME
    r_tag.font.size = Pt(13)
    r_tag.font.bold = True
    r_tag.font.color.rgb = RGBColor(147, 197, 253)
    
    tb_title = sl.shapes.add_textbox(Inches(1.55), Inches(1.65), Inches(10.5), Inches(1.2))
    tf_title = tb_title.text_frame
    tf_title.word_wrap = True
    p_title = tf_title.paragraphs[0]
    r_title = p_title.add_run()
    r_title.text = "التوزيع المعياري لمهام الفريق وشرح أدوار المناقشة"
    r_title.font.name = FONT_NAME
    r_title.font.size = Pt(36)
    r_title.font.bold = True
    r_title.font.color.rgb = RGBColor(255, 255, 255)
    
    tb_sub = sl.shapes.add_textbox(Inches(1.6), Inches(2.9), Inches(10.5), Inches(0.8))
    tf_sub = tb_sub.text_frame
    p_sub = tf_sub.paragraphs[0]
    r_sub = p_sub.add_run()
    r_sub.text = "توزيع 5 مهام هندسية متكاملة تغطي دورة حياة الذكاء الاصطناعي وهندسة البرمجيات بالكامل"
    r_sub.font.name = FONT_NAME
    r_sub.font.size = Pt(18)
    r_sub.font.color.rgb = RGBColor(34, 197, 94)
    
    p_sub2 = tf_sub.add_paragraph()
    r_sub2 = p_sub2.add_run()
    r_sub2.text = "دليل تفصيلي لكل عضو: المسمى الوظيفي، الملفات البرمجية، وماذا يقول أمام الدكتورة ولجنة التحكيم"
    r_sub2.font.name = FONT_NAME
    r_sub2.font.size = Pt(15)
    r_sub2.font.color.rgb = RGBColor(203, 213, 225)
    
    # 5 Role Badges at bottom
    roles_summary = [
        ("العضو 1", "Machine Learning & Data", C_ROLE1_BLUE),
        ("العضو 2", "XAI & Risk Engine", C_ROLE2_PURPLE),
        ("العضو 3", "Backend & Security", C_ROLE3_GREEN),
        ("العضو 4", "Frontend & UI/UX", C_ROLE4_AMBER),
        ("العضو 5", "Analytics & QA", C_ROLE5_CYAN)
    ]
    for i, (m_id, r_name, col) in enumerate(roles_summary):
        cx = Inches(1.6 + i * 2.1)
        cy = Inches(4.5)
        add_rect(sl, cx, cy, Inches(1.95), Inches(1.5), fill_color=C_CARD_DARK, line_color=RGBColor(51, 65, 85))
        add_rect(sl, cx, cy, Inches(1.95), Inches(0.08), fill_color=col, line_color=None)
        
        tb_b = sl.shapes.add_textbox(cx + Inches(0.1), cy + Inches(0.2), Inches(1.75), Inches(1.1))
        tf_b = tb_b.text_frame
        tf_b.word_wrap = True
        p1 = tf_b.paragraphs[0]
        r1 = p1.add_run()
        r1.text = m_id
        r1.font.name = FONT_NAME
        r1.font.size = Pt(14)
        r1.font.bold = True
        r1.font.color.rgb = col
        
        p2 = tf_b.add_paragraph()
        r2 = p2.add_run()
        r2.text = r_name
        r2.font.name = FONT_NAME
        r2.font.size = Pt(11)
        r2.font.color.rgb = RGBColor(255, 255, 255)

# ── SLIDE 2: OVERVIEW OF TEAM METHODOLOGY ─────────────────────────────────────
def build_slide_2(prs):
    sl = blank_slide(prs)
    add_header(sl, "الهيكل الهندسي لتوزيع مهام الفريق (المعيار الأكاديمي)", "Engineering Workflow & Task Distribution Methodology", 2)
    
    # Top explanation card
    add_rect(sl, Inches(0.8), Inches(1.45), Inches(11.73), Inches(1.2), fill_color=C_CARD_WHITE, line_color=C_BORDER)
    add_rect(sl, Inches(0.8), Inches(1.45), Inches(0.12), Inches(1.2), fill_color=C_ROLE1_BLUE, line_color=None)
    
    tb_top = sl.shapes.add_textbox(Inches(1.1), Inches(1.55), Inches(11.2), Inches(1.0))
    tf_top = tb_top.text_frame
    tf_top.word_wrap = True
    p1 = tf_top.paragraphs[0]
    r1 = p1.add_run()
    r1.text = "🎯 لماذا هذا التقسيم مثالي ويحمي الفريق أمام الدكتورة؟"
    r1.font.name = FONT_NAME
    r1.font.size = Pt(16)
    r1.font.bold = True
    r1.font.color.rgb = C_ROLE1_BLUE
    
    p2 = tf_top.add_paragraph()
    p2.space_before = Pt(4)
    r2 = p2.add_run()
    r2.text = "بعد توجيه الدكتورة بحذف الـ NLP والـ Feedback، لم ينقص دور أي عضو، بل أعدنا هندسة المشروع ليغطي دورة التطوير المتكاملة (Full-Stack AI Lifecycle): من هندسة البيانات والنمذجة، إلى محرك التفسير والرياضيات، إلى حماية الخادم والـ APIs، إلى الواجهات ثنائية اللغة، وحتى تكامل الرسوم البيانية وضمان الجودة."
    r2.font.name = FONT_NAME
    r2.font.size = Pt(12)
    r2.font.color.rgb = RGBColor(51, 65, 85)
    
    # 5 Summary Horizontal Bars
    roles_flow = [
        ("العضو 1", "Machine Learning & Data", "تجهيز 1000 موظف، تقسيم 80/20، وتدريب Random Forest (95.5%)", C_ROLE1_BLUE),
        ("العضو 2", "XAI & Risk Engine", "محرك حساب الخطر الرياضي (0–100) وتفسير الأسباب عبر SHAP", C_ROLE2_PURPLE),
        ("العضو 3", "Backend & API Security", "خادم FastAPI، نماذج Pydantic، وتشفير وصلاحيات JWT & Bcrypt", C_ROLE3_GREEN),
        ("العضو 4", "Frontend & UI/UX", "نظام التصميم الموحد، دعم اللغتين (RTL/LTR)، وتقارير الـ PDF", C_ROLE4_AMBER),
        ("العضو 5", "Analytics & QA Integration", "رسوم Chart.js الحية، لوحة المؤشرات، واختبارات الجودة الشاملة", C_ROLE5_CYAN)
    ]
    
    for i, (m_id, title, desc, col) in enumerate(roles_flow):
        cy = Inches(2.85 + i * 0.8)
        add_rect(sl, Inches(0.8), cy, Inches(11.73), Inches(0.72), fill_color=C_CARD_WHITE, line_color=C_BORDER)
        add_rect(sl, Inches(0.8), cy, Inches(0.1), Inches(0.72), fill_color=col, line_color=None)
        
        # Pill
        add_rect(sl, Inches(1.1), cy + Inches(0.12), Inches(1.2), Inches(0.48), fill_color=col, line_color=None)
        tb_p = sl.shapes.add_textbox(Inches(1.1), cy + Inches(0.16), Inches(1.2), Inches(0.4))
        p_p = tb_p.text_frame.paragraphs[0]
        p_p.alignment = PP_ALIGN.CENTER
        r_p = p_p.add_run()
        r_p.text = m_id
        r_p.font.name = FONT_NAME
        r_p.font.size = Pt(12)
        r_p.font.bold = True
        r_p.font.color.rgb = RGBColor(255, 255, 255)
        
        # Title & Desc
        tb_txt = sl.shapes.add_textbox(Inches(2.45), cy + Inches(0.12), Inches(9.8), Inches(0.5))
        tf_txt = tb_txt.text_frame
        p_t = tf_txt.paragraphs[0]
        r_t = p_t.add_run()
        r_t.text = title + "  —  "
        r_t.font.name = FONT_NAME
        r_t.font.size = Pt(13)
        r_t.font.bold = True
        r_t.font.color.rgb = col
        
        r_d = p_t.add_run()
        r_d.text = desc
        r_d.font.name = FONT_NAME
        r_d.font.size = Pt(12)
        r_d.font.color.rgb = C_TEXT_DARK

# ── HELPER FOR INDIVIDUAL ROLE SLIDES ─────────────────────────────────────────
def build_role_slide(prs, page_num, member_title_ar, member_title_en, accent_color,
                     files_list, tasks_list, speech_text):
    sl = blank_slide(prs)
    add_header(sl, member_title_ar, member_title_en, page_num, 9, accent_color)
    
    # Left Card: Files & Technical Tasks (Width: 6.8 Inches)
    lx = Inches(0.8)
    ly = Inches(1.45)
    lw = Inches(6.8)
    lh = Inches(5.35)
    add_rect(sl, lx, ly, lw, lh, fill_color=C_CARD_WHITE, line_color=C_BORDER)
    add_rect(sl, lx, ly, lw, Inches(0.08), fill_color=accent_color, line_color=None)
    
    tb_l = sl.shapes.add_textbox(lx + Inches(0.25), ly + Inches(0.15), lw - Inches(0.5), lh - Inches(0.3))
    tf_l = tb_l.text_frame
    tf_l.word_wrap = True
    
    # Files Header
    p = tf_l.paragraphs[0]
    r = p.add_run()
    r.text = "📂 الملفات البرمجية المسندة للعضو:"
    r.font.name = FONT_NAME
    r.font.size = Pt(15)
    r.font.bold = True
    r.font.color.rgb = accent_color
    
    for f in files_list:
        pf = tf_l.add_paragraph()
        pf.space_before = Pt(3)
        rf = pf.add_run()
        rf.text = f"✔ {f}"
        rf.font.name = "Consolas"
        rf.font.size = Pt(11)
        rf.font.bold = True
        rf.font.color.rgb = C_TEXT_DARK
        
    # Tasks Header
    pt_h = tf_l.add_paragraph()
    pt_h.space_before = Pt(10)
    rt_h = pt_h.add_run()
    rt_h.text = "⚙️ المسؤوليات والمهام التقنية المنفذة:"
    rt_h.font.name = FONT_NAME
    rt_h.font.size = Pt(15)
    rt_h.font.bold = True
    rt_h.font.color.rgb = accent_color
    
    for t in tasks_list:
        pt = tf_l.add_paragraph()
        pt.space_before = Pt(4)
        rt = pt.add_run()
        rt.text = f"• {t}"
        rt.font.name = FONT_NAME
        rt.font.size = Pt(12)
        rt.font.color.rgb = RGBColor(51, 65, 85)
        
    # Right Card: Speech Script for Doctor (Width: 4.6 Inches)
    rx = Inches(7.9)
    rw = Inches(4.63)
    add_rect(sl, rx, ly, rw, lh, fill_color=C_CARD_WHITE, line_color=C_BORDER)
    add_rect(sl, rx, ly, rw, Inches(0.08), fill_color=C_ROLE1_BLUE, line_color=None)
    
    tb_r = sl.shapes.add_textbox(rx + Inches(0.25), ly + Inches(0.15), rw - Inches(0.5), lh - Inches(0.3))
    tf_r = tb_r.text_frame
    tf_r.word_wrap = True
    
    pr = tf_r.paragraphs[0]
    rr = pr.add_run()
    rr.text = "🎤 ماذا يقول العضو للدكتورة في المناقشة؟"
    rr.font.name = FONT_NAME
    rr.font.size = Pt(15)
    rr.font.bold = True
    rr.font.color.rgb = C_ROLE1_BLUE
    
    pr_sub = tf_r.add_paragraph()
    rr_sub = pr_sub.add_run()
    rr_sub.text = "(Speech Script جاهز للحفظ والإلقاء بثقة)"
    rr_sub.font.name = FONT_NAME
    rr_sub.font.size = Pt(11)
    rr_sub.font.color.rgb = C_TEXT_MUTED
    
    pr_body = tf_r.add_paragraph()
    pr_body.space_before = Pt(12)
    rr_body = pr_body.add_run()
    rr_body.text = speech_text
    rr_body.font.name = FONT_NAME
    rr_body.font.size = Pt(13)
    rr_body.font.color.rgb = C_TEXT_DARK

# ── SLIDE 3: MEMBER 1 (ML & DATA) ─────────────────────────────────────────────
def build_slide_3(prs):
    files = [
        "train_model.py (كود التدريب والتقسيم والتقييم)",
        "data/employees.csv (بيانات 1000 موظف بالـ 6 متغيرات)",
        "data/generate_data.py (سكريبت تخليق ومعالجة البيانات)",
        "models/workload_model.pkl (ملف النموذج الثنائي المحفوظ)"
    ]
    tasks = [
        "تنظيف وهندسة البيانات واستبعاد المتغيرات غير الموضوعية (الـ NLP والسن والنوع) التزاماً بمعايير أخلاقيات الذكاء الاصطناعي (AI Fairness).",
        "تقسيم البيانات وفق المعيار العلمي (80% تدريب و 20% اختبار) باستخدام Stratified Sampling و random_state=42 لمنع التحيز وضمان التكرارية.",
        "بناء وتدريب نموذج Random Forest ومقارنته بنموذج Logistic Regression، وإثبات تفوق RF في مقياس Recall بنسبة 96.6%.",
        "حفظ وتصدير النموذج النهائي بصيغة joblib للاستدعاء الفوري عبر السيرفر."
    ]
    speech = (
        "«دكتورة، دوري في المشروع كان هندسة البيانات وتدريب نموذج تعلم الآلة.\n\n"
        "بناءً على توجيه حضرتك، قمت باستبعاد الفيدباك الذاتي لمنع انحياز الاستجابة (Response Bias)، واستبعدت السن والجنس لمنع أي تمييز جندري أو عمري في الذكاء الاصطناعي.\n\n"
        "اعتمدت على 6 مؤشرات تشغيلية دقيقة، وقسمت الـ 1000 موظف بنظام Stratified Split بنسبة 80/20 مع تثبيت random_state=42. قارنت النماذج ونجحت في الوصول لـ Recall بنسبة 96.6% بفضل Random Forest، وهو ما يضمن كشف 97 من كل 100 موظف مجهد فعلياً دون تفويت أي حالة حرجة.»"
    )
    build_role_slide(prs, 3, "العضو الأول: مهندس تعلم الآلة وهندسة البيانات",
                     "Member 1: Machine Learning & Data Pipeline Engineer", C_ROLE1_BLUE,
                     files, tasks, speech)

# ── SLIDE 4: MEMBER 2 (XAI & RISK ENGINE) ─────────────────────────────────────
def build_slide_4(prs):
    files = [
        "backend/risk.py (المحرك الرياضي لاحتساب مؤشر ومستويات الخطر)",
        "backend/explain.py (محرك التفسير عبر خوارزمية SHAP)",
        "models/feature_importance.png (مخطط ترتيب أهمية المتغيرات)",
        "models/confusion_matrix.png (مصفوفة أخطاء التنبؤ)"
    ]
    tasks = [
        "بناء خوارزمية حساب مؤشر الإجهاد الرياضي في `risk.py` لتحويل احتمالية النموذج إلى نسبة مئوية (0–100) وتصنيفها لمستويات (Low, Medium, High).",
        "تطبيق خوارزمية SHAP (Shapley Additive Explanations) لضمان قابلية تفسير الذكاء الاصطناعي (XAI) وعدم تركه كصندوق أسود مغلق.",
        "استخراج الأوزان النسبية للقرار (Feature Importance): ساعات الإضافي 30.1%، الإجازات 22.9%، وساعات الدوام 21.9%.",
        "برمجة توليد أسباب تشخيصية واضحة للإدارة بدلاً من مجرد إعطاء رقم صامت."
    ]
    speech = (
        "«دكتورة، دوري كان ضمان شفافية الذكاء الاصطناعي ومسؤوليته (Explainable AI).\n\n"
        "أنظمة الموارد البشرية ترفض الذكاء الاصطناعي المبهم؛ لذلك طوّرت في risk.py معادلة حساب مؤشر الخطر من 0 إلى 100 وتحديد مستويات التدخل الإداري.\n\n"
        "ثم طبقت في explain.py خوارزمية SHAP العالمية لاستخراج الأسباب الفردية وراء كل قرار؛ فالنظام لا يكتفي بقول الموظف معرض للخطر، بل يوضح له وللإدارة أن السبب هو تراكم 14 ساعة إضافية وانعدام الإجازات السنوية، مما يمنح الإدارة قرارات علاجية قابلة للتنفيذ (Actionable Insights).»"
    )
    build_role_slide(prs, 4, "العضو الثاني: مهندس محرك المخاطر والذكاء الاصطناعي التفسيري",
                     "Member 2: Explainable AI & Algorithmic Risk Engineer", C_ROLE2_PURPLE,
                     files, tasks, speech)

# ── SLIDE 5: MEMBER 3 (BACKEND & SECURITY) ────────────────────────────────────
def build_slide_5(prs):
    files = [
        "backend/main.py (خادم FastAPI ومسارات الـ REST APIs)",
        "backend/database.py (نماذج الجداول عبر SQLAlchemy ORM)",
        "backend/auth.py (نظام الحماية والمصادقة وتشفير JWT & Bcrypt)",
        "requirements.txt (إدارة حزم وبيئة العمل الخلفية)"
    ]
    tasks = [
        "تطوير خادم عالي الأداء باستخدام إطار عمل FastAPI وتجهيز التوثيق التفاعلي التلقائي عبر Swagger / OpenAPI.",
        "برمجة مسارات الـ REST APIs الكاملة: تسجيل التقييمات اللحظية (`/assess`)، استخراج الإحصائيات (`/stats`)، وإدارة الموظفين (`/employees`).",
        "تأمين النظام عبر تشفير كلمات المرور باستخدام Salted Bcrypt Hashing، وتوليد توكنات الجلسة المشفرة (JWT Access Tokens).",
        "تصميم وتطبيق نماذج التحقق الصارم من صحة المدخلات (Pydantic Schemas) وإدارة قاعدة بيانات SQLite عبر SQLAlchemy."
    ]
    speech = (
        "«دكتورة، كنت مسؤولاً عن هندسة الخادم والواجهات البرمجية (Backend Architecture).\n\n"
        "بنيت الخادم باستخدام FastAPI لضمان سرعة استجابة فائقة في أجزاء من الثانية. قمت ببرمجة مسارات REST APIs وربطها بنموذج الذكاء الاصطناعي وقاعدة البيانات عبر SQLAlchemy ORM.\n\n"
        "كما صممت نظام الحماية بالكامل في auth.py باستخدام تشفير Bcrypt لكلمات المرور وتوكنات JWT المشفرة، مع الفصل الصارم بين صلاحيات مدير النظام (Admin) وصلاحيات الموظف العادي لحماية خصوصية بيانات الصحة المهنية.»"
    )
    build_role_slide(prs, 5, "العضو الثالث: مهندس الخادم والواجهات البرمجية والأمان",
                     "Member 3: Backend Architecture & API Security Engineer", C_ROLE3_GREEN,
                     files, tasks, speech)

# ── SLIDE 6: MEMBER 4 (FRONTEND & UI/UX) ──────────────────────────────────────
def build_slide_6(prs):
    files = [
        "frontend/index.html & employees.html (لوحة التحكم ودليل الموظفين)",
        "frontend/assess.html & employee-portal.html (شاشات التقييم والبوابة)",
        "frontend/login.html (شاشة تسجيل الدخول الموحدة)",
        "frontend/css/style.css (نظام التصميم الشامل والتنسيقات)",
        "frontend/js/i18n.js (محرك الترجمة الفورية عربي/إنجليزي الكامل)"
    ]
    tasks = [
        "تصميم نظام واجهات عصري (Custom Modern Design System) يوفر تجربة استخدام مريحة ومتوافقة مع المعايير المؤسسية.",
        "برمجة محرك الترجمة الفورية الكامل في `i18n.js` مع ضبط التبديل التلقائي لاتجاه الصفحة كاملاً بين العربية (RTL) والإنجليزية (LTR).",
        "بناء النوافذ المنبثقة التفاعلية (Modals) لإضافة وتعديل بيانات الموظفين وإجراءات الحذف الآمن.",
        "تخصيص شاشات الطباعة التنفيذية لتصدير تقارير فحص الإجهاد بصيغة PDF مهنية معتمدة بضغطة زر واحدة."
    ]
    speech = (
        "«دكتورة، تخصصت في تطوير الواجهة الأمامية وتجربة المستخدم (Frontend UI/UX).\n\n"
        "قمت ببناء Design System متكامل في style.css يضمن تناسق الأزرار والكروت والألوان في جميع الصفحات. وبرمجت محرك ترجمة وتوطين فوري في i18n.js يدعم التحويل اللحظي الكامل بين العربية (RTL) والإنجليزية (LTR) بضغطة زر دون إعادة تحميل الصفحة.\n\n"
        "كما صممت واجهات التقييم التفاعلية، ونوافذ إضافة وتعديل الموظفين، وضبطت تنسيقات تقارير الطباعة التنفيذية PDF بأسلوب مؤسسي راقٍ.»"
    )
    build_role_slide(prs, 6, "العضو الرابع: مهندس الواجهة الأمامية والترجمة الفورية",
                     "Member 4: Frontend Architecture & Bilingual UI/UX Engineer", C_ROLE4_AMBER,
                     files, tasks, speech)

# ── SLIDE 7: MEMBER 5 (ANALYTICS & QA) ────────────────────────────────────────
def build_slide_7(prs):
    files = [
        "frontend/js/app.js (منطق الرسوم البيانية وجلب البيانات اللحظية)",
        "frontend/js/auth.js (إدارة جلسات المتصفح وحماية التوجيه)",
        "frontend/js/config.js (إعدادات الربط وعناوين الخادم)",
        "scripts/sync_database_scores_fast.py (مزامنة بيانات الـ 1000 موظف)",
        "scripts/audit_system.py (أداة الفحص الشامل وضمان الجودة)"
    ]
    tasks = [
        "ربط الواجهة الأمامية بالخادم عبر تقنيات Fetch/AJAX غير المتزامنة لعرض الإحصائيات لحظة بلحظة.",
        "برمجة المخططات البيانية التفاعلية باستخدام مكتبة `Chart.js`: مخطط الدونات لتوزيع المخاطر، ومخطط مقارنة ساعات العمل بالأوفرتايم.",
        "تطوير جدول المراقبة العاجلة (Critical Attention Watchlist) الذي يرصد تلقائياً الموظفين الأكثر عرضة للاحتراق للتدخل الفوري.",
        "إجراء اختبارات الجودة الشاملة (End-to-End Testing) والتأكد من خلو المنظومة من الثغرات، ومزامنة بيانات قاعدة البيانات بالكامل."
    ]
    speech = (
        "«دكتورة، كان دوري تكامل النظام والتحليلات البصرية وضمان الجودة (Analytics & QA).\n\n"
        "قمت بربط الواجهة ببيانات السيرفر عبر AJAX في app.js، وبرمجت المخططات التفاعلية باستخدام Chart.js لعرض نسب توزيع الاحتراق ومقارنة ساعات العمل بمعدلات الأوفرتايم.\n\n"
        "كما صممت جدول المراقبة الحرجة (Watchlist) لتنبيه الإدارة فورياً بأعلى الحالات خطورة. وقمت بإجراء فحص الجودة الشامل لكافة مسارات النظام ومزامنة بيانات الـ 1000 موظف في قاعدة البيانات للتأكد من خلو المنظومة من أي ثغرات برمجية.»"
    )
    build_role_slide(prs, 7, "العضو الخامس: مهندس تحليلات الداشبورد وتكامل النظام وضمان الجودة",
                     "Member 5: Dashboard Analytics, Integration & QA Engineer", C_ROLE5_CYAN,
                     files, tasks, speech)

# ── SLIDE 8: INTEGRATION & WORKFLOW MATRIX ────────────────────────────────────
def build_slide_8(prs):
    sl = blank_slide(prs)
    add_header(sl, "مصفوفة التكامل الهندسي وتدفق العمل بين أعضاء الفريق", "Cross-Functional Integration Matrix & Team Handover", 8)
    
    # Explanatory card
    add_rect(sl, Inches(0.8), Inches(1.45), Inches(11.73), Inches(0.9), fill_color=C_CARD_WHITE, line_color=C_BORDER)
    tb_t = sl.shapes.add_textbox(Inches(1.0), Inches(1.52), Inches(11.3), Inches(0.75))
    tf_t = tb_t.text_frame
    p_t = tf_t.paragraphs[0]
    r_t = p_t.add_run()
    r_t.text = "🔄 كيف تتكامل مخرجات كل عضو لتشغيل المنظومة ككتلة واحدة متناغمة؟"
    r_t.font.name = FONT_NAME
    r_t.font.size = Pt(15)
    r_t.font.bold = True
    r_t.font.color.rgb = C_ROLE1_BLUE
    
    p_t2 = tf_t.add_paragraph()
    r_t2 = p_t2.add_run()
    r_t2.text = "العمل لم يكن عشوائياً أو مجزأً؛ كل عضو يسلم مخرجاته الهندسية للعضو التالي عبر واجهات بينية واضحة وموثقة برمجياً."
    r_t2.font.name = FONT_NAME
    r_t2.font.size = Pt(12)
    r_t2.font.color.rgb = RGBColor(71, 85, 105)
    
    # 5 Handover Steps
    matrix_steps = [
        ("خطوة 1: مخرجات العضو 1 ➔ العضو 2 و 3",
         "يدرب النموذج ويحفظه كملف `workload_model.pkl`، ويسلمه لمحرك التفسير والباك إند.", C_ROLE1_BLUE),
        ("خطوة 2: مخرجات العضو 2 ➔ العضو 3",
         "يسلم دوال `compute_risk()` وحساب الـ SHAP في `explain.py` ليدمجها الباك إند داخل نقاط الـ API.", C_ROLE2_PURPLE),
        ("خطوة 3: مخرجات العضو 3 ➔ العضو 4 و 5",
         "يوفر خادم FastAPI الموثق وواجهات الـ RESTful APIs الآمنة لاستقبال وإرسال البيانات.", C_ROLE3_GREEN),
        ("خطوة 4: مخرجات العضو 4 ➔ العضو 5",
         "يسلم صفحات الـ HTML المتجاوبة ونظام التصميم الموحد ومحرك الترجمة `i18n.js` جاهزاً للعرض.", C_ROLE4_AMBER),
        ("خطوة 5: مخرجات العضو 5 ➔ المنظومة ككل",
         "يدمج الرسوم البيانية عبر Chart.js، ويربط الـ APIs، ويجري اختبارات الجودة الشاملة للمشروع.", C_ROLE5_CYAN)
    ]
    
    for i, (head, body, col) in enumerate(matrix_steps):
        cy = Inches(2.55 + i * 0.92)
        add_rect(sl, Inches(0.8), cy, Inches(11.73), Inches(0.8), fill_color=C_CARD_WHITE, line_color=C_BORDER)
        add_rect(sl, Inches(0.8), cy, Inches(0.1), Inches(0.8), fill_color=col, line_color=None)
        
        tb = sl.shapes.add_textbox(Inches(1.1), cy + Inches(0.12), Inches(11.2), Inches(0.6))
        tf = tb.text_frame
        p = tf.paragraphs[0]
        r1 = p.add_run()
        r1.text = head + "\n"
        r1.font.name = FONT_NAME
        r1.font.size = Pt(13)
        r1.font.bold = True
        r1.font.color.rgb = col
        
        r2 = p.add_run()
        r2.text = body
        r2.font.name = FONT_NAME
        r2.font.size = Pt(12)
        r2.font.color.rgb = C_TEXT_DARK

# ── SLIDE 9: THESIS DEFENSE GOLDEN RULES ──────────────────────────────────────
def build_slide_9(prs):
    sl = blank_slide(prs)
    add_rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_color=C_BG_DARK, line_color=None)
    
    tb_h = sl.shapes.add_textbox(Inches(1.0), Inches(0.5), Inches(11.3), Inches(0.8))
    p_h = tb_h.text_frame.paragraphs[0]
    r_h = p_h.add_run()
    r_h.text = "نصائح وقواعد ذهبية للفريق يوم المناقشة أمام الدكتورة واللجنة"
    r_h.font.name = FONT_NAME
    r_h.font.size = Pt(28)
    r_h.font.bold = True
    r_h.font.color.rgb = RGBColor(255, 255, 255)
    
    tb_sub = sl.shapes.add_textbox(Inches(1.0), Inches(1.15), Inches(11.3), Inches(0.4))
    r_sub = tb_sub.text_frame.paragraphs[0].add_run()
    r_sub.text = "Golden Rules for a Confident, United, and Flawless Thesis Defense"
    r_sub.font.name = FONT_NAME
    r_sub.font.size = Pt(14)
    r_sub.font.color.rgb = RGBColor(147, 197, 253)
    
    rules = [
        ("1. وحدة الفريق والتسليم السلس", "عندما تسأل الدكتورة سؤالاً، يبدأ العضو المختص بالإجابة ثم يكمل زميله: «كما قام زميلي فلان بربط ذلك مع الباك إند...» لإظهار روح الفريق الواحد.", C_ROLE1_BLUE),
        ("2. التمسك بالسبب العلمي لحذف الفيدباك", "إذا سُئلتم: أين الـ NLP؟ الإجابة فوراً: «حذفناه احتراماً للتوجيه الأكاديمي ولمنع انحياز الاستجابة (Response Bias) والاعتماد على القياسات الموضوعية».", C_ROLE2_PURPLE),
        ("3. تبرير استبعاد السن والجنس بأخلاقيات الذكاء الاصطناعي", "استبعدناهم عمداً لمنع التمييز الجندري والعمري (AI Fairness & Ethics)، ولأن الاحتراق ناتج عن ضغط العمل الفعلي وليس السن.", C_ROLE3_GREEN),
        ("4. الافتخار بنسبة الالتقاط (Recall: 96.6%)", "دائماً ركزوا على أن معيار النجاح الأهم في الصحة المهنية ليس الدقة المجردة بل الـ Recall لمنع تفويت أي موظف محترق.", C_ROLE4_AMBER),
        ("5. استعراض النظام الحي بثقة", "ابدأوا بالداشبورد، اقلبوا اللغة عربي وإنجليزي بضغطة زر، استعرضوا كارت التفسير SHAP، وأظهروا تقرير الطباعة PDF المعتمد.", C_ROLE5_CYAN),
        ("6. الهدوء والاحترافية", "أنتم بنيتم نظاماً هندسياً حقيقياً كامل الأركان يعمل بالفعل وليس مجرد فكرة نظرية، فكونوا فخورين بما أنجزتموه!", RGBColor(34, 197, 94))
    ]
    
    for i, (title, desc, accent) in enumerate(rules):
        col = i % 2
        row = i // 2
        cx = Inches(1.0 + col * 5.8)
        cy = Inches(1.8 + row * 1.7)
        
        add_rect(sl, cx, cy, Inches(5.5), Inches(1.5), fill_color=C_CARD_DARK, line_color=RGBColor(51, 65, 85))
        add_rect(sl, cx, cy, Inches(0.1), Inches(1.5), fill_color=accent, line_color=None)
        
        tb = sl.shapes.add_textbox(cx + Inches(0.25), cy + Inches(0.15), Inches(5.1), Inches(1.2))
        tf = tb.text_frame
        tf.word_wrap = True
        
        p1 = tf.paragraphs[0]
        r1 = p1.add_run()
        r1.text = title
        r1.font.name = FONT_NAME
        r1.font.size = Pt(15)
        r1.font.bold = True
        r1.font.color.rgb = RGBColor(255, 255, 255)
        
        p2 = tf.add_paragraph()
        p2.space_before = Pt(6)
        r2 = p2.add_run()
        r2.text = desc
        r2.font.name = FONT_NAME
        r2.font.size = Pt(12)
        r2.font.color.rgb = RGBColor(203, 213, 225)

def main():
    prs = create_presentation()
    build_slide_1(prs)
    build_slide_2(prs)
    build_slide_3(prs)
    build_slide_4(prs)
    build_slide_5(prs)
    build_slide_6(prs)
    build_slide_7(prs)
    build_slide_8(prs)
    build_slide_9(prs)
    
    out_dir = r"c:\Users\abduu\Desktop\Tawazon\docs"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Tawazon_Team_Roles_and_Responsibilities.pptx")
    prs.save(out_path)
    size = os.path.getsize(out_path)
    print(f"SUCCESS: Saved {len(prs.slides)} slides to {out_path} ({size:,} bytes)")

if __name__ == "__main__":
    main()
