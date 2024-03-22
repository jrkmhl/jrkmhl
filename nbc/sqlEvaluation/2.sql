select
ordr_smry.order_month,
ordr_smry.product_name,
ordr_smry.product_category,
ordr_smry.product_category,
cumulative_by_month.cumulative_sum_by_month
	from
(select ss.order_month,
	pd.product_name,
	pd.product_category,
	pd.product_category,
	sum(Order_Quantity) as order_qty
from salesstore ss
left join product pd on ss.product_name and pd.product_name
group by  ss.order_month,pd.product_name,pd.product_category,pd.product_category
)ordr_smry
left join
(select
order_month,
sum(ordr_qty_by_month) over(order by order_month desc rows between unbounded preceding and current row) as  cumulative_sum_by_month
from
(select
order_month,
sum(Order_Quantity) as ordr_qty_by_month,
from salesstore group by salesstore)sales_per_month
)cumulative_by_month on ordr_smry.order_month =cumulative_by_month.order_month