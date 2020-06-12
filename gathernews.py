import nltk
import newspaper

# Declare variables

summaryDocName = 'news_summary.txt'

newsWebsiteOne = 'https://www.destructoid.com/'
newsWebsiteTwo = 'https://www.gamesradar.com/'
newsWebsiteThree = 'https://www.nintendolife.com/'

retrievedArticles = list()
retrievedArticlesWithKeyword = list()

# List of functions

def GetUserKeyword(prompt):
    keyword = input(prompt)
    return keyword

def ScrapeArticle(source):
    src = newspaper.build(source, memoize_articles=False)

    for article in src.articles:
        retrievedArticles.append(article)

def FindArticlesWithKeyword(keyword):
    for article in retrievedArticles:
        if keyword in article.keywords:
            retrievedArticlesWithKeyword.append(article)

def WriteArticleToDocument(article):

    article.nlp()

    title = article.title

    authorTxt = ""

    for author in article.authors:

        if author != article.authors[0]:
            authorTxt += ", "

        authorTxt += str(author)

    summary = article.summary

    summaryDoc = open(summaryDocName, 'w')

    summaryDoc.write(title + "-" + authorTxt)
    summaryDoc.write(summary)
    summaryDoc.write('\n')

    summaryDoc.close()

keyword = GetUserKeyword("Enter a keyword to guide your search! ")

ScrapeArticle(newsWebsiteOne)
ScrapeArticle(newsWebsiteTwo)
ScrapeArticle(newsWebsiteThree)

FindArticlesWithKeyword(keyword)

for article in retrievedArticlesWithKeyword:

    try:
        article.download()
        article.parse()
    except:
        continue

    WriteArticleToDocument(article)