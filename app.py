import streamlit as st
import pandas as pd

from services.graph_service import GraphService
from components.graph_visualization import create_graph_figure


# ------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------

st.set_page_config(
    page_title="TruthMesh AI",
    page_icon="🔮",
    layout="wide",
    initial_sidebar_state="expanded",
)


# ------------------------------------------
# CUSTOM CSS
# ------------------------------------------

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0B0D14;
        color: #F3F4F8;
    }

    [data-testid="stSidebar"] {
        background-color: #11131D;
        border-right: 1px solid #292D40;
    }

    .block-container {
        padding-top: 2rem;
        max-width: 1450px;
    }

    .hero {
        background: linear-gradient(120deg, #19152E, #251A40);
        border: 1px solid #393052;
        padding: 26px;
        border-radius: 18px;
        margin-bottom: 24px;
    }

    .hero h1 {
        color: #FFFFFF;
        font-size: 36px;
        margin-bottom: 8px;
    }

    .hero p {
        color: #C4B5FD;
        font-size: 15px;
        margin-bottom: 0;
    }

    .stButton button[kind="primary"] {
        background-color: #8B5CF6;
        color: white;
        border: none;
        border-radius: 9px;
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------
# SIDEBAR
# ------------------------------------------

with st.sidebar:
    st.markdown("# 🔮 TruthMesh")
    st.caption("Knowledge Intelligence")

    st.divider()

    page = st.radio(
        "NAVIGATION",
        [
            "Overview",
            "Knowledge Graph",
            "Conflict Explorer",
            "About",
        ],
    )

    st.divider()

    st.caption("Powered by FalkorDB")
    st.caption("Prototype v0.1")


# ------------------------------------------
# HEADER
# ------------------------------------------

st.markdown(
    """
    <div class="hero">
        <h1>TruthMesh AI</h1>
        <p>
        Connect the facts. Detect the conflicts.
        Understand the evidence.
        </p>
    </div>
    """,
    unsafe_allow_html=True,
)


# ------------------------------------------
# CONNECT TO FALKORDB
# ------------------------------------------

@st.cache_resource
def get_graph_service():
    return GraphService()


try:
    service = get_graph_service()

    facts = service.get_facts()
    conflicts = service.get_conflicts()

    facts_df = pd.DataFrame(
        facts,
        columns=["Document", "Date", "Event"],
    )

    conflicts_df = pd.DataFrame(
        conflicts,
        columns=[
            "Event",
            "Document 1",
            "Date 1",
            "Document 2",
            "Date 2",
        ],
    )

except Exception as error:
    st.error("Unable to retrieve data from FalkorDB.")
    st.code(str(error))
    st.stop()


# ------------------------------------------
# METRICS
# ------------------------------------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Documents",
        facts_df["Document"].nunique(),
    )

with col2:
    st.metric(
        "Connected Facts",
        len(facts_df),
    )

with col3:
    st.metric(
        "Potential Discrepancies",
        len(conflicts_df),
    )

with col4:
    st.metric(
        "Database",
        "Connected",
    )


# ------------------------------------------
# OVERVIEW
# ------------------------------------------

if page == "Overview":

    st.subheader("Knowledge Graph Overview")

    st.caption(
        "Explore connected information retrieved from FalkorDB."
    )

    figure = create_graph_figure(facts)

    if figure:
        st.plotly_chart(
            figure,
            use_container_width=True,
        )
    else:
        st.info("No graph data available.")

    st.subheader("Recent Potential Discrepancies")

    if conflicts_df.empty:
        st.success("No potential date differences found.")
    else:
        st.dataframe(
            conflicts_df,
            use_container_width=True,
            hide_index=True,
        )


# ------------------------------------------
# KNOWLEDGE GRAPH
# ------------------------------------------

elif page == "Knowledge Graph":

    st.subheader("Interactive Knowledge Graph")

    st.write(
        "Explore relationships between documents, facts, and events."
    )

    figure = create_graph_figure(facts)

    if figure:
        st.plotly_chart(
            figure,
            use_container_width=True,
        )
    else:
        st.info("No graph data available.")

    st.subheader("Graph Facts")

    st.dataframe(
        facts_df,
        use_container_width=True,
        hide_index=True,
    )


# ------------------------------------------
# CONFLICT EXPLORER
# ------------------------------------------

elif page == "Conflict Explorer":

    st.subheader("Conflict Explorer")

    st.write(
        "Inspect the source documents and dates behind each finding."
    )

    if conflicts_df.empty:
        st.success("No potential discrepancies found.")

    else:
        for _, row in conflicts_df.iterrows():

            title = (
                f"{row['Event']} — "
                f"{row['Date 1']} vs {row['Date 2']}"
            )

            with st.expander(title):

                left, right = st.columns(2)

                with left:
                    st.markdown("**Source Document A**")
                    st.write(row["Document 1"])
                    st.code(str(row["Date 1"]))

                with right:
                    st.markdown("**Source Document B**")
                    st.write(row["Document 2"])
                    st.code(str(row["Date 2"]))

                st.warning(
                    "Potential discrepancy: review the source documents "
                    "before deciding whether these claims conflict."
                )

                st.info(
                    "Suggested action: Verify the authoritative date "
                    "with the project owner."
                )


# ------------------------------------------
# ABOUT
# ------------------------------------------

elif page == "About":

    st.subheader("About TruthMesh AI")

    st.write(
        """
        TruthMesh AI is a graph-powered knowledge intelligence prototype.

        It connects information stored in FalkorDB, retrieves related
        facts using Cypher, and identifies potential date discrepancies.
        """
    )

    st.markdown("### Technology Stack")

    st.write(
        """
        - Python
        - Streamlit
        - FalkorDB
        - Cypher
        - Plotly
        - NetworkX
        """
    )

    st.markdown("### Current Limitations")

    st.write(
        """
        - The current prototype uses predefined graph data.
        - Different dates are treated as potential discrepancies.
        - Semantic conflict verification is not yet implemented.
        - Document ingestion and AI-assisted extraction are future features.
        """
    )


# ------------------------------------------
# FOOTER
# ------------------------------------------

st.divider()

st.caption(
    "TruthMesh AI | Graph-powered knowledge intelligence"
)