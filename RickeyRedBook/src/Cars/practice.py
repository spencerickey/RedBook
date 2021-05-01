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

col_names = ['transmission', 'odometer', 'year', 'fuel_type', 'type', 'price']

cars = pd.read_csv('p3.csv', header=None, names=col_names)

cars.head()

feature_cols = ['transmission', 'odometer', 'year', 'fuel_type', 'type']

X = cars[feature_cols]
y = cars.price

# Split the dataset. Test will be 30%, train 70%, using shuffler 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

clf = DecisionTreeClassifier(criterion="entropy", max_depth=5, splitter="random" , max_features=4)

clf = clf.fit(X_train, y_train)

y_predict = clf.predict(X_test)

accuracy = metrics.accuracy_score(y_test, y_predict)

print("Accuracy: ", accuracy)
dotfile = StringIO()

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
graph = pydotplus.graph_from_dot_data(dotfile.getvalue())
graph.write_svg('cars.svg')
i = Image(graph.create_svg())

transmission = input("Enter transmission type (manual or automatic): ")
odometer = int(input("Enter engine odometer in kilometers: "))
print("odometer: ",odometer//25000)
year = int(input("Enter year manufactured: "))
fuel_type = input("Enter fuel type (gasoline or diesel)(0 or 1): ")
btype = input("Enter body type (sedan or hatchback)(0 or 1): ")

p = {'transmission': [transmission],
     'odometer': [odometer],
     'year': [year], 'fuel_type': [fuel_type], 'type': [btype]}

predict = pd.DataFrame(p)
print(predict)
answer = clf.predict(predict)
print("\nWith", (round(accuracy, 3) * 100), "% certainty, your car is a class", answer[0])

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
