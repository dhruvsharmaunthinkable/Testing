import pytest
from playwright.sync_api import Page, expect


@pytest.mark.asyncio
async def test_test_case___4(page: Page):
    """
    Open youtube.
    
    Generated from QA Pass execution
    Test Case ID: 69329764ba329718c87b940a
    """

    # Step 0: Go to the YouTube website using the provided URL.
    await page.goto('https://www.youtube.com')

    # Step 1: Wait for the network to be idle to ensure the YouTube homepage is fully loaded before any further actions.
    await self.wait_for_network_idle(page)
