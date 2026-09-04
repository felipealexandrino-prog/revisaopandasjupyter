import pandas as pd

dataframekingdom = pd.read_csv(r"c:\Users\Pichau\Downloads\mercado_reinos_medievais.csv")

dataframekingdom["total"] = dataframekingdom["preco"] * dataframekingdom["quantidade"]

print(dataframekingdom)

sales_quantity = dataframekingdom.shape

amount_sold = dataframekingdom["quantidade"].sum()

gold_total = dataframekingdom["total"].sum()


# PRODUCT INFORMATION

dataframe_product = dataframekingdom.groupby("produto").agg(

    Total_Gold_Produced=("total", "sum"),

    Quantity_Sold=("quantidade", "sum"),

    Average_Price=("preco", "mean"),

    Highest_Price=("preco", "max")

).reset_index().rename(columns={

    "produto": "Product"

}).sort_values(

    by="Total_Gold_Produced",

    ascending=False

)

print(f"\nDataframe for Products\n{dataframe_product}")

print(f"The total number of sales was {sales_quantity[0]}!")

print(f"{amount_sold} units were sold!")

print(f"The total gold generated in the kingdom was {gold_total} Golden Coins!")


# CATEGORY INFORMATION

dataframe_category = dataframekingdom.groupby("categoria").agg(

    Total_Gold=("total", "sum"),

    Total_Quantity=("quantidade", "sum")

).sort_values(

    by="Total_Gold",

    ascending=False

).reset_index()

print(f"\nDataframe for Categories\n{dataframe_category}")


top_sold_idx = dataframe_category["Total_Gold"].idxmax()

top_sold_category = dataframe_category.loc[top_sold_idx]

print(f"\nCategory that generated the most gold:\n{top_sold_category}")


top_quantity_idx = dataframe_category["Total_Quantity"].idxmax()

top_quantity_category = dataframe_category.loc[top_quantity_idx]

print(f"\nCategory with the most units sold:\n{top_quantity_category}")


# KINGDOM REPORT

dataframekingdom_report = dataframekingdom.groupby("reino").agg(

    gold_generated_per_kingdom=("total", "sum"),

    quantity_sold_per_kingdom=("quantidade", "sum")

).reset_index().rename(columns={

    "reino": "Kingdom"

})

print(f"\nKingdom Dataframe Report\n{dataframekingdom_report}")

top_kingdom_gold = dataframekingdom_report["gold_generated_per_kingdom"].idxmax()

dataframereport_topkingdom = dataframekingdom_report.loc[top_kingdom_gold]

print(f"\nKingdom with the highest gold movement:\n{dataframereport_topkingdom}")


# KNIGHT REPORT

dataframeknight_report = dataframekingdom.groupby("cavaleiro").agg(

    revenue_per_knight=("total", "sum"),

    quantity_per_knight=("quantidade", "sum")

).reset_index()

top_knight_sales = dataframeknight_report["revenue_per_knight"].idxmax()

dfreport_topknight = dataframeknight_report.loc[top_knight_sales]

print(f"\nReport of the Knights of the Kingdom:\n{dataframeknight_report}")

print(f"\nThe Knight with the Highest Sales:\n{dfreport_topknight}")


# INDIVIDUAL SALES

top5_sales_df = dataframekingdom.nlargest(5, "total")

print(f"\nTOP 5 LARGEST SALES\n{top5_sales_df}")
with pd.ExcelWriter("Kingdom_Report.xlsx") as writer:
    dataframekingdom.to_excel(writer,index=False,sheet_name="General_Report_Table"),
    dataframe_product.to_excel(writer,index=False,sheet_name="Product_Report_Table"),
    dataframe_category.to_excel(writer,index=False,sheet_name="Category_Report_Table"),
    dataframekingdom_report.to_excel(writer,index=False,sheet_name="Report_Per_Kingdom_Table")
    dataframeknight_report.to_excel(writer,index=False,sheet_name="Knight_Report_Table")