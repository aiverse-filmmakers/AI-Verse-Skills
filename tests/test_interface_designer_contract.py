import json
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class InterfaceDesignerContractTests(unittest.TestCase):
    def test_orchestrator_is_registered_and_stack_neutral(self):
        skills = json.loads((ROOT / "registry/skills.json").read_text(encoding="utf-8"))
        packages = json.loads((ROOT / "registry/packages.json").read_text(encoding="utf-8"))
        ids = {item["id"] for item in skills["employee"]}
        self.assertIn("interface-designer", ids)

        source = packages["sources"]["ai-verse"]
        pkg = next(item for item in source["packages"] if item["id"] == "interface-designer")
        self.assertTrue(pkg["vendored"])

        text = (ROOT / "skills/imported/ai-verse/interface-designer/SKILL.md").read_text(encoding="utf-8")
        for marker in (
            "PLAIN_HTML_CSS_JS_ARTIFACT",
            "REACT_WEB_APP",
            "NATIVE_DESKTOP_APP",
            "CODE_DRIVEN_VIDEO_MOTION_HANDOFF",
            "Never migrate a plain HTML/CSS/JavaScript artifact to React",
            "Never require Vercel hosting",
        ):
            self.assertIn(marker, text)

    def test_scope_classifier_and_progressive_routing_are_explicit(self):
        text = (ROOT / "skills/imported/ai-verse/interface-designer/SKILL.md").read_text(encoding="utf-8")
        for scope in (
            "MICRO_CHANGE",
            "COMPONENT",
            "SCREEN",
            "FULL_PRODUCT",
            "REFERENCE_RECREATION",
            "INTERACTION_HEAVY",
            "SCROLL_IMMERSIVE",
            "MOBILE_EXPO",
        ):
            self.assertIn(scope, text)

        routing = (ROOT / "skills/imported/ai-verse/interface-designer/references/routing.md").read_text(encoding="utf-8")
        for capability in (
            "frontend-design",
            "ui-ux-pro-max",
            "prototype",
            "apple-design",
            "animate",
            "review-animations",
            "react-best-practices",
            "composition-patterns",
            "shadcn",
            "scroll-craft",
            "web-design-guidelines",
        ):
            self.assertIn(capability, routing)

        self.assertIn("Do not merge all expert bodies into this context.", text)


if __name__ == "__main__":
    unittest.main()
