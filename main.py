from cow_dung_calc import (
    get_cow_dung_input,
    get_buyer_order_quantity,
    get_packing_charges,
    get_loading_charges,
    get_transport_charges,
    get_output_preference,
    display_results
)

def main():
    """Main program function"""

    print("COW DUNG BUSINESS COST CALCULATION")
    print("Purchase: Lump sum by Truck | sales: Metric Tons to Buyers")
    print("*" * 80)

    while True:
        """Get purchase details (Lump sum)"""
        lump_sum_amount,total_purchased_mt,cow_dung_rate_per_mt = get_cow_dung_input()

        """Get buyer order quantity"""
        buyer_quantity = get_buyer_order_quantity()

        """Calculate cow dung cost for buyer's quantity"""
        cow_dung_cost = cow_dung_rate_per_mt * buyer_quantity

        cow_dung_data = {
            'cost': cow_dung_rate_per_mt,
            'lump_sum_paid': lump_sum_amount,
            'total_purchased': total_purchased_mt
        }

        """Get other charges"""
        packing_data = get_packing_charges()
        loading_data = get_loading_charges()
        transport_data = get_transport_charges()

        """Get output preference"""
        output_choice = get_output_preference()

        """Display results"""
        display_results(buyer_quantity,cow_dung_data,packing_data,loading_data,transport_data,output_choice)

        """Continue or exit"""
        continue_calc = input("\nPerfom another calculation? (y/n): ")
        if continue_calc != 'y':
            print("Thank you for using the cow dung business calculator!")
            break

"""Run the program"""


if __name__ == "__main__":
    main()


