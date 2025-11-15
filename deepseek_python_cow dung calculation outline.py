# cow_dung_calculator.py
import math

def get_cow_dung_input():
    """Get cow dung purchase details - bought in lump sum, sold in MT"""
    print("\n=== COW DUNG PURCHASE DETAILS ===")
    print("(Purchased in lump sum by truck, sold in metric tons)")
    
    # Get lump sum purchase amount
    while True:
        try:
            lump_sum_amount = float(input("Enter total lump sum amount paid for cow dung: ₹"))
            if lump_sum_amount <= 0:
                print("Amount must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Get total quantity purchased (in MT)
    while True:
        try:
            total_purchased_mt = float(input("Enter total quantity purchased (in MT): "))
            if total_purchased_mt <= 0:
                print("Quantity must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    # Calculate rate per MT for cow dung
    cow_dung_rate_per_mt = lump_sum_amount / total_purchased_mt
    
    print(f"\nCalculated Cow Dung Rate: ₹{cow_dung_rate_per_mt:,.2f} per MT")
    print(f"Total Purchase: {total_purchased_mt} MT for ₹{lump_sum_amount:,.2f}")
    
    return lump_sum_amount, total_purchased_mt, cow_dung_rate_per_mt

def get_buyer_order_quantity():
    """Get the quantity required by buyer"""
    print("\n=== BUYER ORDER DETAILS ===")
    
    while True:
        try:
            buyer_quantity = float(input("Enter buyer's required quantity (in MT): "))
            if buyer_quantity <= 0:
                print("Quantity must be positive. Please try again.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    return buyer_quantity

def get_packing_charges():
    """Get packing charges with multiple input options"""
    print("\n=== PACKING CHARGES ===")
    print("Choose input method:")
    print("1. Per metric ton (MT)")
    print("2. Per kilogram (KG)") 
    print("3. Per labour (head count)")
    print("4. Per bag")
    print("5. Lumpsum for entire order")
    
    while True:
        choice = input("Enter choice (1-5): ").strip()
        
        if choice == '1':
            rate = float(input("Enter packing rate per MT: ₹"))
            return {'method': 'per_mt', 'rate': rate}
            
        elif choice == '2':
            rate = float(input("Enter packing rate per KG: ₹"))
            return {'method': 'per_kg', 'rate': rate}
            
        elif choice == '3':
            labour_count = int(input("Enter number of packing labourers: "))
            rate_per_labour = float(input("Enter rate per labourer: ₹"))
            return {'method': 'per_labour', 'count': labour_count, 'rate': rate_per_labour}
            
        elif choice == '4':
            bags_count = int(input("Enter number of bags: "))
            rate_per_bag = float(input("Enter rate per bag: ₹"))
            return {'method': 'per_bag', 'count': bags_count, 'rate': rate_per_bag}
            
        elif choice == '5':
            lumpsum = float(input("Enter lumpsum packing amount: ₹"))
            return {'method': 'lumpsum', 'amount': lumpsum}
            
        else:
            print("Please enter a valid choice (1-5).")

def get_loading_charges():
    """Get loading charges with multiple input options"""
    print("\n=== LOADING CHARGES ===")
    print("Choose input method:")
    print("1. Per metric ton (MT)")
    print("2. Per kilogram (KG)")
    print("3. Per labour (head count)") 
    print("4. Lumpsum for entire order")
    
    while True:
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            rate = float(input("Enter loading rate per MT: ₹"))
            return {'method': 'per_mt', 'rate': rate}
            
        elif choice == '2':
            rate = float(input("Enter loading rate per KG: ₹"))
            return {'method': 'per_kg', 'rate': rate}
            
        elif choice == '3':
            labour_count = int(input("Enter number of loading labourers: "))
            rate_per_labour = float(input("Enter rate per labourer: ₹"))
            return {'method': 'per_labour', 'count': labour_count, 'rate': rate_per_labour}
            
        elif choice == '4':
            lumpsum = float(input("Enter lumpsum loading amount: ₹"))
            return {'method': 'lumpsum', 'amount': lumpsum}
            
        else:
            print("Please enter a valid choice (1-4).")

def get_transport_charges():
    """Get transport charges with multiple input options"""
    print("\n=== TRANSPORT CHARGES ===")
    print("Choose input method:")
    print("1. Per metric ton (MT)")
    print("2. Per kilogram (KG)")
    print("3. Per truck (fixed amount)")
    print("4. Lumpsum for entire order")
    
    while True:
        choice = input("Enter choice (1-4): ").strip()
        
        if choice == '1':
            rate = float(input("Enter transport rate per MT: ₹"))
            return {'method': 'per_mt', 'rate': rate}
            
        elif choice == '2':
            rate = float(input("Enter transport rate per KG: ₹"))
            return {'method': 'per_kg', 'rate': rate}
            
        elif choice == '3':
            truck_cost = float(input("Enter cost per truck: ₹"))
            return {'method': 'per_truck', 'rate': truck_cost}
            
        elif choice == '4':
            lumpsum = float(input("Enter lumpsum transport amount: ₹"))
            return {'method': 'lumpsum', 'amount': lumpsum}
            
        else:
            print("Please enter a valid choice (1-4).")

def calculate_packing_cost(packing_data, quantity_mt):
    """Calculate packing cost based on input method"""
    method = packing_data['method']
    
    if method == 'per_mt':
        cost = packing_data['rate'] * quantity_mt
        rate_per_mt = packing_data['rate']
        
    elif method == 'per_kg':
        cost = packing_data['rate'] * (quantity_mt * 1000)
        rate_per_mt = packing_data['rate'] * 1000
        
    elif method == 'per_labour':
        cost = packing_data['count'] * packing_data['rate']
        rate_per_mt = cost / quantity_mt
        
    elif method == 'per_bag':
        cost = packing_data['count'] * packing_data['rate']
        rate_per_mt = cost / quantity_mt
        
    else:  # lumpsum
        cost = packing_data['amount']
        rate_per_mt = cost / quantity_mt
    
    return cost, rate_per_mt

def calculate_loading_cost(loading_data, quantity_mt):
    """Calculate loading cost based on input method"""
    method = loading_data['method']
    
    if method == 'per_mt':
        cost = loading_data['rate'] * quantity_mt
        rate_per_mt = loading_data['rate']
        
    elif method == 'per_kg':
        cost = loading_data['rate'] * (quantity_mt * 1000)
        rate_per_mt = loading_data['rate'] * 1000
        
    elif method == 'per_labour':
        cost = loading_data['count'] * loading_data['rate']
        rate_per_mt = cost / quantity_mt
        
    else:  # lumpsum
        cost = loading_data['amount']
        rate_per_mt = cost / quantity_mt
    
    return cost, rate_per_mt

def calculate_transport_cost(transport_data, quantity_mt):
    """Calculate transport cost based on input method"""
    method = transport_data['method']
    
    if method == 'per_mt':
        cost = transport_data['rate'] * quantity_mt
        rate_per_mt = transport_data['rate']
        
    elif method == 'per_kg':
        cost = transport_data['rate'] * (quantity_mt * 1000)
        rate_per_mt = transport_data['rate'] * 1000
        
    elif method == 'per_truck':
        # Assume one truck can carry 25 MT (adjust as needed)
        truck_capacity = 25
        trucks_needed = math.ceil(quantity_mt / truck_capacity)
        cost = transport_data['rate'] * trucks_needed
        rate_per_mt = cost / quantity_mt
        
    else:  # lumpsum
        cost = transport_data['amount']
        rate_per_mt = cost / quantity_mt
    
    return cost, rate_per_mt

def get_output_preference():
    """Get user preference for output units"""
    print("\n=== OUTPUT PREFERENCE ===")
    print("Choose output unit for buyer:")
    print("1. Per Metric Ton (MT)")
    print("2. Per Kilogram (KG)")
    
    while True:
        choice = input("Enter choice (1-2): ").strip()
        if choice in ['1', '2']:
            return choice
        print("Please enter a valid choice (1-2).")

def display_results(buyer_quantity, cow_dung_data, packing_data, loading_data, transport_data, output_choice):
    """Display final results in required format"""
    
    cow_dung_cost = cow_dung_data['cost']
    cow_dung_rate_per_mt = cow_dung_data['rate_per_mt']
    
    packing_cost, packing_rate_per_mt = calculate_packing_cost(packing_data, buyer_quantity)
    loading_cost, loading_rate_per_mt = calculate_loading_cost(loading_data, buyer_quantity)
    transport_cost, transport_rate_per_mt = calculate_transport_cost(transport_data, buyer_quantity)
    
    # Total calculations
    total_cost = cow_dung_cost + packing_cost + loading_cost + transport_cost
    total_rate_per_mt = total_cost / buyer_quantity
    
    print(f"\n{'='*80}")
    print(f"FINAL COST CALCULATION FOR BUYER")
    print(f"{'='*80}")
    print(f"Buyer Quantity: {buyer_quantity} MT")
    print(f"{'-'*80}")
    
    # Display based on output preference
    if output_choice == '1':  # Per MT
        print(f"COST BREAKDOWN PER METRIC TON:")
        print(f"{'-'*50}")
        print(f"Cow Dung:       ₹{cow_dung_rate_per_mt:,.2f}/MT")
        print(f"Packing:        ₹{packing_rate_per_mt:,.2f}/MT")
        print(f"Loading:        ₹{loading_rate_per_mt:,.2f}/MT") 
        print(f"Transport:      ₹{transport_rate_per_mt:,.2f}/MT")
        print(f"{'-'*50}")
        print(f"TOTAL PER MT:   ₹{total_rate_per_mt:,.2f}/MT")
        print(f"{'='*50}")
        print(f"TOTAL COST FOR {buyer_quantity} MT: ₹{total_cost:,.2f}")
        
    else:  # Per KG
        total_kg = buyer_quantity * 1000
        cost_per_kg = total_cost / total_kg
        
        cow_dung_per_kg = cow_dung_rate_per_mt / 1000
        packing_per_kg = packing_rate_per_mt / 1000
        loading_per_kg = loading_rate_per_mt / 1000
        transport_per_kg = transport_rate_per_mt / 1000
        
        print(f"COST BREAKDOWN PER KILOGRAM:")
        print(f"{'-'*50}")
        print(f"Cow Dung:       ₹{cow_dung_per_kg:,.4f}/KG")
        print(f"Packing:        ₹{packing_per_kg:,.4f}/KG")
        print(f"Loading:        ₹{loading_per_kg:,.4f}/KG")
        print(f"Transport:      ₹{transport_per_kg:,.4f}/KG")
        print(f"{'-'*50}")
        print(f"TOTAL PER KG:   ₹{cost_per_kg:,.4f}/KG")
        print(f"{'='*50}")
        print(f"TOTAL COST FOR {total_kg:,.0f} KG: ₹{total_cost:,.2f}")
    
    print(f"\nDETAILED COST BREAKDOWN:")
    print(f"{'-'*50}")
    print(f"Cow Dung:    ₹{cow_dung_cost:,.2f}")
    print(f"Packing:     ₹{packing_cost:,.2f}")
    print(f"Loading:     ₹{loading_cost:,.2f}")
    print(f"Transport:   ₹{transport_cost:,.2f}")
    print(f"{'-'*50}")
    print(f"GRAND TOTAL: ₹{total_cost:,.2f}")
    print(f"{'='*80}")