import os
import random

import requests.utils

__version__ = "2022.09.07"

UA_PLATFORM = os.getenv('UA_PLATFORM')

ANDROID_USER_AGENTS_FILE = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'v4ul5j9v7.txt')
with open(ANDROID_USER_AGENTS_FILE) as fh:
    AND_USER_AGENTS = fh.read().splitlines()

if UA_PLATFORM == "android":
    requests.utils.default_user_agent = lambda: random.choice(AND_USER_AGENTS)
