# AI News Aggregator

This project is designed to scrape AI-related news articles from specified websites, store them in a SQLite database (news.db),
and provide a simple API for keyword-based search and retrieval.

## Table of Contents

 [Project Overview](#project-overview)
 [Features](#features)
 [Installation](#installation)
[Running the Scraper](#running-the-scraper)
[Starting the API Server](#starting-the-api-server)
 [Accessing the News Data](#accessing-the-news-data)
[API Endpoints](#api-endpoints)
[Configuration](#configuration)
 
## Project Overview

The AI News Aggregator automates the collection of news articles related to artificial intelligence from various online sources. 
It stores the extracted data in a SQLite database (news.db) and offers a RESTful API to retrieve and search the stored articles using keyword-based queries.

## Features

- *Web Scraping:* Automated extraction of AI-related news articles from predefined websites.
- *Data Storage:* Storage of scraped articles in a SQLite database (news.db).
- *API Service:* Provision of a RESTful API to search and retrieve articles based on keywords.

## Installation

Follow these steps to set up the project locally:

1. *Clone the repository:*
   ```bash
   git clone  https://github.com/Hudakhanum/webscraper-and-api.git

2. Navigate to the project:
    cd ai-news-aggregator

3.install the required dependencies:
    pip install -r requirements.txt

4.Set up the database:
The scraper.py script will initialize the news.db database upon its first run. Ensure that the script has the necessary permissions to create and write to files in the project directory.

## Running the Scraper

To extract AI-related news articles and populate the database, execute:

python scraper.py

This script will connect to predefined news websites,scrape relevant articles,and store them in news.db.

## starting the API server
to launch the Api server for quwrying the stored  article:
python api.py

by default , the server will run on http://127.0.0.1:5000/.

## Accessing the News Data

With the API server running, you can interact with the endpoints using tools like Postman or curl to search and retrieve articles based on keywords.

## API Endpoints
	•	GET /search
	•	Description: Retrieve articles matching specified keywords.
	•	Query Parameters:
	•	q (string): The keyword to search for in article titles and content.
	•	Response:
	•	200 OK: Returns a JSON array of matching articles.
	•	400 Bad Request: If the query parameter is missing.

 Example request:
 curl "http://127.0.0.1:5000/search?q=AI"

 Example Response:

 [
    {
      "id": 1,
      "title": "Advancements in AI Technology",
      "content": "Recent developments in artificial intelligence have...",
      "url": "http://example.com/advancements-in-ai",
      "published_date": "2025-04-01"
    },
    ...
  ]

  Configuration
	•	Database: Ensure that news.db is present in the project directory. The scraper.py script will create and initialize this database if it does not exist.
	•	Logging: Both scraper.py and api.py include logging to provide insights into their operations. Review the log messages for debugging and monitoring purposes.


