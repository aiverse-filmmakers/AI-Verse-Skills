---
name: web-design-guidelines
description: Review UI code for Web Interface Guidelines compliance. Use when asked to "review my UI", "check accessibility", "audit design", "review UX", or "check my site against best practices".
metadata:
  author: vercel
  version: "1.0.0"
  argument-hint: <file-or-pattern>
---

# Web Interface Guidelines

Review files for compliance with Web Interface Guidelines.

## How It Works

1. Read the pinned guidelines from `references/command.md`
2. Read the specified files (or prompt user for files/pattern)
3. Check against all rules in the pinned guidelines
4. Output findings in the terse `file:line` format

## Guidelines Source

Read `references/command.md`. AI-Verse snapshots that file from the verified upstream Web Interface Guidelines commit recorded in `SOURCE.json`, so one immutable Skills generation cannot drift to a different ruleset during execution.


## Usage

When a user provides a file or pattern argument:
1. Read `references/command.md`
2. Read the specified files
3. Apply all rules from the pinned guidelines
4. Output findings using the format specified in the guidelines

If no files specified, ask the user which files to review.
