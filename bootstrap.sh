#!/bin/sh
set -eu

REPO_URL="${AI_VERSE_SKILLS_REPO:-https://github.com/aiverse-filmmakers/AI-Verse-Skills.git}"
DEST="${AI_VERSE_SKILLS_HOME:-$HOME/.aiverse/tools/AI-Verse-Skills}"
BIN_DIR="${AI_VERSE_BIN_DIR:-$HOME/.local/bin}"

command -v git >/dev/null 2>&1 || { echo "git is required" >&2; exit 2; }
command -v python3 >/dev/null 2>&1 || { echo "python3 is required" >&2; exit 2; }

mkdir -p "$(dirname "$DEST")" "$BIN_DIR"
if [ -d "$DEST/.git" ]; then
  git -C "$DEST" fetch --quiet origin main
  git -C "$DEST" checkout --quiet main
  git -C "$DEST" pull --quiet --ff-only origin main
else
  git clone --quiet "$REPO_URL" "$DEST"
fi

ln -sfn "$DEST/aiverse-skills" "$BIN_DIR/ai-verse-skills"

echo "AI-Verse Skills CLI installed at $BIN_DIR/ai-verse-skills"
case ":${PATH}:" in
  *":$BIN_DIR:"*) ;;
  *) echo "Add $BIN_DIR to PATH to use ai-verse-skills globally." ;;
esac

"$DEST/aiverse-skills" install --profile "${AI_VERSE_SKILLS_PROFILE:-full}"
"$DEST/aiverse-skills" doctor --readiness
