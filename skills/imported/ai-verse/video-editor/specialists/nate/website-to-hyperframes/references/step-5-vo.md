# Step 5: Generate VO + Map Timing

## Provider Preflight

Before generating narration, resolve the active audio/TTS route through the installed
AI-Verse/HyperFrames provider and the user's authorization.

For the accepted HyperFrames 0.8.40 provider:

- `npx hyperframes tts` is the local Kokoro route;
- `npx hyperframes transcribe` is the maintained word-level transcription/import route;
- cloud/provider-specific voice generation must respect the active provider's authentication,
  billing, upload and consent boundaries;
- do not silently fall back from a requested cloud/brand voice to another voice because
  credentials are missing.

If the current provider requires an authentication/preflight choice, complete that
choice before synthesizing audio.

## Audition Voices

Do not lock the first voice merely because it is available.

When the user has not already chosen an exact voice:

1. resolve 2-3 suitable candidates from the authorized provider route;
2. audition the first sentence or another representative line;
3. compare naturalness, pacing, breath, tone and pronunciation;
4. choose the best match for the storyboard's VO direction;
5. record the provider and voice identity in the project handoff.

If the user specified a voice, gender, accent, language or tone, preserve that
constraint instead of substituting a convenient default.

### Local HyperFrames example

```bash
npx hyperframes tts "First audition line" --voice af_nova --output audition.wav
```

Use `npx hyperframes tts --list` for the installed local voice list.

## Generate Full Narration

Generate the approved script as `narration.wav` or another explicitly supported
project audio format.

Record at least:

- provider/route;
- voice id/name;
- language;
- speed/pacing setting when non-default;
- output path;
- any external upload/billing decision that mattered.

## Obtain Word-Level Timing

If the selected TTS route already returns trustworthy word timestamps, normalize
them into the canonical project transcript shape and preserve their provenance.

Otherwise run the maintained transcription route on the generated narration:

```bash
npx hyperframes transcribe narration.wav
```

This produces/normalizes `transcript.json` with word-level timing.

**The actual generated narration and its normalized word timestamps are the source
of truth for beat timing. Estimated script duration is not.**

## Map Timestamps to Beats

Go through STORYBOARD.md beat by beat. For each beat:

1. find the first retained word of that beat's VO cue in `transcript.json`;
2. find the last retained word of that beat's VO cue;
3. set `beat.start` from the first word onset;
4. set `beat.end` from the last word end;
5. add only the deliberate visual breathing room required by the story, commonly
   around 0.3-0.5s where it does not collide with the next spoken beat;
6. update STORYBOARD.md with the real measured timing.

Beat boundaries should follow speech and editorial intent, not evenly divided math.

## Update the Composition

Update each scene/composition slot's `data-start` and `data-duration` from the
real mapped timing. Update total composition/audio duration from the encoded audio
and transcript evidence.

Do not invent timing independently in the composition after this point. Any later
edit to narration, silence, or words requires the affected timing map to be
re-derived from the canonical edit/transcript evidence.

## Verify Before Build Continues

Before Step 6:

- narration file exists and is the approved take;
- transcript identity matches that narration;
- all required words have valid ordered timing;
- storyboard beat times were replaced with measured values;
- no beat points to an older narration take;
- external-provider provenance/authorization is recorded when applicable.

## AI-Verse Adaptation Notes

Adapted from Nate Herk's MIT-licensed Step 5 at `b1afdb1dcbcad39dd27638ea699f132fe44ce6df`.

Preserved:
- audition before committing to a voice;
- narration generated before final beat timing;
- word-level transcript as timing authority;
- storyboard durations updated from the actual VO;
- composition timing derived from those measured beats.

Adapted:
- removed hard-coded MCP/provider names from Nate's environment;
- current HyperFrames 0.8.40 local TTS/transcribe surfaces are documented accurately;
- cloud TTS routes are provider/authorization-aware rather than silently assumed;
- generated VO/transcript provenance is explicit.
