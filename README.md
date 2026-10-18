# 🔮 TruthMesh AI

### Graph-Powered Company Knowledge Intelligence

TruthMesh AI connects information from company documents using FalkorDB
and identifies potential discrepancies between facts associated with
the same event.

It helps users inspect connected information, compare source documents,
and investigate differences before making decisions.

## 🎯 Problem Statement

Organizations store information across multiple documents. Dates and
other claims may differ between sources, making it difficult to identify
inconsistencies and determine which information requires verification.

## 💡 Solution

TruthMesh AI represents documents, facts, and events as a connected
knowledge graph. It queries the graph to identify differing dates
associated with the same event and presents the evidence through an
interactive dashboard.

## ✨ Features

- Interactive knowledge graph visualization
- Document-to-fact-to-event relationships
- Potential date discrepancy detection
- Side-by-side source document comparison
- Suggested verification actions
- Streamlit dashboard powered by FalkorDB

## 🧰 Tech Stack

- Python
- FalkorDB — graph database
- Streamlit — interactive dashboard
- NetworkX — graph visualization layout
- Plotly — interactive graph rendering
- Pytest — testing

## 🏗️ Graph Architecture

The graph uses three node types:

- `Document` — the source document
- `Fact` — a claim extracted from a document
- `Event` — the event associated with the claim

Relationships:

- `(Document)-[:CONTAINS]->(Fact)`
- `(Fact)-[:REFERS_TO]->(Event)`

Example:

`Project Plan → Fact: 2026-11-10 → Product Launch`

FalkorDB stores and queries these relationships to identify potential
date discrepancies across documents referring to the same event.

## 🔎 Detection Logic

The current prototype compares dates associated with the same event.
When two documents contain different dates, it reports a potential
discrepancy for human review.

A difference does not necessarily mean the claims contradict each
other. For example, a campaign start date can legitimately differ
from a product launch date. Users should verify the source documents
before deciding whether a genuine conflict exists.

## 🚀 Getting Started

### Prerequisites

- Python 3.11 or newer
- Docker
- Git

### 1. Clone the repository

```bash
git clone https://github.com/Tanushri-07/truthmesh-ai.git
cd truthmesh-ai