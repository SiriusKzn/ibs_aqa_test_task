"""
Модуль содержит локаторы элементов страницы HomePage
"""
from selenium.webdriver.common.by import By

LIST_USERS_BTN = (By.CSS_SELECTOR, "li[data-id='users']")
SINGLE_USERS_BTN = (By.CSS_SELECTOR, "li[data-id='users-single']")
SINGLE_USERS_NEG_BTN = (By.CSS_SELECTOR, "li[data-id='users-single-not-found']")
UNKNOWN_BTN = (By.CSS_SELECTOR, "li[data-id='unknown']")
SINGLE_UNKNOWN_BTN = (By.CSS_SELECTOR, "li[data-id='unknown-single']")
SINGLE_UNKNOWN_NEG_BTN = (By.CSS_SELECTOR, "li[data-id='unknown-single-not-found']")
CREATE_USER_BTN = (By.CSS_SELECTOR, "li[data-id='post']")
UPDATE_USER_PUT_BTN = (By.CSS_SELECTOR, "li[data-id='put']")
UPDATE_USER_PATCH_BTN = (By.CSS_SELECTOR, "li[data-id='patch']")
DELETE_USER_BTN = (By.CSS_SELECTOR, "li[data-id='delete']")
REGISTER_BTN = (By.CSS_SELECTOR, "li[data-id='register-successful']")
REGISTER_NEG_BTN = (By.CSS_SELECTOR, "li[data-id='register-unsuccessful']")
LOGIN_BTN = (By.CSS_SELECTOR, "li[data-id='login-successful']")
LOGIN_NEG_BTN = (By.CSS_SELECTOR, "li[data-id='login-unsuccessful']")
DELAYED_RESPONSE = (By.CSS_SELECTOR, "li[data-id='delay']")

OUTPUT_RESPONSE_FIELD = (By.CSS_SELECTOR, "pre[data-key='output-response']")
OUTPUT_REQUEST_FIELD = (By.CSS_SELECTOR, "pre[data-key='output-request']")
OUTPUT_STATUS_CODE_TXT = (By.CSS_SELECTOR, "span[data-key='response-code']")

ENDPOINT_TXT = (By.CSS_SELECTOR, "span[data-key='url']")
REQUEST_KEY_TXT = (By.CSS_SELECTOR, "span[class='key']")
REQUEST_STRING_TXT = (By.CSS_SELECTOR, "span[class='string']")
