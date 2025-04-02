import argparse
from scraper import run_scraper
from api import run_api_server

def main():
    parser = argparse.ArgumentParser(description="Manage the AI News Aggregator components.")
    parser.add_argument('--scraper', action='store_true', help="Run the web scraper.")
    parser.add_argument('--api', action='store_true', help="Start the API server.")
    args = parser.parse_args()

    if args.scraper:
        run_scraper()
    if args.api:
        run_api_server()
    if not (args.scraper or args.api):
        print("No action specified. Use --scraper to run the scraper and/or --api to start the API server.")

if __name__ == "_main_":
    main()