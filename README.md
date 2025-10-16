# GitScribe

Transform your git history into shareable content for documentation, marketing, and more.

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

```bash
# Get help
gitscribe post --help

# Generate content from last 5 commits
gitscribe post --last 5

# Generate content from specific commit range
gitscribe post --from <commit-hash> --to <commit-hash>
```

## Uninstall

### macOS/Linux

```bash
sudo rm /usr/local/bin/gitscribe
```

### Windows

```powershell
Remove-Item "$env:USERPROFILE\gitscribe.exe"
# Or remove from wherever you placed it in your PATH
```

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/FayZ676/gitscribe.git
cd gitscribe

# Create and activate virtual environment and install dependencies
make install
```

### Running Locally

```bash
# Run the CLI directly
python cli.py --help
python cli.py post --last 5
```

### Building

```bash
# Build the binary
make build_binary

# Test the binary
./dist/gitscribe post --last 5

# Install locally (optional)
make install_binary
```
