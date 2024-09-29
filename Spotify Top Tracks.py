import tkinter as tk
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from PIL import Image, ImageTk
import urllib.request
import os  # Import to use environment variables

# Function to search for an artist and display their top tracks and album art
def search_artist():
    artist_name = entry.get()  # Get the artist's name from the entry box
    if not artist_name:  # If no artist name is entered, exit the function
        return

    # Search for the artist using Spotify's search API
    results = sp.search(q="artist:" + artist_name, type="artist")
    artist_uri = results["artists"]["items"][0]["uri"]  # Get the unique URI of the artist

    # Get the top tracks of the artist using their URI
    results = sp.artist_top_tracks(artist_uri)

    # Clear any previous text in the text widget
    text.delete("1.0", tk.END)

    # Remove any existing album artwork labels from the window
    for label in album_art_labels:
        label.destroy()  # Destroy each existing label
    album_art_labels.clear()  # Clear the list of labels to prepare for new ones

    # Initialize row and column positions for album art display
    row = 0
    column = 0

    # Loop through the top 10 tracks of the artist
    for track in results['tracks'][:10]:
        # Insert the track name and audio preview link into the text widget
        text.insert(tk.END, 'Track: ' + track['name'] + '\n')
        text.insert(tk.END, 'Audio: ' + (track['preview_url'] or 'No preview available') + '\n\n')

        # Load and display the album artwork
        url = track['album']['images'][0]['url']  # Get the album artwork URL
        image_data = urllib.request.urlopen(url).read()  # Download the image data
        image = Image.open(io.BytesIO(image_data))  # Open the image from the downloaded data
        photo = ImageTk.PhotoImage(image)  # Convert the image to a format usable by Tkinter

        # Create and place a label with the album art on the grid
        label = tk.Label(root, image=photo)
        label.image = photo  # Keep a reference to the image to prevent garbage collection
        label.grid(row=row, column=column)

        album_art_labels.append(label)  # Add label to the list of album art labels

        # Update grid position for the next album artwork
        column += 1
        if column > 2:  # Move to the next row after 3 images in a row
            column = 0
            row += 1

# Prompt the user for their own client credentials
client_id = os.getenv("SPOTIPY_CLIENT_ID") or input("Enter your Spotify Client ID: ")
client_secret = os.getenv("SPOTIPY_CLIENT_SECRET") or input("Enter your Spotify Client Secret: ")
redirect_uri = os.getenv("SPOTIPY_REDIRECT_URI") or "http://localhost:8080"

# OAuth authentication for Spotify API using user-provided client credentials
SpotifyOAuthObj = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri=redirect_uri)
sp = spotipy.Spotify(auth_manager=SpotifyOAuthObj)  # Initialize Spotify client with OAuth

# Set up the main Tkinter application window
root = tk.Tk()
root.title("Spotify Artist Search")  # Set the window title

# Create and pack the label and entry widgets for artist search input
entry_label = tk.Label(root, text="Enter an artist name:")
entry_label.pack()

entry = tk.Entry(root)  # Text entry field for the artist name
entry.pack()

# Create and pack the search button, which calls the search_artist function
search_button = tk.Button(root, text="Search", command=search_artist)
search_button.pack()

# Create and pack the text widget to display track info
text = tk.Text(root)
text.pack()

# List to keep track of album art labels, so they can be removed later
album_art_labels = []

# Start the Tkinter event loop (this keeps the window open)
root.mainloop()
