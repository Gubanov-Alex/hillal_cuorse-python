import codecs
import re


def delete_html_tags(html_file, result_file='cleaned.txt'):
    """Clean Tags Function:
    1.Reads an HTML file.
    2.Removes all HTML tags.
    3.Removes all empty lines.
    4.Writes the cleaned text to the output file.

    :param html_file: File for checking.
    :type html_file: File HTML.
    :param result_file: Result of checking.
    :rtype: File txt.
    """

    with codecs.open(html_file, 'r', 'utf-8') as file:
        html = file.read()
        clean_html = re.sub(r'<[^>]+>', '', html)  # Tags cleaning
        clean_html = '\n'.join(line for line in clean_html.splitlines() if line.strip() != '')  # Space cleaning

    with open(result_file, 'w', encoding='utf-8') as file:
        file.write(clean_html)


delete_html_tags(
    'draft.html',
    'draft_cleaned.txt')
