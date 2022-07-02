# windows
https://winlibs.com/

install gcc and wingw in
and set path:
C:\mingw64\bin
## linux
sudo apt-get install gcc-10
sudo apt-get install g++-10
sudo apt-get install gdb

##  
install C++ VS module

## configure vs code

vscode=>teminal => configure task

```
{
	"version": "2.0.0",
	"tasks": [
		{
			"type": "cppbuild",
			"label": "C/C++: g++.exe build active file build with gcc 11.2",
			"command": "C:\\mingw64\\bin\\g++.exe",
			"args": [
				"-fdiagnostics-color=always",
				"-g",
				"-std=c++20",                                                     <== enable c++20
				"${file}",
				"-o",
				"${fileDirname}\\${fileBasenameNoExtension}.exe"
			],
			"options": {
				"cwd": "${fileDirname}"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": "build",
			"detail": "compiler: C:\\mingw64\\bin\\g++.exe"
		}
	]
}
```
## reference

Learn modern C++ 20 programming in this comprehensive course.

💻 Source code: https://github.com/rutura/The-C-20-Ma...

✏️ Course developed by Daniel Gakwaya. Check out his YouTube channel: https://www.youtube.com/channel/UCUYU...
🐦 Twitter: https://twitter.com/learnqtguide
🔗 Want more from Daniel? https://www.learnqt.guide/udemy-disco...
🔗 Join Daniel's discord server for support: https://discord.com/invite/PcATcraESW


## links

https://cppinsights.io/
