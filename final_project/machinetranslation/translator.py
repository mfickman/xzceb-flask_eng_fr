import os
import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

APIKEY = os.environ['apikey']
URL = os.environ['url']
VERSION = '2018-05-01'

authenticator = IAMAuthenticator(APIKEY)
language_translator = LanguageTranslatorV3(
    version=VERSION,
    authenticator=authenticator
)

language_translator.set_service_url(URL)


def english_to_french(english_text):
    translation = language_translator.translate(
    text=english_text,
    model_id='en-fr').get_result()
    # frenchText = translation.json()
    french_text = translation["translations"][0]["translation"]
    return french_text


def french_to_english(french_text):
    translation = language_translator.translate(
    text=french_text,
    model_id='fr-en').get_result()
    # englishText = translation.json()
    english_text = translation["translations"][0]["translation"]
    return english_text
