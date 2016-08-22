#!/usr/bin/python
from slugify import slugify
from sheet import get_google_sheet

def get_chapters():
    sheet = get_google_sheet()
    chapter_list = []

    for i, chapter in enumerate(sheet):
        chapter['slug'] = slugify(unicode(chapter['Name']))
        chapter_list.append(chapter)

    return chapter_list
