[Setup]
AppName=auto_ZONA_translator
OutputBaseFilename=auto_ZONA_translator_installer_DE
AppVersion=v0.1.5-alpha
DefaultDirName={src}
UsePreviousAppDir=no
DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\auto_ZONA_translator.exe
DisableDirPage=no
SetupIconFile=.\auto_ZONA_translator.ico

[Languages]
Name: "de"; MessagesFile: "compiler:Languages\German.isl"

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
  SRC_Page := CreateInputOptionPage(wpWelcome, 'Auswahl der VOICEs im Spiel', '', 'Wählen Sie Ihre bevorzugte Sprache für die VOICEs im Spiel:', True, False);
  SRC_Page.Add('Ukrainisch (Prypjats Heimatsprache, maximale Immersion!)');
  SRC_Page.Add('Russisch');
  SRC_Page.Values[0] := True;

  // Destination language (Texts and Subtitles)
  DST_LanguageCode := 'fr'
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // Source language (Voices)
    if SRC_Page.Values[0] then
    begin
      SRC_LanguageCode := 'uk';
      SRC_LanguageName := 'UKRAINISCH';
    end
    else
    begin
      SRC_LanguageCode := 'ru';
      SRC_LanguageName := 'RUSSISCH';
    end;
    
    // Destination language (Texts and Subtitles)
    DST_LanguageMsg := 'Um die Texte auf DEUTSCH und die Stimmen in ' + SRC_LanguageName + ' zu genießen: Starten Sie Ihr Spiel Z.O.N.A von Steam aus und wählen Sie ''' + SRC_LanguageName + ''' in den Spracheinstellungen des Spiels. VIEL SPASS IN DER ZONE!'
      
    // Execute auto_ZONA_translator.exe with the selected language and capture the return code
    Exec(ExpandConstant('{app}\auto_ZONA_translator.exe'), '-ls ' + SRC_LanguageCode + ' -l ' + DST_LanguageCode + ' --force', '', SW_SHOW, ewWaitUntilTerminated, ResultCode);

    // Check if the return code is -1, initiate uninstallation if -1 or not equal 0
    // if ResultCode = -1 then
    if (ResultCode = -1) or (ResultCode <> 0) then
    begin
      MsgBox('Der Installer ist auf einen Fehler gestoßen. Die Übersetzungen wurden nicht richtig installiert. Deinstallationsvorgang läuft.', mbError, MB_OK);
      Exec(ExpandConstant('{uninstallexe}'), '/VERYSILENT', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    end
    else
    begin
      MsgBox(DST_LanguageMsg, mbInformation, MB_OK);
    end;
  end;
end;
