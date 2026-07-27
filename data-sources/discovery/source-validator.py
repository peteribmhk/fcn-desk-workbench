#!/usr/bin/env python3
"""
Source Validator — Generic health checker for all registered data sources.
Run by GitHub Actions every 4 hours. Updates data-sources/registry.json.
"""
import json
import time
import urllib.request
import urllib.error
from datetime import datetime, timezone

REGISTRY_PATH = "data-sources/registry.json"
TIMEOUT_SEC = 15


def load_registry():
    with open(REGISTRY_PATH, "r") as f:
        return json.load(f)


def save_registry(registry):
    with open(REGISTRY_PATH, "w") as f:
        json.dump(registry, f, indent=2)


def check_source(source):
    """Probe a single source and return updated status dict."""
    name = source["name"]
    endpoint = source.get("endpoint")
    if not endpoint or "{" in endpoint:  # template endpoint, skip direct probe
        return {**source, "status": "HEALTHY", "last_success": now_iso(), "notes": source.get("notes", "") + " (template endpoint — not probed directly)"}

    headers = {"User-Agent": "FCN-Desk-Workbench/1.0 (peteribmhk)"}
    req = urllib.request.Request(endpoint, headers=headers, method="HEAD")

    try:
        start = time.time()
        with urllib.request.urlopen(req, timeout=TIMEOUT_SEC) as resp:
            latency = int((time.time() - start) * 1000)
            if resp.status == 200:
                return {
                    **source,
                    "status": "HEALTHY",
                    "last_success": now_iso(),
                    "latency_ms": latency,
                }
            else:
                return {
                    **source,
                    "status": "DEGRADED",
                    "last_success": now_iso(),
                    "latency_ms": latency,
                    "notes": f"HTTP {resp.status} — " + source.get("notes", ""),
                }
    except urllib.error.HTTPError as e:
        return {
            **source,
            "status": "DEGRADED" if e.code in (429, 503) else "DOWN",
            "last_success": source.get("last_success"),
            "latency_ms": None,
            "notes": f"HTTP {e.code} — " + source.get("notes", ""),
        }
    except Exception as e:
        return {
            **source,
            "status": "DOWN",
            "last_success": source.get("last_success"),
            "latency_ms": None,
            "notes": f"Error: {str(e)[:100]} — " + source.get("notes", ""),
        }


def now_iso():
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")


def main():
    registry = load_registry()
    updated_sources = []
    any_down = False

    for src in registry["sources"]:
        updated = check_source(src)
        updated_sources.append(updated)
        if updated["status"] in ("DOWN", "DEGRADED"):
            any_down = True
        print(f"{updated['name']}: {updated['status']} (latency: {updated.get('latency_ms', 'N/A')}ms)")

    registry["sources"] = updated_sources
    registry["meta"]["last_updated"] = now_iso()
    save_registry(registry)

    if any_down:
        print("\nWARNING: One or more sources are degraded or down. Check registry.json for fallback chain.")
        exit(1)
    else:
        print("\nAll sources healthy.")


if __name__ == "__main__":
    main()
