#!/bin/bash

# Default max for live device path on mac
root=~/"Music/Ableton/User Library/Presets/MIDI Effects/Max MIDI Effect/"

# Copy zoa and js
# TODO embed js in patch
cp ./Zoa.amxd "$root"
cp ./stringFormat.js "$root"
cp ./MockZoaHardware.amxd "$root"