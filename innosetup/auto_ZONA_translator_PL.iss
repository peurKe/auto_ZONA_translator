[Setup]
AppName=auto_ZONA_translator
OutputBaseFilename=auto_ZONA_translator_installer_PL
AppVersion=v0.1.5-alpha
DefaultDirName={src}
UsePreviousAppDir=no
DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\auto_ZONA_translator.exe
DisableDirPage=no
SetupIconFile=.\auto_ZONA_translator.ico

[Languages]
Name: "pl"; MessagesFile: "compiler:Languages\Polish.isl"

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
  SRC_Page := CreateInputOptionPage(wpWelcome, 'Wybieranie GŁOSÓW w grze', '', 'Wybierz preferowany język GŁOSÓW w grze:', True, False);
  SRC_Page.Add('Ukraiński (język ojczysty Prypeci, maksymalne zanurzenie!)');
  SRC_Page.Add('Rosyjski');
  SRC_Page.Values[0] := True;

  // Destination language (Texts and Subtitles)
  DST_LanguageCode := 'pl'
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Source language (Voices)
    if SRC_Page.Values[0] then
    begin
      SRC_LanguageCode := 'uk';
      SRC_LanguageName := 'UKRAIŃSKI';
    end
    else
    begin
      SRC_LanguageCode := 'ru';
      SRC_LanguageName := 'ROSYJSKI';
    end;
    
    // Destination language (Texts and Subtitles)
    DST_LanguageMsg := 'Aby cieszyć się TEKSTEM we FRANCUSKIM i głosami w ' + SRC_LanguageName + ' : Uruchom grę Z.O.N.A ze Steam, a następnie wybierz ''' + SRC_LanguageName + ''' w ustawieniach językowych gry. MIŁEJ ZABAWY W STREFIE!'
      
    // Execute auto_ZONA_translator.exe with the selected language and capture the return code
    Exec(ExpandConstant('{app}\auto_ZONA_translator.exe'), '-ls ' + SRC_LanguageCode + ' -l ' + DST_LanguageCode + ' --force', '', SW_SHOW, ewWaitUntilTerminated, ResultCode);

    // Check if the return code is -1, initiate uninstallation if -1 or not equal 0
    // if ResultCode = -1 then
    if (ResultCode = -1) or (ResultCode <> 0) then
    begin
      MsgBox('Instalator napotkał błąd. Tłumaczenia nie zostały poprawnie zainstalowane. Trwa deinstalacja.', mbError, MB_OK);
      Exec(ExpandConstant('{uninstallexe}'), '/VERYSILENT', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    end
    else
    begin
      MsgBox(DST_LanguageMsg, mbInformation, MB_OK);
    end;
  end;
end;
