import nltk
import newspaper

# Declare variables

summaryDocName = 'news_summary.txt'

newsWebsiteOne = 'https://www.nintendolife.com/'
newsWebsiteTwo = 'https://www.ign.com/'
newsWebsiteThree = 'https://www.eurogamer.net/'

retrievedArticles = list()
retrievedArticlesWithKeyword = list()

# List of functions

def GetUserKeyword(prompt):
    return input(prompt)

def ScrapeArticle(source):
    src = newspaper.build(source, memoize_articles=False)

    for article in src.articles:
        retrievedArticles.append(article)

def FindArticlesWithKeyword(keyword):

    for article in retrievedArticles:

        try:
            article.download()
            article.parse()
            article.nlp()
        except:
            continue

        if keyword in article.keywords:
            retrievedArticlesWithKeyword.append(article)

def WriteArticles():

    for article in retrievedArticlesWithKeyword:
        WriteArticleToDocument(article)

def WriteArticleToDocument(article):

    title = article.title

    authorTxt = ""

    for author in article.authors:

        if author != article.authors[0]:
            authorTxt += ", "

        authorTxt += str(author)

    summary = article.summary

    print(title + "-" + authorTxt)
    print(summary)
    print('\n')

    summaryDoc.write(title + "-" + authorTxt)
    summaryDoc.write(summary)
    summaryDoc.write('\n')

keyword = GetUserKeyword("Enter a keyword to guide your search! ")

print("The search begins! Please wait...")

ScrapeArticle(newsWebsiteOne)
ScrapeArticle(newsWebsiteTwo)
ScrapeArticle(newsWebsiteThree)

FindArticlesWithKeyword(keyword)

summaryDoc = open(summaryDocName, 'w')

WriteArticles()

summaryDoc.close()