from index import app
from flask import render_template, request
from config import BASE_URL
from query import get_chapters, get_slugs

chapters = get_chapters()

social = {
    'url': BASE_URL,
    'title': "Timeline",
    'subtitle': "A Podcast from Vermont Public Radio",
    'img': "",
    'description': "",
    'twitter_text': "",
    'twitter_hashtag': ""
}

@app.route('/')
def index():
    page_title = 'VPR Classical Timeline'
    page_url = BASE_URL + request.path
    landing = True
    slugs, links = get_slugs(Name=False)

    return render_template('content.html',
        page_title=page_title,
        social=social,
        slugs=slugs,
        links=links,
        landing=landing,
        chapters=chapters,
        page_url=page_url)

@app.route('/<Name>')
def chapter_page(Name):
    for chapter in chapters:
        if 'slug' in chapter and Name == chapter['slug']:
            chapters.remove(chapter)
            chapters.insert(0, chapter)

    page_url = BASE_URL + request.path
    page_title =  "VPR Classical Timeline: " + chapters[0]['Name']

    slugs, links = get_slugs(Name)


    social = {
        'title': page_title,
        'subtitle': "",
        'img': "",
        'description': chapters[0]['Name'],
        'twitter_text': "",
        'twitter_hashtag': ""
    }

    return render_template('content.html',
        page_title=page_title,
        social=social,
        slugs=slugs,
        links=links,
        chapters=chapters,
        page_url=page_url)


@app.route('/menu')
def menu():
    page_title = 'VPR Classical Timeline'
    page_url = BASE_URL + request.path
    menu = True

    return render_template('menu.html',
        page_title=page_title,
        social=social,
        menu=menu,
        chapters=chapters,
        page_url=page_url)


@app.route('/about')
def about():
    page_title = 'VPR Classical Timeline'
    page_url = BASE_URL + request.path
    about = True

    return render_template('about.html',
        page_title=page_title,
        social=social,
        about=about,
        page_url=page_url)
