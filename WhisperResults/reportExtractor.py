# Whisper-Features Extractor

# Histogram Range: 
# Deep4SNet ->
# ResNet18 -> -1 to 1
# RawPC -> 0 to 1
# RawNet2 -> 0 to 1
# Whisper -> 0 to 1

import sys
import numpy as np
from sklearn.metrics import roc_auc_score, roc_curve

def tpr_at_max_fpr(y_true, y_score, max_fpr=0.05):
    fpr, tpr, _ = roc_curve(y_true, y_score, drop_intermediate=False)
    closest_index = np.argmin(np.abs(fpr - max_fpr))
    tpr_at_target_fpr = tpr[closest_index]
    #index = np.argmax(fpr > max_fpr) - 1
    return tpr_at_target_fpr

file_path = "/home/soumyas_kvmohan/whisper-features/results/" + sys.argv[1]

y_pred_proba = []
y_test = []

truePositive = 0
falsePositive = 0
falseNegative = 0
trueNegative = 0

with open(file_path, 'r') as file:
    for line in file:
        line = line.split()
        if line[2] == "bonafide" and float(line[3])>0.5:
            truePositive += 1
        elif line[2] == "bonafide" and float(line[3])<=0.5:
            falseNegative +=1
        elif line[2] == "spoof" and float(line[3])<=0.5:
            trueNegative +=1
        else:
            falsePositive += 1
with open(file_path, "r") as file:
    for line in file:
        score = float(line.strip().split()[3])
        y_pred_proba.append(score)

with open(file_path, "r") as file:
    for line in file:
        if len(y_test) >= len(y_pred_proba):
            break
        realclass = 0 if line.strip().split()[2] == "spoof" else 1
        y_test.append(realclass)

roc_auc_score1 = roc_auc_score(y_test, y_pred_proba)

print("Accuracy:", round(100 * (truePositive+trueNegative)/(truePositive+trueNegative+falsePositive+falseNegative), 2), "%")
print("Precision:", round(100 * truePositive/(truePositive+falsePositive), 2), "%")
print("Recall:", round(100 * truePositive/(truePositive+falseNegative), 2), "%")
print("Specificity:", round(100 * trueNegative/(trueNegative+falsePositive), 2), "%")
print("F1 Score:", round(100 * 2 * truePositive/(2*truePositive+falsePositive+falseNegative), 2), "%")
print("ROC AUC Score:", round(roc_auc_score1, 3))
print("TPR@ 0.05 FPR  :", round(tpr_at_max_fpr(y_test, y_pred_proba, 0.05), 4))

print("TP:", truePositive)
print("FP:", falsePositive)
print("FN:", falseNegative)
print("TN:", trueNegative)
