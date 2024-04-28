import requests
import json
from urllib.parse import urlencode

from access_tokens.obtain_access_token import initialize_zoho_tokens


# Constants
BASE_URL = "https://www.zohoapis.com/crm/v6/Products"
FIELDS = {
    "fields": "Product,Product_Active,Product_Name,Unit_Price,Unit_Price_Recurring,Product_Type,Product_Category,Product_Code,Description"
}
PARAMS = {
    "product_active": "true"
}

def get_active_products():
    """Retrieve active products from Zoho CRM."""
    access_token = initialize_zoho_tokens()
    query_params = urlencode(FIELDS) + "&" + urlencode(PARAMS)
    call_url = f"{BASE_URL}?{query_params}"

    # Headers containing authorization token
    headers = {
        "Authorization": f"Zoho-oauthtoken {access_token}"
    }

    try:
        # Making a GET request to retrieve active products
        response = requests.get(call_url, headers=headers)

        # Check if the request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print("Failed to retrieve active products. Status code:", response.status_code)
            return None
    except Exception as e:
        print("An error occurred:", e)
        return None
    
def clean_product_data(product_data):
    cleaned_data = []
    for product in product_data:
        cleaned_product = {
            'Product_Category': product['Product_Category'],
            'Product_Code': product['Product_Code'],
            'Product_Name': product['Product_Name'],
            'Description': product['Description'].replace('\n', ' ') if product['Description'] else None,
            'Product_Type': product['Product_Type'],
            'Unit_Price_Recurring': product['Unit_Price_Recurring'],
            'Product_Active': product['Product_Active'],
            'Unit_Price': product['Unit_Price']
        }
        cleaned_data.append(cleaned_product)
    return cleaned_data

def get_cleaned_product_data():
    """Retrieve and return cleaned product information."""
    active_products = get_active_products()
    if active_products:
        return clean_product_data(active_products['data'])
    else:
        return None
