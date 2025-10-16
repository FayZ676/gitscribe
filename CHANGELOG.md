# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.0.14] - 2025-10-15

### Added

- Introduced a command to uninstall git hooks.
- Added support for installing a pre-push hook and updated binary commands.
- Implemented a command for generating commit messages from git diffs.
- Enabled file output via an `--output` flag.
- Provided a default style file, and support for specifying a style example file with a CLI flag.
- Added a feature to use OpenAI LLM to summarize commit messages via the content command, as well as a configure command for setting OpenAI API keys.
- Message style file and configuration command added.
- Reorganized repository structure for improved file organization.
- Added instructions for uninstalling in release notes.
- Included install instructions in release notes.
- Added a test command to Makefile for local CLI script validation.

### Changed

- Moved installation and usage instructions to the README. Added and updated the CHANGELOG.
- Renamed CLI tool from `commit2content` to `gitscribe`. Updated repository and workflow references accordingly.
- Renamed content/message commands to post/commit for better clarity.
- Utility and prompt functions moved to dedicated modules for cleaner code separation.
- Release workflow updated to publish to the current repository and use the correct path for PyInstaller.

### Fixed

- Fixed the path to PyInstaller within the GitHub release workflow.
- Cleaned up code by removing unused files, comments, and improving spacing.
- Simplified exception handling in code sections.
- Ensured app behavior remains robust when style files are absent—returns empty string instead of an error, allowing user to optionally specify a custom style file.
