import pytest
from playwright.sync_api import Page, expect


@pytest.mark.asyncio
async def test_test_case___1(page: Page):
    """
    Open youtube.
    
    Generated from QA Pass execution
    Test Case ID: 693658e4b21d6481ea23bfe6
    """

    # Step 0: Navigate to the YouTube homepage.
    await page.goto('https://www.youtube.com')

    # Step 1: Wait until the YouTube homepage network activity is idle to ensure page fully loads.
    await self.wait_for_network_idle(page)
