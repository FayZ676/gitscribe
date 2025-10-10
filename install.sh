#!/bin/bash
set -e

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Configuration
REPO="FayZ676/commit2content"
BINARY_NAME="commit2content"
INSTALL_DIR="/usr/local/bin"

echo "Installing commit2content..."

# Detect OS and architecture
OS="$(uname -s)"
case "${OS}" in
    Linux*)     PLATFORM=linux;;
    Darwin*)    PLATFORM=macos;;
    *)          
        echo -e "${RED}Error: Unsupported OS: ${OS}${NC}"
        echo "This installer supports macOS and Linux only."
        echo "For Windows, please download the .exe from the releases page."
        exit 1
        ;;
esac

echo -e "${YELLOW}Detected platform: ${PLATFORM}${NC}"

# Get the latest release version
echo "Fetching latest release..."
LATEST_VERSION=$(curl -s "https://api.github.com/repos/${REPO}/releases/latest" | grep '"tag_name":' | sed -E 's/.*"([^"]+)".*/\1/')

if [ -z "$LATEST_VERSION" ]; then
    echo -e "${RED}Error: Could not fetch latest release version${NC}"
    exit 1
fi

echo -e "${GREEN}Latest version: ${LATEST_VERSION}${NC}"

# Construct download URL
ASSET_NAME="${BINARY_NAME}-${PLATFORM}"
DOWNLOAD_URL="https://github.com/${REPO}/releases/download/${LATEST_VERSION}/${ASSET_NAME}"

echo "Downloading from: ${DOWNLOAD_URL}"

# Download the binary
TMP_FILE="/tmp/${BINARY_NAME}"
if ! curl -L -f "${DOWNLOAD_URL}" -o "${TMP_FILE}"; then
    echo -e "${RED}Error: Failed to download binary${NC}"
    exit 1
fi

# Make it executable
chmod +x "${TMP_FILE}"

# Install the binary
echo "Installing to ${INSTALL_DIR}..."
if [ -w "${INSTALL_DIR}" ]; then
    mv "${TMP_FILE}" "${INSTALL_DIR}/${BINARY_NAME}"
else
    sudo mv "${TMP_FILE}" "${INSTALL_DIR}/${BINARY_NAME}"
fi

# Verify installation
if command -v ${BINARY_NAME} &> /dev/null; then
    echo -e "${GREEN}✓ Installation successful!${NC}"
    echo ""
    echo "Try running: ${BINARY_NAME} --help"
else
    echo -e "${YELLOW}Warning: Binary installed but not found in PATH${NC}"
    echo "You may need to add ${INSTALL_DIR} to your PATH"
fi
