# Deception Analysis Platform

> Replay-driven cyber threat analysis pipeline for reconstructing attacker activity from T-Pot honeypot telemetry.

---

## Overview

The Deception Analysis Platform is a Python-based cybersecurity analysis pipeline that reconstructs attacker activity from replayed T-Pot honeypot telemetry. Rather than executing malicious payloads, the platform performs deterministic replay, session reconstruction, attack clustering, payload fingerprinting, indicator extraction, and standards-based detection engineering to generate reproducible forensic artifacts.

The project was designed to demonstrate software engineering, cybersecurity analysis, and reproducible research practices. Every artifact produced by the pipeline is traceable, cryptographically verifiable, and suitable for assessment or incident investigation.

---

## Objectives

- Reconstruct attack sessions from normalized replay telemetry
- Cluster related attacker activity
- Extract Indicators of Compromise (IOCs)
- Generate STIX 2.1 threat intelligence bundles
- Produce Sigma and Suricata detection rules
- Maintain cryptographic integrity of generated artifacts
- Document analytical evidence using an evidence index
- Ensure deterministic and reproducible execution

---

## Features

- Replay Adapter
- Session Reconstruction
- Attack Clustering
- IOC Extraction
- STIX 2.1 Export
- Sigma Rule Generation
- Suricata Rule Generation
- Payload Hash Ledger
- Payload Isolation Report
- Evidence Index
- Replay Verification
- Integrity Attestation
- Continuity Record
- Assessment Manifest
- Provenance Tracking

---

## Architecture

```text
Replay Dataset
      │
      ▼
Replay Adapter
      │
      ▼
Normalized Events
      │
      ▼
Session Engine
      │
      ▼
Cluster Engine
      │
      ▼
Payload Hash Engine
      │
      ▼
IOC Engine
      │
      ▼
Artifact Manager
      │
      ▼
Generated Artifacts
```

---

## Repository Structure

```text
src/
│
├── adapters/
├── artifacts/
├── assessment/
├── clustering/
├── continuity/
├── detections/
├── evidence/
├── exporters/
├── integrity/
├── ioc/
├── isolation/
├── manifest/
├── models/
├── payloads/
├── profiling/
├── provenance/
├── session_analysis/
├── sessionization/
└── verification/

tests/
replay/
derived/
```

---

## Installation

```bash
git clone https://github.com/<your-username>/deception-analysis-platform.git

cd deception-analysis-platform

python -m venv .venv

source .venv/bin/activate

pip install -r requirements.txt
```

---

## Running the Pipeline

```bash
python -m pipeline.main
```

---

## Quality Assurance

Run the complete verification suite.

```bash
pytest

ruff check src tests

ruff format src tests

black src tests

mypy src
```

---

## Generated Artifacts

| Artifact | Purpose |
|-----------|---------|
| sessions.parquet | Reconstructed attack sessions |
| clusters.json | Clustered attacker activity |
| hash-ledger.csv | SHA-256 payload ledger |
| iocs.csv | Extracted indicators |
| stix-bundle.json | STIX 2.1 intelligence bundle |
| replay-verification.json | Replay validation |
| isolation-results.json | Payload isolation metadata |
| evidence-index.csv | Evidence mapping |
| continuity-record.md | Reproducibility documentation |
| integrity-attestation.md | Integrity controls |
| session-analysis.md | Representative attack session |
| sigma-rules.yml | Portable SIEM detections |
| suricata.rules | IDS signatures |
| assessment-manifest.json | Assessment metadata |
| manifest.sha256 | Cryptographic hashes |

---

## Testing Status

Current project quality gates:

- 33 unit and integration tests passing
- Ruff static analysis clean
- Black formatting compliant
- MyPy type checking clean

---

## Roadmap

Future enhancements include:

- Live T-Pot Adapter
- Docker deployment
- Zeek integration
- Elastic Stack support
- Wazuh integration
- Threat intelligence feed ingestion
- Automated Sigma conversion
- Web dashboard
- REST API

---

## Technologies

- Python 3.13
- Pydantic
- PyArrow
- PyYAML
- Pytest
- Ruff
- Black
- MyPy

---

## Author

**Adedayo Ogunsemoyin**

Cybersecurity Analyst • Detection Engineer 

GitHub: https://github.com/Spotter1091/deception-sensor-pipeline.git
