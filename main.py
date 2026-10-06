import requests

class UnsupportedCurrency(Exception):
    pass

def fetch_rates(base="USD"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
    if data.get("result") != "success":
        raise UnsupportedCurrency(base)
    return data["rates"]

def is_valid_currency(code, rates):
    return code.strip().upper() in rates

def convert(amount, source, target):
    rates = fetch_rates(source)
    if not is_valid_currency(target, rates):
        raise UnsupportedCurrency(target)
    return amount * rates[target]

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount: "))
        if amount <= 0:
            raise ValueError("The amount must be greater than zero.")
        source = input("Enter the source currency (e.g. USD): ").strip().upper()
        target = input("Enter the target currency (e.g. EUR): ").strip().upper()
        result = convert(amount, source, target)
        print(f"{amount} {source} = {result:.2f} {target}")
    except ValueError as e:
        print(f"Error: The amount is not valid: {e}")
    except requests.ConnectionError:
        print("Error: Could not connect to the conversion service.")
    except requests.Timeout:
        print("Error: The request to the conversion service timed out.")
    except requests.RequestException as e:
        print(f"Error: An error occurred while making the request: {e}")
    except UnsupportedCurrency as e:
        print(f"Error: The currency entered is not valid: {e}")