# Installation

This guide covers installing GitScribe on macOS, Linux, and Windows, plus manual installation.

## macOS

```bash
curl -L https://github.com/FayZ676/commit2content/releases/latest/download/gitscribe-macos -o /tmp/gitscribe && chmod +x /tmp/gitscribe && sudo mv /tmp/gitscribe /usr/local/bin/
```

## Linux

```bash
curl -L https://github.com/FayZ676/commit2content/releases/latest/download/gitscribe-linux -o /tmp/gitscribe && chmod +x /tmp/gitscribe && sudo mv /tmp/gitscribe /usr/local/bin/
```

## Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri "https://github.com/FayZ676/commit2content/releases/latest/download/gitscribe-windows.exe" -OutFile "$env:USERPROFILE\gitscribe.exe"
# Then add to PATH or move to a directory in your PATH
```

## Manual Installation

Download the appropriate binary for your platform from the [Releases page](https://github.com/FayZ676/commit2content/releases/latest), make it executable, and move it to a directory in your PATH.

## Verify Installation

```bash
gitscribe --help
```

If the command prints the help text, you’re good to go.


## Next Steps

After installation, run the configuration command to set up your OpenAI API key and default style files:

```bash
gitscribe configure
```

See [USAGE.md](USAGE.md) for detailed configuration instructions and usage examples.
## Uninstall

### Binary Installation

If you installed using the binary installation method:

**macOS/Linux:**

```bash
sudo rm /usr/local/bin/gitscribe
rm -rf ~/.gitscribe
```

**Windows:**

```powershell
Remove-Item "$env:USERPROFILE\gitscribe.exe"
Remove-Item -Recurse -Force "$env:USERPROFILE\.gitscribe"
# Or remove from wherever you placed it in your PATH
```

### Development Installation

If you installed locally during development:

```bash
make uninstall
```

**Note:** These commands will permanently delete your stored OpenAI API key, default style file configuration, and any other GitScribe settings. You'll need to reconfigure if you reinstall GitScribe later.
