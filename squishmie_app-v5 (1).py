import streamlit as st

st.set_page_config(
    page_title="Squ!shmie Enterprise | UUM Online Store",
    page_icon="🐰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    .main-title {
        color: #2E7D32;
        text-align: center;
        font-family: 'Helvetica Neue', sans-serif;
        font-weight: 800;
        margin-bottom: 0px;
    }
    .sub-title {
        text-align: center;
        color: #555;
        font-size: 1.2rem;
        margin-bottom: 25px;
    }
    .product-card {
        background-color: #F4FBF7;
        border: 2px solid #C8E6C9;
        border-radius: 12px;
        padding: 15px;
        text-align: center;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
    }
    .price-tag {
        color: #1B5E20;
        font-weight: bold;
        font-size: 1.3rem;
    }
    .stButton>button {
        background-color: #2E7D32;
        color: white;
        border-radius: 8px;
        font-weight: bold;
        width: 100%;
    }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🐰 Squ!shmie Enterprise</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Squeeze Away Your Study Stress! ✨ | UUM Campus Online Store</p>", unsafe_allow_html=True)

with st.sidebar:
    st.title("About Squ!shmie")
    st.write("""
    **Squ!shmie Enterprise** brings high-quality, non-toxic, slow-rising squishies to UUM students!
    
    📍 **Pickup Points:** Varsity Mall, Inasis Cafeterias, or Dorm Lobbies.  
    💵 **Payment:** DuitNow QR / Cash on Delivery.  
    ⚡ **Fast Delivery:** Direct campus handoffs!  
    """)
    st.info("🏷️ **Official Price:** All squishies are **RM 4.00** each!")

tab1, tab2, tab3 = st.tabs(["🛍️ Shop & Order", "🧮 Price Calculator", "❓ FAQ & Contact"])

with tab1:
    st.header("Select Your Squishies (RM 4.00 each)")
    
    products = [
        {"name": "Pink Butter Squishy", "desc": "Ultra-soft, slow-rising creamy pink texture.", "price": 4.00, "icon": "🩷"},
        {"name": "Yellow Butter Squishy", "desc": "Satisfying butter-block aesthetic with slow rebound.", "price": 4.00, "icon": "💛"},
        {"name": "Cheese Vent Toy", "desc": "Cute Swiss cheese design with ultra-squishy feel.", "price": 4.00, "icon": "🧀"},
        {"name": "NeeDoh Nice Cube", "desc": "Translucent stress cube with firm, slow-rising core.", "price": 4.00, "icon": "🧊"},
        {"name": "Ice Cream & Dessert Squishy", "desc": "Sweet dessert model for desk decor and stress relief.", "price": 4.00, "icon": "🍦"},
        {"name": "Coconut Oil Sphere", "desc": "Smooth, rounded tactile stress-reliever.", "price": 4.00, "icon": "🥥"}
    ]
    
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    
    cart = {}
    
    for idx, prod in enumerate(products):
        with cols[idx % 3]:
            st.markdown(f"""
            <div class='product-card'>
                <h3>{prod['icon']} {prod['name']}</h3>
                <p>{prod['desc']}</p>
                <p class='price-tag'>RM {prod['price']:.2f}</p>
            </div>
            """, unsafe_allow_html=True)
            qty = st.number_input(f"Quantity for {prod['name']}", min_value=0, max_value=20, value=0, key=f"qty_{idx}")
            if qty > 0:
                cart[prod['name']] = {"qty": qty, "price": prod['price']}
            st.write("")

    st.markdown("---")
    st.header("📋 Checkout Details")
    
    with st.form("order_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            name = st.text_input("Full Name *", placeholder="e.g. Nur Allysha")
            matric = st.text_input("Matric No. / Student ID *", placeholder="e.g. 320273")
            phone = st.text_input("WhatsApp Number *", placeholder="e.g. 0123456789")
        
        with col_b:
            inasis = st.selectbox("UUM Residential Hall (Inasis) *", [
                "Inasis Tradewinds", "Inasis MAS", "Inasis TNB", "Inasis Proton", 
                "Inasis Petronas", "Inasis EON", "Inasis Sime Darby", "Inasis MISC", 
                "Inasis BSN", "Inasis Bank Muamalat", "Inasis YAB", "Inasis Yayasan Al-Bukhary", "Off Campus"
            ])
            pickup_loc = st.selectbox("Preferred Pickup Location *", [
                "Varsity Mall Foyer", "Inasis Cafeteria", "UUM Student Center", "Direct Dorm Lobby"
            ])
            pickup_time = st.selectbox("Preferred Pickup Time Slot *", [
                "Slot A: 12:00 PM – 2:00 PM",
                "Slot B: 5:00 PM – 7:00 PM",
                "Slot C: 8:00 PM – 10:00 PM"
            ])

        payment_method = st.radio("Payment Method *", ["DuitNow QR (Online)", "Cash on Delivery"], horizontal=True)
        notes = st.text_area("Special Instructions / Notes (Optional)", placeholder="e.g. Please call when arriving at dorm lobby.")
        
        submit_btn = st.form_submit_button("Generate Order Summary 🚀")
        
    if submit_btn:
        if not name or not matric or not phone or not cart:
            st.error("⚠️ Please fill in all required fields (*) and select at least 1 squishy!")
        else:
            total_items = sum(item["qty"] for item in cart.values())
            final_total = total_items * 4.00
            
            items_str = "\n".join([f"• {k}: {v['qty']} unit(s) @ RM 4.00" for k, v in cart.items()])
            
            msg = f"""🐰 *NEW SQU!SHMIE ORDER* 🐰

👤 *Customer Details:*
• Name: {name}
• Matric No: {matric}
• WhatsApp: {phone}
• Inasis: {inasis}

📦 *Order Summary:*
{items_str}

📍 *Pickup Details:*
• Location: {pickup_loc}
• Time Slot: {pickup_time}
• Payment Method: {payment_method}

💰 *Payment Total:*
• Total Items: {total_items}
• Unit Price: RM 4.00
• *FINAL TOTAL: RM {final_total:.2f}*

📝 *Notes:* {notes if notes else 'None'}"""

            st.success("✅ Order generated successfully!")
            
            st.markdown(f"""
            ### 🧾 Final Order Summary
            * **Total Items:** {total_items}
            * **Unit Price:** RM 4.00
            * **Total Amount Due:** **RM {final_total:.2f}**
            """)

            st.text_area("Copy & Paste Message to WhatsApp:", value=msg, height=250)

with tab2:
    st.header("🧮 Simple Order Calculator")
    st.write("Calculate your total cost based on RM 4.00 per squishy.")
    
    num_squishies = st.slider("Select Number of Squishies:", min_value=1, max_value=20, value=2)
    calc_total = num_squishies * 4.00
    
    col_m1, col_m2 = st.columns(2)
    col_m1.metric("Unit Price", "RM 4.00")
    col_m2.metric("Total Cost", f"RM {calc_total:.2f}")

with tab3:
    st.header("❓ Frequently Asked Questions")
    
    with st.expander("Q: What materials are the squishies made of?"):
        st.write("All Squ!shmie items are made from non-toxic, high-density polyurethane (PU) foam, offering a durable and satisfying slow-rising rebound.")
        
    with st.expander("Q: How do I collect my order on campus?"):
        st.write("We conduct scheduled handoffs at Varsity Mall, student cafeterias, and residential hall lobbies. Our team will WhatsApp you 15 minutes before your time slot.")
        
    with st.expander("Q: How does DuitNow QR payment work?"):
        st.write("When submitting your order, select DuitNow QR. You will receive our official DuitNow QR image on WhatsApp to complete the transfer via your bank or e-wallet app.")

    st.markdown("---")
    st.subheader("📞 Customer Service Contact")
    st.write("Need custom orders or have questions? Contact **Nur Allysha (Customer Service Manager)** on WhatsApp.")
