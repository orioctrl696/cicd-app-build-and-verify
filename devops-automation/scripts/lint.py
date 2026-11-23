#!/usr/bin/env python3
"""
Linting script for Java code
Performs basic code quality checks
"""
import os
import sys
import subprocess
from pathlib import Path

def find_java_files():
    """Find all Java files in src directory"""
    java_files = []
    src_dir = Path("src")

    if not src_dir.exists():
        print("❌ ERROR: src directory not found")
        return []

    for java_file in src_dir.rglob("*.java"):
        java_files.append(str(java_file))

    return java_files

def check_basic_patterns(java_files):
    """Check basic code patterns and quality"""
    issues = []

    for file_path in java_files:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            lines = content.split('\n')

            for line_num, line in enumerate(lines, 1):
                # Check for System.out.println (should use logger)
                if 'System.out.println' in line and not line.strip().startswith('//'):
                    issues.append(f"{file_path}:{line_num} - Use logger instead of System.out.println")

                # Check for TODO comments
                if 'TODO' in line.upper() and not line.strip().startswith('//'):
                    issues.append(f"{file_path}:{line_num} - TODO found in code")

                # Check line length (warning if > 120 chars)
                if len(line) > 120:
                    issues.append(f"{file_path}:{line_num} - Line too long ({len(line)} chars)")

    return issues

def main():
    """Main linting function"""
    print("🔍 Running Java Lint Checks...")
    print("=" * 60)

    java_files = find_java_files()

    if not java_files:
        print("⚠️  WARNING: No Java files found to lint")
        return 0

    print(f"📁 Found {len(java_files)} Java files")

    issues = check_basic_patterns(java_files)

    if issues:
        print(f"\n⚠️  Found {len(issues)} linting issues:\n")
        for issue in issues[:10]:  # Show first 10 issues
            print(f"  • {issue}")

        if len(issues) > 10:
            print(f"\n  ... and {len(issues) - 10} more issues")

        # Don't fail the build for lint warnings, just report them
        print("\n✅ Lint check completed with warnings")
        return 0
    else:
        print("\n✅ All lint checks passed!")
        return 0

if __name__ == "__main__":
    sys.exit(main())
