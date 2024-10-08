import csv
import sys

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    # print('ev', evidence)
    # print('labels', labels)
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    ans_evidence = []
    ans_labels = []
    with open(filename) as f:
        reader = csv.DictReader(f)
        for row in reader:
            evidence = []
            labels = []
            for index, i in enumerate(row):
                if index in [0, 2, 4, 11, 12, 13, 14]:
                    evidence.append(int(row[i]))
                elif index in [1, 3, 5, 6, 7, 8, 9]:
                    evidence.append(float(row[i]))
                elif index == 10:
                    for ind, j in enumerate(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'June', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']):
                        if row[i] == j:
                            evidence.append(ind)
                elif index == 15:
                    evidence.append(1 if row[i] == 'Returning_Visitor' else 0)
                elif index == 16:
                    evidence.append(0 if row[i] == 'FALSE' else 1)
                if index == len(row) - 1:
                    ans_labels.append(0 if row[i] == 'FALSE' else 1)
            ans_evidence.append(evidence)
    return (ans_evidence, ans_labels)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    neigh = KNeighborsClassifier(n_neighbors=1)
    neigh.fit(evidence, labels)
    return neigh


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    sensivity = 0
    specifity = 0 
    sensivity_counter = 0
    specifity_counter = 0
    for index, p in enumerate(predictions):
        if p == 0:
            if p == labels[index]:
                specifity += 1
        else: 
            if p == labels[index]:
                sensivity += 1
        if labels[index] == 1:
            sensivity_counter += 1
        else:
            specifity_counter += 1
            
    print('sens', sensivity, 'sens_count', sensivity_counter)
    
    return (sensivity/sensivity_counter, specifity/specifity_counter)


if __name__ == "__main__":
    main()
