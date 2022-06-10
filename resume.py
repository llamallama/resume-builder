#!/usr/bin/env python

import yaml
import pdfkit
from jinja2 import Environment, FileSystemLoader
from math import floor

env = Environment(
    loader=FileSystemLoader('./'),
)

template = env.get_template('resume.html.j2')

with open(r'resume.yaml') as file:
    resume = yaml.load(file, Loader=yaml.FullLoader)

    name = resume["name"]
    title = resume["title"]
    info = resume["info"]
    skills = resume["skills"]
    intro = resume["intro"]
    experience = resume["experience"]
    education = resume["education"]

    html = template.render(name = name,
                           title = title,
                           info = info,
                           skills = skills,
                           intro = intro,
                           experience = experience,
                           education = education)

    options = {
      "enable-local-file-access": None,
      "page-size": "Letter",
      "margin-top": "0",
      "margin-right": "0",
      "margin-bottom": "0",
      "margin-left": "0",
      "encoding": "UTF-8"
    }

    with open('resume.html', 'w') as f:
        f.write(html)

    pdfkit.from_string(html, "resume.pdf", options=options)
