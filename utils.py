import pandas as pd
import re

def clean_linkedin_data(file_path):
    """
    Open the CSV file at the given file path, and drop all rows where fullName is "LinkedIn Member".
    Save the cleaned data back to the same file path.
    
    Parameters:
    file_path (str): The path to the CSV file to be cleaned.
    """
    try:
        # Load the CSV file into a DataFrame
        df = pd.read_csv(file_path)

        # Drop rows where fullName is "LinkedIn Member"
        cleaned_df = df[df['fullName'] != "LinkedIn Member"]

        # Save the cleaned DataFrame back to the CSV file
        cleaned_df.to_csv(file_path, index=False)
        print(f"Cleaned data saved to '{file_path}'.")

    except FileNotFoundError:
        print(f"Error: The file '{file_path}' was not found.")
    except pd.errors.EmptyDataError:
        print("Error: The CSV file is empty.")
    except pd.errors.ParserError:
        print("Error: The CSV file could not be parsed.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


def escape_markdown_v2(text):
    # List of characters that need to be escaped in MarkdownV2
    reserved_characters = r'_[]()>#+-=|{}.!'
    
    # Escape each character by preceding it with a backslash
    return re.sub(r'([{}])'.format(re.escape(reserved_characters)), r'\\\1', text)




# Example usage:
if __name__ == '__main__':
    # file_path = 'linkedin-people-search-scraper_5.csv'
    # clean_linkedin_data(file_path)

    # Example usage
    text = "This is a sentence with reserved characters like * and . and _."
    escaped_text = escape_markdown_v2(text)

    print(escaped_text)
