# GitScribe Usage Examples

This document provides comprehensive examples of how to use GitScribe to transform your git history into shareable content.

## Prerequisites

Before using GitScribe, make sure you have:

1. Installed GitScribe (see [README.md](README.md) for installation instructions)
2. Configured your OpenAI API key: `gitscribe configure`

## Basic Usage

### Get Help

```bash
# General help
gitscribe --help

# Help for specific commands
gitscribe post --help
gitscribe commit --help
gitscribe configure --help
```

### Configuration

```bash
# Configure your OpenAI API key (required for first use)
gitscribe configure
```

## Post Generation Examples

The `post` command generates shareable content from your git commits.

### Basic Examples

```bash
# Generate content from the last commit
gitscribe post

# Generate content from the last 5 commits
gitscribe post --last 5

# Generate content from the last 10 commits
gitscribe post --last 10
```

### Date-Based Examples

```bash
# Generate content from commits since a specific date
gitscribe post --since 2024-01-01

# Generate content from commits until a specific date
gitscribe post --until 2024-12-31

# Generate content from commits in a date range
gitscribe post --since 2024-01-01 --until 2024-01-31
```

### Style Customization

```bash
# Use default post style
gitscribe post --last 5

# Use a different style file
gitscribe post --last 5 --style styles/release_style.txt
```

### Output Options

```bash
# Save to default file (gitscribe_output.txt)
gitscribe post --last 5

# Save to a specific file
gitscribe post --last 5 --output my_update.md
```

**Tip 💡: Generated content is automatically copied to your clipboard for easy sharing and pasting.**

## Commit Message Generation Examples

The `commit` command generates commit messages from your current git diff.

### Basic Usage

```bash
# Generate a commit message from staged and unstaged changes
gitscribe commit

# Generate a commit message with custom style
gitscribe commit --style styles/commit_style.txt
```

## Style Files

GitScribe comes with several built-in style files:

- `styles/post_style.txt` - For general post content
- `styles/commit_style.txt` - For commit messages
- `styles/release_style.txt` - For release notes and announcements

### Creating Custom Styles

You can create your own style files to customize the output. Style files contain instructions for the AI on how to format and present the content.

Example custom style file (`my_style.txt`):

```
Generate content in a professional blog post format with:
- Clear headings
- Bullet points for features
- Technical details in code blocks
- Casual but informative tone
- Include emojis for visual appeal
```

Then use it:

```bash
gitscribe post --last 5 --style my_style.txt
```

## Tips and Best Practices

1. **Commit Quality**: The better your commit messages, the better the generated content. Use the `gitscribe commit` command to easily generate consistent, high quality messages.
2. **Style Consistency**: Use consistent style files across your project
3. **Review Output**: Always review and edit the generated content before publishing
