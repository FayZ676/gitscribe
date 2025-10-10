# commit2content

Tool to convert commit messages to easily readable and shareable text content.

## Installation

### Quick Install (macOS/Linux)

```bash
curl -sSL https://raw.githubusercontent.com/FayZ676/commit2content/main/install.sh | bash
```

#### macOS

```bash
# Download
curl -L https://github.com/FayZ676/commit2content/releases/latest/download/commit2content-macos -o commit2content

# Make executable
chmod +x commit2content

# Move to PATH
sudo mv commit2content /usr/local/bin/
```

#### Linux

```bash
# Download
curl -L https://github.com/FayZ676/commit2content/releases/latest/download/commit2content-linux -o commit2content

# Make executable
chmod +x commit2content

# Move to PATH
sudo mv commit2content /usr/local/bin/
```

#### Windows

1. Download `commit2content-windows.exe` from the [Releases page](https://github.com/FayZ676/commit2content/releases)
2. Move to a directory in your PATH (e.g., `C:\Windows\System32` or add a custom directory to PATH)

## Usage

```bash
# Show help
commit2content --help
```

## Creating a Release

To create a new release with automated binary builds:

1. Update version in your code if needed
2. Create and push a version tag:
   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```
3. GitHub Actions will automatically:
   - Build binaries for macOS, Linux, and Windows
   - Create a GitHub Release
   - Attach all binaries to the release

## License

MIT
