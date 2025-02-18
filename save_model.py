# save_model.py
import joblib

# Load your trained model from NID.py
from NID import rf_model  # Make sure rf_model is the name of your trained model

# Save the model
model_filename = 'intrusion_detection_model.pkl'
joblib.dump(rf_model, model_filename)
print(f"Model saved as {model_filename}")




# how to run :python3 save_model.py
