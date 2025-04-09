import requests
import time
import json
import re

GEMINI_API_KEY = "my_gemini_api_key"
GEMINI_API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"

def moderate_comment(comment_text):
    prompt = f"""
Classify the following comment:
"{comment_text}"

Return a JSON response like this:
{{
  "is_offensive": true/false,
  "offense_type": "hate speech / harassment / toxicity / profanity / none",
  "explanation": "brief explanation"
}}
"""

    body = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }

    headers = {"Content-Type": "application/json"}

    for _ in range(3):
        try:
            response = requests.post(GEMINI_API_URL, headers=headers, json=body)
            result = response.json()

            if "candidates" not in result:
                print("⚠️ Gemini response error:", result.get("error", "No candidates"))
                return {
                    "is_offensive": False,
                    "offense_type": "none",
                    "explanation": "Invalid response from Gemini"
                }

            text = result['candidates'][0]['content']['parts'][0]['text'].strip()
            print("🔹 Gemini Output:", text)

            # Remove markdown-style ```json ``` wrappers
            cleaned = re.sub(r"^```json|```$", "", text).strip()
            return json.loads(cleaned)

        except Exception as e:
            print("⚠️ Gemini exception:", e)
            time.sleep(1)

    return {
        "is_offensive": False,
        "offense_type": "none",
        "explanation": "Gemini API failed"
    }

def analyze_comments(comments):
    for i, comment in enumerate(comments):
        print(f"⏳ Processing comment {i+1}/{len(comments)}...")
        result = moderate_comment(comment['comment_text'])
        comment.update(result)
    return comments
