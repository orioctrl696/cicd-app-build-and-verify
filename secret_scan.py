#!/usr/bin/env python3
"""
Secret scanning script
Detects potential secrets, API keys, and sensitive data in code
"""
import os
import sys
import re
from pathlib import Path

# Patterns to detect potential secrets
SECRET_PATTERNS = {
    'AWS Access Key': r'AKIA[0-9A-Z]{16}',
    'Generic API Key': r'[aA][pP][iI]_?[kK][eE][yY].*[\'"]([0-9a-zA-Z]{32,45})[\'"]',
    'Generic Secret': r'[sS][eE][cC][rR][eE][tT].*[\'"]([0-9a-zA-Z]{32,45})[\'"]',
    'Password in code': r'[pP][aA][sS][sS][wW][oO][rR][dD].*[\'"](.+?)[\'"]',
    'Private Key': r'-----BEGIN (RSA |EC )?PRIVATE KEY-----',
    'JWT Token': r'eyJ[A-Za-z0-9-_=]+\.eyJ[A-Za-z0-9-_=]+\.?[A-Za-z0-9-_.+/=]*',
    'GitHub Token': r'gh[pousr]_[A-Za-z0-9]{36,}',
    'Slack Token': r'xox[baprs]-[0-9a-zA-Z]{10,48}',
}

# Files to exclude from scanning
EXCLUDED_FILES = {
    '.git', 'node_modules', 'target', 'build', '.idea',
    'venv', '__pycache__', '.pytest_cache', 'dist'
}

# File extensions to scan
SCAN_EXTENSIONS = {
    '.java', '.xml', '.properties', '.yml', '.yaml',
    '.json', '.txt', '.sh', '.py', '.js', '.ts'
}

def should_scan_file(file_path):
    """Check if file should be scanned"""
    path = Path(file_path)

    # Check if in excluded directory
    for part in path.parts:
        if part in EXCLUDED_FILES:
            return False

    # Check file extension
    return path.suffix in SCAN_EXTENSIONS

def scan_file_for_secrets(file_path):
    """Scan a single file for potential secrets"""
    findings = []

    try:
        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
            content = f.read()
            lines = content.split('\n')

            for line_num, line in enumerate(lines, 1):
                for secret_type, pattern in SECRET_PATTERNS.items():
                    matches = re.finditer(pattern, line)
                    for match in matches:
                        # Skip if it's a comment or example
                        if any(marker in line for marker in ['#', '//', '/*', 'example', 'EXAMPLE', 'YOUR_']):
                            continue

                        findings.append({
                            'file': file_path,
                            'line': line_num,
                            'type': secret_type,
                            'context': line.strip()[:80]
                        })
    except Exception as e:
        print(f"⚠️  Warning: Could not scan {file_path}: {e}")

    return findings

def main():
    """Main secret scanning function"""
    print("🔒 Running Secret Scan...")
    print("=" * 60)

    all_findings = []
    scanned_files = 0

    # Scan current directory recursively
    for root, dirs, files in os.walk('.'):
        # Remove excluded directories
        dirs[:] = [d for d in dirs if d not in EXCLUDED_FILES]

        for file in files:
            file_path = os.path.join(root, file)

            if should_scan_file(file_path):
                scanned_files += 1
                findings = scan_file_for_secrets(file_path)
                all_findings.extend(findings)

    print(f"📁 Scanned {scanned_files} files")

    if all_findings:
        print(f"\n🚨 ALERT: Found {len(all_findings)} potential secrets!\n")

        for finding in all_findings:
            print(f"  ⚠️  {finding['type']}")
            print(f"      File: {finding['file']}:{finding['line']}")
            print(f"      Context: {finding['context']}")
            print()

        print("❌ Secret scan FAILED - Please review and remove sensitive data")
        return 1
    else:
        print("\n✅ No secrets detected!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
