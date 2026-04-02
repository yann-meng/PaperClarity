import React from "react";
import { Block } from "../types";

type Props = {
  blocks: Block[];
  selectedBlockIds: string[];
  onToggleBlock: (id: string) => void;
};

export const PDFReaderPane: React.FC<Props> = ({ blocks, selectedBlockIds, onToggleBlock }) => {
  return (
    <div style={{ width: "55%", borderRight: "1px solid #ddd", padding: 12, height: "100vh", overflow: "auto" }}>
      <h3>论文阅读区（MVP 文本块视图）</h3>
      {blocks.map((block) => {
        const selected = selectedBlockIds.includes(block.id);
        return (
          <div
            key={block.id}
            onClick={() => onToggleBlock(block.id)}
            style={{
              marginBottom: 10,
              padding: 8,
              cursor: "pointer",
              border: selected ? "2px solid #3b82f6" : "1px solid #ccc",
              background: selected ? "#eff6ff" : "white",
            }}
          >
            <small>
              p{block.page} · {block.id}
            </small>
            <p>{block.text}</p>
          </div>
        );
      })}
    </div>
  );
};
