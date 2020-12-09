# Number of page requested to Openfoodfact
MAX_PAGE = 200

# Category and subcategory datas
DATA_DICT = {
    "industriel": {
        "subcategory": [
            {"name": "industriel", "duration": 0},
        ],
    },
    "viande": {
        "subcategory": [
            {"name": "boeuf", "duration": 240},
            {"name": "boeuf haché", "duration": 90},
            {"name": "agneau", "duration": 180},
            {"name": "veau", "duration": 120},
            {"name": "porc", "duration": 180},
            {"name": "porc haché", "duration": 90},
            {"name": "porc saucisse", "duration": 30},
            {"name": "poulet", "duration": 360},
        ],
    },
    "poisson": {
        "subcategory": [
            {"name": "saumon", "duration": 90},
            {"name": "sardine", "duration": 90},
            {"name": "colin", "duration": 90},
        ],
    },
    "legume": {
        "subcategory": [
            {"name": "aubergine", "duration": 360},
            {"name": "brocolis", "duration": 360},
            {"name": "carotte", "duration": 240},
            {"name": "chou-fleur", "duration": 180},
            {"name": "courge", "duration": 180},
            {"name": "courgette", "duration": 90},
            {"name": "épinard", "duration": 360},
            {"name": "haricot verts", "duration": 360},
            {"name": "petit pois", "duration": 360},
            {"name": "tomate", "duration": 90},
            {"name": "tomate en coulis", "duration": 360},
        ],
    },
    "fruit": {
        "subcategory": [
            {"name": "abricot", "duration": 360},
            {"name": "cerise", "duration": 360},
            {"name": "fraise", "duration": 360},
            {"name": "framboise", "duration": 360},
            {"name": "kiwi", "duration": 180},
            {"name": "banane", "duration": 180},
            {"name": "poire", "duration": 360},
            {"name": "pomme", "duration": 360},
            {"name": "quetsche", "duration": 360},
        ],
    },
    "produit laitier": {
        "subcategory": [
            {"name": "beurre", "duration": 120},
            {"name": "fromage fermenté", "duration": 90},
            {"name": "fromage à pâte cuite", "duration": 180},
            {"name": "fromage râpé", "duration": 90},
        ],
    },
    "boulangerie": {
        "subcategory": [
            {"name": "baguette", "duration": 7},
            {"name": "pain", "duration": 30},
            {"name": "gâteau", "duration": 90},
            {"name": "viennoiserie", "duration": 60},
            {"name": "pâte, fond de tarte", "duration": 90},
        ],
    },
    "autre": {
        "subcategory": [
            {"name": "autre", "duration": 0},
        ],
    },
}
