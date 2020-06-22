import asyncio
import os
from datetime import datetime

import pyppeteer


async def make_screenshot(url, file_path):
    """Go to url and make a screenshot"""   
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await page.setViewport({"width": 1920, "height": 1080})
    await page.goto(url)
    await page.screenshot(path=file_path, fullPage=True)
    await browser.close()
