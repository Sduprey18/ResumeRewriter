from huggingface_hub import InferenceClient
from dotenv import load_dotenv
import os

load_dotenv() 
api_key = os.getenv("api_key")

client = InferenceClient(
    provider="novita",
    api_key=f"{api_key}",
)

job_desc = """Curious about what you'll do? Here's a sample of tasks and projects our co-op's work on:

Implement a database-driven web application, its features and tests.
Join the team's code review process in an active and timely fashion.
Take part in the resolution of production issues and work with team members, including Technical Support teams, to see the resolution through to completion.
Collaborate with fellow team members across all roles to deliver on a shared responsibility for quality.
Participate in writing automated tests to ensure comprehensive test coverage of features.
Assist in product roadmap discussions and implementation.
Follow the mentorship of full-time team members.
Participate in initiatives that make us stronger as a team (e.g. internal dash-boarding, metrics for our success in production, improved build processes).
Contribute ideas and effort for continuous improvement for the team, in its Agile process and in its general team effectiveness.
We encourage you to apply if you have most (or all!!) of the following:

Experience with Java and SQL
Understanding of HTML, CSS and DOM
A passion for software quality
Knowledge of QA processes and methodologies is a plus
Co-op/intern or other industry experience in software is a plus
Ability to participate in a full time co-op experience over the fall term from September 2025 to December 2025
Enrolled in a Bachelors/Masters degree program and grad date no later than August 2027"
"""

resume_text ="""Sherkeem Duprey\n\n347-423-3123 | sherkeemduprey@gmail.com | linkedin.com/in/sherkeem-duprey/ | github.com/Sduprey18\n\nEDUCATION\nUniversity of Rochester Rochester, NY\nBachelor of Arts in Computer Science Aug. 2022 - May 2026\n\nRelevant Coursework:\nData Structures & Algorithms, Web Programming, Computation Formal Systems, Artificial Intelligence,\nMobile App Development\n\nEXPERIENCE\nFullstack Software Engineering Intern May 2025\nIntuit Mountain View , CA\n¢ Incoming summer 2025\nHVAC Automation Intern June 2024 — August 2024\nMerck Rahway, NJ\n\n¢ Facilitated data analysis and automated processes through the implementation of Pi Displays for 10 buildings,\nresulting in 30% increase in HVAC cooling efficiency and real-time monitoring of key metrics.\n\n« Developed a PowerApp to simplify disabled point reporting and viewing for 900+ points per month incorporating,\nPowerBI integration, and PI WebAPI for accurate tag location and validation.\n\n¢ Identified and addressed over 300 undocumented points in the PI system, ensuring accurate and comprehensive\ndocumentation for all data points.\n\nXR Applications Developer Sep. 2023 — Present\nStudio X Rochester, NY\n¢ Spearheaded the advancement of the coding team in Aurum, the in-house alchemy VR game, creating C# scripts\nto create game functionality, exhibited to over 500 patrons at exclusive events.\n¢ Teaching and providing support for over 60 workshops, attended by over 1,700 participants, through the academic\nyear, on topics such as Unity, Blender and XR development.\n\n¢ Provided technical consultations in-person and on Discord for XR development.\n\nPROJECTS\n\nJava Street Mapping | Java Github link\n« Developed a Java program for map processing, to determine the fastest/shortest destination route.\n¢ Utilized my own custom built HashMap, and LinkedLists for graph representation.\n¢ Enacted Dijkstra’s algorithm for finding the shortest path.\n¢ Implemented Kruskal’s algorithm for finding the minimum weight spanning tree.\n\nFinite Automata String Validator | C Github link\n\n¢ Developed a C-based application to simulate Deterministic Finite Automata (DFA) and Nondeterministic Finite\nAutomata (NFA) for string validation tasks.\n\n¢ Built interactive REPL functions for both DFA and NFA simulations, allowing dynamic user input to test string\nacceptance.\n\n¢ Utilized custom C structures and functions to manage states, transitions, and string evaluation for both automata\ntypes.\n\n¢ Utilized custom C structures and functions, improving automata processing efficiency by 20% through optimized\nstate transitions and reduced computational overhead.\n\nTECHNICAL SKILLS & ORGANIZATIONS\n\nLanguages: Swift, Java, Python, C/C#, JavaScript, HTML/CSS\n\nFrameworks: React, Node.js, Flask, SwiftUI\n\nDeveloper Tools: Git, Docker, Aveva PI System, VS Code, Visual Studio, Xcode, PlasticSCM, Unity\nOrganizations: ColorStack, National Society of Black Engineers, Participant of Amazon’s Campus Summer Series,\nGoogle Software Engineering Program (G-SWEP)\n
"""


with open("backend/partialTemplate.tex", "r", encoding="utf-8") as f:
    latex_template = f.read()

#print(latex_template)



completion = client.chat.completions.create(
    model="deepseek-ai/DeepSeek-V3-0324",
    messages=[
        {
            "role": "system",
            "content": "You are an expert resume writer. Fill this LaTeX template with content tailored to the job description. Prioritize matching keywords and quantifiable achievements. Generate nothing else other than the LaTeX itself, no extra text."
            
        },

        {
                "role": "user",
                "content" : f"""JOB DESCRIPTION: {job_desc}
                RESUME DATA: {resume_text}
                LATEX TEMPLATE: {latex_template}
                Generate a tailored resume in LaTeX, replacing placeholders with relevant content."
                """
            }
    ],
)

print(completion.choices[0].message.content)
