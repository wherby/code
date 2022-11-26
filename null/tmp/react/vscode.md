

# using npm in wsl 

export PATH=$(echo "$PATH" | sed -e 's/:\/mnt[^:]*//g') # strip out problematicWindows %PATH%

https://stackoverflow.com/questions/39311147/cannot-run-npm-commands

## upgrade nodejs

https://askubuntu.com/questions/426750/how-can-i-update-my-nodejs-to-the-latest-version
Use n module from npm in order to upgrade node
```
sudo npm cache clean -f
sudo npm install -g n
sudo n stable
```

npm i libnpx