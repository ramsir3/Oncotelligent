from bs4 import BeautifulSoup
import urllib2

htmlOutput = open('thepage.html', 'w')
testPageOneQueryResult = open('firstPageTest.html', 'w')

# Components of the URL
natTrialsBaseUrl = "https://clinicaltrials.gov/"
searchString = "Melanoma+Miami"
searchQuery = "search?cond=%s".format(searchString)
recruitingStatus = "recr=Open"

searchUrl = natTrialsBaseUrl + searchQuery + "&" + recruitingStatus

soup = BeautifulSoup(urllib2.urlopen(searchUrl).read(), 'html.parser')
print(soup.prettify())

htmlOutput.write(soup.__str__())

pageData = soup.find(class_="data_table")
testPageOneQueryResult.write(pageData.__str__())
testPageOneQueryResult.close()

# the following two lines are a prayer to the Python gods
lastPageAnchorTag = list(soup.select('div[id="list_page_controls_bottom"]')[-1].children)[-2].select('a[href]')[-1].attrs["href"].__str__();
numberOfSearchResultPages = int(lastPageAnchorTag[lastPageAnchorTag.rindex("=") + 1 : len(lastPageAnchorTag)])
print(numberOfSearchResultPages)

if numberOfSearchResultPages > 1:
	for n in range(2, numberOfSearchResultPages):
		htmlOutput.write(BeautifulSoup(urllib2.urlopen(searchUrl + "&pg="+str(numberOfSearchResultPages)).read(), 'html.parser').__str__())

htmlOutput.close()