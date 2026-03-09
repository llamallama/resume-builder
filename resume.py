#!/usr/bin/env python

import sys
import yaml
from jinja2 import Environment, FileSystemLoader
from os import listdir
from pathlib import Path
from playwright.sync_api import sync_playwright

env = Environment(
    loader=FileSystemLoader('./'),
)

template = env.get_template('resume.html.j2')
if len(sys.argv) > 1:
    resume_yaml = sys.argv[1]
else:
    resume_yaml = "resume.yaml"


if len(sys.argv) > 1:
    resume_yaml = sys.argv[1]
else:
    resume_yaml = "resume.yaml"

# What is yaml?
# print(yaml)

# cssFiles = []
# for css in listdir("./styles"):
#     cssFiles.append("./styles/" + css)

css = './styles/styles.css'

with open(resume_yaml, 'r') as file:
    resume = yaml.load(file, Loader=yaml.FullLoader)

    name = resume["name"]
    title = resume["title"]
    info = resume["info"]
    skills = resume["skills"]
    intro = resume["intro"]
    experience = resume["experience"]
    education = resume["education"]
    certifications = resume["certifications"]
    honors = resume["honors"]

    html = template.render(name = name,
                           title = title,
                           info = info,
                           skills = skills,
                           intro = intro,
                           experience = experience,
                           education = education,
                           css=css)

    options = {
      "enable-local-file-access": None,
      "page-size": "Letter",
      "margin-top": "2",
      "margin-right": "2",
      "margin-bottom": "2",
      "margin-left": "2",
      "encoding": "UTF-8"
    }

    with open('resume.html', 'w') as f:
        f.write(html)

def generate_pdf(output_pdf):
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        page.goto(Path('resume.html').absolute().as_uri())
        page.add_style_tag(path='./styles/styles.css')
        page.emulate_media(media="screen")
        # page.pdf(path=output_pdf, format='Letter', print_background=True)
        page.pdf(path=output_pdf, format='Letter', print_background=True, margin={'top': '8px', 'bottom': '8px', 'left': '8px', 'right': '8px'})
        browser.close()

generate_pdf('resume.pdf')
