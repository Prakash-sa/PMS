import { useState } from "react";
import { api } from "../api/client";

export default function ProposalForm() {
  const [title, setTitle] = useState("");
  const [pestType, setPestType] = useState("weed");
  const [chemical, setChemical] = useState("");
  const [submitting, setSubmitting] = useState(false);

  async function submit() {
    try {
      setSubmitting(true);
      const payload = {
        title,
        pest_type: pestType,
        chemical,
        geometry: {
          type: "MultiPolygon",
          coordinates: [
            [
              [
                [-105, 39],
                [-105, 40],
                [-104, 40],
                [-104, 39],
                [-105, 39],
              ],
            ],
          ],
        },
      };
      await api.post("/proposals", payload);
      setTitle("");
      setChemical("");
      setPestType("weed");
      // Friendly confirmation
      window.alert(
        "Proposal submitted — it may take a few moments to appear on the map."
      );
    } catch (err: any) {
      console.error(err);
      window.alert("Submission failed: " + (err?.message || "unknown error"));
    } finally {
      setSubmitting(false);
    }
  }

  return (
    <div className="space-y-2">
      <div className="form-group">
        <label className="label">Title</label>
        <input
          className="input"
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Title"
        />
      </div>

      <div className="form-group">
        <label className="label">Pest type</label>
        <select
          className="input"
          value={pestType}
          onChange={(e) => setPestType(e.target.value)}
        >
          <option value="weed">Weed</option>
          <option value="insect">Insect</option>
          <option value="disease">Disease</option>
        </select>
      </div>

      <div className="form-group">
        <label className="label">Chemical</label>
        <input
          className="input"
          value={chemical}
          onChange={(e) => setChemical(e.target.value)}
          placeholder="Chemical"
        />
      </div>

      <div style={{ display: "flex", gap: 8, justifyContent: "flex-end" }}>
        <button
          className="btn btn-ghost"
          onClick={() => {
            setTitle("");
            setChemical("");
            setPestType("weed");
          }}
          disabled={submitting}
        >
          Reset
        </button>
        <button
          className="btn btn-primary"
          onClick={submit}
          disabled={submitting}
        >
          {submitting ? "Submitting…" : "Submit Proposal"}
        </button>
      </div>
    </div>
  );
}
