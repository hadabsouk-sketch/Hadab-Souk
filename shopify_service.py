import requests

STORE = "jdfd0q-2v.myshopify.com"
TOKEN = "7b9bd70862a709961032165e5f2d2e0e"

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
