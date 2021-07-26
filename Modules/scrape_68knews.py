__author__ = "Bob Failla"
__description__ = "Uses the article class.  Imports news articles from 68knews and parses the returned web content" \
                  " into a list of articles consisting of URL, title and body using beautiful soup." \
                  "Parses out extraneous return on the web page.  The list created contains Article objects."


from article import Article
import requests
from bs4 import BeautifulSoup


def scrape_68knews():
    linkList = []
    try:
        page = requests.get('http://68k.news')
    except BaseException:
        print("Something went wrong trying to reach 68k.news.  Quitting")
        exit(1)
    soup = BeautifulSoup(page.content, 'html.parser')
    for link in soup.find_all('a'):
        linkList.append(str(link.get('href')).replace(
            'article.php?loc=US&a=', 'http://68k.news/article.php?loc=US&a='))
    # Now that we have all the articles in a list, let's create some objects
    count = 0
    aL = []  # article list
    for i in linkList:
        if str(i).startswith("http://68"):
            page = requests.get(str(i))
            if page.status_code == 200:
                soup = BeautifulSoup(page.content, "html.parser")
                title = str(
                    soup.find('title')).replace(
                    '<title>',
                    '').replace(
                    '</title>',
                    '')
                tag = soup.body
                body = ''
                for string in tag.strings:
                    if "< Back to" in string or \
                            "68k.news" in string or \
                            "US front page" in string or \
                            "Original source (on modern site) | Article images:" in string:
                        pass
                    else:
                        body = body + str(string).strip("\n")
                a = Article(count, title, body, i)
                count += 1
                aL.append(a)
        else:
            # It is possible that a link may no longer be reachable.  In this
            # case, just ignore it and move on.
            pass
    return aL
