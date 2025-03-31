import pandas as pd
import os

def save_results_to_excel(data, filename="data/results.xlsx"):
    """Save crawled links to an Excel file"""
    os.makedirs(os.path.dirname(filename), exist_ok=True)

    results = []
    for url, links in data:
        for link in links:
            results.append({"Source URL": url, "Extracted Link": link})

    if results:
        df = pd.DataFrame(results)
        df.to_excel(filename, index=False)
        print(f"Results saved in {filename}")
    else:
        print("⚠ No links found. Excel file not updated.")
