#!/usr/bin/env python

import sys
import yaml
import pdfkit
from jinja2 import Environment, FileSystemLoader
from math import floor
from os import listdir

env = Environment(
    loader=FileSystemLoader('./'),
)

template = env.get_template('resume.html.j2')
if len(sys.argv) > 1:
    resume_yaml = sys.argv[1]
else:
    resume_yaml = "resume.yaml"

cssFiles = []
for css in listdir("./styles"):
    cssFiles.append("./styles/" + css)

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
                           cssFiles = cssFiles,
                           certifications = certifications,
                           honors = honors)

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

    pdfkit.from_string(html, "resume.pdf", options=options, css=cssFiles)
