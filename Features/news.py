import requests	 

def GetNews():
	try:
		query_params = {
		"source": "bbc-news",
		"sortBy": "top",
		"apiKey": "d4ce510ba09248b6b7f1d2dc813982cb"
		}
		main_url = " https://newsapi.org/v1/articles"

		res = requests.get(main_url, params=query_params)
		open_bbc_page = res.json()

		article = open_bbc_page["articles"]

		results = []
		
		for ar in article:
			results.append(ar["title"])
		news=results[0:5]
		return f"The latest news are as follows. {news[0]}. {news[1]}. {news[2]}. {news[3]}. {news[4]}"
	except:
		return "Sorry, I don't have any news updates, at the moment."
