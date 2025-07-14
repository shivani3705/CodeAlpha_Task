import csv
from datetime import datetime

STOCK_PRICES = {
    "AAPL": 190, # Apple Inc.
    "MSFT": 345, # Microsoft Corporation
    "GOOGL": 135, # Alphabet Inc. (Google)
    "AMZN": 130, # Amazon.com Inc.
    "TSLA": 265, # Tesla Inc.
    "META": 310, # Meta Platforms Inc.
    "NVDA": 490, # NVIDIA Corporation
    "NFLX": 415, # Netflix Inc.
    "AMD": 125, # Advanced Micro Devices
    "INTC": 36, # Intel Corporation
    "JPM": 155, # JPMorgan Chase & Co.
    "V": 245, # Visa Inc.
    "MA": 395, # Mastercard Inc.
    "DIS": 88, # The Walt Disney Company
    "KO": 61, # Coca-Cola Co.
    "PEP": 177, # PepsiCo Inc.
    "WMT": 160, # Walmart Inc.
    "MCD": 295, # McDonald's Corp.
    "SPY": 545, # S&P 500 ETF
    "QQQ": 465 # Nasdaq 100 ETF
}

def display_available_stocks():
    print("📈 Available Stocks:")
    for stock, price in STOCK_PRICES.items():
        print(f"  {stock}: ${price}")
    print("-" * 40)

def get_portfolio():
    portfolio = {}
    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper()
        if stock == 'DONE':
            break
        if stock not in STOCK_PRICES:
            print(f"❌ {stock} is not available in price list.")
            continue
        try:
            qty = int(input(f"Enter quantity of {stock}: "))
            if qty <= 0:
                print("⚠️ Quantity must be a positive number.")
                continue
            portfolio[stock] = portfolio.get(stock, 0) + qty
        except ValueError:
            print("⚠️ Please enter a valid number.")
    return portfolio

def calculate_investment(portfolio):
    investments = []
    total = 0
    for stock, qty in portfolio.items():
        price = STOCK_PRICES[stock]
        investment = qty * price
        investments.append((stock, qty, price, investment))
        total += investment
    return investments, total

def display_summary(investments, total):
    print("\n📊 Portfolio Summary")
    print(f"{'Stock':<8} {'Qty':>5} {'Price':>8} {'Investment':>12}")
    print("-" * 36)
    for stock, qty, price, inv in investments:
        print(f"{stock:<8} {qty:>5} {price:>8} {inv:>12}")
    print("-" * 36)
    print(f"{'TOTAL':<8} {'':>5} {'':>8} {total:>12}")
    print()

def save_to_files(investments, total):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    txt_filename = f"portfolio_{timestamp}.txt"
    csv_filename = f"portfolio_{timestamp}.csv"

    with open(txt_filename, 'w') as f:
        f.write("Stock   Qty   Price   Investment\n")
        for stock, qty, price, inv in investments:
            f.write(f"{stock:<8} {qty:>5} {price:>8} {inv:>12}\n")
        f.write(f"{'TOTAL':<8} {'':>5} {'':>8} {total:>12}\n")
    print(f"✅ Saved summary to {txt_filename}")

    with open(csv_filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Stock", "Quantity", "Price", "Investment"])
        for row in investments:
            writer.writerow(row)
        writer.writerow(["TOTAL", "", "", total])
    print(f"✅ Saved summary to {csv_filename}\n")

def main():
    print("=== Advanced Stock Portfolio Tracker ===")
    display_available_stocks()
    portfolio = get_portfolio()
    if not portfolio:
        print("No stocks added. Exiting.")
        return

    investments, total = calculate_investment(portfolio)
    display_summary(investments, total)

    save_choice = input("Do you want to save the result to files? (y/n): ").lower()
    if save_choice == 'y':
        save_to_files(investments, total)

if __name__ == "__main__":
    main()
