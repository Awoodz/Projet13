import requests


class Openfoodfact_request:
    """Makes JSON requests on OpenFoodFact API"""

    def category_request(category, page_nb):
        """Request category JSON on OpenfoodFact API"""
        request = requests.get(
            "https://fr.openfoodfacts.org/category/"
            + category
            + "/"
            + str(page_nb)
            + ".json"
        )
        return request.json()

    def product_request(product_id):
        """Request product JSON on OpenfoodFact API"""
        request = requests.get(
            "https://fr.openfoodfacts.org/api/v0/product/" + product_id + ".json"
        )
        return request.json()
