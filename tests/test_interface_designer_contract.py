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


    def test_expert_catalog_is_exactly_pinned_and_preserves_vendor_identity(self):
        skills = json.loads((ROOT / "registry/skills.json").read_text(encoding="utf-8"))
        packages = json.loads((ROOT / "registry/packages.json").read_text(encoding="utf-8"))
        ids = {item["id"] for item in skills["employee"]}
        experts = {
            "frontend-design",
            "ui-ux-pro-max",
            "react-best-practices",
            "composition-patterns",
            "web-design-guidelines",
            "shadcn",
            "design-first-ui-prompting",
            "video-to-superprompt",
            "stitched-full-page-capture",
            "apple-design",
            "animate",
            "prototype",
            "review-animations",
            "pick-ui-library",
            "improve-animations",
            "find-animation-opportunities",
            "animate-expo",
            "scroll-craft",
        }
        self.assertTrue(experts.issubset(ids))
        self.assertEqual(skills["counts"]["employee"], 99)
        self.assertEqual(skills["counts"]["total"], 119)
        self.assertEqual(packages["counts"]["employee"], 99)
        self.assertEqual(packages["counts"]["canonical_total"], 119)

        expected_pins = {
            "anthropic-frontend": "34040c9c568585f6929bedeaad110ad08f079624",
            "nextlevelbuilder-ui": "7f69fed6a2717900085f1bc3b263721f8ba025e2",
            "vercel-design": "063bee94c3f4df8453406c830b0a7df0f2860278",
            "shadcn-ui": "2b3e6d4f8d9161fe5c19340dc383aade392012dd",
            "mengto-ui": "321c769739b823de5eb94eb3a52aa1974fe783a2",
            "emil-design": "d23d7f88a2e21c9e4b1418c7abe420f5c1052ba7",
            "scroll-craft": "0b816225945e45380397d6a0487efa3c98916858",
        }
        for source_id, commit in expected_pins.items():
            self.assertEqual(packages["sources"][source_id]["commit"], commit)

    def test_conditional_pipeline_graph_prevents_context_bloat(self):
        graph = json.loads(
            (ROOT / "skills/imported/ai-verse/interface-designer/references/orchestration.json")
            .read_text(encoding="utf-8")
        )
        self.assertIn("MICRO_CHANGE", graph["scope_pipelines"])
        self.assertNotIn("prototype_divergence", graph["scope_pipelines"]["MICRO_CHANGE"])
        self.assertNotIn("visual_direction", graph["scope_pipelines"]["MICRO_CHANGE"])
        self.assertIn("prototype_divergence", graph["scope_pipelines"]["FULL_PRODUCT"])
        self.assertEqual(
            graph["target_experts"]["REACT_WEB_APP"],
            ["react-best-practices", "composition-patterns"],
        )
        self.assertEqual(graph["target_experts"]["PLAIN_HTML_CSS_JS_ARTIFACT"], [])
        self.assertEqual(graph["target_experts"]["REACT_NATIVE_EXPO"], ["animate-expo"])
        self.assertEqual(
            graph["conditional_experts"]["scroll_craft"]["capability"],
            "scroll-craft",
        )
        self.assertIn(
            "Do not load all experts into one context.",
            graph["invariants"],
        )

    def test_vercel_review_rules_are_generation_pinned(self):
        package = ROOT / "skills/imported/vercel/web-design-guidelines"
        skill = (package / "SKILL.md").read_text(encoding="utf-8")
        rules = (package / "references/command.md").read_text(encoding="utf-8")
        source = json.loads((package / "SOURCE.json").read_text(encoding="utf-8"))

        self.assertIn("references/command.md", skill)
        self.assertNotIn("raw.githubusercontent.com/vercel-labs/web-interface-guidelines/main", skill)
        self.assertIn("## Rules", rules)
        self.assertTrue(source["modified"])
        self.assertEqual(
            source["adaptation"]["guideline_commit"],
            "e3d624baaf29dc1fc645aff3e38f03e564d2d6b1",
        )


if __name__ == "__main__":
    unittest.main()
