import nltk
import newspaper

# Declare variables

summaryDocName = 'news_summary.txt'

newsWebsiteOne = 'https://www.nintendolife.com/'
newsWebsiteTwo = 'https://www.ign.com/'
newsWebsiteThree = 'https://www.eurogamer.net/'

# 0nly pass a max of 5 articles per web source
maxArticlesPerWebsite = 5

doneWithEnteringKeywords = False

keywordList = list()

# List of functions

def GetUserKeyword(prompt):
    return input(prompt)

def ScrapeArticles(source):

    articles = 0

    src = newspaper.build(source, memoize_articles=False)

    for article in src.articles:

        # Attempt to download an article
        try:
            article.download()
            article.parse()
            article.nlp()
        except:
            continue

        foundKeyword = False

        # Only write article to file if it has any of the keywords.
        for keyword in keywordList:
            if ArticleHasKeyword(article, keyword):
                foundKeyword = True

        if foundKeyword:
            WriteArticleToDocument(article)
            articles += 1

        if articles == maxArticlesPerWebsite:
            break

def ArticleHasKeyword(article, keyword):
    if keyword in article.keywords or keyword in article.title or keyword in article.summary:
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

# Core functionality

prompt = "We focus on gaming news! Enter a keyword to guide your search OR type nothing if ready to search: "

while not doneWithEnteringKeywords:

    keyword = GetUserKeyword(prompt)

    if (keyword != ""):
        prompt = "Enter another keyword OR type nothing if ready to search: "
        keywordList.append(keyword)
    else:

        # Only add blank keyword to keyword list if the list is empty
        if len(keywordList) <= 0:
            keywordList.append(keyword)

        doneWithEnteringKeywords = True

print("The search begins! Please wait...")

summaryDoc = open(summaryDocName, 'w')

ScrapeArticles(newsWebsiteOne)
ScrapeArticles(newsWebsiteTwo)
ScrapeArticles(newsWebsiteThree)

summaryDoc.close()