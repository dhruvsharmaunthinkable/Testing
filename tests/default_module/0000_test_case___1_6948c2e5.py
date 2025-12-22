import pytest
from playwright.sync_api import Page, expect


@pytest.mark.asyncio
async def test_test_case___1(page: Page):
    """
    Open youtube
    
    Generated from QA Pass execution
    Test Case ID: 6948c2e5f4697bfb52f14cea
    """

    # Step 0: Navigate to the YouTube website
    await page.goto('https://www.youtube.com')

    # Step 1: Wait for the page to finish loading all resources
    await self.wait_for_network_idle(page)
