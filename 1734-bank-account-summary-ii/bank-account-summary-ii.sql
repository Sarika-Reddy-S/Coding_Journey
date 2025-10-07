# Write your MySQL query statement below
select NAME, sum(amount) as BALANCE from Users
join Transactions on Users.account=Transactions.account
group by name,Transactions.account
having balance>10000;