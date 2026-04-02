import React from "react";
import { SkillInfo } from "../types";

type Props = {
  skills: SkillInfo[];
  selectedSkill: string;
  onSelectSkill: (skill: string) => void;
  onRun: () => void;
  output: unknown;
  userInput: string;
  onUserInputChange: (v: string) => void;
};

export const AIWorkspacePane: React.FC<Props> = ({
  skills,
  selectedSkill,
  onSelectSkill,
  onRun,
  output,
  userInput,
  onUserInputChange,
}) => {
  return (
    <div style={{ width: "45%", padding: 12, height: "100vh", overflow: "auto" }}>
      <h3>AI 工作区</h3>
      <label>选择 Skill</label>
      <select value={selectedSkill} onChange={(e) => onSelectSkill(e.target.value)} style={{ width: "100%" }}>
        {skills.map((skill) => (
          <option key={skill.name} value={skill.name}>
            {skill.display_name} ({skill.name})
          </option>
        ))}
      </select>
      <textarea
        placeholder="补充说明（可选）"
        value={userInput}
        onChange={(e) => onUserInputChange(e.target.value)}
        style={{ width: "100%", minHeight: 80, marginTop: 10 }}
      />
      <button onClick={onRun} style={{ marginTop: 10 }}>
        运行 Skill
      </button>

      <h4>结构化输出</h4>
      <pre style={{ background: "#111", color: "#f5f5f5", padding: 12, borderRadius: 8 }}>
        {JSON.stringify(output, null, 2)}
      </pre>
    </div>
  );
};
