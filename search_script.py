#!/usr/bin/python3

from playwright.sync_api import sync_playwright

def run_automation():
    with sync_playwright() as p:
    
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

    
        print("Navigating to Google...")
        page.goto("https://www.google.com")

        
        
        try:
            if page.get_by_role("button", name="Accept all").is_visible():
                page.get_by_role("button", name="Accept all").click()
        except:
            pass

    
        search_query = "what is the future of SDET role in IT"
        print(f"Searching for: {search_query}")
        
        
        search_bar = page.locator('textarea[name="q"]') 
        search_bar.fill(search_query)
        search_bar.press("Enter")

        
        page.wait_for_selector("#search")
        print("Search results loaded.")

        
        page.wait_for_timeout(5000)

        
        browser.close()

if __name__ == "__main__":
    run_automation()
