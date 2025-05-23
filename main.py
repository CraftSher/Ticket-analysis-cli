from utils import (
load_tickets, get_tickets_count,
get_unique_clients, get_status_count,
search_by_client_subject, filter_publication_date, filter_priority
)
from colorama import init, Fore
import re
import sys  # Import the sys module

init(autoreset=True)

def validate_date_input(date_str):
    """Проверяет формат даты (YYYY-MM)."""
    return re.match(r'^\d{4}-\d{2}$', date_str) is not None

def main():
    print(Fore.YELLOW + "\n--- Tickets Data Analysis ---")

    try:
        tickets = load_tickets("data/tickets.csv")
    except FileNotFoundError as e:
        print(Fore.RED + f"Error: {e}. Exiting.")
        sys.exit(1)  # Exit with an error code
    except ValueError as e:
        print(Fore.RED + f"Error: {e}. Exiting.")
        sys.exit(1)

    if not tickets:
        print(Fore.RED + "No data loaded. Exiting.")
        return

    while True:
        print(Fore.CYAN + "\nMenu:")
        print("1. Tickets Count")
        print("2. Unique Clients")
        print("3. Status Count")
        print("4. Search by Clients or Subject")
        print("5. Filter by Date")
        print("6. Filter by Priority")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            ticket_count = get_tickets_count(tickets)
            print(Fore.GREEN + "\nTickets Count:")
            print(Fore.CYAN + f'Ticket quantity: {ticket_count}')

        elif choice =='2':
            uniq_cl = get_unique_clients(tickets)
            print(Fore.GREEN + "\nUnique Clients:")
            print(Fore.CYAN + f'Unique Clients quantity: {uniq_cl}')

        elif choice == '3':
            stat_count = get_status_count(tickets)
            print(Fore.GREEN + "\nStatus Count:")
            for key, value in stat_count.items():
                print(f"{key.replace('_', ' ').title()}: {value}")

        elif choice == '4':
            query = input("Enter client name or subject to search: ")
            results = search_by_client_subject(tickets, query)
            if results:
                print(Fore.GREEN + "\nSearch Results:")
                for order in results:
                    print(order)
            else:
                print(Fore.YELLOW + "No matching orders found.")

        elif choice =='5':
            date_str = input("Enter year and month (YYYY-MM): ")
            if validate_date_input(date_str):
                filtered_orders = filter_publication_date(tickets, date_str)
                if filtered_orders:
                    print(Fore.GREEN + "\nFiltered Orders:")
                    for order in filtered_orders:
                        print(order)
                else:
                    print(Fore.YELLOW + "No orders found for the given date.")
            else:
                print(Fore.RED + "Error: Invalid date format. Use YYYY-MM.")

        elif choice =='6':
            priority_search = input("Enter priority to search: ").lower()
            fil_prior = filter_priority(tickets, priority_search)
            if fil_prior:
                print(Fore.GREEN + f"\nPriority Tickets: {priority_search}")
                for prior in fil_prior:
                    print(f"- ID: {prior['ticket_id']}, Client Name: {prior['client_name']}, "
                          f"Subject: {prior['subject']}, Status: {prior['status']}, Date: {prior['date']}")
            else:
                print(f'No priority tickets available: {priority_search}')

        elif choice == "0":
            print(Fore.CYAN + "Exiting.")
            break

        else:
            print(Fore.RED + "Invalid choice. Please try again.")



if __name__ == "__main__":
    main()