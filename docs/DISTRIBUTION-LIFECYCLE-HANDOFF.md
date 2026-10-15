# Distribution Whole-Install Lifecycle Handoff

**Status:** OWNER BOUNDARY CONFIRMED  
**Skills owner:** `aiverse-filmmakers/AI-Verse-Skills`  
**Whole-install orchestrator:** `aiverse-filmmakers/ai-verse-distribution`

This document records the Safe Infrastructure closeout boundary. It changes no Skills runtime behavior, package ownership or lifecycle semantics.

## AI-Verse-Skills remains authoritative for

AI-Verse-Skills continues to own:

- managed reusable task/professional capability packages;
- immutable Skills generations and their package contents;
- active-generation selection inside the Skills component;
- Skills install/update/rollback/disable/uninstall behavior;
- retained rollback/uninstall state defined by the Skills lifecycle;
- Skills component status/doctor truth;
- release descriptors and owner-native qualification;
- Skills-local adapters and package compatibility contracts.

Distribution does not become a second Skills package manager or managed-generation owner.

## Distribution owns only the whole-install layer

For an installed AI-Verse product, Distribution owns:

- compatible release-set selection and exact admitted software transitions;
- whole-install update orchestration;
- aggregate whole-install doctor over owner-native health checks;
- collection/classification of owner-published structural state;
- explicit structural-upgrade orchestration;
- the rotating whole-install Last-Known-Good recovery point;
- whole-install restore preview/apply;
- supported runtime lifecycle adapters;
- cross-repository lifecycle qualification.

The member-facing lifecycle therefore routes through:

```text
aiverse update
aiverse update --plan
aiverse doctor
aiverse upgrade
aiverse upgrade --apply
aiverse restore
aiverse restore --apply
```

These commands do not transfer managed Skills generation semantics into Distribution.

## Provider and scope boundary

The OS capability resolver owns provider scope/resolution/placement. AI-Verse-Skills owns the managed distributed Skills provider lifecycle.

A wider personal reuse decision may route a capability to the user-owned local provider rather than to managed Skills. That provider change is not a hidden Skills mutation and does not make Distribution the capability-placement owner.

Distribution may orchestrate a whole-install transition that contains an owner-published Skills operation. It must treat that operation as opaque owner authority and verify the owner result rather than reconstructing the Skills mutation itself.

## Doctor boundary

Skills status/doctor remain owner-native evidence.

`aiverse doctor` is a Distribution aggregate. It may invoke Skills health and combine that result with other owners, but it must preserve Skills failure truth and must not turn an owner failure into an aggregate false PASS.

## Recovery boundary

Distribution's whole-install Last-Known-Good/restore contract does not replace Skills rollback and uninstall semantics.

Whole-install recovery records the exact software reconstruction and declared covered state needed to reproduce the qualified install. Skills-managed generation state is handled according to the canonical recovery coverage and owner lifecycle, not by inventing a second managed-Skills snapshot model.

## Qualification handoff

At Safe Infrastructure Slice 5.3 start, the frozen Skills ref is:

`d4a02888ba8d83c4a15ce1b538ffdafaaf83bee1`

Owner-native supporting evidence at that ref:

- Validate AI-Verse Skills `38298548847`: SUCCESS;
- Release Descriptor `38298549229`: SUCCESS.

Slice 5.3 changes documentation only in this repository. Final qualification must keep Skills owner-native CI green and Distribution's permanent Safe Infrastructure Regression/Convergence gates green.

## Maintenance rule

Future whole-install lifecycle changes belong in Distribution unless they require a real Skills semantic change. Future managed Skills lifecycle changes remain owner changes here and must be published through the existing owner descriptors/contracts before Distribution can orchestrate them.

No second Skills generation manager, Skills doctor, rollback engine or reusable-capability package owner may be created in Distribution.
