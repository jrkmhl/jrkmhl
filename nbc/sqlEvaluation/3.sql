select
order_month,
Customer_Segment,
sum(Order_Qty) over(partition by order_month,Customer_Segment order by order by Order_ID rows between unbounded preceding and current row) as cum_ord_qty_cs_m,
sum(sales) over(partition by order_month,Customer_Segment order by order by Order_ID rows between unbounded preceding and current row) as cum_sales_cs_m

from salesstore ss
