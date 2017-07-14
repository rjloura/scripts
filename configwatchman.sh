#!/bin/bash

echo 99999 | sudo tee /proc/sys/fs/inotify/max_user_instances
echo 99999 | sudo tee /proc/sys/fs/inotify/max_user_watches 
echo 99999 | sudo tee /proc/sys/fs/inotify/max_queued_events

watchman watch-del-all
watchman shutdown-server

