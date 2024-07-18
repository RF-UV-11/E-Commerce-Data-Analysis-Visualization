from flask import Flask, render_template
from modules import *

app = Flask(__name__)

# start postgres connection
postgressConn = postgresConnection()
conn = postgressConn.makePostgresConnection()

# Generate figures
totalAmountByProductCategory = totalAmountByProductCategory(conn)
totalAmountByProductCategory_df = totalAmountByProductCategory.makeDataFrameFromQuery()
totalAmountByProductCategoryFig = totalAmountByProductCategoryFig()
totalAmountByProductCategoryFig = totalAmountByProductCategoryFig.makeFig(totalAmountByProductCategory_df)

inventorySizeByProductByCountry = inventorySizeByProductByCountry(conn)
inventorySizeByProductByCountry_df = inventorySizeByProductByCountry.makeDataFrameFromQuery()
inventorySizeByProductByCountryFig = inventorySizeByProductByCountryFig()
inventorySizeByProductByCountryFig = inventorySizeByProductByCountryFig.makeFig(inventorySizeByProductByCountry_df)

databaseClassDiagram = databaseClassDiagram(conn)
databaseClassDiagram_info = databaseClassDiagram.makeRelationInfo()
databaseClassDiagramFig = databaseClassDiagramFig()
databaseClassDiagramFig = databaseClassDiagramFig.makeFig(databaseClassDiagram_info)

averagePriceRateByCountry = averagePriceRateByCountry(conn)
averagePriceRateByCountry_df = averagePriceRateByCountry.makeDataFrameFromQuery()
averagePriceRateByCountryFig = averagePriceRateByCountryFig()
averagePriceRateByCountryFig = averagePriceRateByCountryFig.makeFig(averagePriceRateByCountry_df)

customerCountByCountry = customerCountByCountry(conn)
customerCountByCountry_df = customerCountByCountry.makeDataFrameFromQuery()
customerCountByCountryFig = customerCountByCountryFig()
customerCountByCountryFig = customerCountByCountryFig.makeFig(customerCountByCountry_df)

customerRegistrationByCountry = customerRegistrationByCountry(conn)
customerRegistrationByCountry_df = customerRegistrationByCountry.makeDataFrameFromQuery()
customerRegistrationByCountryFig = customerRegistrationByCountryFig()
customerRegistrationByCountryFig = customerRegistrationByCountryFig.makeFig(customerRegistrationByCountry_df)

distributorCountByCountry = distributorCountByCountry(conn)
distributorCountByCountry_df = distributorCountByCountry.makeDataFrameFromQuery()
distributorCountByCountryFig = distributorCountByCountryFig()
distributorCountByCountryFig = distributorCountByCountryFig.makeFig(distributorCountByCountry_df)

totalAmountByYear = totalAmountByYear(conn)
totalAmountByYear_df = totalAmountByYear.makeDataFrameFromQuery()
totalAmountByYearFig = totalAmountByYearFig()
totalAmountByYearFig = totalAmountByYearFig.makeFig(totalAmountByYear_df)

totalSalesByCountry = totalSalesByCountry(conn)
totalSalesByCountry_df = totalSalesByCountry.makeDataFrameFromQuery()
totalSalesByCountryFig = totalSalesByCountryFig()
totalSalesByCountryFig = totalSalesByCountryFig.makeFig(totalSalesByCountry_df)

totalSalesByDistributor = totalSalesByDistributor(conn)
totalSalesByDistributor_df = totalSalesByDistributor.makeDataFrameFromQuery()
totalSalesByDistributorFig = totalSalesByDistributorFig()
totalSalesByDistributorFig = totalSalesByDistributorFig.makeFig(totalSalesByDistributor_df)

# close postgres connection
postgressConn.closePostgresConnection()


# figures
figures = {
    "Class Diagram" : databaseClassDiagramFig,
    "Total Amount By Product Category": totalAmountByProductCategoryFig,
    "Inventory Size By Product By Country" : inventorySizeByProductByCountryFig,
    "Average Price Rate By Country" : averagePriceRateByCountryFig,
    "Customer Count By Country" : customerCountByCountryFig,
    "Customer Registration By Country" : customerRegistrationByCountryFig,
    "Distributor Count By Country" : distributorCountByCountryFig,
    "Total Sales By Year" : totalAmountByYearFig,
    "Total Sales By Country" : totalSalesByCountryFig,
    "Total Sales By Distributor" : totalSalesByDistributorFig

}

@app.route('/')
def index():
    """
    Renders the index page with a list of figure names.

    Returns
    -------
    str
        Rendered HTML template for the index page.
    """
    figure_names = list(figures.keys())
    return render_template('index.html', figures=figure_names)

@app.route('/figure/<name>')
def figure(name):
    """
    Renders the specified figure in an HTML template.

    Parameters
    ----------
    name : str
        The name of the figure to render.

    Returns
    -------
    str
        Rendered HTML template for the figure page if the figure exists.
        Otherwise, returns a 404 error message.
    """
    fig = figures.get(name)
    if fig:
        fig.write_html("templates/plot.html")
        return render_template('plot.html')  # Render the saved plot.html
    return "Figure not found", 404

if __name__ == '__main__':
    app.run(debug=True)
