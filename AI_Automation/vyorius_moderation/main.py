import argparse
from moderation import analyze_comments
from utils import load_comments, save_results, print_summary
from charts import plot_offense_chart

def main():
    parser = argparse.ArgumentParser(description="Vyorius AI Comment Moderation Tool (Gemini Powered)")
    parser.add_argument('--input', type=str, required=True, help="Input file (CSV)")
    parser.add_argument('--output', type=str, default="flagged_comments.csv", help="Output file")
    parser.add_argument('--plot', action='store_true', help="Plot offense type chart")
    parser.add_argument('--limit', type=int, default=10, help="Number of comments to process")
    args = parser.parse_args()

    comments = load_comments(args.input, limit=args.limit)
    analyzed = analyze_comments(comments)
    save_results(analyzed, args.output)
    print_summary(analyzed)
    if args.plot:
        plot_offense_chart(analyzed)

if __name__ == "__main__":
    main()
