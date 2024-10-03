import requests

API_KEY = 'AIzaSyBA4Igl0EyQcVOl3xqYZQTA97TtJBVIjRU'
SEARCH_ENGINE_ID = 'a018626eaeaa24e9f'
API_URL = 'https://www.googleapis.com/customsearch/v1'

def google_search(query):
    params = {
        'key': API_KEY,
        'cx': SEARCH_ENGINE_ID,
        'q': query,
    }
    response = requests.get(API_URL, params=params)
    if response.status_code == 200:
        search_results = response.json()
        if 'items' in search_results:
            # Extract the snippets from the top results
            snippets = [item['snippet'] for item in search_results['items']]
            return snippets
        else:
            return ["No results found"]
    else:
        return [f"Error: {response.status_code}"]

def summarize_snippets(snippets):
    # You can customize this function to create a more coherent summary
    return " ".join(snippets[:3])  # Join the top 3 snippets for a summary

def search_info():
    while True:
        user_input = input("Enter your question or type 'exit' to quit: ").strip()
        
        if user_input.lower() == 'exit':
            print("Goodbye!")
            break
        
        # Get search results for the user input
        search_results = google_search(user_input)
        answer = summarize_snippets(search_results)
        print(f"Answer: {answer}\n")

if __name__ == "__main__":
    search_info()
