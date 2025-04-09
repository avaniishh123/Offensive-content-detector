import matplotlib.pyplot as plt
from collections import Counter

def plot_offense_chart(data):
    offenses = [d['offense_type'] for d in data if d.get('is_offensive')]
    counter = Counter(offenses)

    if not counter:
        print("📊 No offensive comments to plot.")
        return

    labels, values = zip(*counter.items())
    plt.figure(figsize=(6, 4))
    plt.bar(labels, values)
    plt.title("Offense Type Distribution")
    plt.ylabel("Count")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
