import os
from dotenv import load_dotenv
from elasticsearch import Elasticsearch
from elasticsearch.exceptions import ConnectionError, NotFoundError, RequestError
from elastic_transport import TlsError


class ElasticsearchClient:
    def __init__(self):
        """
        Initializes an Elasticsearch client connection based on environment variables.
        """
        load_dotenv()
        host = os.getenv("ELASTICSEARCH_HOST", "localhost")
        port = int(os.getenv("ELASTICSEARCH_PORT", 9200))
        api_key = os.getenv("ELASTICSEARCH_API_KEY")

        if api_key:
            self.es = Elasticsearch(
                [f"https://{host}:{port}"],
                api_key=api_key,
                verify_certs=False,  # Disable SSL verification (for development only)
                ssl_show_warn=False,
            )
        else:
            self.es = Elasticsearch([{"host": host, "port": port}])

    def create_index(self, index_name: str):
        """
        Creates a new index in Elasticsearch.

        Args:
            index_name (str): The name of the index to create.

        Returns:
            None
        """
        try:
            response = self.es.indices.create(index=index_name)
            print("Index created:", response)
        except (RequestError, ConnectionError) as e:
            print(f"Error creating index: {e}")

    def delete_index(self, index_name: str):
        """
        Deletes an existing index from Elasticsearch.

        Args:
            index_name (str): The name of the index to delete.

        Returns:
            None
        """
        try:
            response = self.es.indices.delete(index=index_name)
            print("Index deleted:", response)
        except (NotFoundError, ConnectionError) as e:
            print(f"Error deleting index: {e}")

    def search_documents(self, index_name: str, query: dict):
        """
        Searches for documents in the specified Elasticsearch index based on a query.

        Args:
            index_name (str): The name of the Elasticsearch index to search.
            query (dict): The search query as a dictionary.

        Returns:
            list: A list of matching documents (hits) or None if there's an error.
        """
        try:
            response = self.es.search(index=index_name, body=query)
            print("Search results:", response)
            return response["hits"]["hits"]
        except (RequestError, ConnectionError, TlsError) as e:
            print(f"Error searching documents: {e}")
            return None
