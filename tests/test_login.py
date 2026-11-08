import pandas as pd
import pytest
from playwright.sync_api import expect
from pages.login_page import LoginPage
import data

# Read the CSV; keep empty cells as empty strings
login_data = pd.read_csv(
    "test_data/login_data.csv",
    dtype=str,
    keep_default_na=False,
).to_dict("records")


@pytest.mark.parametrize("login_data", login_data)
def test_login(page, login_data):
    page.goto(data.url)

    login_page = LoginPage(page)
    login_page.enter_username(login_data["username"])
    login_page.enter_password(login_data["password"])
    login_page.login()

    if login_data["expected_result"] == data.inventory_url:
        expect(page).to_have_url(
            data.inventory_url
        )
    else:
        expect(login_page.validation_message).to_have_text(
            login_data["expected_result"]
        )