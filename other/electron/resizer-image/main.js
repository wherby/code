const path = require('path');
const os = require('os');
const fs = require('fs');
const resizeImg= require('resize-img');
const {app,BrowserWindow,Menu,ipcMain,shell} = require('electron');
const isMac = process.platform === 'darwin';
process.env.NODE_ENV='production';
const isDev = process.env.NODE_ENV !=='production'

let mainWindow;
//create main window
function createMainWindow(){
    mainWindow = new BrowserWindow({
        title: "Image Resizer",
        width: isDev?1000: 500,
        height:600,
        webPreferences:{
            contextIsolation:true,
            nodeIntegration:true,
            preload:path.join(__dirname,'preload.js')
        }
    });

    // open devtool if in dev env
    if(isDev){
        mainWindow.webContents.openDevTools();
    }

    mainWindow.loadFile(path.join(__dirname,'./renderer/index.html'));
}

//create about window
function createAboutWindow(){
    const aboutWindow = new BrowserWindow({
        title: "About Image Resizer",
        width: 300,
        height:300
    });


    aboutWindow.loadFile(path.join(__dirname,'./renderer/about.html'));
}

//app is ready
app.whenReady().then(()=>{
    createMainWindow();

    //Implement menu
    const mainMenu = Menu.buildFromTemplate(menu);
    Menu.setApplicationMenu(mainMenu);

    //remove mainwindow from memory on close
    mainWindow.on('closed',()=>{mainWindow = null})

    app.on('activate', () => {
        if (BrowserWindow.getAllWindows().length === 0) {
            createMainWindow();
        }
      });
});

// const menu = [
//     {
//         label: 'File',
//         submenu:[
//             {
//                 label:'Quit',
//                 click: ()=> app.quit(),
//                 accelerator:'CmdOrCtrl+W'
//             }
//         ]
//     }
// ];
const menu=[
    ...(isMac 
        ? [
            {
        label: app.name,
        submenu:[
            {
            label:'About',
            click:createAboutWindow,
        },
    ]
    }]:[]),
    {
        role:'fileMenu'
    },
    ...(!isMac
        ? [
            {
              label: 'Help',
              submenu: [
                {
                  label: 'About',
                  click:createAboutWindow,
                },
              ],
            },
          ]
        : []),
]
console.log(menu)

//respond to ipcRenderer resize
ipcMain.on('image:resize',(e,options)=>{
    options.dest = path.join(os.homedir(),'imageresizer');
    
    resizeImage(options);
    console.log(options);
})

//resize the image
async function resizeImage({imgPath,height,width,dest}){
    try {
        const newPath = await resizeImg(fs.readFileSync(imgPath),{
            width:+width,
            height:+height
        });
        //create filename
        const fileName = path.basename(imgPath);
        // create dest folder
        if(!fs.existsSync(dest)){
            fs.mkdirSync(dest);
        }
        
        //write file to dest
        fs.writeFileSync(path.join(dest,fileName),newPath);

        //send success to render
        mainWindow.webContents.send('image:done');
        // open dest folder
        shell.openPath(dest);
    } catch (error) {
        console.log(error)
    }
}

app.on('window-all-closed', () => {
    if (!isMac) {
      app.quit();
    }
  });