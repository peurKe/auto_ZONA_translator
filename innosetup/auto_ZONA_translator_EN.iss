[Setup]
AppName=auto_ZONA_translator
OutputBaseFilename=auto_ZONA_translator_installer_EN
AppVersion=v0.1.5-alpha
DefaultDirName={src}
UsePreviousAppDir=no
DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\auto_ZONA_translator.exe
DisableDirPage=no
SetupIconFile=.\auto_ZONA_translator.ico

[Languages]
Name: "en"; MessagesFile: "compiler:Default.isl"

[Files]
Source: "auto_ZONA_translator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "resources\*"; DestDir: "{app}\"; Flags: ignoreversion recursesubdirs createallsubdirs

[Code]
var
  SRC_Page: TInputOptionWizardPage;
  SRC_LanguageCode: String;
  SRC_LanguageName: String;
  DST_Page: TInputOptionWizardPage;
  DST_LanguageCode: String;
  DST_LanguageMsg: String;
  ResultCode: Integer;

procedure InitializeWizard;
begin
  // Source language (Voices)
  SRC_Page := CreateInputOptionPage(wpWelcome, 'Selecting the game''s VOICES', '', 'Choose your preferred language for the game''s VOICES:', True, False);
  SRC_Page.Add('Ukrainian (Prypiat''s native tongue, maximum immersion!)');
  SRC_Page.Add('Russian');
  SRC_Page.Values[0] := True;

  // Destination language (Texts and Subtitles)
  DST_LanguageCode := 'en'
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Source language (Voices)
    if SRC_Page.Values[0] then
    begin
      SRC_LanguageCode := 'uk';
      SRC_LanguageName := 'UKRAINIAN';
    end
    else
    begin
      SRC_LanguageCode := 'ru';
      SRC_LanguageName := 'RUSSIAN';
    end;
    
    // Destination language (Texts and Subtitles)
    DST_LanguageMsg := 'To enjoy TEXT in FRENCH and voices in ' + SRC_LanguageName + ': Launch your Z.O.N.A game from Steam, then select ''' + SRC_LanguageName + ''' in the game''s language settings. HAVE FUN IN THE ZONE!'
      
    // Execute auto_ZONA_translator.exe with the selected language and capture the return code
    Exec(ExpandConstant('{app}\auto_ZONA_translator.exe'), '-ls ' + SRC_LanguageCode + ' -l ' + DST_LanguageCode + ' --force', '', SW_SHOW, ewWaitUntilTerminated, ResultCode);

    // Check if the return code is -1, initiate uninstallation if -1 or not equal 0
    // if ResultCode = -1 then
    if (ResultCode = -1) or (ResultCode <> 0) then
    begin
      MsgBox('The installer encountered an error. The translations have not been installed correctly. Unistallation in progress.', mbError, MB_OK);
      Exec(ExpandConstant('{uninstallexe}'), '/VERYSILENT', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    end
    else
    begin
      MsgBox(DST_LanguageMsg, mbInformation, MB_OK);
    end;
  end;
end;
