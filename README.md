This Python script processes an .eml file to update the links within it. It performs the following tasks:

File Path Input:

Prompts the user to enter the path to the .eml file they wish to modify.
Checks if the specified file exists and prompts again if not.
Extract Links:

Reads the .eml file and extracts all URLs found in the HTML content of the email.
Link Replacement:

Asks the user if they want to replace all links at once or individually.
If replacing all links at once, the user is prompted to enter a new link that will replace all existing links in the email.
If replacing links individually, the user is prompted to enter new URLs for each extracted link.
Save Modified Content:

Saves the modified HTML content to a file named output.html.
Saves the modified email content (with updated links) back to a file named output.eml.

