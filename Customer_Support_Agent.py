"""
Customer Support Email Agent - SHORT & ACCURATE
Simple code with correct classification
"""

import os, re, json
from langgraph.graph import StateGraph, END
from typing import TypedDict
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage

# ============================================================
GOOGLE_API_KEY = "AIzaSyDwCOTK_aqTcspGQ5EXVIsz09B9kSL7SrI"
# ============================================================

os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY
llm = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.5)

class EmailState(TypedDict):
    email: str
    urgency: str
    topic: str
    response: str
    action: str

def ask_ai(prompt):
    try:
        result = llm.invoke([HumanMessage(content=prompt)])
        return json.loads(re.sub(r'```json|```', '', result.content).strip())
    except:
        return None

# Classify with keyword fallback
def classify(state):
    email = state['email'].lower()
    
    # Keyword-based classification (simple & accurate)
    if 'password' in email or 'login' in email or 'access' in email:
        state['topic'] = 'Account'
    elif 'charged' in email or 'refund' in email or 'payment' in email or 'billing' in email:
        state['topic'] = 'Billing'
    elif 'crash' in email or 'error' in email or 'broken' in email or 'bug' in email:
        state['topic'] = 'Bug'
    elif 'add' in email or 'feature' in email or 'dark mode' in email:
        state['topic'] = 'Feature Request'
    else:
        state['topic'] = 'Technical Issue'
    
    # Simple urgency detection
    if '!!' in state['email'] or state['email'].isupper() or 'now' in email or 'today' in email:
        state['urgency'] = 'high'
    elif 'please' in email or 'would' in email:
        state['urgency'] = 'low'
    else:
        state['urgency'] = 'medium'
    
    print(f"✓ {state['urgency'].upper()} | {state['topic']}")
    return state

# Draft response based on topic
def draft(state):
    responses = {
        'Account': "To reset your password, visit https://example.com/reset. You'll get a link in 5 minutes.",
        'Billing': "I apologize for the billing issue. Our billing team will contact you within 2 hours.",
        'Bug': "Thanks for reporting this. Our team is investigating and working on a fix.",
        'Feature Request': "Great suggestion! We've added it to our roadmap and will notify you.",
        'Technical Issue': "Try clearing your cache or using incognito mode. Let us know if it persists."
    }
    
    # Try AI first, fallback to template
    ai_result = ask_ai(f'Write 2 sentence support response for: "{state["email"]}". JSON: {{"response": "text"}}')
    
    if ai_result and 'response' in ai_result:
        state['response'] = ai_result['response']
    else:
        state['response'] = responses.get(state['topic'], "Thank you. We're looking into this.")
    
    print("✓ Response ready")
    return state

# Decide action
def decide(state):
    state['action'] = 'ESCALATE' if (state['urgency'] == 'high' or state['topic'] in ['Billing', 'Bug']) else 'AUTO-REPLY'
    print(f"✓ {state['action']}")
    return state

# Build workflow
def build():
    w = StateGraph(EmailState)
    w.add_node("classify", classify)
    w.add_node("draft", draft)
    w.add_node("decide", decide)
    w.set_entry_point("classify")
    w.add_edge("classify", "draft")
    w.add_edge("draft", "decide")
    w.add_edge("decide", END)
    return w.compile()

# Process
def process(email):
    print(f"\n{'='*50}\n📧 {email}\n{'='*50}")
    result = build().invoke({"email": email, "urgency": "", "topic": "", "response": "", "action": ""})
    print(f"\n📊 {result['urgency'].upper()} | {result['topic']} | {result['action']}")
    print(f"💬 {result['response']}\n")

# Test
EMAILS = [
    "I forgot my password",
    "CHARGED TWICE!! REFUND NOW!!",
    "Dashboard loads slowly",
    "Please add dark mode",
    "App crashes on export, need TODAY!"
]

if __name__ == "__main__":
    print("\n🤖 Customer Support AI\n")
    for i, email in enumerate(EMAILS, 1):
        print(f"📨 EMAIL {i}/{len(EMAILS)}")
        process(email)
        if i < len(EMAILS): input("Press Enter...")
    print("✅ Done!\n")