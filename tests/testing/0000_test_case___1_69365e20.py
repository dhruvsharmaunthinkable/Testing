import pytest
from playwright.sync_api import Page, expect


@pytest.mark.asyncio
async def test_test_case___1(page: Page):
    """
    Open Youtube
    
    Generated from QA Pass execution
    Test Case ID: 69365e20bcc7c7ee588607cb
    """

    # Step 0: Navigate to the Youtube website.
    await page.goto('https://www.youtube.com')

    # Step 1: Wait for the page network activity to idle, indicating Youtube is fully loaded.
    await self.wait_for_network_idle(page)

    # Step 2: Check that the Youtube logo is visible, confirming the homepage loaded successfully.
    await page.locator('a#logo[title="YouTube Home"]').is_visible()

    # Step 3: Verify the main Youtube logo at the top-left is visible to confirm we're on the Youtube homepage.
    
            # Find visible element index and assert visibility
            await expect(page.locator("a#logo[title=\"YouTube Home\"]").nth(0)).to_be_visible()
            
