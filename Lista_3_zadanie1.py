import base64

dane = input("Podaj dowolny ciag znakow:")
dane_bytes = dane.encode("ascii")

base64_bytes = base64.b64encode(dane_bytes)
base64_string = base64_bytes.decode("ascii")

print(f"Zaszyfrowany ciag znakow: {base64_string}")
