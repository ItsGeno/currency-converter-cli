#   Currency Converter CLI

A command-line tool that converts an amount between currencies using live exchange rates.

#   Features
-   Converts between any two currencies supported by the API
-   Validates the amount and currency codes
-   Clear error messages for invalid input and connection problems

#   Requirements
-   Python 3.11+ (Tested on 3.11)

##  Installation

```bash
git clone https://github.com/ItsGeno/currency-converter-cli.git
cd currency-converter-cli
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
pip install -r requirements.txt
```

##  Usage

```bash
python main.py
```

Example:

```
Enter the amount: 100
Enter the source currency (e.g. USD): USD
Enter the target currency (e.g. COP): EUR
100.0 USD = 89.21 EUR
```


##  Error handling

| Case              | Message                                               |
|-------------------|-------------------------------------------------------|         
| Invalid amount    | `Error: The amount is not valid.`                     |
| Unknown currency  | `Error: The currency entered is not valid: XYZ`       |
| No internet       | `Error: Could not connect to the conversion service.` |

##  Built with

- Python
- [requests](https://requests.readthedocs.io/)
- Exchange rates from [open.er-api.com](https://www.exchangerate-api.com)

##  About

Practice project to sharpen my Python skills.