from googlesearch import search

# Query to be searched
query = "Python"

# Makes the search and creates a list with the results
result = list(
    search(
        query,
        lang='pt-br',
        num_results=5
    )
)

print(result)
