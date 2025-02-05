[Setup]
AppName=Modustry
AppVersion=0.1.0
DefaultDirName={localappdata}\Programs\Modustry
DefaultGroupName=modustry
UninstallDisplayIcon={app}\icon.ico
OutputDir=userdocs:Inno Setup Examples Output
OutputBaseFilename=Modusry Installer
Compression=lzma
SolidCompression=yes
PrivilegesRequired=lowest

[Files]
Source: "D:\programmation\Github\Modustry\dist\Modustry.exe"; DestDir: "{localappdata}\Programs\Modustry"; Flags: ignoreversion
Source: "D:\programmation\Github\Modustry\source\icons\main_ico.ico"; DestDir: "{localappdata}\Programs\Modustry"; Flags: ignoreversion

[Icons]
Name: "{group}\Modustry"; Filename: "{app}\Modustry.exe"
Name: "{group}\Uninstall Modustry"; Filename: "{uninstallexe}"

[Tasks]
Name: "desktopicon"; Description: "Create a shortcut"; GroupDescription: "Additionnal icons :"; Flags: unchecked

[Run]
Filename: "{app}\Modustry.exe"; Description: "{cm:LaunchProgram,Modustry}"; Flags: nowait postinstall skipifsilent