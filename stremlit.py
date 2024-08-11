import streamlit as st

# Set the app title
st.set_page_config(page_title="employment")

# Add a title
st.title(" وظائف حديثين التخرج في سوق العمل السعودي ")

# Add a statement
statement = "  كحديث تخرج يبحث عن عمل  كان عندي فضول كم نسبة الوظائف اللي تطلب  حديث تخرج و  وما هي اكثر مدينه فيها وظائف عملت تحليل لبيانات منصة جدارة و كانت اعلى نسبة توظيف في الرياض بفرق شاسع عن باقي مدن المملكه وتليها مدينة جدة حيث انه تقريبا 50% من الوظائف في هذه المدينتين و تتشارك باقي مدن المملكه في باقي  النسبه "
st.write(statement)

image = "cities.png"
st.image(image, caption="نسبة اعلانات التوظيف في مدن المملكه ")


# Add a statement
statement = "ما يقارب 60% من اعلانات التوظيف تستهدف حديثين التخرج "
st.write(statement)

# Add an image
image = "نسبة الطلب.png"
st.image(image, caption="نسبة التوظيف  على حسب سنوات الخبره ")



# Add a statement
statement = "كانت الرواتب تتراوح في حدود 5803 ريال حيث ان اكثر راتب كان 8803 و اقل راتب 3000  "
st.write(statement)

# Add an image
image = "range.png"
st.image(image, caption="رواتب حديثين التخرج ")

# Add a statement
statement = "صح رواتبنا كحديثين تخرج تعتبر قليله و نادر ما نحصل احد راتبه عالي لكن كانت فيه اعلانات  وظائف طالبه ناس لهم خبره براتب قريب من رواتب حديثين التخرج "
st.write(statement)
st.text('وزي ما قالو من شاف مصيبة غيره هانت عليه مصيبته')
# Add an image
image = "exper and salary.png"
st.image(image, caption="")


