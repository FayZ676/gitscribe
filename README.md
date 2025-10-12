# GitScribe

Transform your git history into shareable content for documentation, marketing, and more.

## Installation

For installation instructions, see the [Releases page](https://github.com/FayZ676/commit2content-releases/releases/latest).

## Development

### Setup

```bash
# Clone the repository
git clone https://github.com/FayZ676/commit2content.git
cd commit2content

# Create and activate virtual environment and install dependencies
make install
```

### Running Locally

```bash
# Run the CLI directly
python cli.py --help
python cli.py content --last 5
```

### Building

```bash
# Build the binary
make build_binary

# Test the binary
./dist/gitscribe content --last 5

# Install locally (optional)
make install_binary
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
   - Create a GitHub Release in the [public releases repo](https://github.com/FayZ676/commit2content-releases)
   - Attach all binaries to the release
