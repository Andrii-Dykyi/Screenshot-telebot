import asyncio
import os
from datetime import datetime

import pyppeteer


async def make_screenshot(url, file_path):
    """Go to url and make screenshot"""   
    browser = await pyppeteer.launch()
    page = await browser.newPage()
    await page.goto(url)
    await page.screenshot(path=file_path, fullPage=True, omitBackground=True)
    await browser.close()
