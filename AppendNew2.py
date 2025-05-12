import os
import dotenv
import datetime
import pandas as pd

import requests
import io

from github import Github
from github import InputGitTreeElement

user = os.environ.get("GITHUB_USERNAME")
token = os.environ.get("GITHUB_TOKEN")

repo_name = "ECON-8320-Semester-Project"
#path =