#!/usr/bin/env bash

function spotify {
    osascript -e "tell application \"Spotify\" to $*"
}

function play_all_the_songs {
    for i in {1..100}
    do
        spotify next track
        ARTIST=`spotify artist of current track`
        TRACK=`spotify name of current track`
        printf "%s - %s\n" "$ARTIST" "$TRACK" 
    done
}

function create_lock_or_wait () {
    path="$1"
    wait_time="${2:-10}"
    while true; do
        if mkdir "${path}.lock.d"; then
           break;
        fi
        sleep $wait_time
    done
}

function remove_lock () {
    path="$1"
    rmdir "${path}.lock.d"
}

create_lock_or_wait playlist

if [[ $1 = "orderly" ]]; then
    spotify set shuffling to false
elif [[ $1 = "randomly" ]]; then
    spotify set shuffling to true
fi

play_all_the_songs

remove_lock playlist
