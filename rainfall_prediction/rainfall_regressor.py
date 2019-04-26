import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def rain_predictor():

    dataset = pd.read_csv('project_sheet.csv')
    x = dataset.iloc[:-1, 0:1].values
    y_june = dataset.iloc[:-1, 1:2  ].values
    y_july = dataset.iloc[:-1, 2:3  ].values
    y_august = dataset.iloc[:-1, 3:4  ].values
    y_september = dataset.iloc[:-1, 4:5  ].values
    y_october = dataset.iloc[:-1, 5:6  ].values
    z = dataset.iloc[4:5, 0:1].values

    from sklearn.linear_model import LinearRegression
    lin_reg_june = LinearRegression()
    lin_reg_june.fit(x, y_june)
    lin_reg_july = LinearRegression()
    lin_reg_july.fit(x, y_july)
    lin_reg_august = LinearRegression()
    lin_reg_august.fit(x, y_august)
    lin_reg_september = LinearRegression()
    lin_reg_september.fit(x, y_september)
    lin_reg_october = LinearRegression()
    lin_reg_october.fit(x, y_october)


    from sklearn.preprocessing import PolynomialFeatures
    poly_reg = PolynomialFeatures( degree = 4)
    poly_reg_june = PolynomialFeatures( degree = 4 )
    poly_reg_july = PolynomialFeatures( degree = 4 )
    poly_reg_august = PolynomialFeatures( degree = 4 )
    poly_reg_september = PolynomialFeatures( degree = 4 )
    poly_reg_october = PolynomialFeatures( degree = 4 )
    x_poly = poly_reg.fit_transform(x)

    poly_reg_june.fit(x_poly, y_june)
    lin_reg_june_2 = LinearRegression()
    lin_reg_june_2.fit(x_poly, y_june)

    poly_reg_july.fit(x_poly, y_july)
    lin_reg_july_2 = LinearRegression()
    lin_reg_july_2.fit(x_poly, y_july)

    poly_reg_august.fit(x_poly, y_august)
    lin_reg_august_2 = LinearRegression()
    lin_reg_august_2.fit(x_poly, y_august)

    poly_reg_september.fit(x_poly, y_september)
    lin_reg_september_2 = LinearRegression()
    lin_reg_september_2.fit(x_poly, y_september)

    poly_reg_october.fit(x_poly, y_october)
    lin_reg_october_2 = LinearRegression()
    lin_reg_october_2.fit(x_poly, y_october)

    #
    # plt.scatter(x, y_june, color = 'red')
    # plt.plot(x, lin_reg_june.predict(x), color = 'blue')
    # plt.title('June vs Rainfall ')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #

    lin_pred_june = lin_reg_june.predict(z)

    #
    # plt.scatter(x, y_july, color = 'red')
    # plt.plot(x, lin_reg_july.predict(x), color = 'blue')
    # plt.title('July vs Rainfall ')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #
    lin_pred_july = lin_reg_july.predict(z)

    #
    # plt.scatter(x, y_august, color = 'red')
    # plt.plot(x, lin_reg_august.predict(x), color = 'blue')
    # plt.title('August vs Rainfall ')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #
    lin_pred_august = lin_reg_august.predict(z)

    #
    # plt.scatter(x, y_september, color = 'red')
    # plt.plot(x, lin_reg_september.predict(x), color = 'blue')
    # plt.title('September vs Rainfall ')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #
    lin_pred_september = lin_reg_september.predict(z)

    #
    # plt.scatter(x, y_october, color = 'red')
    # plt.plot(x, lin_reg_october.predict(x), color = 'blue')
    # plt.title('October vs Rainfall ')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #
    lin_pred_october = lin_reg_october.predict(z)


    linear_prediction = {'June':lin_pred_june,'July':lin_pred_july,'August':lin_pred_august,'September':lin_pred_september,'October':lin_pred_october}


    #
    # x_grid = np.arange(min(x), max(x), 0.1)
    # x_grid = x_grid.reshape((len(x_grid), 1))
    # plt.scatter(x, y_june, color = 'red')
    # plt.plot(x_grid, lin_reg_june_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
    # plt.title(' June vs Rainfall (Polynomial Regression)')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #

    poly_pred_june = lin_reg_june_2.predict(poly_reg_june.fit_transform(z))

    #
    # x_grid = np.arange(min(x), max(x), 0.1)
    # x_grid = x_grid.reshape((len(x_grid), 1))
    # plt.scatter(x, y_july, color = 'red')
    # plt.plot(x_grid, lin_reg_july_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
    # plt.title(' July vs Rainfall (Polynomial Regression)')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #

    poly_pred_july = lin_reg_july_2.predict(poly_reg_july.fit_transform(z))

    #
    # x_grid = np.arange(min(x), max(x), 0.1)
    # x_grid = x_grid.reshape((len(x_grid), 1))
    # plt.scatter(x, y_august, color = 'red')
    # plt.plot(x_grid, lin_reg_august_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
    # plt.title(' August vs Rainfall (Polynomial Regression)')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #

    poly_pred_august = lin_reg_august_2.predict(poly_reg_august.fit_transform(z))

    #
    # x_grid = np.arange(min(x), max(x), 0.1)
    # x_grid = x_grid.reshape((len(x_grid), 1))
    # plt.scatter(x, y_september, color = 'red')
    # plt.plot(x_grid, lin_reg_september_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
    # plt.title(' September vs Rainfall (Polynomial Regression)')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #

    poly_pred_september = lin_reg_september_2.predict(poly_reg_september.fit_transform(z))

    #
    # x_grid = np.arange(min(x), max(x), 0.1)
    # x_grid = x_grid.reshape((len(x_grid), 1))
    # plt.scatter(x, y_october, color = 'red')
    # plt.plot(x_grid, lin_reg_october_2.predict(poly_reg.fit_transform(x_grid)), color = 'blue')
    # plt.title(' October vs Rainfall (Polynomial Regression)')
    # plt.xlabel('Year')
    # plt.ylabel('Rainfall in mm')
    # plt.show()
    #

    poly_pred_october = lin_reg_october_2.predict(poly_reg_october.fit_transform(z))


    polynomial_prediction = {'June':poly_pred_june, 'July':poly_pred_july, 'August':poly_pred_august, 'September':poly_pred_september, 'October':poly_pred_october }

    return (linear_prediction,polynomial_prediction)
