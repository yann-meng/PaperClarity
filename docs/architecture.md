# PaperClarity MVP Architecture

## Core idea
PaperClarity is a local-first paper understanding workbench where all analysis features are implemented as pluggable **skills**.

## Backend
- FastAPI API service (`paperclarity/app/backend/main.py`)
- Skill abstraction: `BaseSkill`
- Skill discovery and registration: `SkillRegistry`
- Unified model gateway: `LLMGateway`
- PDF parsing with PyMuPDF into `DocumentModel`
- SQLite storage for documents and notes
- Markdown export for analysis notes

## Frontend
- React + TypeScript workbench page
- Left pane: selectable paper blocks
- Right pane: skill picker + structured output view
- Supports PDF upload and skill execution

## Data model
- `DocumentModel`: metadata, sections, blocks, equations, figures, tables
- `Block`: id/page/section/type/text/bbox/order
- `SkillContext`: document context + selected targets
