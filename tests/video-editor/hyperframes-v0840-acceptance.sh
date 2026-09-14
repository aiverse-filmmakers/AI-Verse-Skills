#!/usr/bin/env bash
set -euo pipefail

NATE_REPO="https://github.com/nateherkai/hyperframes-student-kit.git"
NATE_REF="b1afdb1dcbcad39dd27638ea699f132fe44ce6df"
CANDIDATE_VERSION="0.8.40"
WORK_ROOT="${RUNNER_TEMP:-/tmp}/aiverse-video-editor-hf-acceptance"
NATE_DIR="$WORK_ROOT/nate-kit"
ARTIFACT_DIR="$WORK_ROOT/artifacts"
PROJECT_DIR="$WORK_ROOT/hf-smoke"

rm -rf "$WORK_ROOT"
mkdir -p "$WORK_ROOT" "$ARTIFACT_DIR"

exec > >(tee "$ARTIFACT_DIR/acceptance.log") 2>&1

echo "== Environment =="
node --version
npm --version
git --version
ffmpeg -version | head -n 2
ffprobe -version | head -n 1

echo "== Fetch exact Nate kit =="
git clone --quiet "$NATE_REPO" "$NATE_DIR"
cd "$NATE_DIR"
git checkout --quiet "$NATE_REF"
test "$(git rev-parse HEAD)" = "$NATE_REF"

echo "== Install and verify Nate tested baseline =="
npm install --no-audit --no-fund
BASELINE_VERSION="$(node -p "require('./node_modules/hyperframes/package.json').version")"
echo "baseline_hyperframes=$BASELINE_VERSION"
test "$BASELINE_VERSION" = "0.7.109"

npm test | tee "$ARTIFACT_DIR/nate-baseline-tests.log"
npm run check:skills | tee "$ARTIFACT_DIR/nate-baseline-skill-mirrors.log"
npm run check | tee "$ARTIFACT_DIR/nate-baseline-kit-check.log"

echo "== Inject HyperFrames candidate into isolated test copy only =="
npm install --no-save --no-audit --no-fund "hyperframes@$CANDIDATE_VERSION"
CANDIDATE_ACTUAL="$(node -p "require('./node_modules/hyperframes/package.json').version")"
echo "candidate_hyperframes=$CANDIDATE_ACTUAL"
test "$CANDIDATE_ACTUAL" = "$CANDIDATE_VERSION"
npx hyperframes --version | tee "$ARTIFACT_DIR/hyperframes-version.txt"

echo "== Nate behavior tests on candidate runtime =="
npm test | tee "$ARTIFACT_DIR/nate-candidate-tests.log"
npm run check:skills | tee "$ARTIFACT_DIR/nate-candidate-skill-mirrors.log"

echo "== Ensure deterministic browser/runtime =="
npx hyperframes browser ensure | tee "$ARTIFACT_DIR/browser-ensure.log"
npx hyperframes doctor --json | tee "$ARTIFACT_DIR/doctor.json"
node - "$ARTIFACT_DIR/doctor.json" <<'NODE'
const fs=require('fs');
const raw=fs.readFileSync(process.argv[2],'utf8');
const start=raw.indexOf('{');
if(start<0) throw new Error('doctor JSON missing');
const d=JSON.parse(raw.slice(start));
if(d.ok !== true) throw new Error('hyperframes doctor reports not ok: '+JSON.stringify(d));
NODE

echo "== Build synthetic Nate-relevant A/V fixture =="
mkdir -p "$PROJECT_DIR/assets" "$PROJECT_DIR/compositions" "$PROJECT_DIR/frames"

ffmpeg -hide_banner -loglevel error -y \
  -f lavfi -i "testsrc2=size=1280x720:rate=30:duration=8" \
  -f lavfi -i "sine=frequency=880:sample_rate=48000:duration=8" \
  -map 0:v:0 -map 1:a:0 \
  -c:v libx264 -pix_fmt yuv420p -preset veryfast \
  -c:a aac -b:a 160k -shortest \
  "$PROJECT_DIR/assets/source.mp4"

cp "$NATE_DIR/node_modules/gsap/dist/gsap.min.js" "$PROJECT_DIR/assets/gsap.min.js"

cat > "$PROJECT_DIR/index.html" <<'HTML'
<!doctype html>
<html>
<head>
  <meta charset="utf-8" />
  <style>
    html,body{margin:0;background:#111;color:#fff;font-family:Arial,sans-serif}
    [data-composition-id="main"]{position:relative;overflow:hidden;background:#111}
    #main-video{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
    .clip{position:absolute;box-sizing:border-box}
    #panel-a{left:40px;top:40px;padding:24px;background:rgba(0,0,0,.72);font-size:42px}
    #panel-b{right:40px;bottom:40px;padding:24px;background:rgba(255,255,255,.88);color:#111;font-size:36px}
    #pulse{position:absolute;left:50%;top:50%;width:120px;height:120px;margin:-60px;border-radius:50%;background:#fff;opacity:.65}
  </style>
</head>
<body>
  <div id="main" data-composition-id="main" data-start="0" data-duration="6" data-width="1280" data-height="720">
    <video id="main-video" src="assets/source.mp4" data-start="0" data-duration="6" data-media-start="1" data-track-index="0" muted playsinline></video>
    <audio id="main-audio" src="assets/source.mp4" data-start="0" data-duration="6" data-media-start="1" data-track-index="10"></audio>
    <div id="panel-a" class="clip" data-start="0" data-duration="4" data-track-index="1">OVERLAP A</div>
    <div id="panel-b" class="clip" data-start="2" data-duration="4" data-track-index="1">OVERLAP B</div>
    <div id="pulse"></div>
    <div id="nested" data-composition-id="nested" data-composition-src="compositions/nested.html"
         data-start="2" data-duration="2" data-track-index="2" data-width="1280" data-height="720"></div>
  </div>
  <script src="assets/gsap.min.js"></script>
  <script>
    const tl = gsap.timeline({ paused: true });
    const visibleDuration = 6;
    const cycleDuration = 1.25;
    const repeatCount = Math.max(0, Math.floor(visibleDuration / cycleDuration) - 1);
    tl.fromTo("#pulse",{scale:.7,opacity:.25},{scale:1.3,opacity:.85,duration:cycleDuration/2,yoyo:true,repeat:repeatCount,ease:"sine.inOut"},0.1);
    window.__timelines = window.__timelines || {};
    window.__timelines["main"] = tl;
  </script>
</body>
</html>
HTML

cat > "$PROJECT_DIR/compositions/nested.html" <<'HTML'
<template id="nested-template">
  <div data-composition-id="nested" data-duration="2" data-width="1280" data-height="720">
    <video id="nested-video" src="../assets/source.mp4" data-start="0.25" data-duration="1.5"
           data-media-start="2.5" data-track-index="0" muted playsinline
           style="position:absolute;right:70px;top:70px;width:360px;height:203px;object-fit:cover;border:10px solid white"></video>
  </div>
</template>
HTML

cat > "$PROJECT_DIR/captions.srt" <<'SRT'
1
00:00:00,000 --> 00:00:01,000
Hello world

2
00:00:01,100 --> 00:00:02,200
AI Verse editor
SRT

cd "$PROJECT_DIR"

echo "== Transcript import/export =="
npx hyperframes transcribe captions.srt --dir "$PROJECT_DIR" --json | tee "$ARTIFACT_DIR/transcribe-import.json"
test -s "$PROJECT_DIR/transcript.json"
npx hyperframes transcribe "$PROJECT_DIR/transcript.json" --to srt --output "$PROJECT_DIR/roundtrip.srt" --json | tee "$ARTIFACT_DIR/transcribe-export.json"
test -s "$PROJECT_DIR/roundtrip.srt"
node - "$PROJECT_DIR/transcript.json" <<'NODE'
const fs=require('fs');
const t=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const words=Array.isArray(t)?t:(t.words||t.segments||[]);
const flat=words.flatMap(x=>Array.isArray(x.words)?x.words:[x]).filter(Boolean);
if(flat.length < 2) throw new Error('expected transcript words');
const ids=flat.map(x=>x.id).filter(Boolean);
if(ids.length && !ids.every((id,i)=>id===`w${i}`)) throw new Error('unstable generated word ids: '+ids.join(','));
NODE

echo "== HyperFrames current lint/check gates =="
npx hyperframes lint --json | tee "$ARTIFACT_DIR/lint.json"
npx hyperframes check --json | tee "$ARTIFACT_DIR/check.json"

echo "== Prove deprecated validate remains compatibility-only =="
set +e
npx hyperframes validate --json > "$ARTIFACT_DIR/validate-compat.json" 2> "$ARTIFACT_DIR/validate-compat.stderr"
VALIDATE_RC=$?
set -e
echo "validate_rc=$VALIDATE_RC"
grep -qi "deprecated" "$ARTIFACT_DIR/validate-compat.stderr" || grep -qi '"deprecated"' "$ARTIFACT_DIR/validate-compat.json"

echo "== Studio preview smoke =="
npx hyperframes preview --background --no-open | tee "$ARTIFACT_DIR/preview-start.log"
npx hyperframes preview --status | tee "$ARTIFACT_DIR/preview-status.log"
npx hyperframes preview --context --context-fields server,lint,capabilities --json | tee "$ARTIFACT_DIR/preview-context.json"
npx hyperframes preview --stop | tee "$ARTIFACT_DIR/preview-stop.log"

echo "== Draft and looks render =="
npx hyperframes render --quality draft --fps 30 --output "$PROJECT_DIR/draft.mp4" | tee "$ARTIFACT_DIR/render-draft.log"
test -s "$PROJECT_DIR/draft.mp4"
npx hyperframes render --quality looks --fps 30 --output "$PROJECT_DIR/looks.mp4" | tee "$ARTIFACT_DIR/render-looks.log"
test -s "$PROJECT_DIR/looks.mp4"

echo "== A/V and duration assertions =="
ffprobe -v error -of json -show_format -show_streams "$PROJECT_DIR/looks.mp4" > "$ARTIFACT_DIR/ffprobe.json"
node - "$ARTIFACT_DIR/ffprobe.json" <<'NODE'
const fs=require('fs');
const d=JSON.parse(fs.readFileSync(process.argv[2],'utf8'));
const streams=d.streams||[];
if(!streams.some(s=>s.codec_type==='video')) throw new Error('render missing video stream');
if(!streams.some(s=>s.codec_type==='audio')) throw new Error('render missing audio stream');
const dur=Number(d.format?.duration);
if(!Number.isFinite(dur) || Math.abs(dur-6)>0.20) throw new Error('unexpected render duration '+dur);
const a=streams.find(s=>s.codec_type==='audio');
const v=streams.find(s=>s.codec_type==='video');
const ad=Number(a?.duration ?? dur);
const vd=Number(v?.duration ?? dur);
if(Number.isFinite(ad)&&Number.isFinite(vd)&&Math.abs(ad-vd)>0.20) throw new Error(`A/V duration drift too high: audio=${ad} video=${vd}`);
NODE

echo "== Extract representative visual frames =="
for t in 0.5 2.5 3.5 5.5; do
  ffmpeg -hide_banner -loglevel error -y -ss "$t" -i "$PROJECT_DIR/looks.mp4" -frames:v 1 "$PROJECT_DIR/frames/frame-${t}.png"
done
ffmpeg -hide_banner -loglevel error -y \
  -i "$PROJECT_DIR/looks.mp4" \
  -vf "fps=1,scale=480:-1,tile=3x2" -frames:v 1 "$PROJECT_DIR/frames/contact-sheet.png"
test -s "$PROJECT_DIR/frames/contact-sheet.png"

echo "== Basic nonblank-frame assertions =="
python3 - "$PROJECT_DIR/frames" <<'PY'
from pathlib import Path
from PIL import Image, ImageStat
import sys
root=Path(sys.argv[1])
frames=sorted(root.glob("frame-*.png"))
assert len(frames)==4, frames
for p in frames:
    im=Image.open(p).convert("RGB")
    stat=ImageStat.Stat(im)
    extrema=im.getextrema()
    dynamic=max(hi-lo for lo,hi in extrema)
    assert dynamic > 20, f"{p.name}: suspiciously blank/flat frame dynamic={dynamic}"
print("frames_ok", [p.name for p in frames])
PY

echo "== Preserve artifacts =="
cp "$PROJECT_DIR/draft.mp4" "$ARTIFACT_DIR/draft.mp4"
cp "$PROJECT_DIR/looks.mp4" "$ARTIFACT_DIR/looks.mp4"
cp "$PROJECT_DIR/transcript.json" "$ARTIFACT_DIR/transcript.json"
cp "$PROJECT_DIR/roundtrip.srt" "$ARTIFACT_DIR/roundtrip.srt"
cp -R "$PROJECT_DIR/frames" "$ARTIFACT_DIR/frames"

cat > "$ARTIFACT_DIR/result.json" <<JSON
{
  "nate_ref": "$NATE_REF",
  "nate_baseline_hyperframes": "$BASELINE_VERSION",
  "candidate_hyperframes": "$CANDIDATE_ACTUAL",
  "status": "pass",
  "checks": [
    "nate-baseline-tests",
    "nate-skill-mirror-check",
    "nate-baseline-kit-check",
    "nate-tests-on-candidate",
    "candidate-browser-doctor",
    "transcript-import-export",
    "lint",
    "check",
    "validate-deprecation-signal",
    "studio-preview-context",
    "draft-render",
    "looks-render",
    "video-stream-present",
    "audio-stream-present",
    "duration",
    "audio-video-duration-sync",
    "representative-frames-nonblank"
  ]
}
JSON

echo "ACCEPTANCE PASS"
