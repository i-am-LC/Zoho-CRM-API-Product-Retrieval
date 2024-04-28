# Zoho CRM Product Data Retrieval

This project aims to retrieve and clean product data from Zoho CRM using Zoho's API. It includes functionalities to obtain access tokens for API authentication and retrieve active product information.

## Zoho documentation
`https://www.zoho.com/crm/developer/docs/api/v2/`

Read the above Zoho CRM API documentation to assist in setting up OAuth access.

## Installation

1. Clone this repository: 

2. Install the required dependencies:
```pip install -r requirements.txt```

3. Set up your environment variables by creating a `.env` file in the project directory and adding the following variables:
```
ZCRM_CLIENT_ID=your_zoho_client_id
ZCRM_CLIENT_SECRET=your_zoho_client_secret
ZCRM_GRANT_TOKEN=your_zoho_grant_token
```

## Usage
Run the `run_query.py` script to retrieve and display cleaned product data from Zoho CRM.

```
python run_query.py
```

## Project Structure
* `main.py`: Main script to execute the program.
* `access_tokens/`: Module containing functions to handle access tokens for Zoho API authentication.
* `obtain_access_token.py`: Script to initialize Zoho tokens.
* `README.md`: Project documentation.

## Dependencies

* `requests`: For making HTTP requests to Zoho's API.
* `dotenv`: For loading environment variables from the .env file.

## Contributing
Contributions are welcome! Feel free to open issues or submit pull requests.

## License
This project is licensed under the MIT License

