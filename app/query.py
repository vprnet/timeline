#!/usr/bin/python
from slugify import slugify
from sheet import get_google_sheet

sheet = get_google_sheet()

def get_chapters():
    chapter_list = []

    for i, chapter in enumerate(sheet):
        chapter['slug'] = slugify(unicode(chapter['Name']))
        chapter_list.append(chapter)

    return chapter_list


def get_slugs(Name):
    slugs = [slugify(unicode(i['Name'])) for i in sheet]

    links = False
    next = False
    prev = False
    for i in range(len(slugs)):
        if Name == slugs[i]:
            if i + 1 < len(slugs):
                next = slugs[i + 1]
            if i > 0:
                prev = slugs[i - 1]

            links = {'next': next, 'prev': prev}

    return slugs, links
