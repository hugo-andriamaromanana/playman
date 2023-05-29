# YouTube Playlist Scraper

This code is a YouTube playlist scraper written in Python. It allows you to scrape all the playlists and their corresponding video items from a YouTube channel.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/hugo-andriamaromanana/playman/
   ```

2. Install the required dependencies:

   ```
   pip install -r requirements.txt
   ```

3. Set up API credentials:

   - Create a new project in the Google Developer Console.
   - Enable the YouTube Data API v3 for the project.
   - Obtain a YouTube Data API key from the Google Developer Console.

   - Create a new file named `params.json` in the `settings` directory.
   - Copy the API key and replace the value of `PARAMS['key']` in the `params.json` file located in the `settings` directory.
   
   - You will also need an additional directory named docs in the root directory of the project. This is where the scraped data will be stored. 

4. Run the script:

   ```
   python main.py <username> <channel_id>
   ```

   - `<username>`: The username of the YouTube channel.
   - `<channel_id>`: (Optional) The ID of the YouTube channel. If not provided, the script will retrieve it using the username.

## Usage

The script performs the following steps:

1. Checks if the user already exists in the system. If not, it creates a new user with the provided username and channel ID.
2. Scrapes all the playlists from the specified YouTube channel.
3. Scrapes the video items from each playlist and stores the data in a CSV file.

The script makes use of the following modules:

- `scrapper.py`: Contains functions for scraping playlists and video items.
- `user_creation.py`: Contains functions for creating a new user and saving the channel ID.

Those modules are located in the `core` directory.

## Data Storage

The scraped data is stored in the `docs` directory, organized by username. For each user, a directory is created with their username, and an `items.csv` file is generated to store the video item data.

## Note

- This code relies on the YouTube Data API. Make sure to comply with the terms of service and usage limits of the API to avoid any issues.
- It's recommended to run the script sparingly to avoid hitting API rate limits or incurring any quota limitations (Default is set to 50k) .