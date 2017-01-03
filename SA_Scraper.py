import requests 
from bs4 import BeautifulSoup 
import re 

res = requests.get('http://seekingalpha.com/article/2051313-dollar-trees-ceo-discusses-q4-2013-results-earnings-call-transcript') 
res.raise_for_status() 
playFile = open('seeking_alpha_transcript.html', 'wb') 
for chunk in res.iter_content(100000): 
	playFile.write(chunk) 
	f = open('seeking_alpha_transcript.html') 
	soup = BeautifulSoup(f, 'html.parser') 
	links = soup.select('#a-cont')
	with open('output.txt', 'wb') as transcripts_file:
		transcripts_file.write(re.sub(r'<.*?>', '', str(links)))
