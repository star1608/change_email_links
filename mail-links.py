import os
import re
from email.parser import Parser
from email.mime.text import MIMEText

COPYRIGHT_NOTICE = """
# Copyright (c) 2024 Eyal Zabarsky
#
# This script is provided "as is" without any warranty of any kind.
# The author is not responsible for any damages arising from the use
# of this script.
"""

def get_eml_file():
    eml_file = input("Please enter the path to the .eml file: ")
    if not os.path.exists(eml_file):
        print("File not found. Please try again.")
        return get_eml_file()
    return eml_file

def extract_links(eml_file):
    with open(eml_file, 'r') as f:
        email_content = f.read()
    parser = Parser()
    email_message = parser.parsestr(email_content)
    links = []
    for part in email_message.walk():
        if part.get_content_type() == 'text/html':
            html_content = part.get_payload(decode=True)
            links.extend(re.findall(r'<a href="([^"]+)"', html_content.decode('utf-8')))
    return links

def replace_links(links):
    replace_all = input("Do you want to replace all links at once? (yes/no): ").strip().lower()
    new_links = {}
    if replace_all == 'yes':
        new_link = input("Enter the new link to replace all instances: ")
        new_links = {link: new_link for link in links}
    else:
        for link in links:
            new_link = input(f"Enter a new link to replace {link}: ")
            new_links[link] = new_link
    return new_links

def save_as_html(eml_file, new_links):
    with open(eml_file, 'r') as f:
        email_content = f.read()
    parser = Parser()
    email_message = parser.parsestr(email_content)
    for part in email_message.walk():
        if part.get_content_type() == 'text/html':
            html_content = part.get_payload(decode=True)
            for link, new_link in new_links.items():
                html_content = html_content.replace(link.encode('utf-8'), new_link.encode('utf-8'))
            output_file = 'output.html'
            with open(output_file, 'wb') as f:
                f.write(html_content)
            print(f"HTML file saved as {output_file}")

def save_as_eml(eml_file, new_links):
    with open(eml_file, 'r') as f:
        email_content = f.read()
    parser = Parser()
    email_message = parser.parsestr(email_content)
    for part in email_message.walk():
        if part.get_content_type() == 'text/html':
            html_content = part.get_payload(decode=True)
            for link, new_link in new_links.items():
                html_content = html_content.replace(link.encode('utf-8'), new_link.encode('utf-8'))
            part.set_payload(html_content)
    output_file = 'output.eml'
    with open(output_file, 'w') as f:
        f.write(email_message.as_string())
    print(f"EML file saved as {output_file}")

def main():
    eml_file = get_eml_file()
    links = extract_links(eml_file)
    new_links = replace_links(links)
    save_as_html(eml_file, new_links)
    save_as_eml(eml_file, new_links)
    print(COPYRIGHT_NOTICE)

if __name__ == '__main__':
    main()
