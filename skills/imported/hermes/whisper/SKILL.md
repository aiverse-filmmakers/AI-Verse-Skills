---
name: whisper
description: Transcribe speech from audio or video, produce timed captions, or translate speech into English using an available transcription tool. Use for interviews, podcasts, meetings, footage and subtitles.
license: MIT
---
# Whisper transcription

Turn an accessible recording into the requested transcript or timed subtitle file. Whisper is one possible local engine; never assume it is installed or that a cloud provider is authorized.

1. Identify the input, requested language, transcription versus English translation, output format, and whether timestamps or speaker labels are needed. Preserve the original and use a separate output path. Ask only when a missing choice affects the result.
2. Inspect available tools and local models. Prefer an existing suitable local tool for private material. Whisper typically needs Python, FFmpeg and a model download; check rather than install automatically. If no suitable tool is available, explain what is missing and offer a setup route consistent with the host's installation rules. Do not send recordings to a third party without the user's permission.
3. Choose an installed model appropriate to available memory, time, language and quality. Larger models may require substantial memory and downloads; do not promise a fixed speed or accuracy. For translation verify that the selected model supports it; Whisper turbo is not suitable for translation to English.
4. Transcribe a short representative portion first when feasible. Listen and compare with the text, especially names, numbers, multiple speakers, silence and noisy sections. If audio playback is unavailable, say the transcript has not been checked against the recording.
5. Process the full recording using the selected tool. Preserve source timings for subtitle requests and check any chunk boundaries. Whisper does not identify speakers by itself: use a suitable separate method if available or label speakers as uncertain. Never invent dialogue, a speaker or an inaudible passage.
6. Check the actual output exists, opens, has the requested language and format, and covers the expected duration. For subtitles inspect timing and readability against the audio when possible. Mark uncertain words and gaps. Avoid claiming accuracy or listening that was not verified.
7. Deliver the requested file or text and briefly state the method, any unchecked parts and limitations. For video editing, pass source timings to the video editor; do not silently replace its editorial decisions.

Examples of output include plain text, SRT and VTT. Use the installed engine's documented commands and supported options. A transcript is not a verified quotation until checked against the source.
