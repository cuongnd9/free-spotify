#!/bin/bash

echo '###---------- free-spotify ----------###' >> /etc/hosts
curl https://raw.githubusercontent.com/x0uid/SpotifyAdBlock/master/SpotifyBlocklist.txt >> /etc/hosts
echo '###---------- made by @103cuong ----------###' >> /etc/hosts
