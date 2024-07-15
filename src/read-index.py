from elasticsearch_client import ElasticsearchClient

if __name__ == "__main__":
    client = ElasticsearchClient()

    query = {"query": {"match_all": {}}}
    index_name = "my-index"
    results = client.search_documents(index_name, query)

    for result in results:
        print("Document found:", result)
