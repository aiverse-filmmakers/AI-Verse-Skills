# Mapping a codebase before changing it

Read only. Nothing is edited while mapping.

## What the map must answer

1. Where does the program start? (entry points)
2. Where is the thing defined?
3. Who uses it?
4. What tests cover it?
5. Where else is its name written: settings, text strings, documentation, generated files?
6. What changed here recently?

## How to find each

| Question | How |
| --- | --- |
| Entry points | `package.json` scripts and `main`, route folders, command line files, top level `index` or `main` files |
| Every file in the project | `git ls-files` |
| Every mention of a name | `git grep -n -w "Name"` (`-w` matches the whole word only) |
| Tests that mention it | `git grep -l "Name" -- '*test*' '*spec*'` |
| Definition and real references | The language's own "find references" tool when one is available; it is more exact than text search |
| Recent changes to a file | `git log --oneline -10 -- <path>` |
| When a name appeared or vanished | `git log -S"Name" --oneline` |
| Who imports whom | Search for the file's path in import lines |

## Uses that text search misses

Check these by hand; they are where half finished renames hide.

- Names built from pieces of text at run time
- Names in settings files, environment variables and templates
- Names in database columns and saved data
- Names in web addresses that people or other sites link to
- Generated files: never edit them; find what generates them and change that

## The map

```
Changing:       what, in one line
Defined in:     file and line
Used by:        each caller, grouped by area
Tests:          which cover it, and which behaviour has none
Also named in:  settings, strings, documentation, generated files
Depends on:     what it needs
Depended on by: what breaks if it changes
Recent changes: anything in the last few weeks
Fact or guess:  mark every line you inferred and did not see
Not searched:   folders or kinds of file you did not look in
```

"Not searched" is part of the map. A blind spot you name is safe; one you hide is not.
