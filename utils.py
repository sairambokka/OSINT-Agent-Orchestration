import os
from typing import List
from exa_py import Exa
from crewai.tools import tool

class ExaSearchTool:
    @tool("Search")
    def search(query: str) -> str:
        """Search for a webpage based on a query. It returns a list of results with titles, URLs, and IDs."""
        try:
            exa = Exa(api_key=os.environ.get("EXA_API_KEY"))
            response = exa.search(f"{query}", use_autoprompt=True, num_results=10)
            
            parsed_results = []
            for res in response.results:
                parsed_results.append(
                    f"<Title>{res.title}</Title>\n<URL>{res.url}</URL>\n<ID>{res.id}</ID>\n<PublishedDate>{res.published_date}</PublishedDate>\n<Author>{res.author}</Author>"
                )
            
            return "\n\n".join(parsed_results)
        except Exception as e:
            return f"An error occurred during search: {e}"

    @tool("Find Similar")
    def find_similar(url: str) -> str:
        """Search for webpages similar to a given URL. The input must be a URL from the 'Search' tool."""
        try:
            exa = Exa(api_key=os.environ.get("EXA_API_KEY"))
            response = exa.find_similar(url, num_results=10)

            parsed_results = []
            for res in response.results:
                parsed_results.append(
                    f"<Title>{res.title}</Title>\n<URL>{res.url}</URL>\n<ID>{res.id}</ID>\n<PublishedDate>{res.published_date}</PublishedDate>\n<Author>{res.author}</Author>"
                )
            
            return "\n\n".join(parsed_results)
        except Exception as e:
            return f"An error occurred while finding similar: {e}"

    @tool("Get Contents")
    def get_contents(ids: List[str]) -> str:
        """Get the contents of webpages. The input must be a list of IDs from the 'Search' or 'Find Similar' tool."""
        try:
            # Ensure ids is a list of strings
            if isinstance(ids, str):
                import json
                try:
                    ids = json.loads(ids)
                except json.JSONDecodeError:
                    ids = [ids]

            exa = Exa(api_key=os.environ.get("EXA_API_KEY"))
            response = exa.get_contents(ids)

            parsed_contents = []
            for content in response.results:
                parsed_contents.append(
                    f"<ID>{content.id}</ID>\n<URL>{content.url}</URL>\n<Title>{content.title}</Title>\n<Content>{content.text}</Content>"
                )
            
            return "\n\n".join(parsed_contents)
        except Exception as e:
            return f"An error occurred while getting contents: {e}"

    @staticmethod
    def tools():
      # The decorator automatically makes these functions available as tools
      return [
          ExaSearchTool.search,
          ExaSearchTool.find_similar,
          ExaSearchTool.get_contents,
      ]