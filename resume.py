#!/usr/bin/env python

import yaml
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

    print(template.render(name = name,
                          title = title,
                          info = info,
                          skills = skills,
                          intro = intro,
                          experience = experience,
                          education = education))
