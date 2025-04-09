import pandas as pd
import csv

def load_comments(filename, limit=10):
    df = pd.read_csv(filename).dropna(subset=['comment_text']).head(limit)
    df.reset_index(drop=True, inplace=True)

    comments = []
    for i, row in df.iterrows():
        comments.append({
            'comment_id': i + 1,
            'username': row.get('username', f"user_{i+1}"),
            'comment_text': row['comment_text']
        })
    return comments

def save_results(data, filename):
    with open(filename, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)

def print_summary(data):
    offensive = [d for d in data if d.get("is_offensive")]
    print(f"\n🔍 Total Comments: {len(data)}")
    print(f"🚨 Offensive Comments: {len(offensive)}")

    offense_types = {}
    for c in offensive:
        offense_types[c['offense_type']] = offense_types.get(c['offense_type'], 0) + 1

    print("\n📊 Offense Type Breakdown:")
    for k, v in offense_types.items():
        print(f"• {k}: {v}")

    print("\n🔥 Top 5 Most Offensive Comments:")
    sorted_off = sorted(offensive, key=lambda x: len(x['explanation']), reverse=True)[:5]
    for i, c in enumerate(sorted_off):
        print(f"{i+1}. {c['username']} – \"{c['comment_text']}\"")
        print(f"   ↳ {c['offense_type']}: {c['explanation']}")
