#!/usr/bin/python3
from playwright.sync_api import sync_playwright
import time

def run_automation():
    with sync_playwright() as p:
        
        browser = p.chromium.launch(headless=True) 
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        )
        page = context.new_page()

        print("Step 1: Navigating to Google...")
        page.goto("https://www.google.com")

    
        try:
    
            accept_btn = page.get_by_role("button", name="Accept all")
            if accept_btn.is_visible(timeout=3000):
                accept_btn.click()
        except:
            pass

        search_query = "what is the future of SDET role in IT"
        print(f"Step 2: Searching for: '{search_query}'")
        
    
        search_bar = page.locator('textarea[name="q"]') 
        search_bar.fill(search_query)
        search_bar.press("Enter")

    
        print("Step 3: Waiting for search results...")
        page.wait_for_selector("#search", timeout=10000)
        
        
        page.screenshot(path="google_search_result.png", full_page=True)
        print("Success: Screenshot saved as google_search_result.png")

        browser.close()

if __name__ == "__main__":
    run_automation()
