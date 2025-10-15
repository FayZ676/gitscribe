from string import Template


post_prompt = Template(
    """
## Instructions:
Your job is to transform commit messages into meaningful content in the style of other provided content.
    
## Commits:
$commits

## Style References
$style

Return only the transformed text content and nothing else.
"""
)


commit_prompt = Template(
    """
## Instructions:
Your job is to generate a clear, concise commit message based on the git diff provided below.
The commit message should follow best practices and accurately describe the changes made.

$style

## Git Diff:
$diff

Return only the commit message text and nothing else.
"""
)
