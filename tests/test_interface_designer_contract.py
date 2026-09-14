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

    def test_design_md_persistence_contract_is_scoped_and_non_destructive(self):
        package = ROOT / "skills/imported/ai-verse/interface-designer/references"
        contract = (package / "design-md-contract.md").read_text(encoding="utf-8")
        template = (package / "DESIGN.template.md").read_text(encoding="utf-8")
        skill = (ROOT / "skills/imported/ai-verse/interface-designer/SKILL.md").read_text(encoding="utf-8")

        for marker in (
            "## Read Rule",
            "## Create Rule",
            "## Update Rule",
            "If a project-level `DESIGN.md` exists",
            "Do not create it for:",
            "preserve unrelated existing decisions",
            "Do not define mobile as",
            "## Accessibility Requirements",
            "## Forbidden Patterns",
        ):
            self.assertIn(marker, contract)

        self.assertIn("`DESIGN.md` contract", skill)
        self.assertIn("accepted reusable product grammar actually changed", skill)
        self.assertIn("# Responsive & Mobile Direction", template)
        self.assertIn("# Accessibility Requirements", template)
        self.assertIn("# Forbidden Patterns / Product-Specific Anti-Patterns", template)

        graph = json.loads(
            (ROOT / "skills/imported/ai-verse/interface-designer/references/orchestration.json")
            .read_text(encoding="utf-8")
        )
        self.assertNotIn(
            "design_system_persistence",
            graph["scope_pipelines"]["MICRO_CHANGE"],
        )
        self.assertIn(
            "design_system_persistence",
            graph["scope_pipelines"]["FULL_PRODUCT"],
        )
        self.assertIn(
            "design_system_persistence",
            graph["scope_pipelines"]["DESIGN_SYSTEM_CHANGE"],
        )

    def test_originality_gate_is_structural_scoped_and_private(self):
        package = ROOT / "skills/imported/ai-verse/interface-designer/references"
        policy = json.loads((package / "originality-policy.json").read_text(encoding="utf-8"))
        guide = (package / "originality.md").read_text(encoding="utf-8")
        graph = json.loads((package / "orchestration.json").read_text(encoding="utf-8"))

        self.assertEqual(len(policy["dimensions"]), 10)
        self.assertEqual(len(policy["structural_dimensions"]), 6)
        for dimension in (
            "information_architecture",
            "navigation_model",
            "layout_grammar",
            "interaction_model",
            "primary_composition",
            "signature_element",
        ):
            self.assertIn(dimension, policy["structural_dimensions"])

        self.assertIn("micro_change", policy["bypass_when"])
        self.assertIn("exact_reference_recreation", policy["bypass_when"])
        self.assertIn("established_design_md_consistency", policy["bypass_when"])
        self.assertIn("other_member_private_design_history", policy["forbidden_comparison_scope"])
        self.assertIn("cross_member_private_fingerprint_registry", policy["forbidden_comparison_scope"])
        self.assertEqual(policy["reskin_review"]["structural_matches_threshold"], 5)
        self.assertEqual(policy["high_similarity_review"]["total_matches_threshold"], 8)

        self.assertNotIn("originality_gate", graph["scope_pipelines"]["MICRO_CHANGE"])
        self.assertIn("originality_gate", graph["scope_pipelines"]["FULL_PRODUCT"])
        self.assertIn("originality_gate", graph["scope_pipelines"]["DESIGN_SYSTEM_CHANGE"])
        self.assertIn("Do not create a shared cross-member fingerprint registry.", guide)

    def test_signature_interaction_is_experience_scoped_not_decorative_app_ceremony(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        policy = json.loads((refs / "signature-interaction-policy.json").read_text(encoding="utf-8"))
        guide = (refs / "signature-interaction.md").read_text(encoding="utf-8")
        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))

        self.assertIn("scroll_immersive", policy["required_when"])
        for app_type in ("dashboard", "admin_tool", "crud_application", "settings"):
            self.assertIn(app_type, policy["optional_functional_when"])
        self.assertIn("decorative_motion_only", policy["invalid_examples"])
        self.assertIn("standard_drawer_or_sheet", policy["invalid_examples"])
        self.assertEqual(
            policy["exact_reference_behavior"],
            "use_reference_signature_if_present_do_not_invent_competing_behavior",
        )

        self.assertNotIn("signature_interaction", graph["scope_pipelines"]["MICRO_CHANGE"])
        self.assertIn("signature_interaction", graph["scope_pipelines"]["FULL_PRODUCT"])
        self.assertIn("signature_interaction", graph["scope_pipelines"]["SCROLL_IMMERSIVE"])
        self.assertIn("A missing signature interaction must not fail a dashboard", guide)

    def test_experience_curve_only_applies_to_meaningful_multi_stage_flows(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        policy = json.loads((refs / "experience-curve-policy.json").read_text(encoding="utf-8"))
        guide = (refs / "experience-curve.md").read_text(encoding="utf-8")
        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))

        for use_case in ("onboarding", "major_agent_workflow", "launch_experience", "complex_wizard"):
            self.assertIn(use_case, policy["use_when"])
        for skipped in ("settings_page", "crud_form", "ordinary_table", "routine_dashboard_inspection", "micro_change"):
            self.assertIn(skipped, policy["skip_when"])
        for state in ("clarity", "confidence", "control", "readiness", "completion"):
            self.assertIn(state, policy["preferred_operational_states"])
        self.assertIn("compare_intended_vs_rendered", policy["review_rules"]["after_implementation"])

        self.assertNotIn("experience_curve", graph["scope_pipelines"]["MICRO_CHANGE"])
        self.assertNotIn("experience_curve", graph["scope_pipelines"]["SCREEN"])
        self.assertIn("experience_curve", graph["scope_pipelines"]["MULTI_SCREEN_FLOW"])
        self.assertIn("experience_curve", graph["scope_pipelines"]["SCROLL_IMMERSIVE"])
        self.assertIn("Do not create an experience curve for:", guide)

    def test_visual_qa_requires_rendered_evidence_and_truthful_blocked_states(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        policy = json.loads((refs / "visual-qa-policy.json").read_text(encoding="utf-8"))
        guide = (refs / "visual-qa.md").read_text(encoding="utf-8")
        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))

        self.assertTrue(policy["evidence_required_for_verified_result"])
        self.assertFalse(policy["source_inspection_is_visual_evidence"])
        for result in ("VERIFIED_PASS", "VERIFIED_FAIL", "NOT_APPLICABLE", "UNVERIFIED_BLOCKED"):
            self.assertIn(result, policy["result_states"])
        for state in ("loading", "empty", "populated", "error"):
            self.assertIn(state, policy["state_groups"]["data_async"])
        for state in ("hover", "focus_visible", "disabled"):
            self.assertIn(state, policy["state_groups"]["control"])
        self.assertIn("reduced_motion", policy["state_groups"]["theme_preference"])
        self.assertEqual(policy["state_groups"]["viewport"], ["desktop", "tablet", "mobile"])

        stage = next(s for s in graph["stages"] if s["id"] == "visual_state_qa")
        self.assertEqual(stage["policy"], "references/visual-qa-policy.json")
        self.assertTrue(stage["evidence_required"])
        self.assertIn("UNVERIFIED_BLOCKED", guide)
        self.assertIn("Source inspection alone does not prove visual appearance.", guide)

    def test_scroll_qa_is_semantic_conditional_and_reduced_motion_complete(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        policy = json.loads((refs / "scroll-qa-policy.json").read_text(encoding="utf-8"))
        guide = (refs / "scroll-qa.md").read_text(encoding="utf-8")
        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))

        self.assertIn("scroll_immersive", policy["run_when"])
        self.assertIn("ordinary_dashboard", policy["skip_when"])
        self.assertTrue(policy["fixed_percentage_samples_are_fallback_only"])
        self.assertIn("every_semantic_transition_or_waypoint", policy["sample"])
        self.assertIn("no_unexplained_dead_scroll", policy["checks"])
        self.assertIn("reduced_motion_complete", policy["checks"])
        self.assertIn("content_left_hidden", policy["reduced_motion_failures"])

        self.assertIn("scroll_state_qa", graph["scope_pipelines"]["SCROLL_IMMERSIVE"])
        self.assertNotIn("scroll_state_qa", graph["scope_pipelines"]["SCREEN"])
        stage = next(s for s in graph["stages"] if s["id"] == "scroll_state_qa")
        self.assertTrue(stage["evidence_required"])
        self.assertIn("Do not install or force Scroll Craft infrastructure merely to test an ordinary site.", guide)

    def test_mobile_art_direction_requires_intentional_mobile_not_shrunk_desktop(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        policy = json.loads((refs / "mobile-art-direction-policy.json").read_text(encoding="utf-8"))
        guide = (refs / "mobile-art-direction.md").read_text(encoding="utf-8")
        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))

        self.assertEqual(
            policy["result_if_desktop_only"],
            "NOT_APPLICABLE_with_product_constraint",
        )
        self.assertEqual(policy["result_if_cannot_render"], "UNVERIFIED_BLOCKED")
        for check in (
            "information_hierarchy",
            "navigation",
            "touch_and_direct_manipulation",
            "media_crop_layering",
            "safe_areas_and_device_chrome",
            "reduced_motion",
        ):
            self.assertIn(check, policy["checks"])
        self.assertIn("target_platform_or_accessibility_minimums", policy["touch_rule"])
        self.assertIn("hover_only_actions_require_touch_path", policy["hover_rule"])
        self.assertEqual(policy["design_md_section"], "Responsive & Mobile Direction")
        self.assertTrue(policy["evidence_required"])

        self.assertNotIn("mobile_art_direction_qa", graph["scope_pipelines"]["MICRO_CHANGE"])
        self.assertIn("mobile_art_direction_qa", graph["scope_pipelines"]["FULL_PRODUCT"])
        self.assertIn("mobile_art_direction_qa", graph["scope_pipelines"]["MOBILE_EXPO"])
        stage = next(s for s in graph["stages"] if s["id"] == "mobile_art_direction_qa")
        self.assertTrue(stage["evidence_required"])
        self.assertIn("not complete merely because desktop CSS fits inside a smaller viewport", guide)

    def test_required_routing_fixtures_resolve_to_valid_scopes_targets_and_experts(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))
        fixture_doc = json.loads((refs / "routing-fixtures.json").read_text(encoding="utf-8"))
        skills = json.loads((ROOT / "registry/skills.json").read_text(encoding="utf-8"))
        registered = {item["id"] for item in skills["employee"]}
        stage_ids = {stage["id"] for stage in graph["stages"]}
        expected_ids = {
            "tiny-padding-change",
            "dashboard-from-scratch",
            "recreate-screenshot",
            "draggable-floating-panel",
            "react-refactor",
            "cinematic-scroll-landing",
            "expo-sheet-interaction",
            "finished-ui-review",
        }
        fixtures = {item["id"]: item for item in fixture_doc["fixtures"]}
        self.assertEqual(set(fixtures), expected_ids)

        for fixture in fixtures.values():
            self.assertIn(fixture["scope"], graph["scopes"])
            self.assertIn(fixture["target"], graph["targets"])
            scope_pipeline = graph["scope_pipelines"][fixture["scope"]]
            for stage in fixture.get("expected_stages", []):
                self.assertIn(stage, stage_ids)
                self.assertIn(stage, scope_pipeline)
            for stage in fixture.get("forbidden_stages", []):
                self.assertNotIn(stage, fixture.get("expected_stages", []))
            for expert in fixture.get("expected_experts", []):
                self.assertIn(expert, registered)
            for expert in fixture.get("forbidden_experts", []):
                self.assertNotIn(expert, fixture.get("expected_experts", []))

        micro = fixtures["tiny-padding-change"]
        self.assertEqual(micro["expected_experts"], [])
        self.assertEqual(micro["scope"], "MICRO_CHANGE")
        self.assertEqual(micro["target"], "EXISTING_WEB_STACK")

        dashboard = fixtures["dashboard-from-scratch"]
        self.assertEqual(
            graph["target_experts"][dashboard["target"]],
            ["react-best-practices", "composition-patterns"],
        )

        scroll = fixtures["cinematic-scroll-landing"]
        self.assertIn("scroll-craft", scroll["expected_experts"])
        self.assertIn("scroll_state_qa", scroll["expected_stages"])

        expo = fixtures["expo-sheet-interaction"]
        self.assertEqual(graph["target_experts"][expo["target"]], ["animate-expo"])
        self.assertIn("apple-design", expo["expected_experts"])

    def test_context_loading_is_progressive_and_vendor_bodies_remain_separate(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))
        fixtures = json.loads((refs / "routing-fixtures.json").read_text(encoding="utf-8"))["fixtures"]
        packages = json.loads((ROOT / "registry/packages.json").read_text(encoding="utf-8"))
        skills = json.loads((ROOT / "registry/skills.json").read_text(encoding="utf-8"))
        registered = {item["id"] for item in skills["employee"]}

        by_id = {item["id"]: item for item in fixtures}
        micro = by_id["tiny-padding-change"]
        self.assertEqual(micro["expected_experts"], [])
        self.assertLessEqual(len(graph["scope_pipelines"]["MICRO_CHANGE"]), 5)
        for forbidden in (
            "frontend-design",
            "ui-ux-pro-max",
            "prototype",
            "scroll-craft",
            "react-best-practices",
            "composition-patterns",
        ):
            self.assertIn(forbidden, micro["forbidden_experts"])

        # A full-product route can resolve every stage-owned and target-owned expert
        # without embedding those expert bodies into the orchestrator.
        stage_by_id = {stage["id"]: stage for stage in graph["stages"]}
        full_required = set(graph["target_experts"]["REACT_WEB_APP"])
        for stage_id in graph["scope_pipelines"]["FULL_PRODUCT"]:
            full_required.update(stage_by_id[stage_id].get("capabilities", []))
        self.assertTrue(full_required)
        self.assertTrue(full_required.issubset(registered))

        conditional = {
            spec["capability"] for spec in graph["conditional_experts"].values()
        }
        pipeline_stage_capabilities = set()
        for stage in graph["stages"]:
            pipeline_stage_capabilities.update(stage.get("capabilities", []))
        self.assertTrue(conditional.isdisjoint(pipeline_stage_capabilities))
        self.assertNotIn("scroll-craft", graph["scope_pipelines"]["FULL_PRODUCT"])
        self.assertNotIn("shadcn", graph["scope_pipelines"]["FULL_PRODUCT"])

        ai_source = packages["sources"]["ai-verse"]
        interface_pkg = next(pkg for pkg in ai_source["packages"] if pkg["id"] == "interface-designer")
        self.assertEqual(interface_pkg["path"], "skills/imported/ai-verse/interface-designer")

        expert_sources = {
            "anthropic-frontend",
            "nextlevelbuilder-ui",
            "vercel-design",
            "shadcn-ui",
            "mengto-ui",
            "emil-design",
            "scroll-craft",
        }
        self.assertTrue(expert_sources.issubset(packages["sources"]))
        for source_id in expert_sources:
            self.assertNotEqual(packages["sources"][source_id]["namespace"], "ai-verse")

        orchestrator_root = ROOT / interface_pkg["path"]
        nested_dirs = {p.name for p in orchestrator_root.iterdir() if p.is_dir()}
        self.assertEqual(nested_dirs, {"references"})

    def test_expert_preservation_manifest_matches_pins_trust_and_local_adaptations(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        manifest = json.loads((refs / "expert-preservation.json").read_text(encoding="utf-8"))
        packages = json.loads((ROOT / "registry/packages.json").read_text(encoding="utf-8"))
        trust = json.loads((ROOT / "registry/trust-policy.json").read_text(encoding="utf-8"))
        skills = json.loads((ROOT / "registry/skills.json").read_text(encoding="utf-8"))
        notices = (ROOT / "THIRD_PARTY_NOTICES.md").read_text(encoding="utf-8")
        registered = {item["id"] for item in skills["employee"]}

        self.assertEqual(len(manifest["sources"]), 7)
        for source in manifest["sources"]:
            registry_source = packages["sources"][source["source_id"]]
            self.assertEqual(registry_source["repo"], source["repo"])
            self.assertEqual(registry_source["commit"], source["commit"])
            self.assertRegex(source["commit"], r"^[0-9a-f]{40}$")
            self.assertEqual(registry_source["license"], source["license"])
            self.assertEqual(registry_source["redistribution"], source["redistribution"])

            trust_entry = trust["sources"][source["repo"]]
            self.assertEqual(trust_entry["redistribution"], source["redistribution"])
            self.assertFalse(trust_entry["auto_mutation"])
            self.assertIn(source["repo"], notices)

            registry_packages = {pkg["id"]: pkg for pkg in registry_source["packages"]}
            for package in source["packages"]:
                self.assertIn(package["id"], registered)
                self.assertIn(package["id"], registry_packages)
                self.assertEqual(registry_packages[package["id"]]["path"], package["path"])
                self.assertTrue(package["expected_files"])
                self.assertTrue(package["core_markers"])

                if "local_path" in package:
                    local_root = ROOT / package["local_path"]
                    for relative in package["expected_files"]:
                        self.assertTrue((local_root / relative).exists(), relative)
                    local_skill = (local_root / "SKILL.md").read_text(encoding="utf-8")
                    for marker in package["core_markers"]:
                        self.assertIn(marker, local_skill)
                    source_meta = json.loads((local_root / "SOURCE.json").read_text(encoding="utf-8"))
                    self.assertEqual(source_meta["upstream_repo"], source["repo"])
                    self.assertEqual(source_meta["upstream_commit"], source["commit"])
                    self.assertEqual(
                        source_meta["adaptation"]["guideline_commit"],
                        package["adaptation_commit"],
                    )

        anthropic = next(s for s in manifest["sources"] if s["source_id"] == "anthropic-frontend")
        self.assertEqual(anthropic["redistribution"], "fetch-only")
        self.assertFalse(trust["sources"][anthropic["repo"]]["vendoring_allowed"])

    def test_existing_design_capabilities_remain_compatible_with_zero_removals(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        compatibility = json.loads((refs / "existing-design-compatibility.json").read_text(encoding="utf-8"))
        skills = json.loads((ROOT / "registry/skills.json").read_text(encoding="utf-8"))
        packages = json.loads((ROOT / "registry/packages.json").read_text(encoding="utf-8"))
        registered = {item["id"] for item in skills["employee"]}
        package_ids = {
            pkg["id"]
            for source in packages["sources"].values()
            for pkg in source["packages"]
        }

        self.assertEqual(compatibility["conclusion"], "zero-destructive-removals")
        self.assertEqual(compatibility["removed_capabilities"], [])
        self.assertEqual(compatibility["replacement_aliases"], [])

        expected_preserved = {
            "brand-guidelines",
            "canvas-design",
            "theme-factory",
            "figma-use",
            "figma-generate-design",
            "canva",
            "design-and-templates",
            "baoyu-article-illustrator",
        }
        recorded = {item["id"] for item in compatibility["preserved_capabilities"]}
        self.assertEqual(recorded, expected_preserved)
        self.assertTrue(expected_preserved.issubset(registered))
        self.assertTrue(expected_preserved.issubset(package_ids))

        graph = json.loads((refs / "orchestration.json").read_text(encoding="utf-8"))
        self.assertEqual(
            graph["target_experts"]["FIGMA"],
            ["figma-use", "figma-generate-design"],
        )
        self.assertEqual(
            graph["target_experts"]["CANVA_OR_STATIC_DESIGN_TOOL"],
            ["canva"],
        )

    def test_design_experts_cannot_bypass_admission_integrity_authority_or_workspace_scope(self):
        refs = ROOT / "skills/imported/ai-verse/interface-designer/references"
        boundary = json.loads((refs / "security-boundaries.json").read_text(encoding="utf-8"))
        preservation = json.loads((refs / "expert-preservation.json").read_text(encoding="utf-8"))
        originality = json.loads((refs / "originality-policy.json").read_text(encoding="utf-8"))
        packages = json.loads((ROOT / "registry/packages.json").read_text(encoding="utf-8"))
        trust = json.loads((ROOT / "registry/trust-policy.json").read_text(encoding="utf-8"))
        admission = (ROOT / "installer/admission.py").read_text(encoding="utf-8")
        lifecycle = (ROOT / "installer/generation_lifecycle.py").read_text(encoding="utf-8")

        for marker in (
            "Admission is deliberately separate from integrity",
            "Unknown sources are never implicitly trusted",
            "security = scan_package",
            "integrity = _package_integrity",
            "\"authorized\": False",
            "host/user execution authority, never granted by Skills admission",
        ):
            self.assertIn(marker, admission)
        self.assertIn("never mutated after commit", lifecycle)
        self.assertIn("single atomic pointer replacement", lifecycle)

        forbidden_fields = set(boundary["forbidden_package_override_fields"])
        for source in preservation["sources"]:
            trust_entry = trust["sources"][source["repo"]]
            self.assertFalse(trust_entry["auto_mutation"])
            registry_source = packages["sources"][source["source_id"]]
            for package in registry_source["packages"]:
                self.assertTrue(forbidden_fields.isdisjoint(package.keys()))

        self.assertIn(
            "other_member_private_design_history",
            originality["forbidden_comparison_scope"],
        )
        self.assertIn(
            "cross_member_private_fingerprint_registry",
            originality["forbidden_comparison_scope"],
        )

        orchestrator = next(
            pkg
            for pkg in packages["sources"]["ai-verse"]["packages"]
            if pkg["id"] == "interface-designer"
        )
        self.assertTrue(forbidden_fields.isdisjoint(orchestrator.keys()))

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
