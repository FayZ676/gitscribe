"""GitScribe CLI - Main entry point."""

import sys
import os

# Add the parent directory to Python path so we can import src modules
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.cli.main import gitscribe


if __name__ == "__main__":
    gitscribe()
