from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, classification_report

# function to evaluate model
def evaluate_model(y_true, y_pred):
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred)
    recall = recall_score(y_true, y_pred)
    f1 = f1_score(y_true, y_pred)

    print(f'Accuracy: {accuracy:.4f}')
    print(f'Precision: {precision:.4f}')
    print(f'Recall: {recall:.4f}')
    print(f'F1 Score: {f1:.4f}')

    # confusion matrix
    cm = confusion_matrix(y_true, y_pred)
    print('Confusion Matrix')
    print(cm)

    # classification report
    cr = classification_report(y_true, y_pred)
    print('Classification Report:')
    print(cr)

    return accuracy, precision, recall, f1

__all__ = ['evaluate_model']