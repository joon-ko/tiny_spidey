import random
from urllib.request import urlopen
from urllib.parse import urljoin, urlparse
from bs4 import BeautifulSoup		# I love BeautifulSoup and I only discovered it 20 minutes ago.

# ACTUAL CODE

print("~ Tiny Spidey 1.0 ~")
link = input("(Full) start URL to crawl: ")			# get start HTML file ('start state')
iters = int(input("Number of (max) iterations: "))	# number of iterations of random walk
walks = int(input("Number of walks: "))				# number of random walks (with iters iterations) to make

start_link = link 	# remember for future walks

for w in range(walks):
	link = start_link
	last_link = start_link	 
	print("Commencing traversal number "+str(w)+".\n")
	for _ in range(iters): 
		try:													# if opening link is troublesome, revert to last link
			file = urlopen(link)								# open link, get html file
		except:
			link = last_link									# continue from last link
			continue
		soup = BeautifulSoup(file, 'html.parser')				# get soup
		links = [l.get('href') for l in soup.find_all('a')]		# get list of links in page
		if len(links) == 0:										# if there are no links to go to:
			link = last_link
			continue
		links = [l for l in links if bool(urlparse(l).netloc)]	# reduce to only absolute links (more interesting)
		url = random.choice(links)								# pick next URL u.a.r
		link = urljoin(link, url)								# make accessible to future iterations

		print("Traveling to: "+link)

	print("Traversal complete.\n")	# done with traversal