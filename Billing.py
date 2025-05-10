# Grocery Store Billing System

def print_receipt(items, prices, quantities, total_price):
    print("\n==================== Grocery Store ====================")
    print("Item\t\t\tQuantity\tPrice\t\tTotal")
    print("-------------------------------------------------------")
    for i in range(len(items)):
        total_item_price = prices[i] * quantities[i]
        print(f"{items[i]}\t\t{quantities[i]}\t\t{prices[i]} \t\t{total_item_price}")
    print("-------------------------------------------------------")
    print(f"Total Price: ₹{total_price}")
    print("==================== Thank You for Shopping! ====================")

def grocery_billing_system():
    items = []
    prices = []
    quantities = []

    print("🛒 Welcome to the Grocery Store Billing System!\n")
    while True:
        item = input("Enter item name (or type 'done' to finish): ").strip()
        if item.lower() == 'done':
            break
        items.append(item)
        
        try:
            price = float(input(f"Enter price for {item}: ₹"))
            quantities.append(int(input(f"Enter quantity for {item}: ")))
        except ValueError:
            print("⚠️ Invalid input. Please enter numeric values for price and quantity.")
            continue

        prices.append(price)

    total_price = sum([prices[i] * quantities[i] for i in range(len(items))])

    print_receipt(items, prices, quantities, total_price)

if __name__ == "__main__":
    grocery_billing_system()
