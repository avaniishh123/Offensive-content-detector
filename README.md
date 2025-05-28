# 🧠 Gemini-Powered Comment Moderation Tool

This project is a smart, AI-powered content moderation system that analyzes user comments, flags offensive or inappropriate content, and provides clean summaries and visual insights. It's built using Google Gemini 2.0 Flash and supports both AI-based classification and optional profanity pre-filtering.

I built this tool as part of a content moderation automation task. It’s simple, functional, and easy to extend — and it reflects my goal to blend responsible AI with practical software design.

---

## 🔍 What It Does

- Reads comments from a CSV file (like those from forums, chat logs, or feedback forms)
- Uses Google Gemini to detect:
  - Hate speech
  - Toxicity
  - Harassment
  - Profanity
- Outputs flagged results into a new CSV file
- (Optional) Shows a bar chart of offense types for quick visual insight

---

## 🚀 How to Use

### ✅ Step 1: Install Dependencies
```bash
pip install pandas matplotlib requests
```

### ✅ Step 2: Get Gemini API Key
1. Visit: [https://aistudio.google.com/app/apikey](https://aistudio.google.com/app/apikey)
2. Click “Create API Key”
3. Copy the key and replace this line in `moderation.py`:
```python
GEMINI_API_KEY = "my_gemini_api_key"
```

---

### ✅ Step 3: Run the Script
```bash
python main.py --input sample_100_comments.csv --output flagged_comments.csv --plot --limit 10
```

#### Arguments:
- `--input`: Input CSV file containing comments
- `--output`: Output file with flagged data
- `--plot`:  Show offense type bar chart
- `--limit`: Limit number of comments to process (for testing)

---

## 🗂 Example Output

The script creates a new CSV like this:

| comment_id | username | comment_text               | is_offensive | offense_type | explanation                                |
|------------|----------|----------------------------|---------------|---------------|---------------------------------------------|
| 1          | user1    | You're such a loser!       | True          | harassment     | Direct insult meant to demean the user      |
| 2          | user2    | Great work on the project! | False         | none           | Positive and respectful                     |

If `--plot` is enabled, it also generates a bar chart showing the distribution of offense types detected.

---

## 🎯 Why I Built This

In real-world systems, offensive content detection needs to be fast, accurate, and explainable. This project reflects that idea — simple but reliable moderation powered by one of the most advanced language models available (Gemini 2.0 Flash).

It also gave me a chance to blend:
- API integration (Gemini)
- CLI design
- Data handling
- Visualization
into one compact solution.

---

## Bar Chart Screenshot

![Figure_1](https://github.com/user-attachments/assets/d484e6fc-e3e2-4887-9b94-e4c10f80c8f6)

## Demo Video 

Link:- [https://drive.google.com/file/d/16G-Ntg28bsKZtqqdfOqyAF8zs_TXFYxX/view?usp=sharing](https://drive.google.com/file/d/1F7hzYRRKmBLb7mb7yP9ZwoU2DgMHBuh7/view?usp=sharing)



## ✅ Bonus Highlights

- Built-in CLI for flexibility
- Error handling for invalid responses
- Can be easily extended with offline profanity libraries other than Gemini API Key (`better_profanity`, `profanity-check`)
- Logs every Gemini output to help debug and understand decisions
