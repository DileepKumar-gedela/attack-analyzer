import { useState, useRef } from "react";
import axios from "axios";
import html2canvas from "html2canvas";
import jsPDF from "jspdf";

import {
  PieChart, Pie, Cell,
  BarChart, Bar, XAxis, YAxis, Tooltip,
  LineChart, Line, CartesianGrid
} from "recharts";

import "./App.css";

const COLORS = [
  "#ff7f0e","#1f77b4","#2ca02c",
  "#d62728","#9467bd","#8c564b"
];

// Order used for matrix visualization
const MITRE_ORDER = [
  "Initial Access",
  "Execution",
  "Persistence",
  "Privilege Escalation",
  "Defense Evasion",
  "Credential Access",
  "Lateral Movement",
  "Collection",
  "Exfiltration"
];

function App() {

  const [file, setFile] = useState(null);
  const [data, setData] = useState(null);
  const [loading, setLoading] = useState(false);

  const reportRef = useRef();

  // ---------- Upload ----------
  const upload = async () => {
    if (!file) return alert("Select file");

    setLoading(true);

    const form = new FormData();
    form.append("file", file);

    const res = await axios.post(
      "http://127.0.0.1:8010/upload",
      form
    );

    setData(res.data);
    setLoading(false);
  };

  // ---------- PDF Export ----------
  const exportPDF = async () => {
    const canvas = await html2canvas(reportRef.current);
    const img = canvas.toDataURL("image/png");

    const pdf = new jsPDF("p","mm","a4");

    const width = pdf.internal.pageSize.getWidth();
    const height = (canvas.height * width) / canvas.width;

    pdf.addImage(img,"PNG",0,0,width,height);
    pdf.save("cyber_report.pdf");
  };

  // ---------- Data transforms ----------
  const tacticData = data
    ? Object.entries(data.analysis.tactics)
        .map(([k,v]) => ({ name:k, value:v }))
    : [];

  const techniqueData = data
    ? data.analysis.techniques.map(t => ({
        name: t.name,
        value: t.confidence
      }))
    : [];

  const trendData = data
    ? data.analysis.trend.map(t => ({
        year: t.year,
        value: t.value
      }))
    : [];

  const heatmapData = data
    ? Object.entries(data.analysis.semantic_scores)
        .map(([k,v]) => ({ tactic:k, score:v }))
    : [];

  const matrixData = MITRE_ORDER.map(t => ({
    tactic: t,
    score: data?.analysis?.semantic_scores[t] || 0
  }));

  return (
    <div className="container">

      <h1>Cyber Attack Analyzer</h1>

      {/* Upload */}
      <div className="section">
        <input
          type="file"
          onChange={e => setFile(e.target.files[0])}
        />

        <button onClick={upload}>
          {loading ? "Analyzing..." : "Analyze"}
        </button>

        {data && (
          <button onClick={exportPDF}>
            Export PDF Report
          </button>
        )}
      </div>

      {data && (
        <div ref={reportRef}>

          {/* Preview */}
          <div className="section">
            <h2>Preview</h2>
            <p>{data.preview}</p>
          </div>

          {/* Charts */}
          <div className="grid">

            <div className="section">
              <h2>Tactic Distribution</h2>
              <PieChart width={350} height={260}>
                <Pie
                  data={tacticData}
                  dataKey="value"
                  nameKey="name"
                  outerRadius={90}
                  label
                >
                  {tacticData.map((_,i)=>
                    <Cell key={i}
                      fill={COLORS[i % COLORS.length]}/>
                  )}
                </Pie>
                <Tooltip/>
              </PieChart>
            </div>

            <div className="section">
              <h2>Technique Confidence</h2>
              <BarChart width={350}
                        height={260}
                        data={techniqueData}>
                <XAxis dataKey="name"/>
                <YAxis/>
                <Tooltip/>
                <Bar dataKey="value"
                     fill="#ff7f0e"/>
              </BarChart>
            </div>

          </div>

          {/* Trend */}
          <div className="section">
            <h2>Trend</h2>
            <LineChart width={700}
                       height={300}
                       data={trendData}>
              <CartesianGrid strokeDasharray="3 3"/>
              <XAxis dataKey="year"/>
              <YAxis/>
              <Tooltip/>
              <Line type="monotone"
                    dataKey="value"
                    stroke="#ff7f0e"/>
            </LineChart>
          </div>

          {/* Semantic Heatmap */}
          <div className="section">
            <h2>Semantic Heatmap</h2>
            <div className="heatmap">
              {heatmapData.map((t,i)=>(
                <div key={i}
                     className="heatcell"
                     style={{
                       backgroundColor:
                       `rgba(255,80,0,${t.score})`
                     }}>
                  <strong>{t.tactic}</strong>
                  <div>{t.score.toFixed(2)}</div>
                </div>
              ))}
            </div>
          </div>

          {/* ⭐ MITRE Matrix */}
          <div className="section">
            <h2>MITRE ATT&CK Matrix View</h2>

            <div className="matrix">
              {matrixData.map((cell,i)=>(
                <div key={i}
                     className="matrixCell"
                     style={{
                       backgroundColor:
                       `rgba(255,0,0,${cell.score})`
                     }}>
                  {cell.tactic}
                  <br/>
                  {cell.score.toFixed(2)}
                </div>
              ))}
            </div>
          </div>

          {/* Mitigations */}
          <div className="section">
            <h2>Mitigations</h2>
            <ul>
              {data.analysis.mitigations.map((m,i)=>
                <li key={i}>{m}</li>
              )}
            </ul>
          </div>

        </div>
      )}

    </div>
  );
}

export default App;
