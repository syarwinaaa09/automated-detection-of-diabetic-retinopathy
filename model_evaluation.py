import numpy as np
from cnn_architecture import model
from normalisation_augmentation import validation_generator
from defining_evaluation_metrics import evaluate_model

# generate predictions on the test set
y_pred_prob = model.predict(validation_generator)
y_pred = np.round(y_pred_prob).astype(int)

# true labels
y_true = validation_generator.classes

# evaluate the model
accuracy, precision, recall, f1 = evaluate_model(y_true, y_pred)