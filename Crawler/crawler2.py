import requests
import bs4
def save_lyrics(text,link):
	fname=link.split("/")[-1].replace(".html",".txt")
	with open(fname,"w") as songfile:
		verse=songfile.write(text)
def get_lyrics(url):
	lyrics=[]
	resp=requests.get(url)
	soup=bs4.BeautifulSoup(resp.content,features="html.parser")
	verses=soup.find_all("p",attrs={"class":"verse"})
	for i in verses:
		lyrics.append(i.get_text())
	return "/n".join(lyrics)
		
def get_all_links(url):
	slink=[]
	response=requests.get(url)
	soup=bs4.BeautifulSoup(response.content,features="html.parser")
	links=soup.find_all("a",attrs={"class":"title"})
	for i in links:
		slink.append(i["href"])
	return slink
		

def main():
	links=get_all_links('https://www.metrolyrics.com/grateful-dead-lyrics.html')
	for i in links:
		var=get_lyrics(i)
		save_lyrics(var,i)
		break
	print("Mission Accomplished")

if __name__=="__main__":
	main()
