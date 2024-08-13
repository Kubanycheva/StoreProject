# SELECT Customers.customer_id, first_name, last_name FROM Customers
# left join Orders
# on Customers.customer_id = Orders.customer_id
# where order_id is null             Найдите клиентов, у которых нет соответствующих заказов в таблице Orders.  




# select item, count(order_id) from Orders
# group by item
# limit 1     Найдите товар, который был заказан наибольшее количество раз.



# Select Customers.customer_id, first_name, last_name from Customers
# Where first_name = 'John' and last_name = 'Doe';       Найдите список клиентов, сделавших заказы на определенный товар из таблицы (например 'Mouse')