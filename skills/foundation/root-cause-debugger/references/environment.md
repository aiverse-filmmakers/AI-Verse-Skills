# Works here, not there

The cause is a difference between the two machines. Collect the same facts on both, compare, then change one thing.

## What to collect

| Fact | macOS or Linux | Windows (PowerShell) |
| --- | --- | --- |
| System and chip | `uname -sm` (macOS: also `sw_vers`) | `systeminfo \| findstr /B /C:"OS"` |
| Runtime versions | `node -v`, `python3 --version`, `ffmpeg -version` | same |
| Which copy of a program runs | `which -a python3` | `where.exe python` |
| Search path, in order | `echo $PATH \| tr ':' '\n'` | `$env:Path -split ';'` |
| Installed packages | `npm ls --depth=0`, `python3 -m pip freeze` | same |
| Environment variable names (never values) | `env \| cut -d= -f1 \| sort` | `Get-ChildItem Env: \| Select-Object Name` |
| What is using a port | `lsof -i :3000` | `netstat -ano \| findstr :3000` |
| File permissions | `ls -l <file>` | `icacls <file>` |
| Free disk space | `df -h` | `Get-PSDrive` |

Run only the rows that could matter for this failure.

## Usual culprits, most common first

1. **Wrong runtime version.** A version manager (nvm, pyenv, a virtual environment) is active on one machine and not the other.
2. **A second copy earlier on the search path.** `which -a` shows every copy; the first one wins.
3. **A missing environment variable.** Present in a local `.env` file, absent on the server.
4. **Capital letters in file names.** macOS and Windows treat `Logo.png` and `logo.png` as the same file. Linux servers do not.
5. **Line endings.** Files saved on Windows can break shell scripts on Linux.
6. **Chip type.** Apple Silicon reports `arm64`; older Macs and most servers report `x86_64`. Some packages ship for one only.
7. **Permissions.** The file exists but the program may not read or run it.
8. **The port is already taken.**
9. **Stale build or cache.** Delete the build folder before deleting installed packages.

## Method

1. Collect on the working machine and the failing one.
2. List only the differences.
3. Rank them by how well each explains the exact error.
4. Change one, re-run the failing command.

Prefer changes that can be undone. Ask before installing anything system wide or changing a shell profile.
