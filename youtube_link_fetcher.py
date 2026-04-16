import requests

# 🔑 Put your SerpAPI key here
API_KEY = "YOUR_SERPAPI_KEY"

def fetch_youtube_links(query):
    url = "https://serpapi.com/search"
    
    params = {
        "engine": "youtube",        # 👈 using general API with youtube engine
        "search_query": query,
        "api_key": API_KEY
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    # Extract only links
    links = [video["link"] for video in data.get("video_results", []) if "link" in video]
    
    return links


# 🎯 User input
topic = input("Enter topic: ")

# 📺 Get results
results = fetch_youtube_links(topic)

# 🔗 Print ONLY links
for link in results:
    print(link)
