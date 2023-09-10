# Import Streamlit
import streamlit as st


# Set page layout to wide
st.set_page_config(layout="wide")

# Header
st.markdown("""
<style>
    .header {
    background-color: white; /* Setting background color to white */
    padding: 20px;
    text-align: center;
    color: white; /* Setting general text color to white */
    }

    .header h1 {
    color: black; /* Setting h1 color to black */
    }

    .header p {
    color: black; /* Setting paragraph text color to black */
    }

    .header h3 {
    color: black; /* Setting h3 color to black */
    }
</style>

<div class="header">
    <h1>ServaTech</h1>
    <h3>Tuko Hapa Kukuhudumia</h3>
</div>
""", unsafe_allow_html=True)




# # Title of your page
# st.title("ServaTech")

# Description of your App
st.write("# 🤖 Whatsapp Auto Reply AI Bot:")
st.write("## Ni chatbot ya kiotomatiki kwa biashara iliyoundwa kujibu maswali ya wateja na kutoa msaada wa manufaa.")
st.write("## Inafanya kazi kwenye live chat ya WhatsApp ya sasa, ikitoa huduma kama mauzo, masoko, na huduma kwa wateja. Inatoa majibu ya haraka lakini sahihi kwa maswali yanayoulizwa mara kwa mara na wateja.")
st.write("## Imeundwa kutoa majibu kwa wakati na kuwarahisishia wauzaji, kutoa huduma kwa haraka zaidi na kutoa majibu mda wowote 24/7.")
st.write("## Ni zana yenye ufanisi kwa biashara yoyote ile, kwani inamrahishia mfanya bishara kutoa majibu kwa watu wengi zaidi kwa wakati.")
# Create two columns
col1, col2 = st.columns([3, 1])

# Column 1: Image and Features
with col1:
    # Display Image
    st.image("servasadolph/whaiautoreply/blob/99e5cc328ae5c1d700b03b3aaaac060feafbe9d8/bot.PNG", caption="", use_column_width=True)

    # Functions of the App
    # Description of your App
    # st.write("# 🌟Vipengele")
    # st.write("## -📈Ukuaji wa Mazungumzo: Mauzo, Masoko na Usaidizi kwa Wafanyabiashara na Wateja kupitia Boti ya WhatsApp ya AI")
    # st.write("## -🔍Gundua Uwezo wa Sifa za Jukwaa Letu la Boti ya WhatsApp ya AI!")
    # st.write("## -🚨Msaada wa Kipaumbele (24/7) kupitia WhatsApp na Barua pepe kwa msaada.")
    st.write("")
    st.write("")
    # st.write("- Secure and Reliable")
    # st.write("- 24/7 Customer Support")
    
    # Indicate the price of the App
    #st.write("### Price: $5.99")

    # Payment Details
    st.write("# 💰Malipo")
    st.write("## -🏷️Bei: 30,000Tshs Full-Package")
    st.write("## -🗓️Uanachama: 10,000Tshs kwa Mwezi")
    st.write("## -🛒Kununua app, tuma malipo kwa nambari ya Mpesa iliyo hapa chini")
    st.write("## -📥Tuma muamala kupitia nambari ya WhatsApp iliyo hapa chini")
    st.write("## -🎯Mpesa: 0766331113")
    st.write("")
    st.write("")
    st.write("## Tazama Video hapo chini:")
    st.write("")

# Column 2: Price and Payment Details
# with col2:
#     # Indicate the price of the App
#     st.write("### Price: $5.99")

#     # Payment Details
#     st.write("## Payment")
#     st.write("To purchase the app, send the payment to the Mpesa number below.")
#     st.write("### Mpesa: 0766331113")

# Embed Youtube Video
st.video("https://youtu.be/SCKR0jd4aHg")

# Run the Streamlit app by navigating to your project directory in the terminal and running the command below:
# streamlit run app.py

# Footer
# Footer
st.markdown("""
<style>
    .footer {
        position: fixed; 
        left: 0; 
        bottom: 0; 
        width: 100%;
        background-color: black; 
        color: white; 
        text-align: center;
    }
   
</style>

<div class="footer">
    
### For Any Questions?
**WhatsApp:** +255 766331113  
**Email:** [servatechtips@gmail.com](mailto:servatechtips@gmail.com)

[YouTube](https://www.youtube.com/channel/UCWPagdH-POziaM_8w4w1B8Q)
© 2023 — Serva Tech. All Rights Reserved.
</div>
""", unsafe_allow_html=True)





