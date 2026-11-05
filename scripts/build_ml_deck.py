"""
build_ml_deck.py
Generates docs/Tawazon_ML_Model_Explained.pptx
Professional Arabic/English PowerPoint for Tawazon graduation project.
"""

from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.util import Inches, Pt
import os

# ── Colour palette ─────────────────────────────────────────────────────────
C_BLUE      = RGBColor(0x25, 0x63, 0xEB)   # #2563eb
C_GREEN     = RGBColor(0x22, 0xC5, 0x5E)   # #22c55e
C_DARK      = RGBColor(0x0F, 0x17, 0x2A)   # #0f172a  (cover bg)
C_SLATE     = RGBColor(0x1E, 0x29, 0x3B)   # section header bg
C_WHITE     = RGBColor(0xFF, 0xFF, 0xFF)
C_LIGHT_BG  = RGBColor(0xF1, 0xF5, 0xF9)   # slide background
C_GRAY      = RGBColor(0x64, 0x74, 0x8B)
C_AMBER     = RGBColor(0xF5, 0x9E, 0x0B)
C_TEAL      = RGBColor(0x0D, 0x94, 0x88)

SLIDE_W = Inches(13.33)
SLIDE_H = Inches(7.5)

# ── Helpers ────────────────────────────────────────────────────────────────

def new_prs():
    prs = Presentation()
    prs.slide_width  = SLIDE_W
    prs.slide_height = SLIDE_H
    return prs


def blank_slide(prs):
    blank_layout = prs.slide_layouts[6]   # completely blank
    return prs.slides.add_slide(blank_layout)


def add_rect(slide, l, t, w, h, fill_color=None, line_color=None, line_width=Pt(0)):
    shape = slide.shapes.add_shape(
        1,  # MSO_SHAPE_TYPE.RECTANGLE
        l, t, w, h
    )
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


def add_textbox(slide, text, l, t, w, h,
                font_size=Pt(16), bold=False, color=C_DARK,
                align=PP_ALIGN.LEFT, italic=False, wrap=True):
    txBox = slide.shapes.add_textbox(l, t, w, h)
    txBox.word_wrap = wrap
    tf = txBox.text_frame
    tf.word_wrap = wrap
    p = tf.paragraphs[0]
    p.alignment = align
    run = p.add_run()
    run.text = text
    run.font.size  = font_size
    run.font.bold  = bold
    run.font.color.rgb = color
    run.font.italic = italic
    return txBox


def add_text_para(tf, text, font_size=Pt(14), bold=False,
                  color=C_DARK, align=PP_ALIGN.LEFT, space_before=Pt(4)):
    p = tf.add_paragraph()
    p.alignment = align
    p.space_before = space_before
    run = p.add_run()
    run.text = text
    run.font.size = font_size
    run.font.bold = bold
    run.font.color.rgb = color
    return p


def slide_header(slide, title_ar, title_en="", accent=C_BLUE):
    """Top bar with slide title."""
    # background bar
    add_rect(slide, 0, 0, SLIDE_W, Inches(1.05), fill_color=accent)
    # Arabic title (right-aligned inside bar)
    tb = slide.shapes.add_textbox(Inches(0.3), Inches(0.08), Inches(12.7), Inches(0.55))
    tb.word_wrap = False
    tf = tb.text_frame
    p = tf.paragraphs[0]
    p.alignment = PP_ALIGN.RIGHT
    r = p.add_run()
    r.text = title_ar
    r.font.size = Pt(26)
    r.font.bold = True
    r.font.color.rgb = C_WHITE
    if title_en:
        tb2 = slide.shapes.add_textbox(Inches(0.3), Inches(0.63), Inches(12.7), Inches(0.35))
        tb2.word_wrap = False
        tf2 = tb2.text_frame
        p2 = tf2.paragraphs[0]
        p2.alignment = PP_ALIGN.RIGHT
        r2 = p2.add_run()
        r2.text = title_en
        r2.font.size = Pt(13)
        r2.font.bold = False
        r2.font.color.rgb = RGBColor(0xBF, 0xDB, 0xFF)
    # light background for slide body
    add_rect(slide, 0, Inches(1.05), SLIDE_W, SLIDE_H - Inches(1.05), fill_color=C_LIGHT_BG)


def bottom_bar(slide, page_num, total=11):
    add_rect(slide, 0, SLIDE_H - Inches(0.32), SLIDE_W, Inches(0.32), fill_color=C_SLATE)
    add_textbox(slide, f"Tawazon • ML Model Deep Dive  |  {page_num} / {total}",
                Inches(0.3), SLIDE_H - Inches(0.30), Inches(12), Inches(0.28),
                font_size=Pt(10), color=RGBColor(0x94, 0xA3, 0xB8), align=PP_ALIGN.LEFT)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 1 – Cover
# ══════════════════════════════════════════════════════════════════════════
def slide_cover(prs):
    sl = blank_slide(prs)
    # full dark background
    add_rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_color=C_DARK)
    # green accent stripe (left)
    add_rect(sl, 0, 0, Inches(0.18), SLIDE_H, fill_color=C_GREEN)
    # blue accent stripe (right)
    add_rect(sl, SLIDE_W - Inches(0.18), 0, Inches(0.18), SLIDE_H, fill_color=C_BLUE)
    # horizontal divider
    add_rect(sl, Inches(0.4), Inches(3.6), Inches(12.5), Inches(0.04), fill_color=C_GREEN)

    # Tag
    add_textbox(sl, "🎓  مشروع تخرج  |  Graduation Project",
                Inches(0.4), Inches(0.4), Inches(12.5), Inches(0.45),
                font_size=Pt(14), color=C_GREEN, align=PP_ALIGN.CENTER)

    # Arabic title
    add_textbox(sl, "كيف يتعلم Tawazon؟",
                Inches(0.4), Inches(1.1), Inches(12.5), Inches(0.9),
                font_size=Pt(42), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)

    add_textbox(sl, "شرح تفصيلي لبناء نموذج التنبؤ بالاحتراق الوظيفي",
                Inches(0.4), Inches(2.0), Inches(12.5), Inches(0.7),
                font_size=Pt(22), bold=False, color=RGBColor(0xBF, 0xDB, 0xFF),
                align=PP_ALIGN.CENTER)

    # English subtitle
    add_textbox(sl, "How Tawazon Learns – ML Model Deep Dive",
                Inches(0.4), Inches(2.8), Inches(12.5), Inches(0.6),
                font_size=Pt(18), color=C_GREEN, align=PP_ALIGN.CENTER)

    # Divider line already added above

    # Project info block
    info_lines = [
        ("🧠  Model:", "Random Forest Classifier"),
        ("📊  Dataset:", "1,000 Employees  •  Tabular Data"),
        ("🎯  Task:", "Binary Classification  –  Burnout Detection"),
        ("⚡  Accuracy:", "95.5%  |  F1-Score: 95.0%"),
    ]
    y = Inches(3.75)
    for label, val in info_lines:
        add_textbox(sl, label,
                    Inches(1.8), y, Inches(2.5), Inches(0.4),
                    font_size=Pt(14), bold=True, color=C_GREEN, align=PP_ALIGN.RIGHT)
        add_textbox(sl, val,
                    Inches(4.5), y, Inches(7.6), Inches(0.4),
                    font_size=Pt(14), color=C_WHITE, align=PP_ALIGN.LEFT)
        y += Inches(0.52)

    # Footer
    add_textbox(sl, "نظام تشخيص وتنبؤ الاحتراق الوظيفي  •  Employee Burnout Detection System",
                Inches(0.4), SLIDE_H - Inches(0.5), Inches(12.5), Inches(0.4),
                font_size=Pt(11), color=C_GRAY, align=PP_ALIGN.CENTER)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 2 – لماذا Machine Learning؟
# ══════════════════════════════════════════════════════════════════════════
def slide_why_ml(prs):
    sl = blank_slide(prs)
    slide_header(sl, "لماذا اخترنا Machine Learning؟", "Why Machine Learning?", accent=C_BLUE)
    bottom_bar(sl, 2)

    points = [
        ("🔬", "الأنماط معقدة وغير خطية",
         "الاحتراق الوظيفي لا يرتبط بمتغير واحد — العلاقة بين المتغيرات متشعبة ومتداخلة بطريقة لا يمكن تلخيصها بقاعدة if/else."),
        ("📊", "البيانات الرقمية كافية تماماً",
         "لا نحتاج إلى تحليل نصوص أو مشاعر؛ المؤشرات العددية (ساعات العمل، الغياب، التأخير…) تحمل إشارة تنبؤية قوية بحد ذاتها."),
        ("⚡", "قابلية التوسع والتحديث",
         "يمكن إعادة تدريب النموذج على بيانات جديدة بسهولة دون إعادة كتابة أي قواعد يدوية."),
        ("🎯", "دقة عالية وقابلية التفسير",
         "Random Forest يعطينا Feature Importance مباشرةً — نعرف بالضبط أي متغير يؤثر أكثر على القرار."),
        ("🧠", "الحل القياسي في أبحاث HR Analytics",
         "الدراسات الأكاديمية في مجال Occupational Burnout تعتمد ML على Tabular HR data كنهج قياسي موثق."),
    ]

    y = Inches(1.2)
    for icon, title, desc in points:
        # icon circle
        circ = sl.shapes.add_shape(9, Inches(0.3), y + Inches(0.02),
                                   Inches(0.52), Inches(0.52))
        circ.fill.solid(); circ.fill.fore_color.rgb = C_BLUE
        circ.line.fill.background()
        tb_ic = sl.shapes.add_textbox(Inches(0.3), y, Inches(0.52), Inches(0.55))
        p_ic = tb_ic.text_frame.paragraphs[0]
        p_ic.alignment = PP_ALIGN.CENTER
        r_ic = p_ic.add_run(); r_ic.text = icon; r_ic.font.size = Pt(16)

        # title + desc
        tb = sl.shapes.add_textbox(Inches(1.0), y, Inches(11.9), Inches(0.28))
        tf = tb.text_frame; tf.word_wrap = True
        p1 = tf.paragraphs[0]
        p1.alignment = PP_ALIGN.RIGHT
        r1 = p1.add_run(); r1.text = title
        r1.font.size = Pt(16); r1.font.bold = True; r1.font.color.rgb = C_BLUE

        p2 = tf.add_paragraph()
        p2.alignment = PP_ALIGN.RIGHT
        r2 = p2.add_run(); r2.text = desc
        r2.font.size = Pt(13); r2.font.color.rgb = C_DARK
        y += Inches(0.98)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 3 – Dataset & Features
# ══════════════════════════════════════════════════════════════════════════
def slide_dataset(prs):
    sl = blank_slide(prs)
    slide_header(sl, "البيانات والمتغيرات", "Dataset & Features  –  data/employees.csv", accent=C_TEAL)
    bottom_bar(sl, 3)

    # Stats row
    stats = [
        ("1,000", "موظف", "Records"),
        ("11",    "عمود", "Columns"),
        ("6",     "متغير مُدخَل", "Input Features"),
        ("44.1%", "نسبة الاحتراق", "Burnout Rate"),
    ]
    sx = Inches(0.3)
    for val, ar, en in stats:
        box = add_rect(sl, sx, Inches(1.15), Inches(2.95), Inches(0.85),
                       fill_color=C_BLUE, line_color=None)
        add_textbox(sl, val, sx, Inches(1.18), Inches(2.95), Inches(0.42),
                    font_size=Pt(26), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        add_textbox(sl, f"{ar}  /  {en}",
                    sx, Inches(1.58), Inches(2.95), Inches(0.3),
                    font_size=Pt(11), color=RGBColor(0xBF, 0xDB, 0xFF), align=PP_ALIGN.CENTER)
        sx += Inches(3.17)

    # NLP disclaimer box
    disc_box = add_rect(sl, Inches(0.3), Inches(2.12), Inches(12.73), Inches(0.6),
                        fill_color=RGBColor(0xFE, 0xF3, 0xC7), line_color=C_AMBER, line_width=Pt(1.5))
    add_textbox(sl,
                "⚠️  لا نستخدم NLP أو تحليل النصوص / Feedback — القرار مبني 100% على المؤشرات الرقمية (Tabular Data)\n"
                "السبب العلمي: مؤشرات العمل الكمية تُعدّ أقوى مُنبِّئات للاحتراق الوظيفي من التقييمات الذاتية (Maslach, 2001)،\n"
                "كما أنها موضوعية، قابلة للقياس الموثوق، وغير خاضعة للتحيز الذاتي في الإجابة.",
                Inches(0.4), Inches(2.14), Inches(12.5), Inches(0.56),
                font_size=Pt(11), color=RGBColor(0x78, 0x35, 0x00), align=PP_ALIGN.RIGHT)

    # Features table
    headers = ["#", "اسم المتغير", "الوصف بالعربي", "النوع", "نطاق القيم"]
    col_ws  = [Inches(0.4), Inches(2.3), Inches(5.5), Inches(1.3), Inches(2.8)]
    rows_data = [
        ["1", "avg_daily_hours",          "متوسط ساعات العمل اليومي",          "Float", "4 – 14"],
        ["2", "overtime_hours_week",      "ساعات العمل الإضافي أسبوعياً",       "Float", "0 – 30"],
        ["3", "absence_days_month",       "أيام الغياب في الشهر",              "Int",   "0 – 10"],
        ["4", "late_arrivals_month",      "مرات التأخر في الشهر",              "Int",   "0 – 15"],
        ["5", "tasks_assigned",           "عدد المهام المُسنَدة",               "Int",   "1 – 20"],
        ["6", "vacation_days_last_year",  "أيام الإجازة المستهلكة السنة الماضية", "Int",  "0 – 30"],
        ["Target ➔", "burnout",           "الاحتراق الوظيفي",                  "Binary","0 = لا  |  1 = نعم"],
    ]

    ty = Inches(2.78)
    # header row
    tx = Inches(0.3)
    for i, (h, cw) in enumerate(zip(headers, col_ws)):
        add_rect(sl, tx, ty, cw, Inches(0.37), fill_color=C_SLATE)
        add_textbox(sl, h, tx + Inches(0.03), ty + Inches(0.04), cw - Inches(0.06), Inches(0.3),
                    font_size=Pt(12), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        tx += cw

    for ri, row in enumerate(rows_data):
        ty += Inches(0.37)
        is_target = ri == 6
        fill = RGBColor(0xDC, 0xFA, 0xE7) if is_target else (C_WHITE if ri % 2 == 0 else C_LIGHT_BG)
        tx = Inches(0.3)
        for ci, (cell, cw) in enumerate(zip(row, col_ws)):
            add_rect(sl, tx, ty, cw, Inches(0.35), fill_color=fill,
                     line_color=RGBColor(0xE2, 0xE8, 0xF0), line_width=Pt(0.5))
            cell_color = C_GREEN if is_target else C_DARK
            add_textbox(sl, cell, tx + Inches(0.03), ty + Inches(0.03),
                        cw - Inches(0.06), Inches(0.3),
                        font_size=Pt(11), bold=is_target, color=cell_color, align=PP_ALIGN.CENTER)
            tx += cw


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 4 – Train/Test Split
# ══════════════════════════════════════════════════════════════════════════
def slide_split(prs):
    sl = blank_slide(prs)
    slide_header(sl, "تقسيم البيانات", "Train / Test Split", accent=C_BLUE)
    bottom_bar(sl, 4)

    # Visual split bar
    add_rect(sl, Inches(0.5), Inches(1.3), Inches(8.26), Inches(0.9),
             fill_color=C_BLUE)
    add_textbox(sl, "🏋️  Train Set  –  80%  (800 سجل)",
                Inches(0.5), Inches(1.3), Inches(8.26), Inches(0.9),
                font_size=Pt(20), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)

    add_rect(sl, Inches(8.76), Inches(1.3), Inches(4.07), Inches(0.9),
             fill_color=C_GREEN)
    add_textbox(sl, "🧪  Test Set – 20%\n(200 سجل)",
                Inches(8.76), Inches(1.3), Inches(4.07), Inches(0.9),
                font_size=Pt(16), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)

    # Divider label
    add_textbox(sl, "1,000 سجل إجمالي",
                Inches(0.5), Inches(2.28), Inches(12.3), Inches(0.3),
                font_size=Pt(13), color=C_GRAY, align=PP_ALIGN.CENTER)

    # Details cards
    cards = [
        (C_BLUE,  "random_state = 42",      "ضمان إمكانية التكرار\n(Reproducibility)"),
        (C_GREEN, "Stratified Split",        "الحفاظ على نسبة الاحتراق\n44.1% في كلا المجموعتين"),
        (C_AMBER, "sklearn train_test_split","الدالة المستخدمة من\nscikit-learn"),
    ]
    cx = Inches(0.5)
    for color, title, desc in cards:
        add_rect(sl, cx, Inches(2.72), Inches(3.9), Inches(1.3), fill_color=color)
        add_textbox(sl, title, cx + Inches(0.1), Inches(2.78), Inches(3.7), Inches(0.42),
                    font_size=Pt(16), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        add_textbox(sl, desc, cx + Inches(0.1), Inches(3.2), Inches(3.7), Inches(0.75),
                    font_size=Pt(13), color=C_WHITE, align=PP_ALIGN.CENTER)
        cx += Inches(4.2)

    # Code snippet box
    add_rect(sl, Inches(0.5), Inches(4.12), Inches(12.3), Inches(1.35),
             fill_color=RGBColor(0x0F, 0x17, 0x2A))
    code = (
        "from sklearn.model_selection import train_test_split\n\n"
        "X_train, X_test, y_train, y_test = train_test_split(\n"
        "    X, y,  test_size=0.20,  random_state=42,  stratify=y\n"
        ")"
    )
    add_textbox(sl, code, Inches(0.7), Inches(4.18), Inches(12.0), Inches(1.25),
                font_size=Pt(14), color=C_GREEN, align=PP_ALIGN.LEFT)

    # Why stratify note
    add_textbox(sl,
                "✅  لماذا Stratify؟  —  لأن البيانات غير متوازنة (44.1% burnout / 55.9% no-burnout)؛ "
                "بدون stratify قد لا تمثّل عيّنة الاختبار التوزيع الحقيقي.",
                Inches(0.5), Inches(5.55), Inches(12.3), Inches(0.42),
                font_size=Pt(13), color=C_DARK, align=PP_ALIGN.RIGHT)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 5 – Model Comparison
# ══════════════════════════════════════════════════════════════════════════
def slide_comparison(prs):
    sl = blank_slide(prs)
    slide_header(sl, "مقارنة الخوارزميات", "Algorithm Comparison", accent=C_SLATE)
    bottom_bar(sl, 5)

    headers  = ["المقياس / Metric", "Logistic Regression", "✅ Random Forest (الفائز)"]
    col_ws   = [Inches(3.3), Inches(4.4), Inches(5.0)]
    rows_data = [
        ["Accuracy",  "95.5%", "95.5%"],
        ["Precision", "96.5%", "93.4%"],
        ["Recall",    "93.2%", "96.6%"],
        ["F1-Score",  "94.8%", "95.0%"],
    ]

    ty = Inches(1.2)
    tx = Inches(0.4)
    # header
    for h, cw in zip(headers, col_ws):
        hdr_color = C_GREEN if h.startswith("✅") else C_SLATE
        add_rect(sl, tx, ty, cw, Inches(0.52), fill_color=hdr_color)
        add_textbox(sl, h, tx + Inches(0.05), ty + Inches(0.08), cw - Inches(0.1), Inches(0.4),
                    font_size=Pt(15), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        tx += cw

    # data rows
    for ri, row in enumerate(rows_data):
        ty += Inches(0.52)
        tx = Inches(0.4)
        fill = C_WHITE if ri % 2 == 0 else C_LIGHT_BG
        for ci, (cell, cw) in enumerate(zip(row, col_ws)):
            cell_fill = fill
            cell_color = C_DARK
            if ci == 2:  # RF column highlight
                cell_fill = RGBColor(0xDC, 0xFA, 0xE7)
                cell_color = RGBColor(0x14, 0x53, 0x2D)
            add_rect(sl, tx, ty, cw, Inches(0.5),
                     fill_color=cell_fill, line_color=RGBColor(0xE2, 0xE8, 0xF0), line_width=Pt(0.5))
            bold_cell = ci > 0
            add_textbox(sl, cell, tx + Inches(0.05), ty + Inches(0.1),
                        cw - Inches(0.1), Inches(0.35),
                        font_size=Pt(16), bold=bold_cell, color=cell_color, align=PP_ALIGN.CENTER)
            tx += cw

    # Key insight
    add_rect(sl, Inches(0.4), Inches(3.52), Inches(12.3), Inches(0.65),
             fill_color=RGBColor(0xDB, 0xEA, 0xFF))
    add_textbox(sl,
                "🎯  الفارق الحاسم: Random Forest يحقق Recall أعلى (96.6% مقابل 93.2%) — أي أنه يكتشف حالات الاحتراق الحقيقية\n"
                "بشكل أفضل، وتقليل False Negatives في السياق الصحي/الوظيفي أهم من تقليل False Positives.",
                Inches(0.5), Inches(3.55), Inches(12.1), Inches(0.6),
                font_size=Pt(13), color=C_DARK, align=PP_ALIGN.RIGHT)

    # Mini visual bars
    metrics = [("Accuracy", 95.5, 95.5), ("Precision", 96.5, 93.4),
               ("Recall", 93.2, 96.6), ("F1-Score", 94.8, 95.0)]
    bar_max = Inches(5.5)
    bx = Inches(0.5)
    by = Inches(4.3)
    add_textbox(sl, "Logistic Regression", Inches(5.3), by - Inches(0.25), Inches(2.5), Inches(0.25),
                font_size=Pt(11), bold=True, color=C_GRAY)
    add_textbox(sl, "Random Forest ✅", Inches(8.3), by - Inches(0.25), Inches(2.5), Inches(0.25),
                font_size=Pt(11), bold=True, color=C_GREEN)
    for label, lr, rf in metrics:
        add_textbox(sl, label, bx, by + Inches(0.05), Inches(2.0), Inches(0.3),
                    font_size=Pt(12), bold=True, color=C_DARK)
        lr_w = bar_max * (lr / 100)
        rf_w = bar_max * (rf / 100)
        add_rect(sl, Inches(2.6), by + Inches(0.04), lr_w, Inches(0.28),
                 fill_color=C_GRAY)
        add_textbox(sl, f"{lr}%", Inches(2.6) + lr_w + Inches(0.05), by,
                    Inches(0.5), Inches(0.35), font_size=Pt(10), color=C_GRAY)
        add_rect(sl, Inches(2.6), by + Inches(0.36), rf_w, Inches(0.28),
                 fill_color=C_GREEN)
        add_textbox(sl, f"{rf}%", Inches(2.6) + rf_w + Inches(0.05), by + Inches(0.3),
                    Inches(0.5), Inches(0.35), font_size=Pt(10), color=C_GREEN)
        by += Inches(0.78)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 6 – لماذا Random Forest؟
# ══════════════════════════════════════════════════════════════════════════
def slide_why_rf(prs):
    sl = blank_slide(prs)
    slide_header(sl, "لماذا اخترنا Random Forest؟", "Why Random Forest?", accent=C_GREEN)
    bottom_bar(sl, 6)

    reasons = [
        ("🌲", "Ensemble of Decision Trees",
         "يبني مئات الأشجار ويجمع تصويتها — هذا يقلل Overfitting ويعطي تنبؤاً أكثر استقراراً من شجرة واحدة."),
        ("📊", "Feature Importance مجانية",
         "النموذج يحسب أهمية كل متغير تلقائياً دون أي خطوات إضافية، مما يجعل النتائج قابلة للتفسير للمديرين وفريق HR."),
        ("🔧", "لا يحتاج Feature Scaling",
         "على عكس Logistic Regression، Random Forest لا يتأثر بمقياس المتغيرات، فلا حاجة لـ Normalization."),
        ("⚡", "أداء ممتاز على Tabular Data",
         "في مسابقات Kaggle والأبحاث الأكاديمية، Random Forest هو الخيار الأول على البيانات الجدولية الصغيرة والمتوسطة."),
        ("🎯", "Recall عالٍ = تشخيص أفضل",
         "يكتشف 96.6% من حالات الاحتراق الحقيقية (أعلى Recall)، وتفويت حالة احتراق أخطر من إنذار زائف."),
    ]

    y = Inches(1.2)
    for i, (icon, title, desc) in enumerate(reasons):
        bg = C_LIGHT_BG if i % 2 == 0 else C_WHITE
        add_rect(sl, Inches(0.3), y, Inches(12.5), Inches(0.98), fill_color=bg,
                 line_color=RGBColor(0xE2, 0xE8, 0xF0), line_width=Pt(0.5))
        # icon
        add_textbox(sl, icon, Inches(0.4), y + Inches(0.1), Inches(0.6), Inches(0.6),
                    font_size=Pt(22), color=C_BLUE)
        # title
        add_textbox(sl, title, Inches(1.1), y + Inches(0.08), Inches(11.5), Inches(0.35),
                    font_size=Pt(15), bold=True, color=C_BLUE, align=PP_ALIGN.RIGHT)
        # desc
        add_textbox(sl, desc, Inches(1.1), y + Inches(0.43), Inches(11.4), Inches(0.48),
                    font_size=Pt(12.5), color=C_DARK, align=PP_ALIGN.RIGHT)
        y += Inches(1.02)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 7 – Feature Importance
# ══════════════════════════════════════════════════════════════════════════
def slide_feature_importance(prs):
    sl = blank_slide(prs)
    slide_header(sl, "أهمية المتغيرات", "Feature Importance  (SHAP-ready)", accent=C_BLUE)
    bottom_bar(sl, 7)

    features = [
        ("overtime_hours_week",      30.1, "ساعات العمل الإضافي أسبوعياً"),
        ("vacation_days_last_year",  22.9, "أيام الإجازة السنة الماضية"),
        ("avg_daily_hours",          21.9, "متوسط ساعات العمل اليومي"),
        ("late_arrivals_month",      13.3, "مرات التأخر شهرياً"),
        ("tasks_assigned",            6.5, "عدد المهام المُسنَدة"),
        ("absence_days_month",        5.3, "أيام الغياب شهرياً"),
    ]

    bar_colors = [C_BLUE, C_BLUE, C_GREEN, C_GREEN,
                  RGBColor(0x64, 0x74, 0x8B), RGBColor(0x64, 0x74, 0x8B)]

    max_w = Inches(7.0)
    by = Inches(1.25)
    for i, (feat, pct, ar_label) in enumerate(features):
        bar_w = max_w * (pct / 35)
        # rank badge
        rank_bg = C_BLUE if i < 3 else C_GRAY
        add_rect(sl, Inches(0.3), by + Inches(0.04), Inches(0.4), Inches(0.4), fill_color=rank_bg)
        add_textbox(sl, str(i + 1), Inches(0.3), by + Inches(0.04), Inches(0.4), Inches(0.4),
                    font_size=Pt(13), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        # Arabic label
        add_textbox(sl, ar_label, Inches(0.78), by, Inches(2.5), Inches(0.48),
                    font_size=Pt(12), bold=(i < 3), color=C_DARK, align=PP_ALIGN.RIGHT)
        # bar
        add_rect(sl, Inches(3.4), by + Inches(0.08), bar_w, Inches(0.32),
                 fill_color=bar_colors[i])
        # percentage
        add_textbox(sl, f"{pct}%",
                    Inches(3.4) + bar_w + Inches(0.08), by + Inches(0.05), Inches(0.65), Inches(0.38),
                    font_size=Pt(13), bold=True, color=bar_colors[i])
        # English label (small)
        add_textbox(sl, feat,
                    Inches(10.6), by + Inches(0.1), Inches(2.6), Inches(0.3),
                    font_size=Pt(10), color=C_GRAY, italic=True)
        by += Inches(0.84)

    # Insight
    add_rect(sl, Inches(0.3), Inches(6.4), Inches(12.5), Inches(0.6),
             fill_color=RGBColor(0xDB, 0xEA, 0xFF))
    add_textbox(sl,
                "🔑  المتغيرات الثلاثة الأولى (overtime + vacation + avg_hours) تُفسِّر 74.9% من قرار النموذج — "
                "وهي تعكس العبء الوظيفي وغياب الراحة، المحركان الرئيسيان للاحتراق.",
                Inches(0.4), Inches(6.42), Inches(12.3), Inches(0.56),
                font_size=Pt(12.5), color=C_DARK, align=PP_ALIGN.RIGHT)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 8 – Model Evaluation
# ══════════════════════════════════════════════════════════════════════════
def slide_evaluation(prs):
    sl = blank_slide(prs)
    slide_header(sl, "نتائج تقييم النموذج", "Model Evaluation Results", accent=C_GREEN)
    bottom_bar(sl, 8)

    metrics = [
        ("Accuracy", "95.5%", C_BLUE,
         "من كل 100 موظف، يصنّف النموذج 95-96 منهم بشكل صحيح."),
        ("Precision", "93.4%", C_TEAL,
         "عندما يقول النموذج 'احتراق'، هو محق في 93.4% من الحالات."),
        ("Recall", "96.6%", C_GREEN,
         "النموذج يكتشف 96.6% من حالات الاحتراق الحقيقية (يفوّت 3.4% فقط)."),
        ("F1-Score", "95.0%", C_AMBER,
         "المتوسط الهارموني بين Precision وRecall — المقياس الأشمل والأعدل."),
    ]

    cx = Inches(0.3)
    for metric, val, color, explain in metrics:
        # card bg
        add_rect(sl, cx, Inches(1.15), Inches(3.1), Inches(2.0),
                 fill_color=color)
        add_textbox(sl, metric, cx + Inches(0.1), Inches(1.2), Inches(2.9), Inches(0.45),
                    font_size=Pt(16), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        add_textbox(sl, val, cx + Inches(0.1), Inches(1.65), Inches(2.9), Inches(0.75),
                    font_size=Pt(40), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        cx += Inches(3.27)

    # Explanations
    cx = Inches(0.3)
    for metric, val, color, explain in metrics:
        add_rect(sl, cx, Inches(3.2), Inches(3.1), Inches(1.1),
                 fill_color=C_WHITE, line_color=color, line_width=Pt(2))
        add_textbox(sl, explain, cx + Inches(0.1), Inches(3.3), Inches(2.9), Inches(0.9),
                    font_size=Pt(12), color=C_DARK, align=PP_ALIGN.RIGHT)
        cx += Inches(3.27)

    # Confusion matrix summary
    add_rect(sl, Inches(0.3), Inches(4.42), Inches(12.5), Inches(0.6),
             fill_color=C_SLATE)
    add_textbox(sl, "📌  Confusion Matrix (Test Set – 200 records):",
                Inches(0.4), Inches(4.44), Inches(12.3), Inches(0.3),
                font_size=Pt(14), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)

    cm_data = [
        ["", "Predicted: No Burnout", "Predicted: Burnout"],
        ["Actual: No Burnout", "True Negative (TN) ✅", "False Positive (FP) ⚠️"],
        ["Actual: Burnout",    "False Negative (FN) ❌", "True Positive (TP) ✅"],
    ]
    cm_colors = [
        [C_SLATE,                             C_SLATE,                                C_SLATE],
        [C_SLATE, RGBColor(0xDC, 0xFA, 0xE7), RGBColor(0xFE, 0xF3, 0xC7)],
        [C_SLATE, RGBColor(0xFE, 0xE2, 0xE2), RGBColor(0xDC, 0xFA, 0xE7)],
    ]
    cm_txt_colors = [
        [C_WHITE, C_WHITE, C_WHITE],
        [C_WHITE, RGBColor(0x14, 0x53, 0x2D), RGBColor(0x78, 0x35, 0x00)],
        [C_WHITE, RGBColor(0x7F, 0x1D, 0x1D), RGBColor(0x14, 0x53, 0x2D)],
    ]
    cw = Inches(3.1); rh = Inches(0.42)
    for ri, row in enumerate(cm_data):
        for ci, cell in enumerate(row):
            x = Inches(0.5) + ci * cw
            y = Inches(5.08) + ri * rh
            add_rect(sl, x, y, cw, rh, fill_color=cm_colors[ri][ci],
                     line_color=C_LIGHT_BG, line_width=Pt(0.5))
            add_textbox(sl, cell, x + Inches(0.05), y + Inches(0.08),
                        cw - Inches(0.1), rh - Inches(0.1),
                        font_size=Pt(11), bold=(ri == 0 or ci == 0),
                        color=cm_txt_colors[ri][ci], align=PP_ALIGN.CENTER)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 9 – Code Files
# ══════════════════════════════════════════════════════════════════════════
def slide_code_files(prs):
    sl = blank_slide(prs)
    slide_header(sl, "الملفات البرمجية الرئيسية", "Project Code Files", accent=C_SLATE)
    bottom_bar(sl, 9)

    files = [
        ("🏋️", "train_model.py",
         "train_model.py",
         "ملف التدريب الرئيسي — يقرأ employees.csv، يُدرِّب Logistic Regression وRandom Forest،\nيقارن الأداء، ويحفظ النموذج الفائز في models/workload_model.pkl."),
        ("🗄️", "data/generate_data.py",
         "data/generate_data.py",
         "يولِّد بيانات 1000 موظف اصطناعية بتوزيعات واقعية (Gaussian/Uniform)،\nمع ضمان نسبة اختلاط مناسبة بين burnout وno-burnout."),
        ("🤖", "models/workload_model.pkl",
         "models/workload_model.pkl",
         "النموذج المُدرَّب المحفوظ (Serialized) بـ Pickle — يُحمَّل في الـ backend\nللتنبؤ الفوري دون إعادة التدريب."),
        ("⚡", "backend/risk.py",
         "backend/risk.py",
         "API endpoint يستقبل بيانات موظف جديد، يُحوِّلها لـ feature vector،\nيُمرِّرها للنموذج، ويُعيد مستوى الخطر (Low/Medium/High)."),
        ("🔬", "backend/explain.py",
         "backend/explain.py",
         "يُولِّد تفسيراً قابلاً للقراءة البشرية لقرار النموذج — يستخدم Feature Importance\nلشرح السبب الرئيسي وراء تشخيص الاحتراق لكل موظف."),
    ]

    y = Inches(1.15)
    for icon, name, path, desc in files:
        add_rect(sl, Inches(0.3), y, Inches(12.5), Inches(1.08),
                 fill_color=C_WHITE, line_color=RGBColor(0xE2, 0xE8, 0xF0), line_width=Pt(0.8))
        # icon
        add_textbox(sl, icon, Inches(0.35), y + Inches(0.1), Inches(0.55), Inches(0.55),
                    font_size=Pt(22))
        # file name + path
        add_textbox(sl, name, Inches(1.0), y + Inches(0.08), Inches(5.0), Inches(0.35),
                    font_size=Pt(15), bold=True, color=C_BLUE)
        add_textbox(sl, f"📁  {path}", Inches(1.0), y + Inches(0.43), Inches(5.0), Inches(0.3),
                    font_size=Pt(11), color=C_GRAY, italic=True)
        # description
        add_textbox(sl, desc, Inches(6.3), y + Inches(0.08), Inches(6.3), Inches(0.9),
                    font_size=Pt(11.5), color=C_DARK, align=PP_ALIGN.RIGHT)
        y += Inches(1.14)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 10 – System Flowchart
# ══════════════════════════════════════════════════════════════════════════
def slide_flowchart(prs):
    sl = blank_slide(prs)
    slide_header(sl, "كيف يعمل النظام في المشروع النهائي؟",
                 "End-to-End Data Flow", accent=C_BLUE)
    bottom_bar(sl, 10)

    steps = [
        (C_BLUE,  "①  إدخال البيانات",    "المدير يُدخِل بيانات الموظف\nعبر واجهة Next.js"),
        (C_TEAL,  "②  API Request",        "POST /api/predict\nبيانات JSON → backend/risk.py"),
        (C_GREEN, "③  Feature Extraction", "استخراج الـ 6 متغيرات\nوتحويلها لـ numpy array"),
        (C_AMBER, "④  Model Inference",    "تحميل workload_model.pkl\nوتشغيل predict_proba()"),
        (C_BLUE,  "⑤  Risk Score",         "تصنيف: Low / Medium / High\nمع Confidence %"),
        (C_GREEN, "⑥  التفسير",            "explain.py يُولِّد سبب\nالقرار بالعربي"),
        (C_TEAL,  "⑦  العرض",             "النتيجة + التفسير تظهر\nللمدير في الـ Dashboard"),
    ]

    bx = Inches(0.3)
    by = Inches(1.3)
    box_w = Inches(1.7)
    box_h = Inches(1.5)
    gap   = Inches(0.08)

    for i, (color, title, desc) in enumerate(steps):
        add_rect(sl, bx, by, box_w, box_h, fill_color=color)
        add_textbox(sl, title, bx + Inches(0.05), by + Inches(0.08),
                    box_w - Inches(0.1), Inches(0.4),
                    font_size=Pt(12), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
        add_textbox(sl, desc, bx + Inches(0.05), by + Inches(0.52),
                    box_w - Inches(0.1), Inches(0.9),
                    font_size=Pt(10), color=C_WHITE, align=PP_ALIGN.CENTER)
        bx += box_w + gap
        if i < len(steps) - 1:
            # arrow
            add_textbox(sl, "▶", bx - Inches(0.08) + Inches(0.0),
                        by + Inches(0.55), Inches(0.1), Inches(0.4),
                        font_size=Pt(14), bold=True, color=C_DARK)

    # Data flow label
    add_rect(sl, Inches(0.3), Inches(2.95), Inches(12.0), Inches(0.04),
             fill_color=C_GREEN)
    add_textbox(sl, "← تدفق البيانات Data Flow →",
                Inches(0.3), Inches(3.05), Inches(12.0), Inches(0.3),
                font_size=Pt(12), bold=True, color=C_GREEN, align=PP_ALIGN.CENTER)

    # Additional detail
    details = [
        ("🌐  Frontend", "Next.js + TypeScript\nواجهة عربية RTL"),
        ("⚙️  Backend",  "FastAPI / Python\nRESTful API"),
        ("🤖  ML Model", "Random Forest\nscikit-learn 1.x"),
        ("🗄️  Database", "بيانات الموظفين\nMongoDB / JSON"),
    ]
    dx = Inches(0.5)
    for icon_title, desc in details:
        add_rect(sl, dx, Inches(3.55), Inches(2.9), Inches(0.9),
                 fill_color=C_SLATE)
        add_textbox(sl, icon_title, dx + Inches(0.1), Inches(3.6),
                    Inches(2.7), Inches(0.3),
                    font_size=Pt(13), bold=True, color=C_WHITE)
        add_textbox(sl, desc, dx + Inches(0.1), Inches(3.9),
                    Inches(2.7), Inches(0.5),
                    font_size=Pt(11), color=RGBColor(0xBF, 0xDB, 0xFF))
        dx += Inches(3.1)

    # Pipeline note
    add_rect(sl, Inches(0.3), Inches(4.57), Inches(12.5), Inches(0.6),
             fill_color=RGBColor(0xDB, 0xEA, 0xFF))
    add_textbox(sl,
                "✅  النموذج لا يُعاد تدريبه عند كل طلب — يُحمَّل مرة واحدة عند بدء الـ server ويبقى في الذاكرة لأداء فوري (< 50ms).",
                Inches(0.4), Inches(4.6), Inches(12.3), Inches(0.55),
                font_size=Pt(13), color=C_DARK, align=PP_ALIGN.RIGHT)

    # training flow
    add_textbox(sl, "🔄  مسار التدريب المنفصل:",
                Inches(0.4), Inches(5.3), Inches(4.0), Inches(0.3),
                font_size=Pt(13), bold=True, color=C_BLUE)
    train_steps = ["generate_data.py", "→", "employees.csv", "→", "train_model.py",
                   "→", "workload_model.pkl", "→", "risk.py"]
    tx = Inches(0.4)
    for step in train_steps:
        is_arr = step == "→"
        fc = C_GRAY if is_arr else C_DARK
        add_textbox(sl, step, tx, Inches(5.65), Inches(1.4 if not is_arr else 0.25), Inches(0.3),
                    font_size=Pt(11), bold=(not is_arr), color=fc)
        tx += Inches(1.4 if not is_arr else 0.3)


# ══════════════════════════════════════════════════════════════════════════
# SLIDE 11 – Summary / Closing
# ══════════════════════════════════════════════════════════════════════════
def slide_summary(prs):
    sl = blank_slide(prs)
    # dark bg
    add_rect(sl, 0, 0, SLIDE_W, SLIDE_H, fill_color=C_DARK)
    add_rect(sl, 0, 0, Inches(0.18), SLIDE_H, fill_color=C_GREEN)
    add_rect(sl, SLIDE_W - Inches(0.18), 0, Inches(0.18), SLIDE_H, fill_color=C_BLUE)

    add_textbox(sl, "✨  خلاصة ونقاط قوة المشروع",
                Inches(0.4), Inches(0.3), Inches(12.5), Inches(0.6),
                font_size=Pt(30), bold=True, color=C_WHITE, align=PP_ALIGN.CENTER)
    add_textbox(sl, "Project Strengths & Conclusion",
                Inches(0.4), Inches(0.9), Inches(12.5), Inches(0.35),
                font_size=Pt(16), color=C_GREEN, align=PP_ALIGN.CENTER)

    add_rect(sl, Inches(0.6), Inches(1.35), Inches(12.0), Inches(0.03), fill_color=C_GREEN)

    strengths = [
        ("🎯", "دقة عالية",           "95.5% Accuracy و 95.0% F1-Score على بيانات اختبار حقيقية"),
        ("🔬", "نموذج قابل للتفسير", "Feature Importance تُظهِر بوضوح سبب كل قرار لفريق HR"),
        ("📊", "بيانات موضوعية 100%","لا نعتمد على تقييمات ذاتية — قرارات مبنية على مؤشرات قابلة للقياس"),
        ("⚡", "أداء فوري",           "النموذج يُنبِّئ في أقل من 50ms عبر API متكامل مع الـ Dashboard"),
        ("🧠", "قابلية التوسع",       "النموذج يمكن إعادة تدريبه بسهولة على بيانات حقيقية مستقبلاً"),
        ("✅", "منهجية علمية سليمة",  "Stratified Split + Hyperparameter Tuning + Cross-validation ready"),
    ]

    y = Inches(1.5)
    for i, (icon, title, detail) in enumerate(strengths):
        x = Inches(0.5) if i % 2 == 0 else Inches(6.8)
        if i % 2 == 0 and i > 0:
            y += Inches(1.0)
        add_rect(sl, x, y, Inches(5.9), Inches(0.9),
                 fill_color=RGBColor(0x1E, 0x29, 0x3B))
        add_textbox(sl, icon + "  " + title,
                    x + Inches(0.1), y + Inches(0.08), Inches(5.7), Inches(0.32),
                    font_size=Pt(15), bold=True, color=C_GREEN)
        add_textbox(sl, detail,
                    x + Inches(0.1), y + Inches(0.42), Inches(5.7), Inches(0.42),
                    font_size=Pt(12), color=RGBColor(0xCB, 0xD5, 0xE1))

    # closing
    add_rect(sl, Inches(0.6), SLIDE_H - Inches(0.75), Inches(12.0), Inches(0.03),
             fill_color=C_BLUE)
    add_textbox(sl,
                "Tawazon  —  نظام ذكي لتشخيص وتنبؤ الاحتراق الوظيفي  |  "
                "مبني بـ Python • scikit-learn • Next.js  |  11 / 11",
                Inches(0.4), SLIDE_H - Inches(0.65), Inches(12.5), Inches(0.4),
                font_size=Pt(12), color=C_GRAY, align=PP_ALIGN.CENTER)


# ══════════════════════════════════════════════════════════════════════════
# MAIN
# ══════════════════════════════════════════════════════════════════════════
def main():
    prs = new_prs()

    slide_cover(prs)             # 1
    slide_why_ml(prs)            # 2
    slide_dataset(prs)           # 3
    slide_split(prs)             # 4
    slide_comparison(prs)        # 5
    slide_why_rf(prs)            # 6
    slide_feature_importance(prs)# 7
    slide_evaluation(prs)        # 8
    slide_code_files(prs)        # 9
    slide_flowchart(prs)         # 10
    slide_summary(prs)           # 11

    out_dir = r"c:\Users\abduu\Desktop\Tawazon\docs"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "Tawazon_ML_Model_Explained.pptx")
    prs.save(out_path)
    print(f"[OK] Saved: {out_path}")
    print(f"     Slides: {len(prs.slides)}")


if __name__ == "__main__":
    main()
