import matplotlib.pyplot as plt
import csv

def main():
    languages = []
    counts = []

    try:
        with open('output.csv', 'r') as f:
            reader = csv.reader(f, delimiter='\t')
            for row in reader:
                if len(row) == 2:
                    languages.append(row[0])
                    counts.append(int(row[1]))
    except FileNotFoundError:
        print("Error: output.csv not found. Please run the pipeline first.")
        return

    # Combine and sort by counts
    data = sorted(zip(languages, counts), key=lambda x: x[1], reverse=True)
    
    # Get top 15
    top_data = data[:15]
    top_languages = [x[0] for x in top_data]
    top_counts = [x[1] for x in top_data]

    # Plot
    plt.figure(figsize=(12, 8))
    bars = plt.bar(top_languages, top_counts, color='skyblue')
    plt.xlabel('Programming Language')
    plt.ylabel('Repository Count')
    plt.title('Top 15 Most Popular Programming Languages on GitHub')
    plt.xticks(rotation=45, ha='right')
    
    # Add counts on top of bars
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, yval + 1, yval, ha='center', va='bottom')

    plt.tight_layout()
    plt.savefig('language_popularity.png')
    plt.show()
    print("Visualization saved to language_popularity.png")

if __name__ == "__main__":
    main()
