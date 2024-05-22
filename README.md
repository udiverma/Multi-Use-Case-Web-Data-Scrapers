# Multi-Use-Case-Web-Data-Scrapers

Welcome to the **Multi-Use-Case-Web-Data-Scrapers** repository! This repository hosts a collection of versatile web and data scrapers designed to address a variety of scraping needs across different domains. 

## Table of Contents
- [Multi-Use-Case-Web-Data-Scrapers](#multi-use-case-web-data-scrapers)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Scrapers](#scrapers)
    - [GMU Patriot Web Scraper](#gmu-patriot-web-scraper)
      - [Scripts](#scripts)
  - [Installation](#installation)
  - [Usage](#usage)

## Introduction
This repository is a one-stop shop for various web scraping tools that can be used to extract and compile data from multiple online sources. Each scraper is tailored for a specific use case, making it easy to gather and process data efficiently.

## Scrapers

### GMU Patriot Web Scraper
**Description**: This scraper is designed to extract information from the George Mason University (GMU) Patriot Web portal. It's perfect for students and researchers who need to gather data related to courses, schedules, and other academic information.

**Key Features**:
- Extracts course schedules, descriptions, and instructor information
- Does not require any login or HTML header parameters
- Customizable query parameters and results for different academic terms

#### Scripts
- `fetchCourse.py`: Retrieves detailed course information including course name, description, schedule, and instructor details.
- `fetchEnrollment.py`: Gathers enrollment data for specified courses, providing insights into class sizes and seat availability.

## Installation
To get started with any of these scrapers, follow these simple steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/udiverma/Multi-Use-Case-Web-Data-Scrapers.git
    ```
2. Navigate to the project directory:
    ```sh
    cd Multi-Use-Case-Web-Data-Scrapers
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
Each scraper comes with its own set of instructions and customizable options. Refer to the individual scraper's README file within their respective directories for detailed usage instructions.