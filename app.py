
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Open the website
@app.route("/")
def home():
    return render_template("index.html")

# Chatbot response
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "").lower()

    if any(word in message for word in ["analytics", "data", "excel", "sql"]):
        reply = "For Data Analytics, learn Excel, SQL, Statistics and Power BI. Practice with small projects."

    elif any(word in message for word in ["software", "coding", "python", "java", "developer"]):
        reply = "For Software Development, learn Python or Java, practice programming and build projects."

    elif any(word in message for word in ["design", "creative", "ui", "ux"]):
        reply = "For UI/UX Design, learn design basics, Figma and user experience. Create a few sample designs."

    elif any(word in message for word in ["career", "job", "purpose"]):
        reply = "Explore your interests and skills. Choose one career pathway and start learning the required skills."

    elif "skill" in message:
        reply = "Choose skills related to your career goal. Practice regularly and build projects to improve."

    else:
        reply = "Hello! I am your PurposeMap career assistant. Ask me about careers, skills, courses or job opportunities."

    return jsonify({"reply": reply})

# Career pathway recommendations
@app.route("/api/pathways", methods=["POST"])
def pathways():
    data = request.get_json()
    text = str(data).lower()

    results = []

    if any(word in text for word in ["excel", "data", "analytics", "sql", "business"]):
        results.append({
            "name": "Business & Data Analytics",
            "skills": "Excel, SQL, Statistics, Power BI"
        })

    if any(word in text for word in ["coding", "python", "java", "software", "computer"]):
        results.append({
            "name": "Software Development",
            "skills": "Programming, Problem Solving, Projects"
        })

    if any(word in text for word in ["design", "creative", "ui", "ux"]):
        results.append({
            "name": "UI/UX Design",
            "skills": "Figma, Design Basics, Creativity"
        })

    if not results:
        results = [
            {
                "name": "Business & Data Analytics",
                "skills": "Excel, SQL, Statistics"
            },
            {
                "name": "Software Development",
                "skills": "Python, Java, Programming"
            },
            {
                "name": "UI/UX Design",
                "skills": "Figma, Creativity, Design"
            }
        ]

    return jsonify({"pathways": results})

if __name__ == "__main__":
    app.run(debug=True)
