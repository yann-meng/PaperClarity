# PaperClarity

PaperClarity 是一个以 skills 为核心扩展单元的本地论文理解工作台，而不是一个带聊天框的 PDF 阅读器。

## MVP 已实现
- 本地 PDF 上传与解析（PyMuPDF）
- 统一文档模型（DocumentModel / Block / SkillContext）
- 技能系统（BaseSkill + 自动扫描注册）
- 6 个基础 skills：
  - `paper_overview`
  - `paragraph_close_reading`
  - `equation_breakdown`
  - `intuition_translation`
  - `experiment_analysis`
  - `reproduction_guide`
- 统一 LLM 网关（OpenAI 兼容接口）
- AI 输出保存为笔记（SQLite）
- 笔记 Markdown 导出
- React + TypeScript 双栏工作台（阅读区 / AI 工作区）

## 快速启动
```bash
pip install -r requirements.txt
uvicorn paperclarity.app.backend.main:app --reload
```

前端可接入任意 React 工程（当前仓库提供 MVP 组件与页面代码于 `paperclarity/app/frontend/src`）。

## 目录
```text
paperclarity/
  app/
    backend/
    frontend/
  data/
  tests/
  docs/
```
