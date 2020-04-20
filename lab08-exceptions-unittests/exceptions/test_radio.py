from radio import Channel, Radio

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 10:14:20 2018

@author: olha
"""

# The FM broadcast band, used for FM broadcast radio by radio stations,
# differs between different parts of the world.
# In Europe, Australia[1] and Africa - from 87.5 to 108 megahertz (MHz)

# A Channel has a frequency (between 87.5 and 108), a name, and a playlist
ch1 = Channel("VGOLOS", 107.2, ["Susy", "Without You", "That's Enough"])
assert(ch1.getFrequency() == 107.2)
assert(str(ch1) == \
"""Channel VGOLOS on 107.2, playlist: ['Susy', 'Without You', "That's Enough"]""")
ch2 = Channel("Oles FM", 91.1, ["911"])
assert(str(ch2) == "Channel Oles FM on 91.1, playlist: ['911']")
assert(ch2.playlist == ['911'])
assert(ch2 == Channel("Oles FM", 91.1, ["911"]))
assert(ch2 != ch1)
assert(ch2 != "Oles FM")
s = set()
assert(ch2 not in s)
s.add(ch2)
assert(Channel("Oles FM", 91.1, ["911"]) in s)
assert(ch1 not in s)
# A Radio (FM Radio) can be tuned to receive channelsself
# based on some different frequencies
channels = { 107.2 : ch1, 91.1 : ch2 }
radio = Radio(channels, 107.25)
assert(radio.getCurrentFrequency() == 107.25)
# A Radio receives a channel if it’s tuned within 0.05 Hz of that channel’s
# frequency. You’re guaranteed that channel frequencies will always be
# at least 0.05 Hz apart.
assert(radio.getCurrentChannel() == ch1)
