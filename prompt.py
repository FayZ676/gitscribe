from string import Template

prompt = Template(
    """
$commits
$max_length
$examples

Instructions here.
"""
)
