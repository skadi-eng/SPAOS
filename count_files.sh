#!/bin/bash
check_path="/etc"
if [ ! -d "$check_path" ]; then
echo "There are no such directory as $check_path"
exit 1
fi
check_result=$(find "$check_path" -maxdepth 1 -type f 2>/dev/null | wc -l)
echo "The result is $check_result"
