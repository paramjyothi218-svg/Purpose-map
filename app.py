

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# PROFILE-BASED CAREER ASSISTANT
@app.route("/api/chat", methods=["POST"])
def chat():
    data = request.get_json() or {}

    message = data.get("message", "").lower()
    profile = data.get("profile", {})

    name = profile.get("name", "there")
    education = profile.get("education", "")
    skills = profile.get("skills", "")
    interests = profile.get("interests", "")
    goal = profile.get("goal", "")

    context = (
        f"Your education is {education}. "
        f"Your skills are {skills}. "
        f"Your interests are {interests}. "
        f"Your career goal is {goal}."
    )

    if any(word in message for word in ["my profile", "about me", "my details"]):
        reply = f"Hello {name}! Here is your profile: {context}"

    elif any(word in message for word in ["analytics", "data", "excel", "sql"]):
        reply = (
            f"Hello {name}! Based on your profile, Data Analytics may be "
            f"worth exploring. Start with Excel, SQL, Statistics and Power BI. "
            f"Your current skills: {skills or 'Not added yet'}. "
            f"Try building a small data dashboard project."
        )

    elif any(word in message for word in ["software", "coding", "python", "java", "developer"]):
        reply = (
            f"Hello {name}! Software Development may be a good pathway to explore. "
            f"Learn Python or Java, practice problem solving and build projects. "
            f"Your interests: {interests or 'Not added yet'}."
        )

    elif any(word in message for word in ["design", "creative", "ui", "ux"]):
        reply = (
            f"Hello {name}! UI/UX Design may match creative interests. "
            f"Learn Figma, design principles and user research. "
            f"Your interests: {interests or 'Not added yet'}."
        )

    elif any(word in message for word in ["career", "job", "pathway", "goal"]):
        reply = (
            f"Hello {name}! Your career goal is {goal or 'not added yet'}. "
            f"Based on your profile: {context} "
            f"Explore the Career Pathways section to compare options."
        )

    elif "skill" in message:
        reply = (
            f"Your current skills are: {skills or 'Not added yet'}. "
            f"Choose one skill connected to your career goal and practise it "
            f"through a small project."
        )

    else:
        reply = (
            f"Hello {name}! I can help you explore careers, skills, courses "
            f"and job opportunities. Your career goal is "
            f"{goal or 'not added yet'}. Ask me about a career you are interested in."
        )

    return jsonify({"reply": reply})

# PROFILE-BASED CAREER PATHWAYS
@app.route("/api/pathways", methods=["POST"])
def pathways():
    data = request.get_json() or {}

    text = " ".join(str(value) for value in data.values()).lower()

    careers = [
        {
            "name": "Data Analyst",
            "description": "Collect, organise and study data to help organisations make better decisions.",
            "skills": "Excel, SQL, Statistics, Power BI, Problem Solving",
            "tools": "Microsoft Excel, SQL, Power BI, Python",
            "responsibilities": "Clean data, prepare reports, create dashboards and explain findings.",
            "jobs": "Junior Data Analyst, Business Analyst, Reporting Analyst, BI Analyst",
            "growth": "Data Analyst → Senior Analyst → Analytics Lead → Data Manager",
            "keywords": ["data", "analytics", "excel", "sql", "business", "statistics", "math"]
        },
        {
            "name": "Software Developer",
            "description": "Design, develop and maintain websites, applications and software systems.",
            "skills": "Python, Java, Programming, Problem Solving, Databases",
            "tools": "VS Code, Git, GitHub, MySQL",
            "responsibilities": "Write code, test applications, fix errors and develop software features.",
            "jobs": "Junior Developer, Python Developer, Java Developer, Web Developer",
            "growth": "Junior Developer → Software Developer → Senior Developer → Tech Lead",
            "keywords": ["coding", "software", "python", "java", "computer", "technology", "programming"]
        },
        {
            "name": "UI/UX Designer",
            "description": "Create attractive and easy-to-use designs for websites and mobile applications.",
            "skills": "Creativity, Wireframing, User Research, Prototyping, Communication",
            "tools": "Figma, Canva, Adobe XD",
            "responsibilities": "Understand user needs, create layouts, design screens and test usability.",
            "jobs": "UI Designer, UX Designer, Product Designer, Interaction Designer",
            "growth": "Junior Designer → UI/UX Designer → Senior Designer → Design Lead",
            "keywords": ["design", "creative", "ui", "ux", "art", "figma"]
        },
        {
            "name": "Digital Marketing Specialist",
            "description": "Promote products and services through online platforms and digital campaigns.",
            "skills": "Communication, Content Writing, SEO, Social Media, Analytics",
            "tools": "Google Analytics, Canva, Google Ads, Social Media Platforms",
            "responsibilities": "Plan campaigns, create content, study audience behaviour and measure results.",
            "jobs": "SEO Executive, Social Media Executive, Content Marketer, Digital Marketing Analyst",
            "growth": "Marketing Executive → Specialist → Marketing Manager → Head of Marketing",
            "keywords": ["marketing", "communication", "content", "social media", "business", "writing"]
        }
    ]

    matched = []

    for career in careers:
        score = 0

        for keyword in career["keywords"]:
            if keyword in text:
                score += 1

        if score > 0:
            matched.append((score, career))

    matched.sort(key=lambda item: item[0], reverse=True)

    if matched:
        results = [item[1] for item in matched]
    else:
        results = careers

    return jsonify({"pathways": results})

if __name__ == "__main__":
    app.run(debug=True)
