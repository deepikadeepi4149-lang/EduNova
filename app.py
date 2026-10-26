import streamlit as st

st.set_page_config(
    page_title="CampusMate | Autonomous Engineering Hub",
    page_icon="🎓",
    layout="wide",
)

DEPARTMENTS = {
    "CSE": ["Programming", "Data Structures", "Database Management Systems", "Operating Systems"],
    "AIML": ["Python for AI", "Linear Algebra", "Machine Learning Fundamentals", "Data Analytics"],
    "ECE": ["Circuit Theory", "Electronic Devices", "Digital Logic", "Signals and Systems"],
    "EEE": ["Electrical Circuits", "Electrical Machines", "Power Systems", "Control Systems"],
    "Mechanical": ["Engineering Mechanics", "Thermodynamics", "Manufacturing Processes", "Fluid Mechanics"],
    "Civil": ["Engineering Graphics", "Building Materials", "Surveying", "Strength of Materials"],
    "IT": ["Programming", "Web Technologies", "Computer Networks", "Information Security"],
    "Chemical": ["Chemical Process Principles", "Fluid Flow", "Heat Transfer", "Mass Transfer"],
    "Biomedical": ["Human Anatomy Basics", "Biomedical Instrumentation", "Biomaterials", "Medical Imaging Basics"],
}

# These are starter examples, not official syllabus entries.
SAMPLE_RESOURCES = [
    {"department": "CSE", "semester": "Semester 1", "subject": "Programming", "unit": "Unit 1", "type": "Notes", "title": "Programming fundamentals — sample outline", "description": "Variables, data types, operators, conditions, loops, and basic problem solving."},
    {"department": "AIML", "semester": "Semester 2", "subject": "Python for AI", "unit": "Unit 1", "type": "Notes", "title": "Python basics — sample outline", "description": "Core syntax, collections, functions, modules, and simple data handling."},
    {"department": "ECE", "semester": "Semester 1", "subject": "Circuit Theory", "unit": "Unit 1", "type": "Practice", "title": "Circuit fundamentals — sample practice", "description": "Voltage, current, resistance, Ohm's law, and series/parallel circuits."},
    {"department": "EEE", "semester": "Semester 1", "subject": "Electrical Circuits", "unit": "Unit 1", "type": "Practice", "title": "Electrical basics — sample practice", "description": "Circuit quantities, units, basic components, and simple circuit analysis."},
    {"department": "Mechanical", "semester": "Semester 1", "subject": "Engineering Mechanics", "unit": "Unit 1", "type": "Notes", "title": "Force systems — sample outline", "description": "Force vectors, moments, equilibrium, and free-body diagrams."},
    {"department": "Civil", "semester": "Semester 1", "subject": "Engineering Graphics", "unit": "Unit 1", "type": "Notes", "title": "Drawing basics — sample outline", "description": "Drawing instruments, lettering, scales, and geometric constructions."},
    {"department": "IT", "semester": "Semester 1", "subject": "Programming", "unit": "Unit 1", "type": "Notes", "title": "Programming fundamentals — sample outline", "description": "Basic constructs, problem-solving methods, and introductory coding."},
    {"department": "Chemical", "semester": "Semester 1", "subject": "Chemical Process Principles", "unit": "Unit 1", "type": "Notes", "title": "Process principles — sample outline", "description": "Units, dimensions, material balances, and basic process calculations."},
    {"department": "Biomedical", "semester": "Semester 1", "subject": "Biomedical Instrumentation", "unit": "Unit 1", "type": "Notes", "title": "Instrumentation — sample outline", "description": "Measurement concepts, sensors, transducers, and basic biomedical applications."},
]

QUIZ = [
    {"q": "Which data structure follows Last In, First Out (LIFO)?", "options": ["Queue", "Stack", "Tree", "Graph"], "answer": "Stack", "why": "A stack removes the most recently added item first."},
    {"q": "Which law relates voltage, current, and resistance?", "options": ["Faraday's law", "Ohm's law", "Newton's law", "Kirchhoff's voltage law only"], "answer": "Ohm's law", "why": "Ohm's law is commonly written V = I × R for an ohmic conductor under constant physical conditions."},
    {"q": "In a database, what is a primary key used for?", "options": ["To uniquely identify a row", "To style a page", "To compress an image", "To create a chart"], "answer": "To uniquely identify a row", "why": "A primary key identifies each row uniquely in a table."},
]

st.markdown("""
<style>
.block-container {max-width: 1200px; padding-top: 1.5rem; padding-bottom: 2.5rem;}
.hero {padding: 1.6rem; border-radius: 20px; background: linear-gradient(120deg,#14213d,#263f68); color: #fff; border: 1px solid #d4a94f;}
.hero h1 {color:#fff; margin-bottom:.35rem;}
.hero p {color:#edf2fa; font-size:1.02rem;}
div[data-testid="stMetric"] {background:#fff; border:1px solid #e5e7eb; padding:12px; border-radius:14px;}
</style>
""", unsafe_allow_html=True)

if "saved_items" not in st.session_state:
    st.session_state.saved_items = []
if "quiz_result" not in st.session_state:
    st.session_state.quiz_result = None

with st.sidebar:
    st.markdown("# 🎓 CampusMate")
    st.caption("Autonomous Engineering Study Hub")
    page = st.radio("Menu", ["Dashboard", "Resource Library", "Practice Quiz", "Lab & Viva", "Saved Items", "Premium Preview", "Admin: Add Resource"])
    st.divider()
    st.caption("Prototype • Sample content only")

if page == "Dashboard":
    st.markdown("""
    <div class="hero">
      <h1>Welcome to CampusMate</h1>
      <p>One organized place for engineering notes, practice, lab preparation, and semester revision.</p>
    </div>
    """, unsafe_allow_html=True)
    st.write("")
    col1, col2, col3 = st.columns(3)
    col1.metric("Departments", len(DEPARTMENTS), "Expandable")
    col2.metric("Sample resources", len(SAMPLE_RESOURCES), "Demo content")
    col3.metric("Practice questions", len(QUIZ), "Starter quiz")
    st.subheader("Explore CampusMate")
    a, b, c = st.columns(3)
    a.markdown("### 📚 Resource Library")
    a.write("Filter by department, semester, subject, unit, and resource type.")
    b.markdown("### 🧠 Practice Quiz")
    b.write("Answer sample questions and view explanations.")
    c.markdown("### 🧪 Lab & Viva")
    c.write("Use practical-preparation checklists and sample viva prompts.")
    st.info("Autonomous colleges may have different syllabi. Confirm your college, regulation year, and subject codes before publishing official study resources.")

elif page == "Resource Library":
    st.title("📚 Resource Library")
    st.write("Filter the demo library. You can add resources through the Admin page; this prototype stores them only for the current session.")
    all_resources = SAMPLE_RESOURCES + st.session_state.get("custom_resources", [])
    f1, f2 = st.columns(2)
    with f1:
        dept = st.selectbox("Department", ["All departments"] + list(DEPARTMENTS.keys()))
        sem = st.selectbox("Semester", ["All semesters"] + [f"Semester {n}" for n in range(1, 9)])
    with f2:
        rtype = st.selectbox("Resource type", ["All types", "Notes", "Question Paper", "Practice", "Lab Record", "Viva", "Assignment"])
        search = st.text_input("Search subject or title", placeholder="e.g. Python, circuits, lab...")
    results = []
    for r in all_resources:
        if dept != "All departments" and r["department"] != dept:
            continue
        if sem != "All semesters" and r["semester"] != sem:
            continue
        if rtype != "All types" and r["type"] != rtype:
            continue
        if search and search.lower() not in (r["subject"] + " " + r["title"] + " " + r["description"]).lower():
            continue
        results.append(r)
    st.caption(f"{len(results)} resource(s) found")
    if not results:
        st.warning("No resources match these filters yet. Try a different filter or add a resource from the Admin page.")
    for i, r in enumerate(results):
        with st.container(border=True):
            left, right = st.columns([4, 1])
            with left:
                st.markdown(f"**{r['title']}**")
                st.caption(f"{r['department']} • {r['semester']} • {r['subject']} • {r['unit']} • {r['type']}")
                st.write(r["description"])
                if r.get("url"):
                    st.link_button("Open resource", r["url"])
                elif r.get("content"):
                    with st.expander("View content"):
                        st.write(r["content"])
                else:
                    st.caption("Demo outline only — upload or link the full approved material.")
            with right:
                key = f"save_{i}_{r['title']}"
                if st.button("☆ Save", key=key, use_container_width=True):
                    if r not in st.session_state.saved_items:
                        st.session_state.saved_items.append(r)
                    st.toast("Saved for this session")

elif page == "Practice Quiz":
    st.title("🧠 Practice Quiz")
    st.write("This is a mixed-discipline sample quiz. Replace or expand it with department-specific question banks.")
    with st.form("quiz"):
        answers = []
        for i, q in enumerate(QUIZ):
            st.markdown(f"**Q{i+1}. {q['q']}**")
            answers.append(st.radio("Select answer", q["options"], key=f"quiz_{i}", label_visibility="collapsed"))
        submit = st.form_submit_button("Submit answers", type="primary", use_container_width=True)
    if submit:
        score = sum(answers[i] == q["answer"] for i, q in enumerate(QUIZ))
        st.session_state.quiz_result = {"score": score, "answers": answers}
    if st.session_state.quiz_result:
        result = st.session_state.quiz_result
        st.success(f"Score: {result['score']} / {len(QUIZ)}")
        for i, q in enumerate(QUIZ):
            correct = result["answers"][i] == q["answer"]
            st.markdown(f"{'✅' if correct else '❌'} **Q{i+1}: {q['answer']}** — {q['why']}")

elif page == "Lab & Viva":
    st.title("🧪 Lab & Viva")
    dept = st.selectbox("Department", list(DEPARTMENTS.keys()))
    st.write(f"Practical preparation checklist for **{dept}**. Customize it to your college lab manual.")
    tasks = ["Read the aim and theory", "List apparatus/software required", "Understand the procedure", "Review safety precautions", "Practice expected output/observations", "Prepare a short conclusion", "Revise likely viva questions"]
    for i, task in enumerate(tasks):
        st.checkbox(task, key=f"lab_{dept}_{i}")
    viva_examples = {
        "CSE": ["What is an algorithm?", "What is the difference between a list and a tuple?", "What is time complexity?"],
        "AIML": ["What is supervised learning?", "Why do we split data into training and testing sets?", "What is overfitting?"],
        "ECE": ["State Ohm's law.", "What is a diode?", "What is a logic gate?"],
        "EEE": ["What is electrical power?", "State Kirchhoff's current law.", "What is a transformer used for?"],
        "Mechanical": ["What is a free-body diagram?", "Define stress and strain.", "What is the purpose of lubrication?"],
        "Civil": ["What is surveying?", "What is the difference between cement and concrete?", "What is a benchmark in levelling?"],
        "IT": ["What is an IP address?", "What is HTTP?", "Why is database normalization used?"],
        "Chemical": ["What is a material balance?", "What is heat transfer?", "What is a unit operation?"],
        "Biomedical": ["What is a biosensor?", "What is a transducer?", "Why is calibration important?"],
    }
    st.subheader("Sample viva prompts")
    for q in viva_examples[dept]:
        st.markdown(f"- {q}")
    st.caption("Sample prompts are for practice; verify against your experiment and college manual.")

elif page == "Saved Items":
    st.title("☆ Saved Items")
    if not st.session_state.saved_items:
        st.info("You have not saved any resources in this session. Open the Resource Library and select Save.")
    else:
        for r in st.session_state.saved_items:
            st.markdown(f"**{r['title']}** — {r['department']}, {r['semester']}, {r['subject']}")
            st.write(r["description"])

elif page == "Premium Preview":
    st.title("⭐ Premium Preview")
    free, premium = st.columns(2)
    with free:
        st.markdown("### Free")
        st.subheader("₹0")
        st.write("- Selected resources")
        st.write("- Sample quizzes")
        st.write("- Basic lab checklists")
        st.button("Current demo tier", disabled=True, use_container_width=True)
    with premium:
        st.markdown("### CampusMate Plus")
        st.subheader("Price to be decided")
        st.write("- Complete approved resource packs")
        st.write("- Additional quizzes and explanations")
        st.write("- Revision collections and progress tools")
        st.button("Coming later", disabled=True, use_container_width=True)
    st.warning("No real payments or paid access controls exist in this prototype. Add secure login, payment integration, refund terms, and privacy terms before selling subscriptions.")

elif page == "Admin: Add Resource":
    st.title("➕ Add a Resource")
    st.write("Add a resource for the current session. This form is for prototyping; content will not persist after the app restarts.")
    with st.form("add_resource", clear_on_submit=True):
        title = st.text_input("Resource title", placeholder="e.g. Unit 1 revision notes")
        department = st.selectbox("Department", list(DEPARTMENTS.keys()))
        semester = st.selectbox("Semester", [f"Semester {n}" for n in range(1, 9)])
        subject = st.text_input("Subject name")
        unit = st.text_input("Unit / module", value="Unit 1")
        kind = st.selectbox("Resource type", ["Notes", "Question Paper", "Practice", "Lab Record", "Viva", "Assignment"])
        description = st.text_area("Short description")
        url = st.text_input("Optional public resource URL")
        content = st.text_area("Optional text content")
        submitted = st.form_submit_button("Add resource", type="primary", use_container_width=True)
    if submitted:
        if not title.strip() or not subject.strip():
            st.error("Please enter at least a resource title and subject.")
        elif url.strip() and not url.strip().startswith(("https://", "http://")):
            st.error("The resource URL should start with https:// or http://")
        else:
            item = {"department": department, "semester": semester, "subject": subject.strip(), "unit": unit.strip() or "Unit 1", "type": kind, "title": title.strip(), "description": description.strip(), "url": url.strip(), "content": content.strip()}
            st.session_state.setdefault("custom_resources", []).append(item)
            st.success("Resource added for this session. A database is needed for permanent storage.")

st.divider()
st.caption("CampusMate • Autonomous Engineering Study Hub • Prototype")
