import sys
import os
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from crawler.crawler import crawl_website
from crawler.storage import save_results_to_excel  # Import storage function

# Ensure Python can find the `crawler` module
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

def start_crawling(url_entry, max_pages_entry, results_text):
    """Start the web crawling process"""
    url = url_entry.get().strip()
    try:
        max_pages = int(max_pages_entry.get().strip())
    except ValueError:
        messagebox.showerror("Error", "Max pages must be an integer.")
        return

    results = crawl_website(url, max_pages)
    save_results_to_excel(results)  # Store in Excel file

    results_text.delete(1.0, tk.END)
    for url, links in results:
        results_text.insert(tk.END, f"URL: {url}\n")
        for link in links:
            results_text.insert(tk.END, f"  -> {link}\n")
        results_text.insert(tk.END, "\n")

def start_gui():
    """Initialize GUI"""
    root = tk.Tk()
    root.title("Web Crawler")
    root.geometry("600x500")
    
    ttk.Label(root, text="Enter URL:").pack(pady=5)
    url_entry = ttk.Entry(root, width=50)
    url_entry.pack(pady=5)

    ttk.Label(root, text="Max Pages to Crawl:").pack(pady=5)
    max_pages_entry = ttk.Entry(root, width=10)
    max_pages_entry.pack(pady=5)

    ttk.Button(root, text="Start Crawling", 
               command=lambda: start_crawling(url_entry, max_pages_entry, results_text)).pack(pady=10)

    results_text = scrolledtext.ScrolledText(root, width=70, height=20, wrap=tk.WORD)
    results_text.pack(pady=5)

    root.mainloop()
