import streamlit
streamlit.set_page_config(page_title="EaseMigraine", page_icon="🧠", layout="centered")
streamlit.markdown("<b style='color:#008080;'>This is bold teal text</b>", unsafe_allow_html=True)

streamlit.title("EaseMigraine")

streamlit.subheader("Get daily health tips based on your lifestyle")





streamlit.write("Migraines are intense offen recurring headaches usually assiciated with nausea,vomiting,light sensitivity and in some cases visual   diturbances.Migraines is a result of lifestyle imbalance,poor digestion,stress or vascular disfunction")
streamlit.image("https://narainhospital.com/wp-content/uploads/2022/11/Migraine-Narain-Hospital-1024x576.jpg", width=300)

sleep = streamlit.slider("How many hours do you sleep daily?", 0, 12, 6)

water = streamlit.slider("Glasses of water per day", 0, 15, 4)

screen_time = streamlit.slider("Screen time (in hours)", 0, 15, 6)

exercise = streamlit.radio("Do you exercise regularly?", ["Yes", "No"])

meals = streamlit.radio("Do you skip meals?", ["Often", "Rarely", "Never"])



if streamlit.button("Prevention Tips"):
    if sleep < 6:
        streamlit.warning("Try to get at least 7-8 hours of sleep.")
    if water < 7:
        streamlit.info("Increase your water intake to avoid dehydration.")
    if screen_time > 6:
        streamlit.warning("Limit screen time and manage eye strain.")
    if meals == "Often":
        streamlit.error("Skipping meals and long gaps between eating can trigger migraine.")

streamlit.subheader("Practice stress management: Walking in nature,creating hobbies")

streamlit.subheader("HOW TO MANAGE ?")
 
streamlit.write("**Eliminate migraine triggers**")
streamlit.write("~ Caffeine,Cheese,Chocolate,Refined Sugar,Alcohol,Processed Foods and sometimes cold foods also")

streamlit.write("**Diet Therapy**")
streamlit.write("1. Anti-inflammatory and alkaline foods")
streamlit.write("~ Leafy Greens (spinach,methi)")
streamlit.write("~ Cruciferous Vegetables (broccoli,cabage)") 
streamlit.write("~ Cucumber,Bottle Gourd(lauki),Ridge Gourd(turai)")
streamlit.write("2. Fresh Froots")
streamlit.write("~ Apple,Pear,Watermelon,Pomegranate,Papaya,Banana(only if not a trigger)")
streamlit.write("3. Whole Grains")
streamlit.write("~ Brown Rice, Millets(Ragi,Jowar,Bajra),Oats")
streamlit.write("4. Healthy Fats")
streamlit.write("~ Flaxseeds, Chea seeds,Wallnuts")
streamlit.write("~ Cold Pressed Oils(Olive,coconut in moderations)")
streamlit.write("5. Hydrating Foods")
streamlit.write("~ Coconut Water,Cucumber,Soaked Raisins")
streamlit.write("~ Herbal Teas")
streamlit.write("6. Detox and Liver Supporting Foods")
streamlit.write("~ Amla,Termuric,Garlic,Lemon Water,Coriander Seed Water")


streamlit.write("**Hydro Therapy**")
streamlit.write("~Cold compress on forehead and eyes — for pain relief.")

streamlit.write("~Hot foot bath + cold compress on head — draws blood from the head, reducing congestion.")

streamlit.write("~Enema — helps relieve constipation (a common migraine trigger.)")

streamlit.write("**Yoga Therapy**")

streamlit.write("~Shashankasana (Child’s Pose)")

streamlit.write("~Setu Bandhasana (Bridge Pose)")

streamlit.write("~Matsyasana (Fish Pose)")

streamlit.write("**Pranayama**")









