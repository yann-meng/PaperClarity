export type SkillInfo = {
  name: string;
  display_name: string;
  description: string;
  supported_contexts: string[];
  output_schema: Record<string, unknown>;
};

export type SkillContext = {
  document_id: string;
  context_type: "paper" | "section" | "paragraph" | "equation";
  selected_block_ids: string[];
  selected_equation_id?: string;
  extra_context?: Record<string, unknown>;
};

export type Block = {
  id: string;
  page: number;
  section_id?: string;
  block_type: string;
  text: string;
  order: number;
};

export type DocumentModel = {
  id: string;
  metadata: Record<string, string>;
  sections: Array<{ id: string; title: string }>;
  blocks: Block[];
};
