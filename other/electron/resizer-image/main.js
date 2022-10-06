const path = require('path');
const {app,BrowserWindow} = require('electron');
const isMac = process.platform === 'darwin';

const isDev = process.env.NODE_ENV !=='production'
function createMainWindow(){
    const mainWindow = new BrowserWindow({
        title: "Image Resizer",
        width: isDev?1000: 500,
        height:600
    });

    // open devtool if in dev env
    if(isDev){
        mainWindow.webContents.openDevTools();
    }

    mainWindow.loadFile(path.join(__dirname,'./rander/index.html'));
}

app.whenReady().then(()=>{
    createMainWindow();
    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createMainWindow();
        }
      });
});

app.on('window-all-closed', () => {
    if (!isMac) {
      app.quit();
    }
  });