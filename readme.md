# Prompt Quality Evaluation Agent (LangChain + Ollama)

## 📌 Overview
This project implements a simple **LangChain-based agent** that evaluates the quality of a given prompt.  
The agent scores the prompt across multiple quality dimensions and provides constructive feedback and improvement suggestions.

The agent uses a **local LLM (Qwen 3 – 8B)** served via **Ollama** and is executed using **Python 3**.

---

## 🎯 Features
- Accepts a **single text prompt** as input
- Evaluates prompt quality based on **5 criteria**
- Assigns scores from **0–10** for each criterion
- Computes a **final average score**
- Provides:
  - Short explanation
  - 2–3 improvement suggestions

---

## 📊 Prompt Quality Criteria
1. **Clarity** – Is the goal clear and easy to understand?
2. **Details** – Are sufficient requirements provided?
3. **Context** – Is background, audience, or use-case mentioned?
4. **Output Format & Constraints** – Are format, tone, or length specified?
5. **Persona Defined** – Is a role or persona assigned?

**Final Score** is the average of all five criteria.

---

## 🧑‍💻 Tech Stack
- Python 3
- LangChain
- Ollama
- Qwen3:8b (local LLM)

---

## ⚙️ Setup Instructions

### 1️⃣ Create and activate a virtual environment
```bash
python -m venv .venv
.venv\Scripts\activate   # Windows

## Install Dependecies
pip install -r requirements.txt

## Ensure Ollama is running
ollama pull qwen3:8b
ollama serve

## Run
python fresh.py
#sample Input 1
Write an email asking my manager for project feedback.

#sample Output1
Clarity Score: 9/10
Details Score: 6/10
Context Score: 5/10
Output Format & Constraints Score: 7/10
Persona Defined Score: 6/10
Final Score (Average): 6.6/10

Short Explanation:
The prompt is clear but lacks sufficient context and constraints.

Improvement Suggestions:
1. Specify the project name and type of feedback required.
2. Add context about the audience or timeline.
3. Define tone or expected length of the email.

#Sample Input2 
write a leave letter for a middle school student for 2days , reason - sick

#Sample Output2
Sending prompt to evaluation agent:
write a leave letter for a middle school student for 2days , reason - sick

--- Prompt Evaluation ---

Clarity Score: 7/10
Details Score: 5/10
Context Score: 6/10
Output Format & Constraints Score: 4/10
Persona Defined Score: 3/10
Final Score (Average): 5/10

Short Explanation:
The prompt is somewhat clear but lacks specific details, context, and format instructions.

Improvement Suggestions:
1. Specify the student's name, teacher's name, and exact school/program context.
2. Define the required format (e.g., formal letter structure, salutation, closing).
3. Clarify tone (polite, respectful) and include optional elements like a parent's note or doctor's note.


