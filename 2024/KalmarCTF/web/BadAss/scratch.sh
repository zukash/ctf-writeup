#!/bin/bash

# protocol=$(echo -n "${request_line[2]}" | sed 's/^\s*//g' | sed 's/\s*$//g')
protocol='[^h]??'
# protocol='HTTP'
echo $protocol

if [ $protocol != 'HTTP/1.0' ] && [ $protocol != 'HTTP/1.1' ]; then
    echo "xxxxx"
fi