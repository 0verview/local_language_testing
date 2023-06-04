import time
from selenium.webdriver.common.by import By


def test_guest_should_see_add_to_basket(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    time.sleep(5)
    try:
        browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
        item_is_visible = True
    except:
        item_is_visible = False
    assert item_is_visible, "Sorry Mylord, but there no such button :(("
