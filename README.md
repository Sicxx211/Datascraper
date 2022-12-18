# Datascraper


# How I wrote the code
I wrote this app in order to save time in the morning, Hacker News is a good place to get insight on technology nowadays but I don't want to waste my own time to find a good article to read, what this app does, basically will scan the first 2 pages on HN and return only the articles that have points higher than 100, so you would save time and read only the good articles.



# Code: 

import requests <br>
from bs4 import BeautifulSoup <br>
import pprint #this is the pretty print library, it will allow us to print things nicely in the terminal <br>
<br>
res = requests.get('https://news.htycombinator.com/news') <br>
res2 = requests.get('https://news.htycombinator.com/news?p=2') <br>
<br>
soup = BeautifulSoup(res.text, 'html.parser') <br>
soup2 = BeautifulSoup(res2.text, 'html.parser') <br>
<br>
links = soup.select('.titleline') <br>
subtext = soup.select('.subtext') <br>
links2 = soup2.select('.titleline') <br>
subtext2 = soup2.select('.subtext') <br>
mega_links = links + links2 <br>
mega_subtext = subtext + subtext2 <br>
<br>
def sort_stories_by_votes(hnlist):  return sorted(hnlist, key=lambda k:k['votes'], reverse=True) #we use this lambda functions because we will need to sort a dictionary between a dictionary, if we used sorted simply like that it will give us an error, this way we will only specify the key that we want to sort and it will get rid of the errors, and we add reversed=True, so we actually get the higher values on top <br>
<br>
#We used enumerate, because here we have two lists, the links and the subtext, and we're only enumerating over the links list.And subtext is not being enumerated.So what happens here, we need the index so that we can access this subtext within our loop.Because otherwise, if we dind't enumerate, there's no way to grab both links and subtext items. #So instead of using title = links[inx].getText... we can actually use item. instead <br>
<br>
def create_custom_hn(links,subtext): <br>
 hn = [] <br>
 for inx,item in enumerate(links): #we will use enumerate for this <br>
  title = item.getText() #this is to get the title from the links <br>
  href = item.get('href', None) #This basically will take all the hyperlinks from the links that we had before, and in case the link is broken or smth we have a default param called None so it won't break our program <br>
  <br>
  vote = subtext[inx].select('.score') #So bascially what we will do is to access the subtext and select the .score class <br>
  if len(vote): <br>
   points = int(vote[0].getText().replace(' points', '')) #this is going to run only if the vote list exists <br>
   if points > 99: #this basically tells if the story has over 99 points then append it to the list, if not do not append it <br>
    hn.append({'title' : title, 'link' : href, 'votes':points}) #This basically will get the Name of each story from the link and convert it to text, and then it will append to the hn list, this finally will append the title and it's link to the list <br>
 <br>
 return sort_stories_by_votes(hn) <br>
pprint.pprint(create_custom_hn(megalinks, megasubtext)) <br>
