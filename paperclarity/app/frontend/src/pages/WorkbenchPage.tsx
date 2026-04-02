import React, { useEffect, useMemo, useState } from "react";
import { AIWorkspacePane } from "../components/AIWorkspacePane";
import { PDFReaderPane } from "../components/PDFReaderPane";
import { fetchDocument, fetchSkills, runSkill, uploadPdf } from "../services/api";
import { DocumentModel, SkillInfo } from "../types";

export const WorkbenchPage: React.FC = () => {
  const [skills, setSkills] = useState<SkillInfo[]>([]);
  const [selectedSkill, setSelectedSkill] = useState<string>("paper_overview");
  const [document, setDocument] = useState<DocumentModel | null>(null);
  const [selectedBlocks, setSelectedBlocks] = useState<string[]>([]);
  const [output, setOutput] = useState<unknown>(null);
  const [userInput, setUserInput] = useState("");

  useEffect(() => {
    fetchSkills().then((list) => {
      setSkills(list);
      if (list.length) setSelectedSkill(list[0].name);
    });
  }, []);

  const contextType = useMemo(() => (selectedBlocks.length ? "paragraph" : "paper"), [selectedBlocks]);

  const onUpload = async (file?: File) => {
    if (!file) return;
    const { document_id } = await uploadPdf(file);
    const parsed = await fetchDocument(document_id);
    setDocument(parsed);
  };

  const onRunSkill = async () => {
    if (!document) return;
    const result = await runSkill(selectedSkill, {
      document_id: document.id,
      context_type: contextType,
      selected_block_ids: selectedBlocks,
      extra_context: { source: "web-workbench" },
    }, userInput);
    setOutput(result);
  };

  const toggleBlock = (id: string) => {
    setSelectedBlocks((prev) => (prev.includes(id) ? prev.filter((v) => v !== id) : [...prev, id]));
  };

  return (
    <div style={{ display: "flex", fontFamily: "system-ui" }}>
      <PDFReaderPane blocks={document?.blocks ?? []} selectedBlockIds={selectedBlocks} onToggleBlock={toggleBlock} />
      <AIWorkspacePane
        skills={skills}
        selectedSkill={selectedSkill}
        onSelectSkill={setSelectedSkill}
        onRun={onRunSkill}
        output={output}
        userInput={userInput}
        onUserInputChange={setUserInput}
      />
      <input
        type="file"
        accept="application/pdf"
        style={{ position: "fixed", top: 10, right: 10 }}
        onChange={(e) => onUpload(e.target.files?.[0])}
      />
    </div>
  );
};
