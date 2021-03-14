select
	ra.member_id ,
	c.calendar_year_month,
	case
		
		when dense_rank() over (partition by ra.member_id order by	c.calendar_year_month) = 1
		and MAX(ra.wager_amount) > 0  then 'New' 
		
		when c.calendar_month_number - LAG(c.calendar_month_number,1) OVER (partition by ra.member_id order by	c.calendar_year_month) = 1 
		and MAX(ra.wager_amount) > 0 then 'Retained'	

		when c.calendar_month_number - LAG(c.calendar_month_number,1) OVER (partition by ra.member_id order by	c.calendar_year_month) = 2 
		and MAX(ra.wager_amount) > 0 then 'Unretained'
		
		when c.calendar_month_number - LAG(c.calendar_month_number,1) OVER (partition by ra.member_id order by	c.calendar_year_month) > 2 
		and MAX(ra.wager_amount) > 0 then 'Reactived'
		
		else 'Lapsed'
		
	end member_lifecycle_status,
	
	
	(DATE_PART('year', now()::date) - DATE_PART('year', LAST_VALUE(max(c.calendar_date)) OVER (partition by ra.member_id )::date)) * 12 +
    (DATE_PART('month', NOW()::date) - DATE_PART('month', LAST_VALUE(MAX(c.calendar_date)) OVER (partition by ra.member_id )::date)) LAPSED_MONTHS
	

from  revenue_analysis ra
left join calendar c on ra.activity_date = c.calendar_date

group by ra.member_id ,	c.calendar_year_month ,c.calendar_month_number

