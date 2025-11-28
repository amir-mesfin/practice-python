menu = {
    "pizza": 34.00,
    "nachos": 35.00,
    "popcorn": 45.00,
    "soda": 67.00,
    "lemonade": 4.78,
    "chips": 32.78
}
cart = []
total = 0

def display_menu():
    print("********************************")
    print("------------  MENU  ------------")
    print()
    for key, values in menu.items():
        print(f"{key:15}......${values:.2f}")
    print()
    print("********************************")

def add_food_item():
    print("\n--- ADD NEW FOOD ITEM ---")
    food_name = input("Enter food name: ").strip().lower()
    
    if food_name in menu:
        print(f"'{food_name}' already exists in the menu!")
        return
    
    try:
        food_price = float(input("Enter food price: $"))
        if food_price <= 0:
            print("Price must be greater than 0!")
            return
        menu[food_name] = food_price
        print(f"✅ '{food_name}' added to menu for ${food_price:.2f}")
    except ValueError:
        print("Invalid price! Please enter a valid number.")

# Main program
while True:
    print("\n1. View Menu")
    print("2. Add Food to Cart")
    print("3. Add New Food Item to Menu")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    
    choice = input("\nSelect an option (1-6): ").strip()
    
    if choice == '1':
        display_menu()
        
    elif choice == '2':
        display_menu()
        while True:
            food = input("\nSelect an item (b to go back): ").strip().lower()
            if food == 'b':
                break
            elif menu.get(food) is not None:
                cart.append(food)
                print(f"✅ '{food}' added to cart!")
            else:
                print("❌ Item not found in menu!")
                
    elif choice == '3':
        add_food_item()
        
    elif choice == '4':
        if not cart:
            print("\n🛒 Your cart is empty!")
        else:
            print("\n--- YOUR CART ---")
            cart_total = 0
            for item in cart:
                price = menu.get(item, 0)
                print(f"{item:15}......${price:.2f}")
                cart_total += price
            print("-" * 30)
            print(f"TOTAL: ${cart_total:.2f}")
            
    elif choice == '5':
        if not cart:
            print("\n🛒 Your cart is empty! Add items before checkout.")
            continue
            
        print("\n" + "="*50)
        print("              FINAL ORDER SUMMARY")
        print("="*50)
        
        final_total = 0
        for item in cart:
            price = menu.get(item, 0)
            print(f"{item:15}......${price:.2f}")
            final_total += price
            
        print("-" * 50)
        print(f"GRAND TOTAL: ${final_total:.2f}")
        print("="*50)
        print("Thank you for your order! 🎉")
        cart.clear()
        break
        
    elif choice == '6':
        print("Goodbye! 👋")
        break
        
    else:
        print("Invalid choice! Please select 1-6.")