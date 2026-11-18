#!/bin/sh
set -eu

REPO_URL="${AI_VERSE_SKILLS_REPO:-https://github.com/aiverse-filmmakers/AI-Verse-Skills.git}"
DEST="${AI_VERSE_SKILLS_HOME:-$HOME/.aiverse/tools/AI-Verse-Skills}"
BIN_DIR="${AI_VERSE_BIN_DIR:-$HOME/.local/bin}"

command -v git >/dev/null 2>&1 || { echo "git is required" >&2; exit 2; }
command -v python3 >/dev/null 2>&1 || { echo "python3 is required" >&2; exit 2; }

mkdir -p "$(dirname "$DEST")" "$BIN_DIR"

CREATED=0
stop() {
  echo "Stopped: $1 Nothing was changed." >&2
  if [ "$CREATED" = 1 ]; then rm -rf "$DEST"; fi
  exit 2
}

if [ -d "$DEST/.git" ]; then
  git -C "$DEST" fetch --quiet origin main 2>/dev/null || stop "could not download the latest release information."
else
  git clone --quiet --no-checkout "$REPO_URL" "$DEST" 2>/dev/null || stop "could not download AI-Verse Skills."
  CREATED=1
fi

# Members get the accepted release recorded in release/component-release.json,
# never whatever is newest on main (same rule as the OS update command).
# AI_VERSE_SKILLS_REF is a developer only override (any branch, tag or commit).
if [ -n "${AI_VERSE_SKILLS_REF:-}" ]; then
  git -C "$DEST" fetch --quiet origin "$AI_VERSE_SKILLS_REF" 2>/dev/null || true
  TARGET="$(git -C "$DEST" rev-parse --verify --quiet "${AI_VERSE_SKILLS_REF}^{commit}" || git -C "$DEST" rev-parse --verify --quiet "origin/${AI_VERSE_SKILLS_REF}^{commit}" || true)"
  [ -n "$TARGET" ] || stop "developer ref not found: $AI_VERSE_SKILLS_REF."
  echo "Developer override: installing $AI_VERSE_SKILLS_REF"
else
  TIP="$(git -C "$DEST" rev-parse --verify --quiet origin/main^{commit} || true)"
  [ -n "$TIP" ] || stop "the latest release information is missing."
  RELEASE="$(git -C "$DEST" show "$TIP:release/component-release.json" 2>/dev/null || true)"
  ACCEPTED="$(printf '%s' "$RELEASE" | python3 -c 'import json,re,sys
r=json.load(sys.stdin)
if r.get("release_status")=="accepted" and re.fullmatch(r"[a-f0-9]{40}",str(r.get("revision",""))):
    print(r["revision"])' 2>/dev/null || true)"
  [ -n "$ACCEPTED" ] || stop "no valid accepted release was found."
  git -C "$DEST" cat-file -e "$ACCEPTED^{commit}" 2>/dev/null || stop "the accepted release $ACCEPTED is not in the downloaded copy."
  TARGET="$ACCEPTED"
  # An acceptance commit only touches release/, so such a tip is that release.
  if git -C "$DEST" merge-base --is-ancestor "$ACCEPTED" "$TIP" 2>/dev/null; then
    CHANGED="$(git -C "$DEST" diff --no-renames --name-only "$ACCEPTED" "$TIP")" || stop "could not compare the release with the latest version."
    OTHER="$(printf '%s\n' "$CHANGED" | grep -v '^release/' | grep -v '^$' || true)"
    if [ -z "$OTHER" ]; then TARGET="$TIP"; fi
  fi
fi

if [ "$CREATED" = 0 ] && [ -n "$(git -C "$DEST" status --porcelain --untracked-files=no 2>/dev/null)" ]; then
  stop "your copy at $DEST has local changes. Commit, stash or revert them, then run this again."
fi
git -C "$DEST" checkout --quiet --detach "$TARGET" 2>/dev/null || stop "could not switch to the accepted release."
echo "AI-Verse Skills release: $(git -C "$DEST" rev-parse --short HEAD)"

ln -sfn "$DEST/aiverse-skills" "$BIN_DIR/ai-verse-skills"

echo "AI-Verse Skills CLI installed at $BIN_DIR/ai-verse-skills"
case ":${PATH}:" in
  *":$BIN_DIR:"*) ;;
  *) echo "Add $BIN_DIR to PATH to use ai-verse-skills globally." ;;
esac

# Exit code 3 from install means partial success: some third party skill sources could
# not be downloaded, everything else is installed (skills already on this computer are
# kept). We carry on to the readiness check, and the final exit code is the readiness
# result: nonzero only when that check fails. Exit code 4 means the install was blocked
# and nothing was installed or changed; that and any other install failure stop here.
PARTIAL=0
"$DEST/aiverse-skills" install --profile "${AI_VERSE_SKILLS_PROFILE:-full}" || {
  RC=$?
  if [ "$RC" -eq 4 ]; then echo "AI-Verse Skills was not installed or changed. See the message above." >&2; fi
  if [ "$RC" -ne 3 ]; then exit "$RC"; fi
  PARTIAL=1
}
"$DEST/aiverse-skills" doctor --readiness
if [ "$PARTIAL" = 1 ]; then
  echo "AI-Verse Skills is installed and ready, but some third party skills were skipped or kept at an older version (listed above). Run this same command again when your connection is stable to add them."
fi
