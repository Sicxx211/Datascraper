import requests
from bs4 import BeautifulSoup
import pprint #this is the pretty print library, it will allow us to print things nicely in the terminal
res = requests.get('https://news.htycombinator.com/news')
res2 = requests.get('https://news.htycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.titleline')
subtext = soup.select('.subtext')
links2 = soup2.select('.titleline')
subtext2 = soup2.select('.subtext')
mega_links = links + links2
mega_subtext = subtext + subtext2
def sort_stories_by_votes(hnlist):  return sorted(hnlist, key=lambda k:k['votes'], reverse=True) #we use this lambda functions because we will need to sort a dictionary between a dictionary, if we used sorted simply like that it will give us an error, this way we will only specify the key that we want to sort and it will get rid of the errors, and we add reversed=True, so we actually get the higher values on top

#We used enumerate, because here we have two lists, the links and the subtext, and we're only enumerating over the links list.And subtext is not being enumerated.So what happens here, we need the index so that we can access this subtext within our loop.Because otherwise, if we dind't enumerate, there's no way to grab both links and subtext items. #So instead of using title = links[inx].getText... we can actually use item. instead

def create_custom_hn(links,subtext):
 hn = []
 for inx,item in enumerate(links): #we will use enumerate for this
  title = item.getText() #this is to get the title from the links
  href = item.get('href', None) #This basically will take all the hyperlinks from the links that we had before, and in case the link is broken or smth we have a default param called None so it won't break our program
  vote = subtext[inx].select('.score') #So bascially what we will do is to access the subtext and select the .score class
  if len(vote):
   points = int(vote[0].getText().replace(' points', '')) #this is going to run only if the vote list exists
   if points > 99: #this basically tells if the story has over 99 points then append it to the list, if not do not append it
    hn.append({'title' : title, 'link' : href, 'votes':points}) #This basically will get the Name of each story from the link and convert it to text, and then it will append to the hn list, this finally will append the title and it's link to the list
 return sort_stories_by_votes(hn)
pprint.pprint(create_custom_hn(megalinks, megasubtext))