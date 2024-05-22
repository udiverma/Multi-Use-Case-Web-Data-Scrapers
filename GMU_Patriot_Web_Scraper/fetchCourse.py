import requests
import argparse

def fetch_class_info(term, crn):
    # Enrollment Info
    url = 'https://ssbstureg.gmu.edu/StudentRegistrationSsb/ssb/searchResults/getClassDetails'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
    }
    cookies = {
        'JSESSIONID': '',  # Blank Session ID // Not Pushing Any Cookies
    }
    data = {
        'term': term  # Session Term
    }

    # Make the POST request
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    if response.status_code == 200:
        # Convert response text (HTML) to string and parse it
        return parse_class_data(response.text)
    else:
        print("Failed to fetch data:", response.status_code)
        return {}

def parse_class_data(html_data):
    class_data = {}

    # Key markers to look for in the HTML content
    markers = {
        "Associated Term": "associated_term",
        "CRN": "crn",
        # "Campus": "campus",
        # "Schedule Type": "schedule_type",
        # "Instructional Method": "instructional_method",
        "Section Number": "section_number",
        "Subject": "subject",
        "Course Number": "course_number",
        "Title": "title",
        # "Credit Hours": "credit_hours",
        # "Grade Mode": "grade_mode"
    }

    # Iterate over each marker and extract the corresponding value
    for key, value in markers.items():
        start_index = html_data.find(key + ':') + len(key) + 1  # Move index past the key and colon
        if start_index > len(key):  # Check that the key was actually found
            if key in ["Associated Term", "CRN", "Section Number", "Subject", "Course Number", "Title"]:
                # These keys have span tags surrounding the values
                start_number_index = html_data.find('>', html_data.find('<span', start_index)) + 1
                end_number_index = html_data.find('</span>', start_number_index)
            else:
                # Other keys do not have span tags around the values
                start_number_index = start_index
                end_number_index = html_data.find('<br', start_number_index)
            
            # Extract the value and strip any extraneous spaces or newline characters
            value_text = html_data[start_number_index:end_number_index].strip()
            # Store in dictionary
            class_data[value] = value_text

    return class_data

# Example usage: Fetching and parsing the data
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch GMU course information.')
    parser.add_argument('--term', type=str, required=True, help='Academic term (e.g., 202470 for Fall 2024)')
    parser.add_argument('--crn', type=str, required=True, help='Course Reference Number (CRN)')

    args = parser.parse_args()

    class_info = fetch_class_info(args.term, args.crn)
    print(class_info)