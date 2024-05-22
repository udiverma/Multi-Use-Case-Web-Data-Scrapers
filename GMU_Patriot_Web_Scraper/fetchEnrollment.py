import requests
import argparse

def fetch_enrollment_info(term, crn):
    # Enrollment Info
    url = 'https://ssbstureg.gmu.edu/StudentRegistrationSsb/ssb/searchResults/getEnrollmentInfo'
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'X-Requested-With': 'XMLHttpRequest',
    }
    cookies = {
        'JSESSIONID': '',  # Blank Session ID // Not Pushing Any Cookies
    }
    data = {
        'courseReferenceNumber': crn,  # CRN Number as per PatriotWeb
        'term': term  # Session Term
    }

    # Make the POST request
    response = requests.post(url, headers=headers, cookies=cookies, data=data)
    if response.status_code == 200:
        # Convert response text (HTML) to string and parse it
        return parse_enrollment_data(response.text)
    else:
        print("Failed to fetch data:", response.status_code)
        return {}

def parse_enrollment_data(html_data):
    # Dictionary to hold the parsed data
    enrollment_data = {}

    # Key markers to look for in the HTML content
    markers = {
        "Enrollment Actual": "enrollment_actual",
        "Enrollment Maximum": "enrollment_maximum",
        "Enrollment Seats Available": "enrollment_seats_available",
        "Waitlist Capacity": "waitlist_capacity",
        "Waitlist Actual": "waitlist_actual",
        "Waitlist Seats Available": "waitlist_seats_available"
    }

    # Iterate over each marker and extract the corresponding value
    for key, value in markers.items():
        # Find the start of the marker
        start_index = html_data.find(key)
        if start_index != -1:
            # Find the start of the number following the key
            start_number_index = html_data.find('<span', start_index)
            start_number_index = html_data.find('>', start_number_index) + 1
            end_number_index = html_data.find('</span>', start_number_index)
            # Extract the number and strip any extraneous spaces or newline characters
            number = html_data[start_number_index:end_number_index].strip()
            # Convert to integer and store in dictionary
            enrollment_data[value] = int(number)

    return enrollment_data

# Example usage: Fetching and parsing the data
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Fetch GMU course information.')
    parser.add_argument('--term', type=str, required=True, help='Academic term (e.g., 202470 for Fall 2024)')
    parser.add_argument('--crn', type=str, required=True, help='Course Reference Number (CRN)')

    args = parser.parse_args()

    class_info = fetch_enrollment_info(args.term, args.crn)
    print(class_info)