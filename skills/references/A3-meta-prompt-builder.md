# A3: Meta Prompt Builder

Generate a reusable prompt based on the style guide from A2.

## Instructions

Create a self-contained prompt with two phases:

### Phase 1: Context Gathering
Interview questions about:
- Product details and problem it solves
- Target audience specifics
- Available proof elements
- Comfort level with different selling styles
- Specific pain points and transformation promises

### Phase 2: Script Generation
Generate for each video archetype identified in the guide:
- 3 variations per archetype
- Follow exact structural patterns from analysis
- Include [HOOK], [SHOW], and [CTA] markers
- Provide delivery notes for each script

## Requirements for Generated Prompt

1. Self-contained and reusable
2. Embed the style guide as knowledge
3. Ask smart questions that surface best angles
4. Output scripts in consistent, actionable format
5. Include "Best Performer Prediction" at the end

## Output Format

Generate complete, copy-paste-ready prompt structured as:

```markdown
# [Creator Style] TikTok Script Generator

## Role
[Define the AI's role based on the style]

## Context
[Embed key elements from the style guide]

## Instructions

### PHASE 1: Context Gathering Interview
[List interview questions derived from the style]

### PHASE 2: Script Generation
[Define output requirements for each archetype]

## Constraints
[List style-specific constraints]

## Output Format
[Define script format matching the analyzed style]
```

## Input Format

```
Here's the style guide from Step A2:

[PASTE COMPLETE STYLE GUIDE HERE]
```
