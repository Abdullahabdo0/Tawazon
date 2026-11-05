# -*- coding: utf-8 -*-
"""
generate_files_architecture_deck.py
===================================
Generates an ultra-clear, professional Arabic PowerPoint presentation (.pptx)
explaining every file in the Tawazon project according to the requested logical flow:
1. Data
2. Machine Learning (ML)
3. Natural Language Processing (NLP)
4. Backend & Database
5. Frontend (UI, Scripts & Styles)
6. End-to-End Execution Lifecycle
"""

import os
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.oxml import parse_xml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_PATH_DOCS = os.path.join(ROOT, "docs", "Tawazon_Project_Architecture_and_Files_Guide.pptx")
OUT_PATH_ROOT = os.path.join(ROOT, "Tawazon_Project_Architecture_and_Files_Guide.pptx")

# ── Colors & Styles ──────────────────────────────────────────────────────────
BG_DARK    = "0F172A"   # Slate 900
CARD_BG    = "1E293B"   # Slate 800
CARD_BG2   = "243247"   # Slightly lighter slate
WHITE      = RGBColor(0xFF, 0xFF, 0xFF)
MUTED      = RGBColor(0x94, 0xA3, 0xB8)
GREEN      = "10B981"   # Emerald
BLUE       = "38BDF8"   # Sky blue
PURPLE     = "A855F7"   # Purple
AMBER      = "F59E0B"   # Amber/Orange
ROSE       = "F43F5E"   # Rose
CYAN       = "06B6D4"

FONT_AR = "Arial"


def create_deck():
    prs = Presentation()
    prs.slide_width = Inches(13.333)
    prs.slide_height = Inches(7.5)
    blank_layout = prs.slide_layouts[6]

    def set_slide_bg(slide, hex_col=BG_DARK):
        bg = slide.background
        fill = bg.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor.from_string(hex_col)

    def add_card(slide, left, top, width, height, hex_accent=None, bg_hex=CARD_BG):
        shape = slide.shapes.add_shape(1, Inches(left), Inches(top), Inches(width), Inches(height))
        shape.fill.solid()
        shape.fill.fore_color.rgb = RGBColor.from_string(bg_hex)
        shape.line.fill.background()
        if hex_accent:
            accent = slide.shapes.add_shape(1, Inches(left), Inches(top), Inches(width), Inches(0.08))
            accent.fill.solid()
            accent.fill.fore_color.rgb = RGBColor.from_string(hex_accent)
            accent.line.fill.background()
        return shape

    def add_header(slide, title_ar, subtitle_ar, category_tag=None, tag_hex=BLUE):
        if category_tag:
            tag_box = slide.shapes.add_textbox(Inches(0.8), Inches(0.4), Inches(11.733), Inches(0.35))
            tf_tag = tag_box.text_frame
            tf_tag.word_wrap = True
            p_tag = tf_tag.paragraphs[0]
            p_tag.text = f"● {category_tag}"
            p_tag.font.size = Pt(13)
            p_tag.font.bold = True
            p_tag.font.color.rgb = RGBColor.from_string(tag_hex)
            p_tag.font.name = FONT_AR
            p_tag.alignment = PP_ALIGN.RIGHT

        txBox = slide.shapes.add_textbox(Inches(0.8), Inches(0.75), Inches(11.733), Inches(0.8))
        tf = txBox.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        p.text = title_ar
        p.font.size = Pt(22)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.font.name = FONT_AR
        p.alignment = PP_ALIGN.RIGHT

        if subtitle_ar:
            p2 = tf.add_paragraph()
            p2.text = subtitle_ar
            p2.font.size = Pt(13)
            p2.font.color.rgb = MUTED
            p2.font.name = FONT_AR
            p2.alignment = PP_ALIGN.RIGHT

    def add_table(slide, headers, rows, left, top, width, col_widths, hex_header=GREEN):
        n_rows = len(rows) + 1
        n_cols = len(headers)
        table_shape = slide.shapes.add_table(n_rows, n_cols, Inches(left), Inches(top), Inches(width), Inches(0.5 * n_rows))
        table = table_shape.table

        for j, w in enumerate(col_widths):
            table.columns[j].width = Inches(w)

        # Header Row
        for j, h in enumerate(headers):
            cell = table.cell(0, j)
            cell.text = h
            for p in cell.text_frame.paragraphs:
                p.font.size = Pt(13)
                p.font.bold = True
                p.font.color.rgb = WHITE
                p.font.name = FONT_AR
                p.alignment = PP_ALIGN.CENTER
            tcPr = cell._tc.get_or_add_tcPr()
            shd = parse_xml(f'<a:solidFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:srgbClr val="{hex_header}"/></a:solidFill>')
            tcPr.append(shd)

        # Data Rows
        for i, row in enumerate(rows):
            bg = CARD_BG if i % 2 == 0 else BG_DARK
            for j, val in enumerate(row):
                cell = table.cell(i + 1, j)
                cell.text = str(val)
                for p in cell.text_frame.paragraphs:
                    p.font.size = Pt(11.5)
                    p.font.bold = (j == 0)
                    p.font.color.rgb = WHITE if j == 0 else RGBColor(0xDF, 0xE5, 0xEE)
                    p.font.name = FONT_AR
                    # Align: first col right/center, others right
                    p.alignment = PP_ALIGN.CENTER if j == 0 else PP_ALIGN.RIGHT
                tcPr = cell._tc.get_or_add_tcPr()
                shd = parse_xml(f'<a:solidFill xmlns:a="http://schemas.openxmlformats.org/drawingml/2006/main"><a:srgbClr val="{bg}"/></a:solidFill>')
                tcPr.append(shd)

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 1: Title Slide
    # ═════════════════════════════════════════════════════════════════════════
    s1 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s1)

    add_card(s1, 1.2, 1.0, 10.933, 5.5, GREEN)

    logo_path = os.path.join(ROOT, 'frontend', 'assets', 'logo.png')
    if os.path.exists(logo_path):
        s1.shapes.add_picture(logo_path, Inches(5.966), Inches(1.2), Inches(1.4), Inches(1.4))

    tb = s1.shapes.add_textbox(Inches(1.5), Inches(2.75), Inches(10.333), Inches(3.4))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "منظومة توازن (Tawazon / WorkPulse)"
    p.font.size = Pt(32)
    p.font.bold = True
    p.font.color.rgb = WHITE
    p.font.name = FONT_AR
    p.alignment = PP_ALIGN.CENTER

    p = tf.add_paragraph()
    p.text = "الدليل المعماري الشامل: وظائف الملفات ودورها بالترتيب المنطقي للمشروع"
    p.font.size = Pt(20)
    p.font.bold = True
    p.font.color.rgb = RGBColor.from_string(BLUE)
    p.font.name = FONT_AR
    p.space_before = Pt(14)
    p.alignment = PP_ALIGN.CENTER

    p = tf.add_paragraph()
    p.text = "Data Pipeline  ➔  Machine Learning  ➔  NLP Sentiment  ➔  Backend Server  ➔  Frontend UI"
    p.font.size = Pt(15)
    p.font.bold = True
    p.font.color.rgb = RGBColor.from_string(AMBER)
    p.font.name = FONT_AR
    p.space_before = Pt(20)
    p.alignment = PP_ALIGN.CENTER

    p = tf.add_paragraph()
    p.text = "شرح تفصيلي لكل ملف: وظيفته البرمجية، أهميته في النظام، وترتيب مروره داخل الموقع"
    p.font.size = Pt(13)
    p.font.color.rgb = MUTED
    p.font.name = FONT_AR
    p.space_before = Pt(14)
    p.alignment = PP_ALIGN.CENTER

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 2: Project Pipeline & Flow Overview
    # ═════════════════════════════════════════════════════════════════════════
    s2 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s2)
    add_header(s2, "المخطط الهيكلي لتدفق البيانات في المشروع (Pipeline Flow)",
               "كيف تتكامل أجزاء المشروع الخمسة بدءاً من تجميع الداتا وحتى ظهور النتائج على الواجهة",
               "نظرة عامة على المراحل", BLUE)

    stages = [
        ("1. Data Pipeline", "هندسة ومعالجة البيانات", "سحب داتا Kaggle الخام، تنظيفها، واستخراج المؤشرات وحفظها في employees.csv", GREEN, 0.8),
        ("2. Machine Learning", "نمذجة إجهاد العمل", "تدريب خوارزمية Random Forest على 6 مؤشرات عملية وحفظ النموذج workload_model.pkl", BLUE, 3.2),
        ("3. NLP Engine", "تحليل مشاعر الموظفين", "معالجة النصوص (عربي/إنجليزي) بـ DistilBERT وقاموس الإجهاد لاستخراج sentiment_risk", PURPLE, 5.6),
        ("4. Backend Server", "خادم الـ API وقواعد البيانات", "سيرفر FastAPI يدمج (60% ML + 40% NLP) ويحفظ السجلات في SQLite (workpulse.db)", AMBER, 8.0),
        ("5. Frontend UI", "واجهات التفاعل والتحكم", "صفحات HTML/JS متجاوبة لعرض الرسوم البيانية، إجراء الفحص، ورفع ملفات CSV", ROSE, 10.4),
    ]

    for title, sub, desc, col, left in stages:
        add_card(s2, left, 1.9, 2.15, 4.8, col)
        tb = s2.shapes.add_textbox(Inches(left + 0.1), Inches(2.1), Inches(1.95), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = title
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor.from_string(col)
        p.font.name = FONT_AR
        p.alignment = PP_ALIGN.CENTER

        p = tf.add_paragraph()
        p.text = sub
        p.font.size = Pt(12)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.font.name = FONT_AR
        p.space_before = Pt(8)
        p.alignment = PP_ALIGN.CENTER

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(11)
        p.font.color.rgb = MUTED
        p.font.name = FONT_AR
        p.space_before = Pt(14)
        p.alignment = PP_ALIGN.RIGHT

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 3: Phase 1 - Data Engineering Files
    # ═════════════════════════════════════════════════════════════════════════
    s3 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s3)
    add_header(s3, "المرحلة الأولى: ملفات البيانات وتجهيزها (Data Engineering)",
               "الملفات المسؤولة عن جلب الداتا، تنظيفها، هندسة الخصائص، والتحليل الاستكشافي",
               "1. Data Pipeline", GREEN)

    headers = ["الملف / المسار", "وظيفته الأساسية", "المحتوى وما هو مهم فيه"]
    rows = [
        ["data/download_kaggle.py",
         "سكريبت تحميل البيانات من Kaggle",
         "يقوم بالاتصال بـ Kaggle API وتنزيل مجموعة بيانات ضغط العمل الأصلية وحفظها محلياً في مجلد data/."],
        ["data/kaggle_raw.csv",
         "ملف البيانات الخام غير المعالجة",
         "يحتوي على السجلات الأصلية المستوردة كما هي بأعمدتها الأولية قبل عمليات التنظيف أو التعديل."],
        ["data/process_kaggle_data.py",
         "سكريبت تنظيف وهندسة البيانات",
         "يحذف القيم الفارغة والشاذة، يوحد مسميات الأعمدة، ويحسب المتغير الهدف (burnout) بناءً على ضغط المهام والإرهاق."],
        ["data/employees.csv",
         "مجموعة البيانات المنقحة والنهائية",
         "الملف المعتمد لتدريب نماذج الذكاء الاصطناعي (يحتوي على المؤشرات الرقمية الستة + تقييم المشاعر + عمود الاحتراق)."],
        ["data/generate_data.py",
         "سكريبت توليد داتا محاكاة صناعية",
         "يولّد بيانات موظفين إضافية واقعية (Synthetic Data) متوافقة مع ظروف بيئة العمل لدعم الاختبارات الموسعة."],
        ["eda.py",
         "التحليل الاستكشافي للبيانات (EDA)",
         "يحلل توزيع المتغيرات، علاقات الارتباط، ويستخرج الرسوم البيانية الإحصائية المحفوظة في مجلد models/."]
    ]
    add_table(s3, headers, rows, 0.8, 1.8, 11.733, [3.0, 3.2, 5.533], GREEN)

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 4: Phase 2 - Machine Learning (ML) Files
    # ═════════════════════════════════════════════════════════════════════════
    s4 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s4)
    add_header(s4, "المرحلة الثانية: ملفات تعلم الآلة (Machine Learning)",
               "الملفات المسؤولة عن تدريب النموذج، حفظ الأوزان، وتفسير أسباب التنبؤ للموظفين",
               "2. Machine Learning", BLUE)

    headers = ["الملف / المسار", "وظيفته الأساسية", "المحتوى وما هو مهم فيه"]
    rows = [
        ["train_model.py",
         "سكريبت تدريب وتقييم النماذج",
         "يدرب خوارزمية Random Forest و Logistic Regression على 6 متغيرات أساسية، يقارن الدقة (F1/Recall)، ويحفظ النموذج."],
        ["models/workload_model.pkl",
         "نموذج الـ ML المُدرَّب والمحفوظ",
         "ملف ثنائي (Joblib/Pickle) يضم شجرة قرارات Random Forest مدربة وجاهزة لاستدعاء predict_proba() فورياً بالباك إند."],
        ["backend/explain.py",
         "محرك التفسير والشفافية (XAI)",
         "يستخدم خوارزميات SHAP وأوزان الشجرة لاستخراج أهم 3 أسباب حقيقية ساهمت في رفع نسبة الخطر لدى الموظف."],
        ["models/feature_importance.png",
         "مخطط أهمية الخصائص والمؤشرات",
         "رسم بياني يوضح بالأرقام تأثير كل عامل (مثل ساعات العمل الإضافية والغياب) على قرار التنبؤ النهائي."],
        ["models/confusion_matrix.png",
         "مصفوفة الدقة والالتباس",
         "توضح دقة النموذج في التمييز بين الحالات المستقرة وحالات الاحتراق مع معدل الخطأ ونسب الدقة والشمول."]
    ]
    add_table(s4, headers, rows, 0.8, 1.8, 11.733, [3.2, 3.0, 5.533], BLUE)

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 5: Phase 3 - Natural Language Processing (NLP) Files
    # ═════════════════════════════════════════════════════════════════════════
    s5 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s5)
    add_header(s5, "المرحلة الثالثة: معالجة اللغات الطبيعية (NLP Sentiment)",
               "تحليل ملاحظات وشكاوى الموظفين باللغتين العربية والإنجليزية لتقييم الضغط النفسي",
               "3. NLP Engine", PURPLE)

    # Left Card: File Breakdown
    add_card(s5, 0.8, 1.8, 5.7, 4.9, PURPLE)
    tb = s5.shapes.add_textbox(Inches(0.9), Inches(1.95), Inches(5.5), Inches(4.6))
    tf = tb.text_frame
    tf.word_wrap = True

    p = tf.paragraphs[0]
    p.text = "الملف الرئيسي: backend/sentiment.py"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor.from_string(PURPLE)
    p.font.name = FONT_AR
    p.alignment = PP_ALIGN.RIGHT

    bullets = [
        "● الوظيفة: استقبال التعليق النصي للموظف وحساب مؤشر الخطر النفسي (sentiment_risk) كقيمة بين 0.0 و 1.0.",
        "● القيمة 0.0: تعني مشاعر إيجابية جداً ولا توجد مؤشرات إحباط أو إرهاق.",
        "● القيمة 1.0: تعني مشاعر شديدة السلبية مع عبارات تدل على الإجهاد والاستنزاف أو نية الاستقالة.",
        "● أهميته المعمارية: يعمل مدمجاً داخل الـ API محلياً بدون الاعتماد على سيرفرات سحابية مكلفة أو إنترنت."
    ]
    for b in bullets:
        p = tf.add_paragraph()
        p.text = b
        p.font.size = Pt(12)
        p.font.color.rgb = WHITE
        p.font.name = FONT_AR
        p.space_before = Pt(10)
        p.alignment = PP_ALIGN.RIGHT

    # Right Card: Bilingual Architecture
    add_card(s5, 6.8, 1.8, 5.7, 4.9, CYAN)
    tb2 = s5.shapes.add_textbox(Inches(6.9), Inches(1.95), Inches(5.5), Inches(4.6))
    tf2 = tb2.text_frame
    tf2.word_wrap = True

    p = tf2.paragraphs[0]
    p.text = "آلية العمل الثنائية (Bilingual Engine)"
    p.font.size = Pt(16)
    p.font.bold = True
    p.font.color.rgb = RGBColor.from_string(CYAN)
    p.font.name = FONT_AR
    p.alignment = PP_ALIGN.RIGHT

    bullets2 = [
        "1. المسار العربي (Workplace Burnout Dictionary):",
        "   - قاموس متخصص يفهم اللهجة المصرية والعربية الفصحى (مثل: 'مش قادر'، 'فوق طاقتي'، 'إرهاق'، 'مفيش تقدير').",
        "   - نظام أوزان ذكي يرصد كلمات التخفيف والتشديد ويعطي درجة دقيقة فورية.",
        "2. المسار الإنجليزي (DistilBERT Transformer):",
        "   - نموذج HuggingFace مدرب مسبقاً (distilbert-base-uncased-finetuned-sst-2-english) يقيس المشاعر السلبية بدقة عالية.",
        "3. التوافق التلقائي:",
        "   - يتعرف الكود تلقائياً على لغة النص المدخل ويوجهه للمسار المناسب فورياً."
    ]
    for b in bullets2:
        p = tf2.add_paragraph()
        p.text = b
        p.font.size = Pt(11.5)
        p.font.color.rgb = WHITE
        p.font.name = FONT_AR
        p.space_before = Pt(6)
        p.alignment = PP_ALIGN.RIGHT

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 6: Phase 4 - Backend & Database Files
    # ═════════════════════════════════════════════════════════════════════════
    s6 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s6)
    add_header(s6, "المرحلة الرابعة: خادم الباك إند وقاعدة البيانات (Backend & DB)",
               "قلب النظام البرمجي الذي يربط الذكاء الاصطناعي بقاعدة البيانات ويقدم واجهات برمجة التطبيقات (APIs)",
               "4. Backend & Database", AMBER)

    headers = ["الملف / المسار", "وظيفته الأساسية", "المحتوى وما هو مهم فيه"]
    rows = [
        ["backend/main.py",
         "خادم التطبيق الرئيسي (FastAPI)",
         "يحتوي مسارات الـ API: تسجيل الدخول، إجراء التقييم الفردي، الرفع الجماعي لملفات CSV، وتغذية الرسوم البيانية."],
        ["backend/database.py",
         "إعداد الاتصال وتهيئة ORM",
         "يربط المشروع بـ SQLite عبر SQLAlchemy، ويعرّف جداول قاعدة البيانات: جدول المستخدمين (users) والتقييمات (assessments)."],
        ["backend/risk.py",
         "خوارزمية دمج المخاطر (Hybrid Engine)",
         "تطبق معادلة الاحتراق الشاملة: Score = (0.60 × Workload + 0.40 × Sentiment) × 100 وتحدد المستوى (Low / Medium / High)."],
        ["workpulse.db",
         "ملف قاعدة البيانات (SQLite)",
         "قاعدة بيانات حقيقية تحفظ بيانات الموظفين، كلمات المرور المشفرة، الصلاحيات، وسجلات الفحص التاريخية."],
        ["scripts/reseed_db.py",
         "سكريبت إعادة تعبئة قاعدة البيانات",
         "يقوم بإعادة بناء قاعدة البيانات وتعبئتها بحسابات تجريبية وتقييمات نموذجية متكاملة لتقديم عروض توضيحية خالية من الأخطاء."]
    ]
    add_table(s6, headers, rows, 0.8, 1.8, 11.733, [2.8, 3.2, 5.733], AMBER)

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 7: Phase 5 - Frontend Pages (HTML)
    # ═════════════════════════════════════════════════════════════════════════
    s7 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s7)
    add_header(s7, "المرحلة الخامسة: صفحات واجهة المستخدم (Frontend UI - HTML)",
               "الصفحات التي يتفاعل معها المستخدم والمدير في المتصفح حسب صلاحياته",
               "5. Frontend Pages", ROSE)

    headers = ["الملف / الصفحة", "المستخدم المستهدف", "الوظيفة والمحتوى المهم"]
    rows = [
        ["frontend/login.html",
         "كافة المستخدمين",
         "شاشة الدخول الموحدة مع إمكانية التبديل التجريبي السريع بنقرة زر بين دور المدير (Manager) ودور الموظف (Employee)."],
        ["frontend/index.html",
         "لوحة تحكم الإدارة (HR / Manager)",
         "عرض بطاقات KPI الرئيسية (نسب الاحتراق، الموظفين المعرضين للخطر)، ومخططات Chart.js الدائرية والشريطية."],
        ["frontend/assess.html",
         "الموظف أو مسؤول الـ HR",
         "نموذج فحص تفاعلي لإدخال ساعات العمل، التأخير، الغياب، والتعليق النصي مع ظهور فوري لدرجة الخطر وأهم 3 أسباب."],
        ["frontend/employees.html",
         "مسؤول الموارد البشرية",
         "جدول شامل لجميع الموظفين، فلترة حسب مستوى الخطورة، وزر الرفع الجماعي (Batch Upload) لتحليل ملف CSV بضغطة واحدة."],
        ["frontend/employee-portal.html",
         "الموظف الفردي",
         "بوابة خاصة بالموظف تعرض سجله الشخصي فقط، مؤشر توازنه الوظيفي، وتوصيات عملية مخصصة لتحسين بيئة عمله."]
    ]
    add_table(s7, headers, rows, 0.8, 1.8, 11.733, [3.0, 2.7, 6.033], ROSE)

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 8: Phase 5 (Cont.) - Frontend Logic, Styles & Config
    # ═════════════════════════════════════════════════════════════════════════
    s8 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s8)
    add_header(s8, "المرحلة الخامسة (تابع): ملفات المنطق والتحكم والتنسيق (JS & CSS)",
               "الملفات المسؤولة عن التواصل مع الباك إند، حماية المسارات، واللغات، والتصميم العصري",
               "5. Frontend Scripts & Styles", CYAN)

    headers = ["الملف / المسار", "وظيفته الأساسية", "المحتوى وما هو مهم فيه"]
    rows = [
        ["frontend/js/app.js",
         "منطق الواجهة ورسم المخططات",
         "يرسل طلبات fetch إلى الـ API، يعالج الردود، يبني جداول الموظفين، ويحدث مخططات Chart.js ديناميكياً بدون إعادة تحميل."],
        ["frontend/js/auth.js",
         "إدارة الجلسات والأمان بالواجهة",
         "يخزن بيانات الدخول والـ Tokens في localStorage، يتحقق من صلاحيات الصفحة، ويدير عمليات تسجيل الخروج والحماية."],
        ["frontend/js/config.js",
         "إعدادات الربط والـ Endpoints",
         "يحدد عنوان خادم الـ API (مثل http://127.0.0.1:8000) لتسهيل تغيير السيرفر أثناء النشر والتشغيل."],
        ["frontend/js/i18n.js",
         "محرك التعريب وتعدد اللغات",
         "يدعم التبديل السلس بين اللغتين العربية والإنجليزية، مع تبديل اتجاه الصفحة تلقائياً بين (RTL) و (LTR)."],
        ["frontend/css/style.css",
         "ملف التصميم والتنسيق الشامل",
         "تنسيق النمط الداكن العصري (Dark Theme)، استجابة كاملة للشاشات (Responsive Design)، وتأثيرات بصرية متقدمة للبطاقات."]
    ]
    add_table(s8, headers, rows, 0.8, 1.8, 11.733, [2.8, 3.2, 5.733], CYAN)

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 9: End-to-End Execution Scenario
    # ═════════════════════════════════════════════════════════════════════════
    s9 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s9)
    add_header(s9, "سيناريو تفاعلي: ماذا يحدث داخل الملفات عند الضغط على 'فحص الموظف'؟",
               "تتبع حركة البيانات بدقة لحظة بلحظة عبر ملفات المشروع من الواجهة وحتى النتيجة",
               "دورة حياة الطلب (Execution Lifecycle)", GREEN)

    steps = [
        ("الخطوة 1: الواجهة", "frontend/assess.html + app.js", "المستخدم يدخل 6 أرقام مع نص الشكوى، يقوم app.js بجمع الحقول وتجهيز JSON وإرساله عبر POST /api/assess.", BLUE, 0.8),
        ("الخطوة 2: الباك إند", "backend/main.py", "يستقبل السيرفر الطلب، يتحقق من صحة البيانات، ويمرر الأرقام لنموذج الـ ML والنص لنموذج الـ NLP بالتوازي.", GREEN, 3.8),
        ("الخطوة 3: الذكاء الاصطناعي", "models/workload_model.pkl + sentiment.py", "الموديل يتوقع ضغط العمل، وsentiment.py يحلل النص، وexplain.py يستخرج أهم 3 أسباب للضغط بـ SHAP.", PURPLE, 6.8),
        ("الخطوة 4: النتيجة والتخزين", "backend/risk.py + workpulse.db", "risk.py يحسب النسبة المدمجة (60%+40%)، تحفظ النتيجة في SQLite، وتعرض النتيجة والتوصيات فورياً بالواجهة.", AMBER, 9.8),
    ]

    for step_title, files_involved, details, col, left in steps:
        add_card(s9, left, 1.9, 2.75, 4.8, col)
        tb = s9.shapes.add_textbox(Inches(left + 0.1), Inches(2.1), Inches(2.55), Inches(4.4))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = step_title
        p.font.size = Pt(15)
        p.font.bold = True
        p.font.color.rgb = RGBColor.from_string(col)
        p.font.name = FONT_AR
        p.alignment = PP_ALIGN.CENTER

        p = tf.add_paragraph()
        p.text = files_involved
        p.font.size = Pt(11)
        p.font.bold = True
        p.font.color.rgb = WHITE
        p.font.name = FONT_AR
        p.space_before = Pt(8)
        p.alignment = PP_ALIGN.CENTER

        p = tf.add_paragraph()
        p.text = details
        p.font.size = Pt(11.5)
        p.font.color.rgb = MUTED
        p.font.name = FONT_AR
        p.space_before = Pt(14)
        p.alignment = PP_ALIGN.RIGHT

    # ═════════════════════════════════════════════════════════════════════════
    # SLIDE 10: Summary & Conclusion
    # ═════════════════════════════════════════════════════════════════════════
    s10 = prs.slides.add_slide(blank_layout)
    set_slide_bg(s10)
    add_header(s10, "خلاصة معمارية المشروع والنقاط الجوهرية للمناقشة",
               "أبرز ما يميز هيكلية توازن وكيف تعكس تكاملاً هندسياً حقيقياً بين البيانات والذكاء الاصطناعي والتطوير الكامل",
               "الخاتمة والتقييم", BLUE)

    highlights = [
        ("فصل تام للمسؤوليات (Separation of Concerns)", "كل مرحلة (Data, ML, NLP, Backend, Frontend) معزولة في مجلد مستقل بملفات واضحة يسهل اختبارها وتطويرها دون تداخل."),
        ("محرك ذكاء اصطناعي هجين وواقعي (Hybrid AI)", "عدم الاعتماد على الأرقام فقط، بل دمج القياسات العددية (60%) مع المشاعر الإنسانية الحقيقية (40%) لتقليل التحيز وتفادي الإنذارات الكاذبة."),
        ("قابلية التفسير والشفافية (Explainable AI - XAI)", "عبر backend/explain.py لا نكتفي بإعطاء نسبة خطر صامتة، بل نفسر لصاحب القرار الأسباب الدقيقة (مثل ساعات إضافية أو قلة إجازات)."),
        ("منظومة كاملة مستقلة (Self-Contained & Production-Ready)", "كل النماذج والبيانات تعمل محلياً (SQLite + Local Transformers / Custom Engine) دون أي تكاليف تشغيل خارجية أو اشتراكات.")
    ]

    for i, (title, desc) in enumerate(highlights):
        top_pos = 1.9 + (i * 1.25)
        add_card(s10, 0.8, top_pos, 11.733, 1.1, GREEN if i % 2 == 0 else BLUE)
        tb = s10.shapes.add_textbox(Inches(1.0), Inches(top_pos + 0.1), Inches(11.333), Inches(0.9))
        tf = tb.text_frame
        tf.word_wrap = True

        p = tf.paragraphs[0]
        p.text = f"✔ {title}"
        p.font.size = Pt(14)
        p.font.bold = True
        p.font.color.rgb = RGBColor.from_string(GREEN if i % 2 == 0 else BLUE)
        p.font.name = FONT_AR
        p.alignment = PP_ALIGN.RIGHT

        p = tf.add_paragraph()
        p.text = desc
        p.font.size = Pt(11.5)
        p.font.color.rgb = WHITE
        p.font.name = FONT_AR
        p.space_before = Pt(4)
        p.alignment = PP_ALIGN.RIGHT

    os.makedirs(os.path.dirname(OUT_PATH_DOCS), exist_ok=True)
    prs.save(OUT_PATH_DOCS)
    prs.save(OUT_PATH_ROOT)
    print(f"[OK] Saved presentation to:")
    print(f"     1. {OUT_PATH_DOCS}")
    print(f"     2. {OUT_PATH_ROOT}")


if __name__ == "__main__":
    create_deck()
