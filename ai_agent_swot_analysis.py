import streamlit as st # Stream lit version (1.43.0)
from google import genai
import os

# Initialize the API client
client = genai.Client(api_key=os.environ['GOOGLE_GEMINI_API_KEY'])

# Streamlit App UI
st.title("SWOT Analysis Generator")
st.write("""The SWOT Analysis Generator is a tool that automates the creation of detailed SWOT analyses for any organization, helping businesses make informed strategic decisions. By simply providing the organization’s name and context, the tool generates an insightful evaluation of strengths, weaknesses, opportunities, and threats. 
         (Powered by - Gemini API) \n

Advantages:
- Time-saving: Automates the SWOT analysis process.
- Data-driven: Provides objective insights based on business context.
- Customizable: Tailored analysis based on organization-specific details.
- Scalable: Can be used for multiple organizations or projects.\n
Uses:
* Strategic planning
* Market research
* Competitor analysis
* Risk management\n
This tool provides analysis of the situation and aids businesses to make strategic decisions faster and with confidence. \n""")

# User input
organization_name = st.text_input("Enter the organization name:")
context = st.text_area("Please provide the current situation of the organization")

if organization_name and context:
    # Create the content prompt for Gemini API based on user input
    content = f"""You are a subject matter expert and a strategic business consultant with expertise in corporate strategy and market analysis. Your task is to perform a comprehensive SWOT analysis for {organization_name} based on the following context in a formal tone: {context}.
Ensure each point is accurately described with a precise description.
Stick closely to the given context without adding generic information.
Use bullet points for clarity, with each Strength, Weakness, Opportunity, and Threat accompanied by a precise description (1-2 lines) following the point.
Provide 3 real-world examples of companies or cases that have faced similar situations, explaining how their SWOT analysis aligns with this case. Provide a 3 liner conclusion indicating the heading.
Example Response -
SWOT Analysis for Tesla
Strengths
Strong Brand Equity – Tesla is a globally recognized leader in electric vehicles (EVs), with a reputation for innovation and cutting-edge technology, attracting strong customer loyalty.
Technological Leadership – Tesla’s proprietary battery technology and self-driving software give it a competitive advantage in vehicle range, efficiency, and autonomous driving.
Vertical Integration and Supply Chain Control – Tesla’s ownership of key components like battery manufacturing (Gigafactories) and charging infrastructure (Superchargers) ensures cost control and faster innovation.
Financial Strength and Market Leadership – Tesla’s high market valuation and profitability provide capital for R&D, production scaling, and global expansion.
Weaknesses
Production and Delivery Bottlenecks – Tesla has faced delays due to supply chain disruptions, semiconductor shortages, and production line inefficiencies.
High Production Costs – The costs of lithium, cobalt, and nickel, along with advanced battery technology, increase manufacturing expenses and reduce profit margins.
Quality Control Issues – Reports of inconsistent product quality (e.g., panel gaps, paint defects) and software malfunctions have affected customer satisfaction.
Overreliance on Elon Musk’s Leadership – Strategic decisions and public statements by Elon Musk have led to stock volatility and reputational risks.
Opportunities
Growing EV Market in Emerging Economies – Expanding into India and Southeast Asia, where EV adoption is rising due to government incentives, could drive revenue growth.
Expansion into Renewable Energy – Tesla’s solar panels and energy storage solutions (Powerwall, Megapack) align with the global shift toward sustainable energy.
Advancement in Autonomous Driving – Enhancing Full Self-Driving (FSD) capabilities and licensing the technology to other manufacturers could create new revenue streams.
Strategic Partnerships and Collaboration – Partnering with governments and infrastructure providers could improve charging infrastructure and increase adoption rates.
Threats
Intensifying Competition – Legacy automakers (e.g., Volkswagen, Ford) and Chinese manufacturers (e.g., BYD) are launching competitive EVs with lower costs and advanced features.
Regulatory and Legal Risks – Changes in emissions regulations, autonomous driving laws, and trade tariffs could increase costs and restrict market access.
Economic Downturns – Inflation and rising interest rates could reduce consumer demand for premium-priced electric vehicles.
Cybersecurity and Data Privacy Risks – Increasing reliance on connected vehicles exposes Tesla to data breaches and regulatory scrutiny over customer data handling.

Comparable Real-World Cases
Apple Inc.
Strength: Apple’s vertical integration and proprietary technology (e.g., A-series chips) give it control over product quality and supply chain efficiency, similar to Tesla's control over battery production and software.
Weakness: Overdependence on CEO leadership (Steve Jobs, Tim Cook) reflects Tesla’s vulnerability to Elon Musk’s strategic decisions.
Opportunity: Apple’s expansion into wearable technology mirrors Tesla’s move into renewable energy solutions.
Threat: Regulatory pressure and competition from Android-based manufacturers align with Tesla’s competitive landscape.

Toyota
Strength: Toyota’s dominance in hybrid technology mirrors Tesla’s leadership in EVs.
Weakness: Toyota faced production delays during the semiconductor shortage, similar to Tesla’s supply chain issues.
Opportunity: Toyota’s shift toward electric and hydrogen vehicles parallels Tesla’s push for sustainable energy solutions.
Threat: Rising competition from Chinese manufacturers affects both Tesla and Toyota’s global market share.

Netflix
Strength: Netflix’s first-mover advantage in streaming reflects Tesla’s leadership in EV technology.
Weakness: Content production costs affect Netflix’s profitability, similar to Tesla’s high production expenses for batteries and EV components.
Opportunity: Global expansion into untapped markets aligns with Tesla’s strategy to enter developing economies.
Threat: Competition from Disney+ and Amazon Prime parallels Tesla’s market pressure from legacy automakers and new EV entrants.
Conclusion: Tesla’s technological and market leadership gives it a competitive advantage, but operational challenges and competitive pressures pose significant risks. Strategic expansion into renewable energy and emerging markets could drive future growth, provided Tesla addresses its quality and production weaknesses.

keep a formal tone throughout the response"""

    # Call Gemini API to generate the response
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=content
        )

        # Display the response
        st.write(response.text)
    except Exception as e:
        st.error(f"Error: {str(e)}")
