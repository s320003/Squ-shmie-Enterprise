import streamlit as st
import urllib.parse
import os

st.set_page_config(page_title="Squ!shmie Enterprise | UUM Online Store", page_icon="🐰", layout="wide")

st.markdown("""
<style>
   .main-title { color: #2E7D32; text-align: center; font-family: sans-serif; font-weight: 800; }
   .sub-title { text-align: center; color: #555; font-size: 1.1rem; margin-bottom: 25px; }
   .product-card { background-color: #F4FBF7; border: 2px solid #C8E6C9; border-radius: 12px; padding: 15px; text-align: center; }
   .price-tag { color: #1B5E20; font-weight: bold; font-size: 1.3rem; margin-top: 5px; }
   .order-btn { display: inline-block; background-color: #25D366; color: white !important; font-weight: bold; font-size: 1.2rem; padding: 14px 28px; border-radius: 10px; text-decoration: none; text-align: center; margin-top: 15px; width: 100%; }
</style>
""", unsafe_allow_html=True)

st.markdown("<h1 class='main-title'>🐰 Squ!shmie Enterprise</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Squeeze Away Your Study Stress! ✨ | UUM Campus Online Store</p>", unsafe_allow_html=True)

with st.sidebar:
    st.title("About Squ!shmie")
    st.write("**Squ!shmie Enterprise** brings high-quality, non-toxic, slow-rising squishies to UUM students!")
    st.success("🏷️ **Pricing:** RM 4.00 (Butter & Cheese) | RM 6.00 (Special Butter, Dessert, Cubes & Spheres)")
    seller_phone = st.text_input("📱 Seller Phone Number", value="60123456789")

tab1, tab2, tab3 = st.tabs(["🛍️ Shop & Order", "🧮 Order Calculator", "❓ FAQ & Contact"])

products = [
    {"name": "Pink Butter Squishy", "desc": "Ultra-soft creamy pink butter stick.", "price": 4.00, "icon": "🩷", "img": "WhatsApp_Image_2026-09-30_at_12.52.32.jpeg"},
    {"name": "Yellow Butter Squishy", "desc": "Satisfying salted butter-block aesthetic.", "price": 4.00, "icon": "💛", "img": "WhatsApp_Image_2026-09-30_at_12.53.42.jpeg"},
    {"name": "Cheese Vent Toy", "desc": "Cute Swiss cheese design with ultra-squishy feel.", "price": 4.00, "icon": "🧀", "img": "WhatsApp_Image_2026-09-30_at_12.52.32.jpeg"},
    {"name": "Special Butter Squishy", "desc": "Premium texture special edition butter squishy.", "price": 6.00, "icon": "✨", "img": "WhatsApp_Image_2026-09-30_at_12.53.42.jpeg"},
    {"name": "NeeDoh Nice Cube", "desc": "Translucent stress cube with solid core.", "price": 6.00, "icon": "🧊", "img": "WhatsApp_Image_2026-10-06_at_23.51.54.jpeg"},
    {"name": "Ice Cream & Dessert Squishy", "desc": "Sweet dessert tub model (Mango, Strawberry, Matcha, Tiramisu).", "price": 6.00, "icon": "🍦", "img": "WhatsApp_Image_2026-10-06_at_23.50.07.jpeg"},
    {"name": "Coconut Oil Sphere", "desc": "Smooth crystal spheres (Purple, Blue, Pink, Clear).", "price": 6.00, "icon": "🥥", "img": "WhatsApp_Image_2026-10-06_at_23.51.24_(1).jpeg"}
]

with tab1:
    st.header("Select Your Squishies")
    col1, col2, col3 = st.columns(3)
    cols = [col1, col2, col3]
    cart = {}
    for idx, prod in enumerate(products):
        with cols[idx % 3]:
            img_path = prod["img"]
            know_path = os.path.join("/workspace/knowledge", img_path)
            if os.path.exists(img_path):
                st.image(img_path, use_container_width=True)
            elif os.path.exists(know_path):
                st.image(know_path, use_container_width=True)
            st.markdown(f"<div class='product-card'><h3>{prod['icon']} {prod['name']}</h3><p>{prod['desc']}</p><p class='price-tag'>RM {prod['price']:.2f}</p></div>", unsafe_allow_html=True)
            qty = st.number_input(f"Quantity for {prod['name']}", min_value=0, max_value=20, value=0, key=f"qty_{idx}")
            if qty > 0:
                cart[prod["name"]] = {"qty": qty, "price": prod["price"]}
    st.markdown("---")
    st.header("📋 Checkout & Payment Details")
    with st.form("order_form"):
        col_a, col_b = st.columns(2)
        with col_a:
            name = st.text_input("Full Name *")
            matric = st.text_input("Matric No. / Student ID *")
            phone = st.text_input("Customer Phone Number *")
        with col_b:
            inasis = st.selectbox("UUM Residential Hall (Inasis) *", ["Inasis Tradewinds", "Inasis MAS", "Inasis TNB", "Inasis Proton", "Inasis Petronas", "Inasis EON", "Inasis Sime Darby", "Inasis MISC", "Inasis BSN", "Inasis Bank Muamalat", "Inasis YAB", "Inasis Yayasan Al-Bukhary", "Off Campus"])
            pickup_loc = st.selectbox("Preferred Pickup Location *", ["Varsity Mall Foyer", "Inasis Cafeteria", "UUM Student Center", "Direct Dorm Lobby"])
            pickup_time = st.selectbox("Preferred Pickup Time Slot *", ["Slot A: 12:00 PM – 2:00 PM", "Slot B: 5:00 PM – 7:00 PM", "Slot C: 8:00 PM – 10:00 PM"])
        payment_method = st.radio("Payment Method *", ["DuitNow QR (Online)", "Cash on Delivery (COD)"], horizontal=True)
        notes = st.text_area("Special Instructions / Notes (Optional)")
        submit_btn = st.form_submit_button("🚀 Submit Order & Open WhatsApp")
    if submit_btn:
        if not name or not matric or not phone or not cart:
            st.error("⚠️ Please fill in all required fields (*) and select at least 1 squishy!")
        else:
            total_items = sum(item["qty"] for item in cart.values())
            final_total = sum(item["qty"] * item["price"] for item in cart.values())
            items_str = "
".join([f"• {k}: {v['qty']} unit(s) @ RM {v['price']:.2f}" for k, v in cart.items()])
            msg = f"🐰 *NEW SQU!SHMIE ORDER* 🐰

👤 *Customer Details:*
• Name: {name}
• Matric No: {matric}
• Phone: {phone}
• Inasis: {inasis}

📦 *Order Items:*
{items_str}

📍 *Pickup Details:*
• Location: {pickup_loc}
• Time Slot: {pickup_time}
• Payment Method: {payment_method}

💰 *Payment Breakdown:*
• Total Items: {total_items} unit(s)
• *TOTAL AMOUNT: RM {final_total:.2f}*

📝 *Notes:* {notes if notes else 'None'}"
            st.success("🎉 Order summary generated!")
            st.markdown(f"### 🧾 Final Order Summary
* **Total Items:** {total_items} unit(s)
* **Total Amount Due:** **RM {final_total:.2f}**
* **Payment Choice:** {payment_method}")
            if payment_method == "DuitNow QR (Online)":
                st.info("💳 **DuitNow QR Payment:** Clicking the green button below opens a direct chat with the seller!")
            else:
                st.info(f"💵 **Cash on Delivery:** Please prepare exact cash (RM {final_total:.2f}) upon campus pickup.")
            encoded_msg = urllib.parse.quote(msg)
            clean_phone = seller_phone.replace("+", "").replace("-", "").replace(" ", "")
            domain = "wa.me"
            link_url = f"https://{domain}/{clean_phone}?text={encoded_msg}"
            st.markdown("---")
            st.subheader("📲 Direct Order Link")
            st.markdown(f'<a href="{link_url}" target="_blank" class="order-btn">💬 Click Here to Send Order Directly</a>', unsafe_allow_html=True)
            with st.expander("📄 View Manual Order Text"):
                st.text_area("Order Text:", value=msg, height=200)

with tab2:
    st.header("🧮 Order Calculator")
    c_item4 = st.number_input("RM 4.00 Items (Butter / Cheese):", min_value=0, max_value=20, value=1)
    c_item6 = st.number_input("RM 6.00 Items (Special Butter, Cubes, Desserts, Spheres):", min_value=0, max_value=20, value=1)
    st.metric("Total Price", f"RM {(c_item4 * 4.00) + (c_item6 * 6.00):.2f}")

with tab3:
    st.header("❓ Frequently Asked Questions")
    with st.expander("Q: How do I pay via DuitNow QR?"):
        st.write("Once you send your order, our team will reply with our official DuitNow QR code so you can pay instantly!")
    st.write("Customer Service Managers: **Nur Allysha & Endre**")