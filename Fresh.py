# 1️⃣ Imports
from langchain_ollama import OllamaLLM
from langchain_core.prompts import PromptTemplate

# 2️⃣ Initialize the LLM
llm = OllamaLLM(
    model="qwen3:8b",
    temperature=0.2,
    streaming=False  # Disable streaming to avoid _stream_with_aggregation errors
)

# 3️⃣ Create the Prompt Template
evaluation_prompt = PromptTemplate(
    input_variables=["user_prompt"],
    template="""
You are a Prompt Quality Evaluation Agent.

Evaluate the following prompt based on the criteria below.
Give a score from 0 to 10 for each criterion.

Criteria:
1. Clarity – Is the goal clear and easy to understand?
2. Details – Are sufficient requirements provided?
3. Context – Is background, audience, or use-case mentioned?
4. Output Format & Constraints – Are format, tone, or length specified?
5. Persona Defined – Is a role or persona assigned?

Prompt:
\"\"\"{user_prompt}\"\"\"

Return the evaluation EXACTLY in this format:

Clarity Score: X/10
Details Score: X/10
Context Score: X/10
Output Format & Constraints Score: X/10
Persona Defined Score: X/10
Final Score (Average): X/10

Short Explanation:
- <1–2 sentence explanation>

Improvement Suggestions:
1. <Suggestion 1>
2. <Suggestion 2>
3. <Suggestion 3>
"""
)

# 4️⃣ Create the chain
chain = evaluation_prompt | llm

# 5️⃣ Define the function to evaluate a prompt
def evaluate_prompt(user_prompt: str):
    return chain.invoke({"user_prompt": user_prompt})


# ✅ Run the whole pipeline
if __name__ == "__main__":
    #test_prompt = "Write an email asking my manager for project feedback."
    #Ask User for a prompt to evalute
    user_prompt = input("Enter the prompt you want to evaluate: ")
    # Debug print to confirm input
    print("\nSending prompt to evaluation agent:")
    print(user_prompt)
    
    result = evaluate_prompt(user_prompt)

    print("\n--- Prompt Evaluation ---\n")
    print(result)
