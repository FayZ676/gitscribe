⸻

Usage

commit2content [options]

⸻

Options
	•	--last <N>
Use the last N commits.
	•	Example: commit2content --last 5
	•	Default: --last 1
	•	--since <date>
Include commits since a given date (YYYY-MM-DD).
	•	Example: commit2content --since 2023-09-01
	•	--until <date>
Include commits up to a given date (YYYY-MM-DD).
	•	Example: commit2content --since 2023-09-01 --until 2023-09-30
	•	--style <file>
Path to a text file containing example outputs (e.g., tweets, changelogs).
Helps guide the LLM's tone and format.
	•	Example: commit2content --style ./examples/tweet.txt
	•	--max-length <N>
Maximum length of generated content, in words.
	•	Example: commit2content --max-length 100
	•	Default: 50
	•	--debug (optional)
Print the full prompt and raw model output for troubleshooting.

⸻

Defaults

If no options are passed:

commit2content

Behaves as:
	•	Uses the last commit
	•	Max 50 words
	•	No style file

⸻

Output

The CLI prints exactly one piece of generated content to stdout.

Example:

🚀 Added dark mode and improved login speed. Try it out now!