[Setup]
AppName=auto_ZONA_translator
OutputBaseFilename=auto_ZONA_translator_installer_CS
AppVersion=v0.3.0-alpha
DefaultDirName={src}
UsePreviousAppDir=no
DisableProgramGroupPage=yes
UninstallDisplayIcon={app}\auto_ZONA_translator.exe
DisableDirPage=no
SetupIconFile=.\auto_ZONA_translator.ico

[Languages]
Name: "cs"; MessagesFile: "compiler:Languages\Czech.isl"

[Files]
Source: "auto_ZONA_translator.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "resources\*"; DestDir: "{app}\"; Flags: ignoreversion recursesubdirs createallsubdirs

[Code]
var
  // BEGIN CONVRGENCE + Paradox of Hope are only Russian Voices / Z.O.N.A project X is only Ukrainian Voices
  SourceDir: String;
  Only_OneLang: Boolean;
  Only_OneLang_1: String;
  Only_OneLang_2: String;
  Only_OneLang_3: String;
  // END CONVRGENCE + Paradox of Hope are only Russian Voices / Z.O.N.A project X is only Ukrainian Voices
  SRC_Page: TInputOptionWizardPage;
  SRC_LanguageCode: String;
  SRC_LanguageName: String;
  DST_Page: TInputOptionWizardPage;
  DST_LanguageCode: String;
  DST_LanguageMsg: String;
  ResultCode: Integer;

procedure InitializeWizard;
begin
  // BEGIN CONVRGENCE + Paradox of Hope are only Russian Voices / Z.O.N.A project X is only Ukrainian Voices
  SourceDir := ExpandConstant('{src}');
  Only_OneLang_1 := 'CONVRGENCE';
  Only_OneLang_2 := 'Paradox of Hope';
  Only_OneLang_3 := 'ZONA';

  Only_OneLang := False;
  if (Pos(Only_OneLang_1, SourceDir) > 0) or (Pos(Only_OneLang_2, SourceDir) > 0) then
  begin
    Only_OneLang := True;
    SRC_LanguageCode := 'ru';
    SRC_LanguageName := 'RUŠTINA'
  end;
  if (Pos(Only_OneLang_3, SourceDir) > 0) then
  begin
    Only_OneLang := True;
    SRC_LanguageCode := 'uk';
    SRC_LanguageName := 'UKRÁNSKÝ';
  end;

  if not Only_OneLang then
  begin
    // Source language (Voices)
    SRC_Page := CreateInputOptionPage(wpWelcome, 'Výběr HLASY ve hře', '', 'Zvolte si preferovaný jazyk pro HLASY ve hře:', True, False);
    SRC_Page.Add('Ukrajinština (Prypiatův rodný jazyk, maximální ponoření!)');
    SRC_Page.Add('Ruský');
    SRC_Page.Values[0] := True;
  end;
  // END CONVRGENCE + Paradox of Hope are only Russian Voices / Z.O.N.A project X is only Ukrainian Voices

  // Destination language (Texts and Subtitles)
  DST_LanguageCode := 'cs'
end;

procedure CurStepChanged(CurStep: TSetupStep);
begin
  if CurStep = ssPostInstall then
  begin
    // BEGIN CONVRGENCE + Paradox of Hope are only Russian Voices / Z.O.N.A project X is only Ukrainian Voices
    if not Only_OneLang then
    begin
      // Source language (Voices)
      if SRC_Page.Values[0] then
      begin
        SRC_LanguageCode := 'uk';
        SRC_LanguageName := 'UKRÁNSKÝ';
      end
      else
      begin
        SRC_LanguageCode := 'ru';
        SRC_LanguageName := 'RUŠTINA';
      end;
    end;
    // END CONVRGENCE + Paradox of Hope are only Russian Voices / Z.O.N.A project X is only Ukrainian Voices
    
    // Destination language (Texts and Subtitles)
    DST_LanguageMsg := 'Chcete-li si vychutnat TEXT ve ČEŠTINĚ a hlasy v ' + SRC_LanguageName + ': Spusťte hru ze služby Steam a v nastavení jazyka hry vyberte ''' + SRC_LanguageName + '''. BAVTE SE V ZÓNĚ!'
      
    // Execute auto_ZONA_translator.exe with the selected language and capture the return code
    Exec(ExpandConstant('{app}\auto_ZONA_translator.exe'), '-ls ' + SRC_LanguageCode + ' -l ' + DST_LanguageCode + ' --force', '', SW_SHOW, ewWaitUntilTerminated, ResultCode);

    // Check if the return code is -1, initiate uninstallation if -1 or not equal 0
    // if ResultCode = -1 then
    if (ResultCode = -1) or (ResultCode <> 0) then
    begin
      MsgBox('Instalační program narazil na chybu. Překlady nebyly správně nainstalovány. Probíhá odinstalace.', mbError, MB_OK);
      Exec(ExpandConstant('{uninstallexe}'), '/VERYSILENT', '', SW_HIDE, ewWaitUntilTerminated, ResultCode);
    end
    else
    begin
      MsgBox(DST_LanguageMsg, mbInformation, MB_OK);
    end;
  end;
end;
