import pytest
from playwright.sync_api import Page, expect


@pytest.mark.asyncio
async def test_test_case___1(page: Page):
    """
    Open youtube.
    
    Generated from QA Pass execution
    Test Case ID: 69365741b21d6481ea23bfd6
    """

    # Step 0: Navigate to YouTube homepage
    await page.goto('https://www.youtube.com')

    # Step 1: Wait for the page to fully load and network activity to become idle
    await self.wait_for_network_idle(page)

    # Step 2: Check that the YouTube logo is visible as a confirmation the homepage is loaded.
    await page.locator('a#logo[title="YouTube Home"]').is_visible()

    # Step 3: Check that the first YouTube logo link (id='logo', title='YouTube Home') is visible as confirmation the homepage loaded.
    
            # Find visible element index and assert visibility
            await expect(page.locator("a#logo[title=\"YouTube Home\"]").nth(0)).to_be_visible()
            
