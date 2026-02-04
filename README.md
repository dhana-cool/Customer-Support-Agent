# Customer Support Email Agent 

A simple AI agent built with LangGraph that automatically processes customer support emails, classifies them, and generates appropriate responses.

## 🎯 What It Does

1. **Classifies** emails by urgency (low/medium/high) and topic
2. **Searches** for relevant solutions
3. **Drafts** professional responses
4. **Decides** whether to auto-reply or escalate to human

## 📋 Requirements

```bash
pip install langgraph langchain-google-genai
```

## 🔑 Setup

1. Get FREE Google API key from: https://aistudio.google.com/app/apikey
2. Open `support_agent_beginner.py`
3. Paste your key on line 10:
   ```python
   GOOGLE_API_KEY = "your-key-here"
   ```
4. Run: `python support_agent_beginner.py`

## 🏗️ Architecture

### Workflow
```
Email Input → Classify → Draft Response → Decide Action → Output
```

### Components
- **LangGraph**: Workflow orchestration
- **Google Gemini**: FREE AI model (1500 requests/day)
- **Keyword Detection**: Simple, reliable classification

## 📊 Classification Logic

### Urgency Detection
- **HIGH**: Contains `!!`, ALL CAPS, words like "NOW", "TODAY", "URGENT"
- **MEDIUM**: Bug reports, technical issues, general questions
- **LOW**: Contains "please", "would", feature requests

### Topic Detection
- **Account**: Keywords: password, login, access
- **Billing**: Keywords: charged, refund, payment, billing
- **Bug**: Keywords: crash, error, broken, bug
- **Feature Request**: Keywords: add, feature, dark mode
- **Technical Issue**: Default for slow/loading issues

## ⚡ Decision Logic

### Auto-Reply When:
- Low urgency + simple question
- Clear solution available
- No investigation needed

### Escalate When:
- **HIGH urgency** (always)
- **Billing** issues (refunds, disputes)
- **Bugs** (need investigation)

## 📧 Sample Inputs & Outputs

### Example 1: Low Urgency - Password Reset
**Input:**
```
"I forgot my password"
```

**Output:**
```
Urgency: LOW
Topic: Account
Action: AUTO-REPLY
Response: To reset your password, visit https://example.com/reset. 
You'll get a link in 5 minutes.
```

---

### Example 2: High Urgency - Billing Issue
**Input:**
```
"CHARGED TWICE!! REFUND NOW!!"
```

**Output:**
```
Urgency: HIGH
Topic: Billing
Action: ESCALATE
Response: I apologize for the billing issue. Our billing team will 
contact you within 2 hours.
```

---

### Example 3: Medium Urgency - Technical Issue
**Input:**
```
"Dashboard loads slowly"
```

**Output:**
```
Urgency: MEDIUM
Topic: Technical Issue
Action: AUTO-REPLY
Response: Try clearing your cache or using incognito mode. Let us 
know if it persists.
```

---

### Example 4: Low Urgency - Feature Request
**Input:**
```
"Please add dark mode"
```

**Output:**
```
Urgency: LOW
Topic: Feature Request
Action: AUTO-REPLY
Response: Great suggestion! We've added it to our roadmap and will 
notify you.
```

---

### Example 5: High Urgency - Critical Bug
**Input:**
```
"App crashes on export, need TODAY!"
```

**Output:**
```
Urgency: HIGH
Topic: Bug
Action: ESCALATE
Response: Thanks for reporting this. Our team is investigating and 
working on a fix.
```

## 🎓 Code Structure (105 lines)

```
1. Setup (API key, imports)          → 15 lines
2. Helper function (ask_ai)          → 7 lines
3. Classify function                 → 20 lines
4. Draft function                    → 20 lines
5. Decide function                   → 5 lines
6. Build workflow                    → 10 lines
7. Process function                  → 8 lines
8. Test emails + main                → 20 lines
```

## 🔧 How to Customize

### Add New Keywords
```python
# In classify() function
if 'new_keyword' in email:
    state['topic'] = 'New Topic'
```

### Add New Response Templates
```python
# In draft() function
responses = {
    'New Topic': "Your custom response here"
}
```

### Change Decision Rules
```python
# In decide() function
if state['topic'] == 'New Topic':
    state['action'] = 'ESCALATE'
```

## 💡 Why This Approach?

### Uses Keyword Detection (Not Just AI)
- **More reliable** than pure AI
- **Faster** (no API call for classification)
- **Predictable** results
- **FREE** (keywords don't cost money)

### AI Only for Responses
- Generates natural, helpful responses
- Fallback templates if AI fails
- Best of both worlds

## 🆓 Cost

**100% FREE!**
- Google Gemini: 1500 requests/day free
- No credit card needed
- Perfect for learning and testing

## 📝 Features

✅ Simple beginner-friendly code
✅ Keyword-based classification (reliable)
✅ AI-generated responses
✅ Fallback templates
✅ Clear escalation logic
✅ Easy to customize


## 🐛 Troubleshooting

### "API Key not found"
- Make sure you pasted the key on line 10
- Key should look like: `AIzaSy...`

### "All emails showing same classification"
- This version uses keywords, not AI for classification
- Very reliable and accurate
- Check if keywords match your test emails

### "JSON parse error"
- This version has fallback templates
- Will use template if AI fails
- Should never crash

## 📚 Learning Resources

- LangGraph Docs: https://langchain-ai.github.io/langgraph/
- Google Gemini: https://ai.google.dev/
- Python Basics: https://docs.python.org/3/tutorial/

## 🎯 Next Steps

1. **Add more keywords** for better classification
2. **Add more topics** (e.g., Sales, Feedback)
3. **Integrate with email** (Gmail API)
4. **Add database** to store results
5. **Build web interface** with Streamlit

## 📄 License

MIT License - Free to use and modify

