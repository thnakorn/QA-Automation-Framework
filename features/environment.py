import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv

# Allure
import allure
from allure_commons.types import AttachmentType

load_dotenv()


def _chrome_driver():
    options = Options()
    if os.getenv("HEADLESS", "true").lower() == "true":
        options.add_argument("--headless=new")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=options)


def before_all(context):
    os.makedirs("reports/allure", exist_ok=True)
    os.makedirs("reports/screenshots", exist_ok=True)
    context.browser = _chrome_driver()
    context.browser.set_window_size(1366, 900)


def after_all(context):
    if context.browser:
        context.browser.quit()


def after_step(context, step):
    # Adjunta evidencia solo si falla el step
    if step.status == "failed":
        try:
            # Screenshot
            png = context.browser.get_screenshot_as_png()
            allure.attach(png, name=f"screenshot_{step.name}", attachment_type=AttachmentType.PNG)
        except Exception:
            pass
        try:
            # Page Source
            html = context.browser.page_source
            allure.attach(html, name=f"page_source_{step.name}", attachment_type=AttachmentType.HTML)
        except Exception:
            pass
        try:
            # URL actual
            allure.attach(context.browser.current_url, name="current_url", attachment_type=AttachmentType.TEXT)
        except Exception:
            pass


def after_scenario(context, scenario):
    # Si el escenario falla, añade un screenshot final a nivel de escenario
    if scenario.status == "failed":
        try:
            png = context.browser.get_screenshot_as_png()
            allure.attach(png, name=f"scenario_failed_{scenario.name}", attachment_type=AttachmentType.PNG)
        except Exception:
            pass
