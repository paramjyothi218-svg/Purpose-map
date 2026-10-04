from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/api/chat")
def chat():
    data = request.get_json() or {}
    message = data.get("message", "").lower()

    if any(x in message for x in ["analytics", "data", "excel", "sql"]):
        reply = "For analytics, start with Excel, basic statistics, SQL and Power BI. Then build one small dashboard project."
    elif any(x in message for x in ["coding", "software", "python", "java", "developer"]):
        reply = "For software, choose one language, learn the fundamentals, solve small problems and build 2–3 simple projects."
    elif any(x in message for x in ["career", "job", "purpose", "confused"]):
        reply = "You do not need to choose your whole future today. Pick one pathway, test it for 30 days, build one project and reflect on what you learned."
    elif "skill" in message:
        reply = "Choose one skill connected to the career you want to test. Practice it regularly and create evidence through a small project."
    else:
        reply = "Tell me your course, skills, interests and desired lifestyle. I can help you explore practical career pathways."

    return jsonify({"reply": reply})

@app.post("/api/pathways")
def pathways():
    data = request.get_json() or {}
    text = " ".join(str(v) for v in data.values()).lower()
    results = []

    if any(x in text for x in ["excel","data","analytics","sql","math","business"]):
        results.append({"name":"Business & Data Analytics","fit":92,"skills":"Excel • SQL • Statistics • Power BI"})
    if any(x in text for x in ["code","coding","python","java","software","technology","computer"]):
        results.append({"name":"Technology & Software","fit":90,"skills":"Programming • Problem Solving • Projects"})
    if any(x in text for x in ["design","creative","content","writing","ui","ux"]):
        results.append({"name":"Digital & Creative","fit":87,"skills":"Design • Storytelling • Content • UX"})
    if any(x in text for x in ["people","teach","help","lead","communication","team"]):
        results.append({"name":"People & Leadership","fit":85,"skills":"Communication • Teamwork • Leadership"})

    if not results:
        results = [
            {"name":"Business & Data Analytics","fit":78,"skills":"Excel • Communication • Problem Solving"},
            {"name":"Technology & Software","fit":76,"skills":"Programming • Logic • Projects"},
            {"name":"People & Leadership","fit":73,"skills":"Communication • Teamwork • Leadership"}
        ]

    return jsonify({"pathways": results[:3]})

if __name__ == "__main__":
    app.run(debug=True)
