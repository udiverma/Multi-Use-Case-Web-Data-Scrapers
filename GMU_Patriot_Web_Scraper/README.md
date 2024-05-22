# GMU Patriot Web Scraper

## Description
The GMU Patriot Web Scraper is designed to extract information from the George Mason University (GMU) Patriot Web portal. It helps students and researchers gather data related to courses, schedules, and enrollment information.

## Features
- Extracts course schedules, descriptions, and instructor information
- Gathers enrollment data including class sizes and seat availability
- Does not require any login or HTML header parameters
- Customizable query parameters for different academic terms

## Installation
To get started with the GMU Patriot Web Scraper, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/udiverma/Multi-Use-Case-Web-Data-Scrapers.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Multi-Use-Case-Web-Data-Scrapers/GMU_Patriot_Web_Scraper
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

### Fetch Course Information
To fetch course information, use the `fetchCourse.py` script. 

#### Example:
```sh
python3 fetchCourse.py --term 202470 --crn 82442
```

## Fetch Enrollment Information
To fetch enrollment information, use the `fetchEnrollment.py` script.

### Example:
```sh
python3 fetchEnrollment.py --term 202470 --crn 82442
```

## Scripts

### fetchCourse.py
This script retrieves detailed course information including course name, description, schedule, and instructor details.
#### Usage:
```sh
python3 fetchCourse.py --term <term> --crn <crn>
```

### fetchEnrollment.py
This script gathers enrollment data for specified courses, providing insights into class sizes and seat availability.
#### Usage:
```sh
python3 fetchEnrollment.py --term <term> --crn <crn>
```
