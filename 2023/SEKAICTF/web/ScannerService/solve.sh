nmap -p 80 https://raw.githubusercontent.com --script http-fetch --script-args http-fetch.destination=/tmp/hoge,http-fetch.url=/PentestBox/nmap/master/scripts/http-ls.nse

nmap -p 1337 --script http-fetch --script-args http-fetch.destination=/tmp/,http-fetch.url=/
