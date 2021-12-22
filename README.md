## Diff Reset Plugin [![codebeat badge](https://codebeat.co/badges/3d31b52f-b534-4543-87db-f3e36392dd97)](https://codebeat.co/projects/github-com-essentialkaos-sublime-plugin-diff-reset-master) [![License](https://gh.kaos.st/apache2.svg)](https://www.apache.org/licenses/LICENSE-2.0)

Simple plugin for Sublime Text 3.2+ for resetting diff after saving file.

### Installation

#### macOS

Open `Terminal.app` and do:

```bash
curl -OL# https://kaos.sh/sublime-plugin-diff-reset/diff_reset_on_save.py
mv diff_reset_on_save.py "$HOME/Library/Application Support/Sublime Text/Packages/User/"
```

#### Windows

Press <kbd>Win+R</kbd>, type `powershell` and press Enter. Then do:

```powershell
Invoke-WebRequest -Uri "https://kaos.sh/sublime-plugin-diff-reset/diff_reset_on_save.py" -OutFile diff_reset_on_save.py
Move-Item -Force -Path diff_reset_on_save.py -Destination "$HOME\AppData\Roaming\Sublime Text 4\Packages\User\"
```

### License

[Apache License, Version 2.0](https://www.apache.org/licenses/LICENSE-2.0)

<p align="center"><a href="https://essentialkaos.com"><img src="https://gh.kaos.st/ekgh.svg"/></a></p>
