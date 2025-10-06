import MapView from "./components/MapView";
import ProposalForm from "./components/ProposalForm";

export default function App() {
  return (
    <div className="container">
      <header className="header">
        <div className="brand">
          <div className="logo">P</div>
          <div>
            <div className="title">PMS</div>
            <div className="subtitle">
              Pesticide Management System
            </div>
          </div>
        </div>
        <div className="pill">Maps • Proposals • Recommendations</div>
      </header>

      <main className="layout">
        <section className="card map-card">
          <div style={{ position: "relative", height: "100%" }}>
            <MapView className="map-inner" />
          </div>
        </section>

        <aside className="card form-card">
          <h3 style={{ margin: 0 }}>New Proposal</h3>
          <div className="meta">
            Submit site proposals and visualize them on the map. Fields are
            minimal for the prototype.
          </div>
          <ProposalForm />
        </aside>
      </main>

      <div className="footer">
        © 2022 PMS. All rights reserved.
      </div>
    </div>
  );
}
