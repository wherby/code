# link
https://learn.deeplearning.ai/courses/gemini-cli-code-and-create-with-an-open-source-agent/lesson/eg40apsy/workflows-with-model-context-protocol-(mcp)
# install cmd 
node -v 
## update node
nvm install --lts


npm install -g @google/gemini-cli

gemini

## create project which may be not needed
https://console.cloud.google.com/

## add memory to gemini.md 
/memory add xxxx 
/meery show 

## create project based gemini.md,   -- project context
/init
will load gemini.md to memory


## shell mode - run command in gemini cli 
!npm install

## add mcp server
gemini mcp add -t http canva https://mcp.canva.com/mcp
/mcp auth <= add auth 

/mcp <=list mcp service

## google extention
geminicli.com/extensions/

## list extensions
/extensions list


Course Materials & Gemini CLI Installation Guide
Course Materials
Great work completing this course!

You can access a repo with all course materials here. Feel free to reuse any prompts and remix and code used in this course!

Repo Structure
starter_files/ - Initial starter files as they would exist at the start of the course, before any changes have been made.
final_files/ - Completed final files as they would exist at the end of the course, after all changes have been made.
prompts/ - Prompt templates and files from each lesson, plus bonus tips and commands.
Installation Guide
This guide explains how to install and configure the official Google Gemini CLI (@google/gemini-cli).

Prerequisites
Before installing, ensure your system meets the following requirements:

Node.js: Version 20.0.0 or higher is recommended (Minimum v18).
Check version: node -v
Download: nodejs.org
Google Account: Required for authentication (Free tier available).
Installation Methods
Option 1: NPM (Recommended)
This is the standard method for most users (Windows, macOS, Linux). It installs the CLI globally on your system.

Open your terminal or command prompt.
Run the install command:
npm install -g @google/gemini-cli
(Note: On Linux or macOS, you might need to use sudo if you encounter permission errors: sudo npm install -g @google/gemini-cli)
Option 2: Homebrew (macOS)
If you use Homebrew on macOS, you can install it directly.

Run the brew install command:
brew install gemini-cli
Option 3: NPX (No Install / One-time Use)
If you want to run the CLI without permanently installing it, use npx. This always fetches the latest version.

Run the command:
npx @google/gemini-cli
Authentication
Once installed, you need to authenticate. The CLI supports a browser-based login flow which is the easiest to set up.

Run the CLI for the first time:
gemini
The CLI will prompt you to select an authentication method.
Select "Login with Google" (using arrow keys and Enter).
A browser window will open. Sign in with your Google Account.
Once authorized, close the browser window. The terminal will confirm you are logged in.
Alternative: API Key
If you prefer using an API key (e.g., for automated scripts or enterprise environments), you can set it as an environment variable.

Get a key from Google AI Studio.
Set the variable in your terminal:
Mac/Linux: export GEMINI_API_KEY="YOUR_KEY_HERE"
Windows (PowerShell): $env:GEMINI_API_KEY="YOUR_KEY_HERE"
Verification
To verify the installation was successful, check the version or run a simple prompt.

gemini --version
