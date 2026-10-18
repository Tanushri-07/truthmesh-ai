# 🔮 TruthMesh AI
### Graph-Powered Company Knowledge Intelligence

**Connect the facts. Detect potential discrepancies. Understand the evidence.**

TruthMesh AI is a graph-powered company knowledge intelligence prototype built using FalkorDB. It connects documents, facts, and events in a knowledge graph to identify potential discrepancies between dates associated with the same event.

The application provides an interactive dashboard where users can explore connected information, compare source documents, and investigate findings before making decisions.

**Hackathon Track:** Company Brain

---

## 🎯 Problem Statement

Organizations rely on multiple documents to manage projects, events, and business decisions. Information such as dates may differ across these documents, making it difficult to identify inconsistencies and determine which claims require further verification.

Traditional document-by-document review can be time-consuming and may overlook relationships between information from different sources.

## 💡 Our Solution

TruthMesh AI represents documents, facts, and events as interconnected nodes in a FalkorDB knowledge graph.

The system queries the graph to identify differing dates associated with the same event and presents the corresponding source documents side by side.

Instead of automatically treating every difference as a confirmed contradiction, TruthMesh AI flags potential discrepancies for human review.

This helps users trace findings back to their sources and determine which information needs verification.

---

## ✨ Key Features

- **Knowledge Graph Visualization:** Explore relationships between documents, facts, and events.
- **Connected Information:** Represent document-to-fact-to-event relationships using FalkorDB.
- **Potential Discrepancy Detection:** Identify differing dates associated with the same event.
- **Source Comparison:** Inspect the documents and dates behind each finding.
- **Suggested Actions:** Display recommendations to help users verify potentially inconsistent information.
- **Interactive Dashboard:** Navigate the knowledge graph and discrepancy findings through a Streamlit interface.

---

## 🏗️ System Architecture

TruthMesh AI uses FalkorDB as its graph database and Python to retrieve and process connected information.

### Graph Data Model

The graph contains three node types:

| Node | Description | Example |
|---|---|---|
| `Document` | Represents a source document | Project Plan |
| `Fact` | Represents a fact associated with a document | 2026-11-10 |
| `Event` | Represents the event associated with a fact | Product Launch |

### Relationships

**1. Document contains Fact**

```cypher
(Document)-[:CONTAINS]->(Fact)
```

Connects each source document to the facts it contains.

**2. Fact refers to Event**

```cypher
(Fact)-[:REFERS_TO]->(Event)
```

Connects a fact to the event it describes.

### Example Graph

```text
Project Plan
     |
  CONTAINS
     |
Fact: 2026-11-10
     |
  REFERS_TO
     |
Product Launch
```

Other documents can connect their own facts to the same event. FalkorDB can then query these relationships to identify differing dates for further investigation.

### Architecture Flow

```text
Source Documents
       |
       v
Document, Fact and Event Nodes
       |
       v
FalkorDB Knowledge Graph
       |
       v
Cypher Queries
       |
       v
Potential Discrepancy Detection
       |
       v
Streamlit Dashboard
       |
       v
Source Comparison and Human Verification
```

---

## 🔎 How Discrepancy Detection Works

1. Documents are represented as nodes in the knowledge graph.
2. Facts are connected to their source documents.
3. Each fact is connected to the event it refers to.
4. A Cypher query finds pairs of facts associated with the same event.
5. When their dates differ, the system flags the pair as a potential discrepancy.
6. The dashboard displays the source documents, dates, and a suggested verification action.

### Example

| Source Document | Event | Date |
|---|---|---|
| Project Plan | Product Launch | 2026-11-10 |
| Management Notes | Product Launch | 2026-11-15 |
| Marketing Plan | Product Launch | 2026-11-12 |

The system identifies the differing dates and presents the relevant comparisons in the Conflict Explorer.

**Important:** Different dates do not necessarily indicate a genuine contradiction. For example, a marketing campaign may begin before a product launch. The current prototype flags date differences for human review rather than determining whether the claims are semantically incompatible.

---

## 🧰 Technology Stack

| Technology | Purpose |
|---|---|
| Python | Application logic |
| FalkorDB | Graph storage and relationship queries |
| Cypher | Graph querying and discrepancy detection |
| Streamlit | Interactive dashboard |
| NetworkX | Graph structure and visualization layout |
| Plotly | Interactive graph visualization |
| Pytest | Automated testing |

---

## 🚀 Getting Started

Follow these instructions to run the project locally.

### Prerequisites

- Python 3.11 or newer
- Docker
- Git
- FalkorDB running locally

### 1. Clone the Repository

```bash
git clone https://github.com/Tanushri-07/truthmesh-ai.git
cd truthmesh-ai
```

### 2. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start FalkorDB

If you already have the project's Docker container, start it with:

```bash
docker start truthmesh-db
```

Ensure that FalkorDB is accessible at:

```text
localhost:6379
```

If you are setting up FalkorDB for the first time, follow the official documentation:

https://docs.falkordb.com/

### 5. Prepare the Graph Data

The application expects a graph named `truthmesh` containing the sample documents, facts, events, and relationships.

Review the Cypher query in the `queries/` directory to understand the graph model and discrepancy-detection logic.

If the graph has not yet been populated, create the graph and load the sample data before starting the application.

### 6. Run the Application

From the project root, run:

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to explore the dashboard.

---

## 🧪 Running Tests

Ensure that FalkorDB is running and that your Python virtual environment is activated.

Run:

```bash
pytest -v
```

The tests that connect to FalkorDB require an accessible database.

---

## 📁 Project Structure

```text
truthmesh-ai/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── services/
│   └── graph_service.py
├── components/
│   └── graph_visualization.py
├── queries/
│   └── detect_conflicts.cypher
├── docs/
│   └── graph-model.md
└── tests/
    └── test_conflicts.py
```

---

## ⚠️ Current Limitations

TruthMesh AI is a working prototype with the following limitations:

- The demonstration uses a small sample dataset.
- The current detection logic compares dates associated with the same event.
- Different dates may represent legitimate differences rather than contradictions.
- The current prototype requires human review to determine whether a flagged difference is a genuine conflict.
- The project does not currently establish which source is authoritative.
- The graph and detection logic can be extended to support more claim types and richer verification rules.

---

## 🔮 Future Improvements

Potential future enhancements include:

- Ingesting information from additional document formats.
- Extracting structured facts from unstructured documents.
- Distinguishing different date types, such as campaign start dates and product launch dates.
- Adding source reliability and claim provenance.
- Supporting richer discrepancy-detection rules.
- Improving evidence-based explanations and review workflows.
- Expanding the dataset to evaluate detection quality.

These are proposed improvements, not claims about functionality already implemented.

---

## 🤖 AI Assistance Disclosure

AI coding assistance was used during the development of this project.

The project team is responsible for reviewing the implementation, understanding the architecture, and explaining the code and design decisions during evaluation.

---

## 🏆 Hackathon Information

- **Project:** TruthMesh AI
- **Track:** Company Brain
- **Primary Graph Database:** FalkorDB
- **Repository:** https://github.com/Tanushri-07/truthmesh-ai

---

## 📌 Project Status

**Working prototype**

TruthMesh AI demonstrates how a graph database can connect company information and help users investigate potential discrepancies across documents.
