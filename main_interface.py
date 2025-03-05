import logging
from simple_sort import simple_sort
from advanced_sort import ai_based_sort

def main():
    # Set logging level to WARNING to suppress INFO messages
    logging.basicConfig(level=logging.WARNING)

    # Ask the user for the path and sorting method
    root_directory = input("Enter the directory path to organize: ").strip()
    #C:\Users\reals\Desktop\test
    sort_method = input("Which sorting method do you want? (simple/advanced enter as s/a): ").strip().lower()

    if sort_method == "s":
        try:
            simple_sort(root_directory)
            print("Sorting completed successfully.")
            logging.info("Sorting completed successfully.")
        except Exception as e:
            print(f"An error occurred during sorting: {e}")
            logging.error(f"An error occurred during sorting: {e}")
    elif sort_method == "a":
        try:
            ai_based_sort(root_directory)
            print("AI-based sorting completed successfully.")
            logging.info("AI-based sorting completed successfully.")
        except Exception as e:
            print(f"An error occurred during AI-based sorting: {e}")
            logging.error(f"An error occurred during AI-based sorting: {e}")
    else:
        print("Invalid sorting method selected. Please choose 'simple' or 'advanced'.")
        logging.error("Invalid sorting method selected. Please choose 'simple' or 'advanced'.")

if __name__ == "__main__":
    main()
