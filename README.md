# Spotify Artist Top Tracks Finder

A Python-based desktop application that allows users to search for their favorite artists on Spotify and view their top tracks along with album artwork. Built using the Spotify API, Tkinter for the GUI, and PIL for displaying images.

## Features

- Search for any artist by name using Spotify's powerful search engine.
- View the top 10 tracks of the searched artist, including links to preview audio.
- Display album artwork for each track, dynamically loaded from Spotify.
- Simple GUI built using Tkinter for an easy and intuitive user experience.

## How to Use

### 1. Clone the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/yourusername/spotify-artist-top-tracks.git
cd spotify-artist-top-tracks
```

### 2. Install Dependencies

This project relies on the following Python libraries:

- `tkinter` (Standard with Python)
- `spotipy`
- `Pillow`

You can install the required libraries using the following command:

```bash
pip install spotipy Pillow
```

### 3. Get Your Spotify Developer Credentials

In order to use this application, you’ll need to get your own Spotify API credentials.

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/applications) and log in with your Spotify account.
2. Create a new app and retrieve your `client_id`, `client_secret`, and set your `redirect_uri`.
3. You can either provide these credentials via environment variables or manually enter them when prompted.

To set environment variables (optional):

```bash
export SPOTIPY_CLIENT_ID='your-client-id'
export SPOTIPY_CLIENT_SECRET='your-client-secret'
export SPOTIPY_REDIRECT_URI='your-redirect-uri'
```

### 4. Run the Application

Once your environment is set up, you can run the application by executing:

```bash
python spotify_top_tracks.py
```

### 5. Search for an Artist

- Enter the name of an artist in the input box and press "Search."
- The top 10 tracks will be displayed with links to the audio previews (if available).
- Album artwork will also be displayed in a grid format.

### Example:

![Spotify Artist Top Tracks GUI](screenshot.png)

## Notes

- You must have a Spotify account to obtain the API credentials.
- This app is designed for personal use and educational purposes, so please ensure compliance with Spotify’s API usage policies.

## Future Improvements

- Search suggestions as you type the artist's name.
- Track statistics, including popularity and release date information.
- Multilingual support for artist names and track information.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
