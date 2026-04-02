import { DocumentModel, SkillContext, SkillInfo } from "../types";

const API_BASE = "http://localhost:8000/api";

export async function fetchSkills(): Promise<SkillInfo[]> {
  const res = await fetch(`${API_BASE}/skills`);
  return res.json();
}

export async function uploadPdf(file: File): Promise<{ document_id: string }> {
  const form = new FormData();
  form.append("file", file);
  const res = await fetch(`${API_BASE}/documents/upload`, { method: "POST", body: form });
  return res.json();
}

export async function fetchDocument(documentId: string): Promise<DocumentModel> {
  const res = await fetch(`${API_BASE}/documents/${documentId}`);
  return res.json();
}

export async function runSkill(skillName: string, context: SkillContext, user_input = "") {
  const res = await fetch(`${API_BASE}/skills/${skillName}/run?user_input=${encodeURIComponent(user_input)}`, {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify(context),
  });
  return res.json();
}

export async function fetchNotes(documentId: string) {
  const res = await fetch(`${API_BASE}/documents/${documentId}/notes`);
  return res.json();
}
