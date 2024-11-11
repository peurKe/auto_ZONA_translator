[Setup]
AppName=auto_ZONA_translator
OutputBaseFilename=auto_ZONA_translator_installer
AppVersion=v0.1.1-alpha
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
  Instructions_msg: String;
  ResultCode: Integer;

procedure InitializeWizard;
begin
  // Source language (Voices)
  SRC_Page := CreateInputOptionPage(wpWelcome, 'VOICES selection', '', 'Choose your preferred language for VOICES:', True, False);
  SRC_Page.Add('Ukrainian');
  SRC_Page.Add('Russian');
  SRC_Page.Values[0] := True;

  // Destination language (Texts and Subtitles)
  DST_Page := CreateInputOptionPage(wpWelcome, 'TEXTS and SUBTITLES selection', '', 'Choose your preferred language for TEXTS and SUBTITLES:', True, True);
  DST_Page.Add('English');
  DST_Page.Add('Čeština');
  DST_Page.Add('Dansk');
  DST_Page.Add('German');
  DST_Page.Add('Español');
  DST_Page.Add('Suomi');
  DST_Page.Add('Français');
  DST_Page.Add('Magyar');
  DST_Page.Add('Italiano');
  DST_Page.Add('Nederlands');
  DST_Page.Add('Polski');
  DST_Page.Add('Português');
  DST_Page.Add('Română');
  DST_Page.Add('Svenska');
  DST_Page.Values[0] := True;
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
    DST_LanguageMsg := 'Launch your Z.O.N.A game and select ''' + SRC_LanguageName + ''' language in game settings.'

    if DST_Page.Values[0] then
      DST_LanguageCode := 'en'
    else if DST_Page.Values[1] then
      DST_LanguageCode := 'cs'
    else if DST_Page.Values[2] then
      DST_LanguageCode := 'da'
    else if DST_Page.Values[3] then
      DST_LanguageCode := 'de'
    else if DST_Page.Values[4] then
      DST_LanguageCode := 'es'
    else if DST_Page.Values[5] then
      DST_LanguageCode := 'fi'
    else if DST_Page.Values[6] then
    begin
      DST_LanguageCode := 'fr'
      DST_LanguageMsg := 'Lancez votre jeu Z.O.N.A et sélectionnez la langue ''' + SRC_LanguageName + ''' dans les paramètres du jeu.'
    end
    else if DST_Page.Values[7] then
      DST_LanguageCode := 'hu'
    else if DST_Page.Values[8] then
      DST_LanguageCode := 'it'
    else if DST_Page.Values[9] then
      DST_LanguageCode := 'nl'
    else if DST_Page.Values[10] then
      DST_LanguageCode := 'pl'
    else if DST_Page.Values[11] then
      DST_LanguageCode := 'pt'
    else if DST_Page.Values[12] then
      DST_LanguageCode := 'ro'
    else
      DST_LanguageCode := 'sv';
      
    // Execute auto_ZONA_translator.exe with the selected language and capture the return code
    Exec(ExpandConstant('{app}\auto_ZONA_translator.exe'), '-ls ' + SRC_LanguageCode + ' -l ' + DST_LanguageCode + ' --force', '', SW_SHOW, ewWaitUntilTerminated, ResultCode);

    // Check if the return code is -1, initiate uninstallation if it is
    // if ResultCode = -1 then
    if (ResultCode = -1) or (ResultCode <> 0) then
    begin
      MsgBox('The application encountered an error and will now uninstall.', mbError, MB_OK);
      Exec(ExpandConstant('{uninstallexe}'), '/VERYSILENT', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    end
    else
    begin
      MsgBox(DST_LanguageMsg, mbInformation, MB_OK);
    end;
  end;
end;