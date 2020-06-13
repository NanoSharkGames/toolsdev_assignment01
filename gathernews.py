import nltk
import newspaper

# Declare variables

summaryDocName = 'news_summary.txt'

newsWebsiteOne = 'https://www.nintendolife.com/'
newsWebsiteTwo = 'https://www.ign.com/'
newsWebsiteThree = 'https://www.eurogamer.net/'

maxArticles = 5

retrievedArticles = list()
retrievedArticlesWithKeyword = list()

# List of functions

def GetUserKeyword(prompt):
    return input(prompt)

def ScrapeArticles(source):

    articles = 0

    src = newspaper.build(source, memoize_articles=False)

    for article in src.articles:
        try:
            article.download()
            article.parse()
            article.nlp()
        except:
            continue

        if ArticleHasKeyword(article):
            WriteArticleToDocument(article)
            articles += 1

        if articles == maxArticles:
            break

def ArticleHasKeyword(article):

    if keyword in article.keywords or keyword in article.title:
        return True
    else:
        if (keyword == ""):
            return True
        else:
            return False

def WriteArticleToDocument(article):

    title = article.title

    authorTxt = ""

    for author in article.authors:

        if author != article.authors[0]:
            authorTxt += ", "

        authorTxt += str(author)

    summary = article.summary

    summaryDoc.write(title + "-" + authorTxt)
    summaryDoc.write('\n')
    summaryDoc.write(summary)
    summaryDoc.write('\n')
    summaryDoc.write('\n')

keyword = GetUserKeyword("We focus on gaming news! Enter a keyword to guide your search! ")

print("The search begins! Please wait...")

summaryDoc = open(summaryDocName, 'w')

ScrapeArticles(newsWebsiteOne)
ScrapeArticles(newsWebsiteTwo)
ScrapeArticles(newsWebsiteThree)

summaryDoc.close()