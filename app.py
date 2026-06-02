from flask import Flask, render_template, request

app = Flask(__name__)

# HOME PAGE
@app.route('/')
def home():
    return render_template('index.html')


# SYMPTOMS PAGE
@app.route('/symptoms')
def symptoms():
    return render_template('symptom.html')


# FEATURES PAGE
@app.route('/features')
def features():
    return render_template('features.html')


# ABOUT PAGE
@app.route('/about')
def about():
    return render_template('about.html')


# CONTACT PAGE
@app.route('/contact')
def contact():
    return render_template('contact.html')


# RESULT PAGE
@app.route('/result', methods=['POST'])
def result():

    selected_symptoms = request.form.getlist('symptoms')

    symptom_advice = {

        'Fever': '🌡️ Fever: Fever may occur with infections or other illnesses. Rest, drink enough fluids, and keep the body cool with light clothing and a cool environment. Mild fever may improve with rest and hydration, but persistent or high fever should be medically evaluated.',

        'Vomiting': '🤮 Vomiting: Take plenty of fluids to avoid dehydration. ORS solution is recommended if available. Seek medical attention if vomiting becomes severe or persistent.',

        'Headache': '🤕 Headache: Headaches can occur with stress, dehydration, infections, or other medical conditions. Rest, drink enough water, and avoid excessive stress or noise. Seek medical attention if headaches become severe, persistent, or are associated with other serious symptoms.',

        'Diarrhea': '🚽 Diarrhea: Drink plenty of fluids such as water and ORS solution to help replace lost fluids and electrolytes. Avoid foods or drinks that may worsen symptoms, including very sugary drinks or oily foods. Soft foods such as bread, rice, and other light meals may help during recovery. Seek medical attention if symptoms become severe or persistent.',

        'Stomach Pain': '🤢 Stomach Pain: Abdominal pain can have different causes, including indigestion, infection, or food-related illness. Rest, drink enough water, and avoid heavy or spicy foods until symptoms improve. If the pain becomes severe, persistent, or is associated with vomiting, fever, or difficulty breathing, seek medical attention promptly.',

        'Nausea': '🥴 Nausea: Nausea can occur with different illnesses, including digestive infections or food-related conditions. Drink plenty of fluids such as water to stay hydrated. Some people may tolerate fruits, smoothies, or light foods as symptoms improve. Avoid heavy, oily, or irritating foods until you feel better. Seek medical attention if symptoms become severe or persistent.',

        'Fatigue': '😴 Fatigue: Weakness or fatigue may occur during illness or dehydration. Ensure proper rest, drink enough fluids, and maintain light nutritious meals or fruits if tolerated. Persistent or worsening fatigue should be medically evaluated.',

        'Loss of Appetite': '🍽️ Loss of Appetite: Loss of appetite can occur during many illnesses. Rest and try small light meals gradually as tolerated. Drink enough fluids and monitor symptoms. Seek medical attention if appetite loss becomes severe or continues for several days.'
    }

    advice_list = []

    for symptom in selected_symptoms:
        if symptom in symptom_advice:
            advice_list.append(symptom_advice[symptom])

    return render_template(
        'result.html',
        symptoms=selected_symptoms,
        advice=advice_list
    )


if __name__ == '__main__':
    app.run(debug=True)