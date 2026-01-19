#!/usr/bin/python3
from playwright.sync_api import sync_playwright

def run_automation():
    with sync_playwright() as p:
        # FIX 1: Use a real browser channel and context to look less like a bot
        browser = p.chromium.launch(headless=True)
        
        # Adding a User-Agent and Viewport is critical for CI/CD environments
        context = browser.new_context(
            user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            viewport={'width': 1280, 'height': 720}
        )
        page = context.new_page()

        print("Navigating to Google...")
        # FIX 2: Wait until the network is idle to ensure the page is fully loaded
        page.goto("https://www.google.com", wait_until="networkidle")

        # Handle the "Accept All" button if it appears (blocking the search)
        try:
            # Using a broader selector for the 'Accept' button
            accept_button = page.get_by_role("button", name="Accept all")
            if accept_button.is_visible(timeout=2000):
                accept_button.click()
                print("Cookie consent accepted.")
        except:
            pass

        search_query = "what is the future of SDET role in IT"
        print(f"Searching for: {search_query}")
        
        # FIX 3: Use a more resilient locator for the search box
        # Google modern UI often uses 'q' name attribute
        search_bar = page.get_by_role("combobox", name="Search") or page.locator('textarea[name="q"]')
        search_bar.fill(search_query)
        search_bar.press("Enter")

        # Wait for the main results container instead of just the ID
        try:
            print("Waiting for results...")
            page.wait_for_selector("div#search, div#rso", timeout=15000)
            print("Search results loaded successfully.")
        except Exception as e:
            # Take a failure screenshot to see what Google actually showed (CAPTCHA?)
            page.screenshot(path="failure_debug.png")
            print(f"Failed to find results. See failure_debug.png. Error: {e}")

        page.screenshot(path="google_search_result.png")
        browser.close()

if __name__ == "__main__":
    run_automation()
