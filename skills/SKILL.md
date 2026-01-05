---
name: tiktok-sales-prompt-flow
description: Complete prompt workflow system for creating high-converting TikTok sales video scripts. Use when users need to (1) Learn and replicate any TikTok creator's selling style, (2) Analyze products to find unique selling angles, (3) Generate scroll-stopping hooks, (4) Create full video scripts in multiple archetypes (Relatable Sufferer, Dramatic Transformer, Casual Discoverer). Triggers on requests for TikTok scripts, short-form video content, product promotion videos, or e-commerce video marketing.
---

# TikTok Sales Prompt Flow

A modular prompt system for generating high-converting TikTok sales video scripts.

## Quick Start

Three execution paths based on user needs:

| Path | When to Use | Steps |
|------|-------------|-------|
| **Full** | Learn specific creator's style | A1→A2→A3→B1→C1→C2→C3 |
| **Standard** | Use default archetypes | B1→C1→C2→C3 |
| **Quick** | Fast script generation | C3 only |

## Module Overview

### Module A: Style Learning (Optional)
Reverse-engineer any TikTok creator's selling style.
- **A1** `references/A1-style-deconstructor.md` - Analyze 1-3 scripts
- **A2** `references/A2-style-synthesizer.md` - Combine into style guide
- **A3** `references/A3-meta-prompt-builder.md` - Generate reusable prompt

### Module B: Product Analysis
- **B1** `references/B1-creative-product-partner.md` - Extract unique angles

### Module C: Content Generation
- **C1** `references/C1-deep-script-generator.md` - 5 script outlines
- **C2** `references/C2-hook-generator.md` - 30 scroll-stopping hooks
- **C3** `references/C3-final-script-generator.md` - 9 complete scripts

## Three Script Archetypes

| Archetype | Style | Length | Best For |
|-----------|-------|--------|----------|
| **Relatable Sufferer** | Pain→Discovery→Relief | 30-45s | Trust building, personal products |
| **Dramatic Transformer** | Proof→Results→Urgency | 15-30s | Visual transformations, fast results |
| **Casual Discoverer** | Share→Demo→Soft CTA | 20-40s | Viral potential, nice-to-have products |

## Execution Instructions

### Path 1: Full Flow (with style learning)
1. Read `references/A1-style-deconstructor.md`
2. Have user provide 2-3 scripts from creator they want to emulate
3. Analyze each script using A1 prompt
4. Read `references/A2-style-synthesizer.md`, synthesize analyses
5. Read `references/A3-meta-prompt-builder.md`, create custom prompt
6. Continue to B1→C1→C2→C3

### Path 2: Standard Flow
1. Read `references/B1-creative-product-partner.md`
2. Interview user about product (follow the 4 breakthrough drivers)
3. Output angle summary
4. Read `references/C1-deep-script-generator.md`, generate 5 outlines
5. Read `references/C2-hook-generator.md`, generate 30 hooks
6. Read `references/C3-final-script-generator.md`, generate 9 scripts

### Path 3: Quick Flow
1. Read `references/C3-final-script-generator.md`
2. Run Phase 1 interview (5-7 questions)
3. Generate 9 scripts directly

## Knowledge Base

Core psychological patterns are documented in `references/content-analysis-framework.md`. Reference when explaining why certain approaches work.

## Output Format

All scripts use this structure:
```
[HOOK]: First 1-3 seconds (scroll-stopper)
[PROBLEM]: Pain articulation
[TURN]: Transition to solution
[SOLUTION]: Product introduction
[SHOW: visual direction]
[PROOF]: Evidence/demonstration
[CTA]: Call-to-action
```

## Key Principles

1. **Native feel** - Scripts should feel like content, not ads
2. **Specificity** - Use exact numbers ("Day 7", "$23", "2 weeks")
3. **Second person** - Use "you" for immediate involvement
4. **Casual grammar** - Contractions, informal language
5. **One memorable moment** - Each script needs a standout element
