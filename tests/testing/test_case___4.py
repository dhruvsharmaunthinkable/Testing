import pytest
from playwright.sync_api import Page, expect


@pytest.mark.asyncio
async def test_test_case___4(page: Page):
    """
    Open Youtube.
    
    Generated from QA Pass execution
    Test Case ID: 69329764ba329718c87b940a
    """

    # Step 0: Navigate to the Youtube website in a new browser tab.
    await page.goto('https://www.youtube.com')

    # Step 1: Wait for network activity to finish to ensure the Youtube homepage is fully loaded.
    await self.wait_for_network_idle(page)
