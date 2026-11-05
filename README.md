# 🌟 Tawazon (توازن) — AI-Powered Workplace Burnout Detection Platform
> **منصة ذكية متكاملة للتنبؤ بمخاطر الاحتراق الوظيفي وحماية رأس المال البشري بالاعتماد على خوارزميات التعلم الآلي والبيانات التشغيلية الموضوعية.**  
> *مشروع تخرج تطبيقي متكامل (Graduation Project) مطور بواسطة فريق عمل من 5 مهندسين.*

---

## 📌 الفهرس (Table of Contents)
1. [نظرة عامة على المشروع (Project Overview)](#1-نظرة-عامة-على-المشروع)
2. [معمارية الذكاء الاصطناعي (AI & Machine Learning Architecture)](#2-معمارية-الذكاء-الاصطناعي)
3. [المتغيرات التشغيلية المعتمدة (The 6 Workload Metrics)](#3-المتغيرات-التشغيلية-المعتمدة)
4. [توزيع المهام بين أعضاء الفريق (Team Roles & Responsibilities)](#4-توزيع-المهام-بين-أعضاء-الفريق)
5. [التقنيات المستخدمة (Tech Stack)](#5-التقنيات-المستخدمة)
6. [هيكل المشروع ومجلداته (Project Structure)](#6-هيكل-المشروع-ومجلداته)
7. [طريقة التثبيت والتشغيل (How to Run)](#7-طريقة-التثبيت-والتشغيل)
8. [حسابات الدخول التجريبية (Demo Credentials)](#8-حسابات-الدخول-التجريبية)
9. [واجهات البرمجة الخلفية (API Endpoints)](#9-واجهات-البرمجة-الخلفية)

---

## 1. نظرة عامة على المشروع
نظام **Tawazon (توازن)** هو حل مؤسسي ذكي مصمم لمساعدة إدارات الموارد البشرية والقيادات التنفيذية على التنبؤ بمخاطر **الاحتراق الوظيفي (Job Burnout)** في مراحله المبكرة. 

يعتمد النظام على **القياسات التشغيلية الموضوعية (Objective Workplace Telemetry)** لساعات العمل الفعلية والإجازات وتراكم المهام، بعيداً عن التقييمات الذاتية غير الموثوقة، مما يوفر تشخيصاً دقيقاً ومحايداً وتوصيات استشفاء استباقية.

---

## 2. معمارية الذكاء الاصطناعي (AI Architecture)

* **الخوارزمية المعتمدة:** `Random Forest Classifier` (غابات عشوائية تجميعية مكونة من 100 شجرة قرار).
* **الدقة العامة (Accuracy):** **95.5%** على بيانات اختبار مستقلة تماماً لم يرها النموذج أثناء التدريب.
* **حساسية الالتقاط (Recall):** **96.6%** (يكتشف 97 من كل 100 حالة احتراق حقيقية، وهو المعيار الأهم في الصحة المهنية لمنع تفويت أي حالة حرجة).
* **المعيار التوافقي (F1-Score):** **95.0%**.
* **منهجية تقسيم البيانات (Data Splitting):**
  * `Train/Test Split (80% / 20%)`: 800 موظف للتدريب و 200 موظف للاختبار.
  * `Stratified Sampling`: للحفاظ على نسبة الاحتراق المتوازنة (44.1%) في كلا المجموعتين.
  * `random_state = 42`: لضمان تكرارية وثبات التجربة العلمية (Reproducibility).
* **الذكاء الاصطناعي القابل للتفسير (Explainable AI - XAI):**
  * استخدام قيم `SHAP (Shapley Additive Explanations)` لتوضيح العوامل الثلاثة الأولى التي رفعت مؤشر الخطر لكل موظف.

---

## 3. المتغيرات التشغيلية المعتمدة (The 6 Workload Metrics)

تم استبعاد النصوص والآراء الذاتية (NLP / Feedback) لتفادي **انحياز الاستجابة (Response Bias)**، كما تم استبعاد السن والجنس التزاماً بأخلاقيات الذكاء الاصطناعي (**AI Fairness**) لمنع التحيز التمييزي. 

المتغيرات الستة المعتمدة وترتيب أهميتها في القرار:
1. 🥇 **`overtime_hours_week` (30.1%):** ساعات العمل الإضافي أسبوعياً (المتسبب الأكبر في الإجهاد).
2. 🥈 **`vacation_days_last_year` (22.9%):** أيام الإجازة المستهلكة (مؤشر الاستشفاء والراحة).
3. 🥉 **`avg_daily_hours` (21.9%):** متوسط ساعات العمل اليومية الأساسية.
4. 🔹 **`tasks_assigned` (15.3%):** عدد المهام المتزامنة النشطة (تشتت التركيز).
5. 🔹 **`absence_days_month` (7.4%):** أيام الغياب الشهري المفاجئ (عارض ناتج عن الإجهاد).
6. 🔹 **`late_arrivals_month` (2.4%):** مرات التأخر في الشهر.

---

## 4. توزيع المهام بين أعضاء الفريق (Team Roles & Responsibilities)

تم تقسيم المشروع بصورة معيارية واحترافية ليغطي دورة حياة هندسة البرمجيات والذكاء الاصطناعي الكاملة بين 5 أعضاء:

### 👤 العضو الأول: مهندس تعلم الآلة وهندسة البيانات (Machine Learning & Data Engineer)
* **المسؤوليات:** معالجة مجموعة البيانات، تنظيف المدخلات، تقسيم البيانات (80/20 Stratified)، تدريب ومقارنة الخوارزميات (Logistic Regression vs Random Forest)، ضبط الـ Hyperparameters، وحفظ النموذج النهائي بصيغة binary.
* **الملفات المسندة:**
  * `train_model.py`
  * `data/employees.csv`
  * `data/generate_data.py`
  * `data/process_kaggle_data.py`
  * `models/workload_model.pkl`

---

### 👤 العضو الثاني: مهندس الذكاء الاصطناعي القابل للتفسير ومحرك المخاطر (XAI & Risk Engine Engineer)
* **المسؤوليات:** بناء محرك حساب مؤشر الخطر الرياضي (تحويل الاحتمالية إلى نسبة 0–100 وتحديد المستويات Low/Medium/High)، تطبيق خوارزمية SHAP لاستخراج مسببات الخطر الفردية، وتوليد مصفوفة الالتباس ورسوم الـ Feature Importance.
* **الملفات المسندة:**
  * `backend/risk.py`
  * `backend/explain.py`
  * `models/feature_importance.png`
  * `models/confusion_matrix.png`

---

### 👤 العضو الثالث: مهندس الخادم والواجهات البرمجية (Backend API & Security Engineer)
* **المسؤوليات:** بناء خادم FastAPI، تصميم مسارات RESTful API الكاملة (`/assess`, `/predict`, `/stats`, `/users`, `/auth`)، نماذج التحقق Pydantic Schemas، تأمين المصادقة وحماية كلمات المرور باستخدام JWT و Bcrypt، وإدارة جلسات SQLAlchemy ORM.
* **الملفات المسندة:**
  * `backend/main.py`
  * `backend/database.py`
  * `backend/auth.py`
  * `requirements.txt`

---

### 👤 العضو الرابع: مهندس الواجهة الأمامية وتجربة المستخدم (Frontend UI/UX Engineer)
* **المسؤوليات:** بناء وتصميم نظام المكونات البصري (Design System)، نظام التوطين والترجمة الفورية ثنائية اللغة (Arabic RTL / English LTR)، صفحات التقييم التفاعلية، النوافذ المنبثقة (Modals)، التنبيهات اللحظية (Toasts)، وتنسيقات الطباعة كتقارير PDF.
* **الملفات المسندة:**
  * `frontend/index.html`
  * `frontend/employees.html`
  * `frontend/assess.html`
  * `frontend/employee-portal.html`
  * `frontend/login.html`
  * `frontend/css/style.css`
  * `frontend/js/i18n.js`

---

### 👤 العضو الخامس: مهندس تحليلات البيانات والداشبورد وجودة النظام (Dashboard Analytics & QA Engineer)
* **المسؤوليات:** تكامل الرسوم البيانية التفاعلية الحية (Chart.js Donut & Benchmark Charts)، حساب مؤشرات الـ KPIs اللحظية، برمجة قائمة المتابعة الحرجة (Critical Watchlist)، مزامنة وتحديث قاعدة البيانات، وتجهيز العروض التقديمية والتوثيق الأكاديمي.
* **الملفات المسندة:**
  * `frontend/js/app.js`
  * `frontend/js/auth.js`
  * `frontend/js/config.js`
  * `docs/Tawazon_ML_Model_Explained_v2.pptx`
  * `scripts/sync_database_scores_fast.py`

---

## 5. التقنيات المستخدمة (Tech Stack)

* **Artificial Intelligence & ML:** `Python 3.10+`, `Scikit-Learn`, `SHAP`, `Pandas`, `NumPy`, `Joblib`.
* **Backend & API:** `FastAPI`, `Uvicorn`, `Pydantic v2`, `SQLAlchemy`, `Bcrypt`, `Python-Multipart`.
* **Database:** `SQLite` (خفيفة وسريعة وجاهزة للترقية إلى PostgreSQL).
* **Frontend:** `HTML5`, `CSS3 (Modern Custom Design System)`, `Vanilla Modern JavaScript (ES6+)`, `Chart.js 4`.
* **Security & Auth:** `JWT Bearer Tokens`, `Password Hashing with Salt`.

---

## 6. هيكل المشروع ومجلداته (Project Structure)

```text
Tawazon/
├── backend/                  # خادم الباك إند ومنطق الذكاء الاصطناعي
│   ├── auth.py               # نظام المصادقة والصلاحيات (JWT + Bcrypt)
│   ├── database.py           # نماذج قاعدة البيانات (SQLAlchemy ORM)
│   ├── explain.py            # محرك تفسير القرارات (SHAP Explainability)
│   ├── main.py               # نقاط اتصال الواجهة البرمجية (FastAPI App)
│   └── risk.py               # محرك حساب مؤشرات ومستويات الخطر
├── data/                     # مجموعات البيانات وسكريبتات التجهيز
│   ├── employees.csv         # مجموعة بيانات 1,000 موظف بالمتغيرات الـ 6
│   ├── generate_data.py      # سكريبت توليد وتخليق البيانات
│   └── process_kaggle_data.py# سكريبت معالجة وتجهيز بيانات Kaggle
├── docs/                     # العروض التقديمية وملفات التوثيق الأكاديمي
│   ├── Tawazon_ML_Model_Explained_v2.pptx  # العرض التقديمي الشامل الجديد
│   ├── Tawazon_Dataset_Description_Arabic.docx
│   └── Tawazon_Dataset_Description_English.docx
├── frontend/                 # الواجهة الأمامية التفاعلية
│   ├── assets/               # شعارات وصور النظام
│   ├── css/style.css         # نظام التصميم الموحد والتنسيقات
│   ├── js/
│   │   ├── app.js            # منطق لوحة التحكم والرسوم البيانية
│   │   ├── auth.js           # إدارة جلسات تسجيل الدخول بالمتصفح
│   │   ├── config.js         # إعدادات رابط السيرفر
│   │   └── i18n.js           # محرك الترجمة الفورية عربي/إنجليزي
│   ├── assess.html           # شاشة إجراء تقييم إرهاق جديد
│   ├── employee-portal.html  # بوابة الموظف الذاتية
│   ├── employees.html        # دليل وإدارة شؤون الموظفين
│   ├── index.html            # لوحة التحليلات التنفيذية المتقدمة
│   └── login.html            # شاشة تسجيل الدخول
├── models/                   # النماذج المدربة ورسوم التقييم
│   ├── workload_model.pkl    # نموذج Random Forest المحفوظ
│   ├── feature_importance.png
│   └── confusion_matrix.png
├── train_model.py            # سكريبت تدريب وتقسيم وتقييم النموذج
├── requirements.txt          # حزم ومكتبات بايثون المطلوبة
└── README.md                 # دليل المشروع الكامل
```

---

## 7. طريقة التثبيت والتشغيل (How to Run)

### المتطلبات الأساسية:
تثبيت بيئة `Python 3.10` أو أحدث.

### 1. تثبيت الحزم المطلوبة:
```bash
pip install -r requirements.txt
```

### 2. تدريب النموذج (اختياري، النموذج محفوظ وجاهز):
```bash
python train_model.py
```

### 3. تشغيل خادم الباك إند (FastAPI):
```bash
uvicorn backend.main:app --reload
```
يعمل السيرفر افتراضياً على: `http://127.0.0.1:8000`  
ويمكن فتح وثائق الـ API التفاعلية عبر: `http://127.0.0.1:8000/docs`

### 4. تشغيل الموقع (Frontend):
افتح أي صفحة من مجلد `frontend/` (مثل `frontend/index.html` أو `frontend/login.html`) مباشرة في المتصفح، أو عبر Live Server.

---

## 8. حسابات الدخول التجريبية (Demo Credentials)

| الدور (Role) | اسم المستخدم (Username) | كلمة المرور (Password) | الصلاحيات |
| :--- | :--- | :--- | :--- |
| **مسؤول النظام (Admin)** |admin` | 04072005` | الوصول للداشبورد التنفيذية، إدارة الموظفين، والتقارير |
---

## 9. واجهات البرمجة الخلفية (API Endpoints)

* `POST /auth/login`: تسجيل الدخول واستخراج توكن الصلاحية.
* `GET /stats`: إحصائيات الداشبورد، نسب توزيع المخاطر، وقائمة المتابعة العاجلة.
* `GET /employees`: استرجاع قائمة الموظفين مع البحث والتصفية وتقسيم الصفحات (Pagination).
* `POST /assess`: تسجيل تقييم إرهاق جديد وحساب الخطر وتوليد الأسباب فورياً عبر ML.
* `POST /predict`: تنبؤ فوري سريع دون حفظ في قاعدة البيانات.
* `GET /employee/profile`: استرجاع بيانات وسجل تقييمات الموظف المسجل حالياً.
