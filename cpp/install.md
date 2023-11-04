# windows
https://winlibs.com/

install gcc and wingw in
and set path:
C:\mingw64\bin
## linux
sudo apt-get install build-essential

sudo apt-get install gcc-10
sudo apt-get install g++-10
sudo apt-get install gdb

## Mac
https://blog.csdn.net/StoryZX/article/details/123242064?spm=1001.2101.3001.6661.1&utm_medium=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-123242064-blog-119876434.pc_relevant_recovery_v2&depth_1-utm_source=distribute.pc_relevant_t0.none-task-blog-2%7Edefault%7ECTRLIST%7ERate-1-123242064-blog-119876434.pc_relevant_recovery_v2&utm_relevant_index=1
``` error
> Executing task: C/C++: clang build active file <

Starting build...
/usr/bin/clang -g -std=c++20 "/Users/steventzhou/software/code/cpp/tmp/main copy.cpp" -o "/Users/steventzhou/software/code/cpp/tmp/main copy"
Undefined symbols for architecture x86_64:
  "std::__1::locale::use_facet(std::__1::locale::id&) const", referenced from:
      std::__1::ctype<char> const& std::__1::use_facet<std::__1::ctype<char> >(std::__1::locale const&) in main copy-f781b7.o
  "std::__1::ios_base::getloc() const", referenced from:
      std::__1::basic_ios<char, std::__1::char_traits<char> >::widen(char) const in main copy-f781b7.o
  "std::__1::basic_ostream<char, std::__1::char_traits<char> >::put(char)", referenced from:
      std::__1::basic_ostream<char, std::__1::char_traits<char> >& std::__1::endl<char, std::__1::char_traits<char> >(std::__1::basic_ostream<char, std::__1::char_traits<char> >&) in main copy-f781b7.o
  "std::__1::basic_ostream<char, std::__1::char_traits<char> >::flush()", referenced from:
      std::__1::basic_ostream<char, std::__1::char_traits<char> >& std::__1::endl<char, std::__1::char_traits<char> >(std::__1::basic_ostream<char, std::__1::char_traits<char> >&) in main copy-f781b7.o
  "std::__1::basic_ostream<char, std::__1::char_traits<char> >::operator<<(bool)", referenced from:
      _main in main copy-f781b7.o
  "std::__1::cout", referenced from:
      _main in main copy-f781b7.o
  "std::__1::ctype<char>::id", referenced from:
      std::__1::ctype<char> const& std::__1::use_facet<std::__1::ctype<char> >(std::__1::locale const&) in main copy-f781b7.o
  "std::__1::locale::~locale()", referenced from:
      std::__1::basic_ios<char, std::__1::char_traits<char> >::widen(char) const in main copy-f781b7.o
  "___gxx_personality_v0", referenced from:
      std::__1::basic_ios<char, std::__1::char_traits<char> >::widen(char) const in main copy-f781b7.o
      Dwarf Exception Unwind Info (__eh_frame) in main copy-f781b7.o
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
```

2.解决办法
  之前在编译 C++ 程序的时候，也遇到过这种情况，但是没有找到解决方案。程序没有语法错误，但是编译会报错。
  上述情形，在使用的程序是 C++ 而不是 C 这一背景下，通常可以使用以下方式解决：

(1) 在编译命令中添加 -lstdc++ 参数，引入 C++ 的标准库。
————————————————
版权声明：本文为CSDN博主「Liu-Feng」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/StoryZX/article/details/123242064


{
	"version": "2.0.0",
	"tasks": [
		{
			"type": "cppbuild",
			"label": "C/C++: clang build active file",
			"command": "/usr/bin/clang",
			"args": [
				"-g",
				"-std=c++20",  
				"-lstdc++",
				"${file}",
				"-o",
				"${fileDirname}/${fileBasenameNoExtension}"
			],
			"options": {
				"cwd": "${workspaceFolder}"
			},
			"problemMatcher": [
				"$gcc"
			],
			"group": "build",
			"detail": "compiler: /usr/bin/clang"
		}
	]
}


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

💻 Source code: https://github.com/rutura/The-C-20-Masterclass-Source-Code

✏️ Course developed by Daniel Gakwaya. Check out his YouTube channel: https://www.youtube.com/channel/UCUYU...
🐦 Twitter: https://twitter.com/learnqtguide
🔗 Want more from Daniel? https://www.learnqt.guide/udemy-disco...
🔗 Join Daniel's discord server for support: https://discord.com/invite/PcATcraESW


## links

https://cppinsights.io/


#
https://www.youtube.com/watch?v=9pjBseGfEPU&ab_channel=CodeVault
ctrl+shift+B : Build

https://stackoverflow.com/questions/56344186/unable-to-start-debugging-the-value-of-midebuggerpath-is-invalid
sudo apt-get install gdb


## code runner settigs

https://stackoverflow.com/questions/51046803/visual-studio-code-c11-extension-warning