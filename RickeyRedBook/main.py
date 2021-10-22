import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.tree import export_graphviz
import sklearn.externals
from IPython.display import Image
from IPython import display
import pydotplus
from sklearn import tree
from io import StringIO
import pydot

def main():
    # Define the column names because p3.csv doesn't have headers
    col_names = ['transmission', 'odometer',
                    'year', 'fuel_type', 'type', 'price']

    # Read the csv file 
    cars = pd.read_csv('p3.csv', header=None, names=col_names)

    # The feature headers won't include price
    feature_cols = ['transmission', 'odometer',
                    'year', 'fuel_type', 'type']
    # Split the dataset into two parts, one with features, one with the prices
    X = cars[feature_cols]
    y = cars.price

    # Split the datasets into training and testing data.
    # The training set will be 1/5 of the whole dataset. 
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=1)

    # Initialize our decision tree classifier
    # I found entropy and a max-depth of 5 or 6 to yield the highest accuracy.
    clf = DecisionTreeClassifier(
        criterion="entropy", max_depth=6, splitter="random", max_features=4)

    # Train the classifier
    clf = clf.fit(X_train, y_train)

    # Test the rest of the data and then see how accurate the model is.
    y_predict = clf.predict(X_test)
    accuracy = metrics.accuracy_score(y_test, y_predict)

    # Format the accuracy
    accuracy = "{:2.2%}".format(accuracy)

    # Tell the user what the accuracy is today
    print("Accuracy: ", accuracy)
    
    # Init the dotfile to use in saving the svg image
    dotfile = StringIO()

    # Save the tree using GraphViz
    tree.export_graphviz(
        decision_tree=clf,
        out_file=dotfile,
        feature_names=feature_cols,
        filled=True,
        # leaves_parallel=True,
        rounded=True,
        label=all,
        max_depth=20,
        proportion=True,
        special_characters=True,
        precision=3,
    )
    # Get the graph from the dotfile
    graph = pydotplus.graph_from_dot_data(dotfile.getvalue())
    # Save the graph of the tree as 'cars.svg'
    graph.write_svg('cars.svg')
    
    # i = Image(graph.create_svg()) # Optional... use for image display
    
    # Initailize the variables to store the user's input for the prediction feature
    transmission, odometer, fuel_type, year, m, btype = '', '', '', '', True, ''

    # Gather user input for the five fields and validate.
    while transmission not in ['1','0']:
        transmission = input("Enter transmission type (manual or automatic)(0 or 1): ")
        if transmission == None:
            print("You must enter the transmission type.")
        if transmission not in ['0','1']:
            print("You made an invalid selection.")

    while not (odometer).isdigit():
        odometer = input("Enter engine odometer in kilometers: ")
        if odometer == None:
            print("You must enter the odometer value.")
        
    # Turn odometer into a category, each 25,000 kilometers is a category    
    odometer = int(odometer)//25000

    while (not year.isdigit()) or (not m):
        year = input("Enter year manufactured: ")
        if not year:
            print("You must enter a valid year.")
            m = False
        elif int(year) > 2019 or int(year) < 1960:
            print("You must enter a value year between 1960 and 2019.")
            m = False
        else:
            m = True

    while fuel_type not in ['0','1']:
        fuel_type = input("Enter fuel type (gasoline or diesel)(0 or 1): ")
        if not fuel_type:
            print("You must enter a valid fuel type.")
        if fuel_type not in ['0','1']:
            print("You must enter a valid fuel type.")

    while btype not in ['0', '1']:
        btype = input("Enter body type (sedan or hatchback)(0 or 1): ")
        if not btype:
            print("You must enter a valid body style.")
        if btype not in ['1','0']:
            print("You must choose 1 or 0 for body type.")

    p = {'transmission': [transmission],
            'odometer': [odometer],
            'year': [year], 'fuel_type': [fuel_type], 'type': [btype]}

    # Make a dataframe of the data to predict.
    predict = pd.DataFrame(p)
    # Show the parsed data to the user.
    print("Data parsed into categories:\n", predict)

    # Make the prediction, which will return a price category (with values from 0 - 10).
    answer = clf.predict(predict)

    # Tell the user the predicted price category.
    print("\nWith %s certainty, your car is a price category: %d" % (accuracy,  answer[0]))

    # Explain what the category means.
    if answer[0] == 0:
        print("This means your car is worth between $0-$5000...")
    elif answer[0] == 1:
        print("This means your car is worth between $5001-$10000...")
    elif answer[0] == 2:
        print("This means your car is worth between $10001-$15000...")
    elif answer[0] == 3:
        print("This means your car is worth between $15001-$20000...")
    elif answer[0] == 4:
        print("This means your car is worth between $20001-$25000...")
    elif answer[0] == 5:
        print("This means your car is worth between $25001-$30000...")
    elif answer[0] == 6:
        print("This means your car is worth between $30001-$35000...")
    elif answer[0] == 7:
        print("This means your car is worth between $35001-$40000...")
    elif answer[0] == 8:
        print("This means your car is worth between $40001-$45000...")
    elif answer[0] == 9:
        print("This means your car is worth between $45001-$50000...")
    elif answer[0] == 10:
        print("This means your car is worth more than %50000...")
    print("\n")
if __name__ == '__main__':
    print("Starting RickeyRedBook...")
    main()

