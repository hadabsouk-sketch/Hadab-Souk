import requests

STORE = "jdfd0q-2v.myshopify.com"
TOKEN = "YOUR_TOKEN_HERE"

def get_products():
    query = """
    {
      products(first: 10) {
        edges {
          node {
            id
            title
            handle
          }
        }
      }
    }
    """

    response = requests.post(
        f"https://{STORE}/api/2025-01/graphql.json",
        headers={
            "Content-Type": "application/json",
            "X-Shopify-Storefront-Access-Token": TOKEN
        },
        json={"query": query}
    )

    return response.json()