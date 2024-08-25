from googlesearch import search
import requests
from bs4 import BeautifulSoup

def scrape_top_results(query, num_results=5):
    try:
        # Perform Google search
        search_results = search(query, num_results=num_results)

        for i, url in enumerate(search_results):
            print(f"Result {i + 1}: {url}")
            
            # Fetch the content of the search result
            response = requests.get(url)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract the title of the page
            title = soup.find('title').text if soup.find('title') else 'No title found'
            print(f"Title: {title}\n")
            
            # Print a separator between results
            print("="*80)
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    query = "Python programming"
    scrape_top_results(query)
