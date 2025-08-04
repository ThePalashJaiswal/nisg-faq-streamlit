import streamlit as st

st.set_page_config(page_title="NISG FAQs", layout="wide")

st.title("📘 NISG - Frequently Asked Questions (Palash Jaiswal)")
st.write("Click on a question to view the answer.")

faq_data = [
    {
        "question": "Why should we choose NISG?",
        "answer": """
NISG is a consulting organization operating in the area of e-governance advisory and digital transformation to both central and state Governments in India. NISG strives for excellence and prides itself in generating value for clients. Since our inception in 2002, we have successfully worked on more than 100 projects with central and state governments including multiple Mission Mode Projects (MMPs), the Passport Seva, e-VBAB Network, MCA-21 and e-Biz, and have experience working across 4 countries in Asia and Africa.
        """
    },
    {
        "question": "Why doesn’t NISG bid? Why does NISG not respond to tenders or Request For Proposals (RFPs)?",
        "answer": """
NISG’s vision and mission statements place emphasis on the Public Private Partnership. In order to achieve the vision and mission, partnering with the private sector is an essential element of NISG’s functioning. Therefore, bidding for projects against private industry players creates a scenario contradictory to NISG’s founding objectives.
        """
    },
    {
        "question": "Is there any documentation that proves NISG has been offered projects on nomination?",
        "answer": """
While NISG is unable to present a document outlining the projects we have been nominated to undertake, aligned with our RTI obligations, our Portfolio Section outlines previous projects we have worked on for the central and State governments and public sector undertakings. On request, we will be happy to share the relevant documents that offer support to us being awarded projects on nomination basis.
        """
    },
    {
        "question": "Why Nomination of Not for Profit under GoI and not RFPs?",
        "answer": """
Selection of a Not-for-Profit Agency under GoI (MeitY), through the process of Nomination / Screening committees is an established mechanism that has been practiced for the last 2 decades.

In fact, consulting, project monitoring and staffing for most of the successful MMPs has been carried out by Not for Profit agencies under GoI such as Prime Minister’s dashboard DISHA, Passport, MCA21, e-MIGRATE, etc.

One of the pre-conditions of RFP is clear scope boundaries, however projects at their conceptualisation and initiation stage and projects that require rapid growth the boundaries of scope can’t be defined at the very beginning.

**Challenges with RFPs:**
- Cumbersome & procedurally overloaded
- Limited flexibility to change scope once finalized
- Time-consuming: 5–6 months
- Ministry/Department has limited control over team deployment
- Strategic control lies with private vendor, not Ministry
- RFPs lack flexibility to hire the best consultants from the market

**Why Nomination works better:**
- Allows faster deployment
- Combines best of RFP (price discovery) with strategic control
- Scales up quickly with flexible scope
        """
    }
]

for faq in faq_data:
    with st.expander(f"❓ {faq['question']}"):
        st.markdown(faq['answer'])
