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