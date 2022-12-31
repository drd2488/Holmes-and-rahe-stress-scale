import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Holmes and Rahe Stress Calculator")

# Create a dictionary with the stress scores
stress_scores = {
    "Death of a spouse": 100,
    "Divorce": 73,
    "Marital separation": 65,
    "Imprisonment": 63,
    "Death of a close family member": 63,
    "Personal injury or illness": 53,
    "Marriage": 50,
    "Dismissal from work": 47,
    "Marital reconciliation": 45,
    "Retirement": 45,
    "Change in health of family member": 44,
    "Pregnancy": 40,
    "Sexual difficulties": 39,
    "Gain a new family member": 39,
    "Business readjustment": 39,
    "Change in financial state": 38,
    "Death of a close friend": 37,
    "Change to different line of work": 36,
    "Change in frequency of arguments": 35,
    "Major mortgage": 32,
    "Foreclosure of mortgage or loan": 30,
    "Change in responsibilities at work": 29,
    "Child leaving home": 29,
    "Trouble with in-laws": 29,
    "Outstanding personal achievement": 28,
    "Spouse starts or stops work": 26,
    "Beginning or end of school": 26,
    "Change in living conditions": 25,
    "Revision of personal habits": 24,
    "Trouble with boss": 23,
    "Change in working hours or conditions": 20,
    "Change in residence": 20,
    "Change in schools": 20,
    "Change in recreation": 19,
    "Change in church activities": 19,
    "Change in social activities": 18,
    "Minor mortgage or loan": 17,
    "Change in sleeping habits": 16,
    "Change in number of family reunions": 15,
    "Change in eating habits": 15,
    "Vacation": 13,
    "Major Holiday": 12,
    "Minor violation of law": 11
}

# Create a list of stressors that the user can select from
stressor_list = list(stress_scores.keys())


# Create a function to calculate the stress score
def calculate_stress_score():
    # Get the selected stressors
    selected_stressors = [stressor_list[i] for i in stressor_listbox.curselection()]

    # Calculate the stress score
    stress_score = sum(stress_scores[stressor] for stressor in selected_stressors)

    # Display the stress score and a message based on the stress score
    if stress_score > 300:
        result_label.configure(text=f"Stress Score: {stress_score}\nAt risk of illness.")
    elif 150 <= stress_score <= 299:
        result_label.configure(text=f"Stress Score: {stress_score}\nRisk of illness is moderate (reduced by 30% from the above risk).")
    elif stress_score < 150:
        result_label.configure(text=f"Stress Score: {stress_score}\nOnly have a slight risk of illness.")

# Create the frame for the stressors
stressor_frame = tk.Frame(window)

# Create the listbox for the stressors
stressor_listbox = tk.Listbox(stressor_frame, selectmode=tk.MULTIPLE, height=10)
for stressor in stressor_list:
    stressor_listbox.insert(tk.END, stressor)

# Create the Calculate button
calculate_button = tk.Button(window, text="Calculate", command=calculate_stress_score)

# Create the result label
result_label = tk.Label(window)

# Create the horizontal scrollbar for the listbox
h_scrollbar = tk.Scrollbar(stressor_frame, orient=tk.HORIZONTAL)
h_scrollbar.pack(side=tk.BOTTOM, fill=tk.X)
h_scrollbar.config(command=stressor_listbox.xview)
stressor_listbox.config(xscrollcommand=h_scrollbar.set)

# Create the vertical scrollbar for the listbox
v_scrollbar = tk.Scrollbar(stressor_frame, orient=tk.VERTICAL)
v_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
v_scrollbar.config(command=stressor_listbox.yview)
stressor_listbox.config(yscrollcommand=v_scrollbar.set)

# Pack the widgets
stressor_listbox.pack(side=tk.LEFT, fill=tk.BOTH)
stressor_frame.pack()
calculate_button.pack()
result_label.pack()

# Run the main loop
window.mainloop()
