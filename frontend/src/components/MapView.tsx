import {
  MapContainer,
  TileLayer,
  Rectangle,
  useMapEvents,
} from "react-leaflet";
import "leaflet/dist/leaflet.css";
import { useState } from "react";
import { api } from "../api/client";

export default function MapView({ className }: { className?: string }) {
  const [bbox, setBbox] = useState<[number, number, number, number] | null>(
    null
  );
  const [items, setItems] = useState<any[]>([]);
  const [loading, setLoading] = useState(false);

  function Events() {
    useMapEvents({
      moveend(e) {
        const b = e.target.getBounds();
        const box: [number, number, number, number] = [
          b.getWest(),
          b.getSouth(),
          b.getEast(),
          b.getNorth(),
        ];
        setBbox(box);
        api
          .get(`/maps/bbox`, {
            params: { minx: box[0], miny: box[1], maxx: box[2], maxy: box[3] },
          })
          .then((r) => setItems(r.data));
      },
    });
    return null;
  }

  return (
    <div className="h-96">
      <MapContainer
        center={[39.7392, -104.9903]}
        zoom={8}
        style={{ height: "100%" }}
        className={className}
      >
        <TileLayer
          url={
            (import.meta as any).env?.VITE_MAP_TILE_URL ||
            "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
          }
        />
        <Events />
        {bbox && (
          <Rectangle
            bounds={[
              [bbox[1], bbox[0]],
              [bbox[3], bbox[2]],
            ]}
          />
        )}
      </MapContainer>
      <div
        className="mt-2 text-sm"
        style={{
          display: "flex",
          justifyContent: "space-between",
          alignItems: "center",
        }}
      >
        <div>
          Found:{" "}
          <strong style={{ color: "var(--accent)" }}>{items.length}</strong>{" "}
          proposals
        </div>
        <div>
          {loading ? (
            <span className="pill">Loading…</span>
          ) : (
            <span className="pill">Live</span>
          )}
        </div>
      </div>
    </div>
  );
}
