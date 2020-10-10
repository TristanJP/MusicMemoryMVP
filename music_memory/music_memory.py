"""
Main
"""

import argparse
import json
import random
import os.path
from pprint import pprint

from selenium import webdriver


PLAYLIST_DIR = "music_memory/resources"

def load_playlist(playlist_name: str) -> dict:
    playlist_path = os.path.join(PLAYLIST_DIR, playlist_name)

    if os.path.isfile(playlist_path):
        with open(playlist_path, 'r') as playlist_file:
            return json.load(playlist_file)
    else:
        print(f"File Not Found: {playlist_path}")
        exit(1)


def play_random_song(playlist: dict):
    rand_song = random.choice(list(playlist.values()))
    pprint(rand_song)


def _parse_args():
    parser = argparse.ArgumentParser(description=('Interact with game'))
    parser.add_argument(
        'PLAYLIST_FILE',
        help='The (JSON) file containing the songs/info for the playlist')
    return parser.parse_args()


def _main():
    args = _parse_args()
    print("Playing")
    playlist = load_playlist(args.PLAYLIST_FILE)
    play_random_song(playlist)
    print("Done")
