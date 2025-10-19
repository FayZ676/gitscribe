# GitScribe Usage Examples

This document provides examples of how to use GitScribe to transform your git history into posts, blogs, release notes, and more.

## Prerequisites

Before using GitScribe, make sure you have:

1. Installed GitScribe (see [INSTALL.md](INSTALL.md) for installation instructions)
2. Configured your OpenAI API key and default style files: `gitscribe configure`

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

## Configuration

### Initial Setup

The first time you use GitScribe, run the configure command to set up your environment:

```bash
gitscribe configure
```

This command will guide you through three setup steps:

1. **OpenAI API Key**: Enter your OpenAI API key (get one from [platform.openai.com/api-keys](https://platform.openai.com/api-keys))
2. **Default Commit Style File**: Specify the path to your default style file for commit messages
3. **Default Post Style File**: Specify the path to your default style file for post generation

**Updating Configuration:**

You can update your default style files at any time by re-running:

```bash
gitscribe configure
```

This allows you to switch between different style preferences without editing the config file manually.

## Post Generation Examples

The `post` command generates posts, blogs, release notes, and more from your commit history.

> **💡 Generated content is automatically copied to your clipboard for easy sharing and pasting.**

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

GitScribe supports style files to control how content is generated. During configuration, you can set default style files that will be used automatically.

```bash
# Use default post style from configuration
gitscribe post --last 5

# Override default with a different style file
gitscribe post --last 5 --style styles/release_style.txt
```

### Output Options

```bash
# Save to default file (gitscribe_output.txt)
gitscribe post --last 5

# Save to a specific file
gitscribe post --last 5 --output my_update.md
```

## Commit Message Generation Examples

The `commit` command generates commit messages from your current git diff.

> **💡 Generated content is automatically copied to your clipboard for easy sharing and pasting.**

### Basic Usage

```bash
# Generate a commit message from staged and unstaged changes
# Uses default commit style from configuration
gitscribe commit

# Override default with a custom style
gitscribe commit --style styles/commit_style.txt

# Use a different custom style
gitscribe commit --style my_custom_commit_style.txt
```

## Style Files

Style files are a core feature of GitScribe that tell the AI how to format and present the content it generates. They allow you to maintain consistent style across all your generated content.

### Default Style Files

During the initial `gitscribe configure` setup, you specify default style files for both commit messages and post generation:

- **Default Commit Style**: Used by `gitscribe commit` when no `--style` option is provided
- **Default Post Style**: Used by `gitscribe post` when no `--style` option is provided

**Benefits of default style files:**

- No need to specify `--style` every time you run a command
- Ensures consistent style across all your commits and posts
- Easy to update by re-running `gitscribe configure`
- Can still override with `--style` option when needed

### Built-in Style Files

GitScribe comes with several built-in style files for various types of content:

- `styles/post_style.txt` - For general post content
- `styles/commit_style.txt` - For commit messages
- `styles/release_style.txt` - For release notes and announcements
- `styles/hacker_news_style.txt` - For Hacker News-style posts

### Creating Custom Styles

You can create your own style files to customize the output. Style files are simple text files that describe how you want the content formatted.

**Example custom style file (`blog_style.txt`):**

```
Generate content in a professional blog post format with:
- Clear headings
- Bullet points for features
- Technical details in code blocks
- Casual but informative tone
- Include emojis for visual appeal
```

**Using custom styles:**

```bash
# Set as default during configuration
gitscribe configure
# Enter the path to blog_style.txt when prompted

# Or use directly with --style option
gitscribe post --last 5 --style blog_style.txt
```

**Tips for creating effective style files:**

- Be specific about formatting preferences (headings, lists, code blocks, etc.)
- Specify the tone (formal, casual, technical, etc.)
- Include examples of desired output if helpful
- Keep instructions clear and concise
- Test and refine based on the generated output

## Tips and Best Practices

1. **Commit Quality**: The better your commit messages, the better the generated content. Use the `gitscribe commit` command to easily generate consistent, high quality messages.
2. **Style Consistency**: Configure default style files during setup to ensure all generated content follows your preferred format
3. **Style File Organization**: Store your custom style files in a dedicated directory (e.g., `~/.gitscribe/` or your project's `styles/` folder)
4. **Regular Updates**: Re-run `gitscribe configure` when you want to switch between different style preferences
5. **Test Your Styles**: After creating a custom style file, test it with a few commits to ensure it produces the desired output
