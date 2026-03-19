import pandas as pd
import matplotlib.pyplot as plt
import os

# Ensure images directory exists
if not os.path.exists('images'):
    os.makedirs('images')

def main():
    # --- Step 1: Data Preparation ---
    print("Step 1: Data Preparation...")
    df = pd.read_csv("Most starred Github Repositories.csv")
    
    # Keep relevant columns and rename repo_name to name if necessary
    # Based on earlier view_file output: rank,item,repo_name,stars,forks,language,repo_url,username,issues,last_commit,description
    relevant_columns = ['repo_name', 'language', 'stars', 'forks']
    df_cleaned = df[relevant_columns].copy()
    df_cleaned.rename(columns={'repo_name': 'name'}, inplace=True)
    
    # Drop null values
    df_cleaned.dropna(inplace=True)
    
    # Create engagement column
    df_cleaned['engagement'] = df_cleaned['stars'] + df_cleaned['forks']
    
    # Save cleaned dataset
    df_cleaned.to_csv("final_dataset.csv", index=False)
    print("→ final_dataset.csv saved.")

    # --- Step 2: KPI Calculations ---
    print("Step 2: KPI Calculations...")
    total_repos = len(df_cleaned)
    total_stars = df_cleaned['stars'].sum()
    total_forks = df_cleaned['forks'].sum()
    avg_stars = df_cleaned['stars'].mean()
    avg_forks = df_cleaned['forks'].mean()
    
    top_10_stars = df_cleaned.sort_values(by='stars', ascending=False).head(10)[['name', 'stars']]
    top_10_forks = df_cleaned.sort_values(by='forks', ascending=False).head(10)[['name', 'forks']]
    
    lang_counts = df_cleaned['language'].value_counts()
    lang_avg_stars = df_cleaned.groupby('language')['stars'].mean().sort_values(ascending=False)
    lang_dist_pct = (lang_counts / total_repos) * 100

    # Save KPI summaries
    with open("kpi_summary.txt", "w", encoding="utf-8") as f:
        f.write("=== GitHub Data Analytics KPI Summary ===\n\n")
        f.write(f"Total Repositories: {total_repos}\n")
        f.write(f"Total Stars: {total_stars}\n")
        f.write(f"Total Forks: {total_forks}\n")
        f.write(f"Average Stars per Repository: {avg_stars:.2f}\n")
        f.write(f"Average Forks per Repository: {avg_forks:.2f}\n\n")
        
        f.write("--- Top 10 Repositories by Stars ---\n")
        f.write(top_10_stars.to_string(index=False) + "\n\n")
        
        f.write("--- Top 10 Repositories by Forks ---\n")
        f.write(top_10_forks.to_string(index=False) + "\n\n")
        
        f.write("--- Repository Count per Language (Top 20) ---\n")
        f.write(lang_counts.head(20).to_string() + "\n\n")
        
        f.write("--- Average Stars per Language (Top 20) ---\n")
        f.write(lang_avg_stars.head(20).to_string() + "\n\n")
        
        f.write("--- Language Distribution Percentage (Top 10) ---\n")
        f.write(lang_dist_pct.head(10).to_string() + "\n")
        
    print("→ kpi_summary.txt saved.")

    # --- Step 3: Create Visualizations ---
    print("Step 3: Create Visualizations...")
    
    # 1. Bar chart: Top 15 languages
    plt.figure(figsize=(12, 6))
    lang_counts.head(15).plot(kind='bar', color='skyblue')
    plt.title('Top 15 Programming Languages by Repository Count')
    plt.xlabel('Language')
    plt.ylabel('Count')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/language_popularity.png')
    plt.close()

    # 2. Pie chart: Language distribution (Top 10 + Others)
    top_10_langs = lang_counts.head(10)
    others_count = lang_counts.iloc[10:].sum()
    pie_data = pd.concat([top_10_langs, pd.Series({'Others': others_count})])
    plt.figure(figsize=(10, 10))
    pie_data.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
    plt.title('Language Distribution')
    plt.ylabel('')
    plt.savefig('images/language_distribution.png')
    plt.close()

    # 3. Bar chart: Top 10 repositories by stars
    plt.figure(figsize=(12, 6))
    plt.barh(top_10_stars['name'][::-1], top_10_stars['stars'][::-1], color='gold')
    plt.title('Top 10 Repositories by Stars')
    plt.xlabel('Stars')
    plt.tight_layout()
    plt.savefig('images/top_repos_stars.png')
    plt.close()

    # 4. Bar chart: Top 10 repositories by forks
    plt.figure(figsize=(12, 6))
    plt.barh(top_10_forks['name'][::-1], top_10_forks['forks'][::-1], color='orange')
    plt.title('Top 10 Repositories by Forks')
    plt.xlabel('Forks')
    plt.tight_layout()
    plt.savefig('images/top_repos_forks.png')
    plt.close()

    # 5. Scatter plot: Stars vs Forks
    plt.figure(figsize=(10, 6))
    plt.scatter(df_cleaned['stars'], df_cleaned['forks'], alpha=0.5, color='purple')
    plt.title('Stars vs Forks')
    plt.xlabel('Stars')
    plt.ylabel('Forks')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.savefig('images/stars_vs_forks.png')
    plt.close()

    # 6. Bar chart: Average stars per language
    plt.figure(figsize=(12, 6))
    lang_avg_stars.head(15).plot(kind='bar', color='salmon')
    plt.title('Average Stars per Language (Top 15)')
    plt.xlabel('Language')
    plt.ylabel('Average Stars')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('images/avg_stars_language.png')
    plt.close()

    print("→ Visualizations saved in images/ directory.")
    print("\nAll KPIs generated, visualizations saved, and dataset prepared for Power BI.")

if __name__ == "__main__":
    main()
