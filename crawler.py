import requests
import bs4
def get_file_name(url):
	return url.split("/")[-1].replace(".html ",".txt")
def get_all_links(url):
	list1=[]
	resp=requests.get(url)
	soup=bs4.BeautifulSoup(resp.content,features="html.parser")
	title=soup.find_all("a",attrs={"class":"title"})
	for i in title:
		lis1.append(i['href'])
def get_all_lyrics(url):
	resp=requests.get(url)
	soup=bs4.BeautifulSoup(resp.content)
	verse=soup.find_all("p",attrs={"class":"verse"})
	for i in verse:
		print(i)
def main():
      	links=get_all_links('https://www.metrolyrics.com/grateful-dead-lyrics.html')
	for link in links:
		fname=get_file_name(link)
		print(fname)
		f=open(fname)
		lyrics=get_song_lyrics(link)
		f.write(lyrics)
		f.close()

if __name__== "__main__":
	main()

