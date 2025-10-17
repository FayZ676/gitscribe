# GitScribe

You love shipping. You hate writing about it. GitScribe turns your commit history into posts, release notes, and updates—so you can keep building.

📖 **[See USAGE.md for usage details and examples](USAGE.md)**

## Installation

### macOS

```bash
curl -L https://github.com/FayZ676/commit2content/releases/latest/download/gitscribe-macos -o /tmp/gitscribe && chmod +x /tmp/gitscribe && sudo mv /tmp/gitscribe /usr/local/bin/
```

### Linux

```bash
curl -L https://github.com/FayZ676/commit2content/releases/latest/download/gitscribe-linux -o /tmp/gitscribe && chmod +x /tmp/gitscribe && sudo mv /tmp/gitscribe /usr/local/bin/
```

### Windows (PowerShell)

```powershell
Invoke-WebRequest -Uri "https://github.com/FayZ676/commit2content/releases/latest/download/gitscribe-windows.exe" -OutFile "$env:USERPROFILE\gitscribe.exe"
# Then add to PATH or move to a directory in your PATH
```

### Manual Installation

Download the appropriate binary for your platform from the [Releases page](https://github.com/FayZ676/commit2content/releases/latest), make it executable, and move it to a directory in your PATH.

## Usage

GitScribe provides two main commands:

- `gitscribe configure` - Set up your OpenAI API key
- `gitscribe post` - Generate shareable content from git commits
- `gitscribe commit` - Generate commit messages from git diff

📖 **[See USAGE.md for usage details and examples](USAGE.md)**

### Quick Start

```bash
# Configure your API key (first time only)
gitscribe configure

# Generate content from your last 5 commits
gitscribe post --last 5
```

## Uninstall

### Binary Installation

If you installed using the binary installation method:

**macOS/Linux:**

```bash
sudo rm /usr/local/bin/gitscribe
```

**Windows:**

```powershell
Remove-Item "$env:USERPROFILE\gitscribe.exe"
# Or remove from wherever you placed it in your PATH
```

### Development Installation

If you installed locally during development:

```bash
make uninstall_binary
```

## Issues and Bug Reports

If you encounter any issues, bugs, or have feature requests, please report them on our [GitHub Issues page](https://github.com/FayZ676/gitscribe/issues).

When submitting an issue, please include:

- A clear description of the problem or feature request
- Steps to reproduce (for bugs)
- Your operating system and GitScribe version
- Any relevant error messages or logs

## Development

For detailed development commands, see the `Makefile` in the project root. Key commands include:

- `make install` - Set up development environment
- `make test_all` - Run all tests
- `make build_binary` - Build the executable
- `make install_binary` - Install binary locally
- `make uninstall_binary` - Remove installed binary

Run `make` without arguments to see all available targets.
