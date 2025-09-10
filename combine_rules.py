#!/usr/bin/env python3
"""
Script to combine all rules markdown files into a single global rules file.
basic-data.md is placed first, followed by all other markdown files.
Output filename format: DDMMYYHHSS_globalrules.md
"""

import os
import glob
from datetime import datetime
from pathlib import Path

def get_timestamp():
    """Generate timestamp in DDMMYYHHSS format"""
    now = datetime.now()
    return now.strftime("%d%m%y%H%M%S")

def find_markdown_files(rules_dir):
    """Find all markdown files in the rules directory, excluding basic-data.md"""
    pattern = os.path.join(rules_dir, "**", "*.md")
    all_files = glob.glob(pattern, recursive=True)
    
    # Separate basic-data.md from other files
    basic_data_file = None
    other_files = []
    
    for file_path in all_files:
        if file_path.endswith("basic-data.md"):
            basic_data_file = file_path
        else:
            other_files.append(file_path)
    
    # Sort other files for consistent ordering
    other_files.sort()
    
    return basic_data_file, other_files

def read_file_content(file_path):
    """Read content from a markdown file"""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        return content
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return f"# Error reading {file_path}\n\n"

def combine_rules():
    """Main function to combine all rules into a single file"""
    # Define paths
    script_dir = Path(__file__).parent
    rules_dir = script_dir / "rules"
    constructed_globals_dir = script_dir / "constructed-globals"
    
    # Create constructed-globals directory if it doesn't exist
    constructed_globals_dir.mkdir(exist_ok=True)
    
    # Generate timestamp and output filename
    timestamp = get_timestamp()
    output_filename = f"{timestamp}_globalrules.md"
    output_path = constructed_globals_dir / output_filename
    
    print(f"Combining rules into: {output_path}")
    
    # Find all markdown files
    basic_data_file, other_files = find_markdown_files(str(rules_dir))
    
    if not basic_data_file:
        print("Warning: basic-data.md not found!")
        return
    
    print(f"Found basic-data.md: {basic_data_file}")
    print(f"Found {len(other_files)} other markdown files")
    
    # Start combining content
    combined_content = []
    
    # Add header with timestamp
    combined_content.append(f"# Windsurf Rules - Global Compilation")
    combined_content.append(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    combined_content.append(f"Timestamp: {timestamp}")
    combined_content.append("\n" + "="*80 + "\n")
    
    # Add basic-data.md first
    print(f"Processing: {basic_data_file}")
    basic_content = read_file_content(basic_data_file)
    combined_content.append(basic_content)
    
    # Add all other files
    for file_path in other_files:
        print(f"Processing: {file_path}")
        
        # Add file content
        content = read_file_content(file_path)
        combined_content.append(content)
    
    # Write combined content to output file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write('\n'.join(combined_content))
        
        print(f"Successfully created: {output_path}")
        print(f"Total files processed: {len(other_files) + 1}")
        
    except Exception as e:
        print(f"Error writing output file: {e}")

if __name__ == "__main__":
    combine_rules()
