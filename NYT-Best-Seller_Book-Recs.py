import requests  # This module helps us to make HTTP requests to the API


# This function is to get bestseller book data from the NYT Books API
def get_bestseller_books(list_name, api_key):
    base_url = "https://api.nytimes.com/svc/books/v3/lists/current/"
    full_url = base_url + list_name + ".json?api-key=" + api_key

    # to make a GET request to the book API
    response = requests.get(full_url)

    # Return the resulting response data as JSON
    return response.json()


# A function to create book suggestions based on the bestseller list
def create_suggestions(books_data):
    suggestions = []
    books = books_data['results']['books']  # creates a list of books

    # Loop through the books and create suggestions based on rank on the NYT list
    for book in books:
        rank = book['rank']
        title = book['title']
        author = book['author']

        if rank <= 5:
            suggestions.append(f"Highly recommended: '{title}' by {author}")
        else:
            suggestions.append(f"Also consider: '{title}' by {author}")

    return suggestions


# Then the main function to run the app
def main():
    api_key = "your_nyt_api_key_here"  # Put your New York Times API key here in ""
    list_name = input(
        # Ask user for the genre-provided examples of main genre's
        "Enter the genre (list name) you are interested in (e.g., 'hardcover-fiction','hardcover-nonfiction',"
        "'young-adult-hardcover','audio-fiction'): ")
    # Fetch the bestseller books data
    books_data = get_bestseller_books(list_name, api_key)

    # Check if the list was found
    if 'results' not in books_data:
        print("List not found. Please check the name and try again.")
        return

    # Get the suggestions based on the bestseller list
    suggestions = create_suggestions(books_data)

    # Save suggestions to a text file
    with open("book_suggestions.txt", "w") as file:
        file.write(f"Book suggestions for the {list_name} list:\n")
        for suggestion in suggestions:
            file.write(f"- {suggestion}\n")

    print(f"Book suggestions have been saved to book_suggestions.txt")


# Run the main function
if __name__ == "__main__":
    main()
