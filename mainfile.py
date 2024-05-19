# This is Mini Google Search Tool Project:
from googlesearch import search
import time
from requests.exceptions import Timeout

def google_search(query):
    try:
        # Inform the user that the search is in progress
        print("Searching on Google...")

        # Use the googlesearch library to perform the search
        # Display the top 5 search results
        results = search(query, num_results=5)
        if results:
            for idx, result in enumerate(results, start=1):
                print(f"{idx}. {result}")
        else:
            print("No results found.")

    except Exception as e:
        # Handle any exceptions that may occur during the search
        print(f"An error occurred: {e}")


# Main program starts here
if __name__ == "__main__":
    # Loop to allow the user to perform multiple searches
    while True:
        # Display a welcome message and prompt the user to enter a query
        print("\nWelcome to Google-Search...")
        query = input("Please enter your query (type 'e' to exit): ")

        # Check if the user wants to exit
        if query.lower() == 'e':
            print("Exited...")
            break

        try:
            # Call the google_search function with the user's query
            google_search(query)

        except KeyboardInterrupt:
            # Handle the case where the user interrupts the search
            print("\nSevearch interrupted by user.")
            break

        # Ask the user if they want to perform another search
        another_query = input("Do you want to perform another search? (yes/no): ")

        # Check if the user wants to exit or continue searching
        if another_query.lower() != 'yes':
            print("Exiting...")
            break
