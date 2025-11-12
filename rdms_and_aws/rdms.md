RDBMS  
•	We have large customer CSV with the fields of Sno, Customer ID, Customer Name, Customer Email, Customer Address, Product ID, Product Name, Quantity, Product Price, Order ID, Order Date. How will you design this?  Fetch specific customer on specific date
•	We have large Users table with millions of rows and columns UserID, Name, Email, LastLoginDate. To find the user who is having specific email is taking lot of time. How to identify where the performance issue is ? and how to fix it?
•	Need to find all departments where total salary expenditure is over 500000 and is having more than 10 employees. The result should contain department name and total salary of it
•	Please list out projects that have employees from more than one department working on them
•	Please list out the employee names whose salary is the 3rd highest in the company   

Simple Tables:
Customers(CustomerID, Name, Email, Address)
Products(ProductID, Name, Price)
Orders(OrderID, CustomerID, OrderDate)
OrderDetails(OrderID, ProductID, Quantity)

eg: Find customer orders on a date
```
SELECT c.Name, o.OrderID, o.OrderDate
FROM Customers c
JOIN Orders o ON c.CustomerID = o.CustomerID
WHERE c.CustomerID = 'C001' AND o.OrderDate = '2025-10-21';
```
Analyze the query:
`EXPLAIN ANALYZE SELECT * FROM Users WHERE Email = 'abc@mail.com';`

Querying by Email is slow
We have a big Users table and checking by email is slow.
First check if there is an index on the email column.

Check Index:
`SHOW INDEX FROM Users;`

Add Index if Missing:
`CREATE INDEX idx_email ON Users(Email);`

find User by Email:
```
SELECT * FROM Users WHERE Email = 'abc@mail.com';
```
- Need to find all departments where total salary expenditure is over 500000 and is having more than 10 employees. The result should contain department name and total salary of it.  

Find Departments with Salary > 500000 and > 10 Employees

Find departments that spend more than 5 lakhs on salary and have more than 10 employees. We use GROUP BY and HAVING to filter.
```
SELECT d.DepartmentName, SUM(e.Salary) AS TotalSalary
FROM Departments d
JOIN Employees e ON d.DepartmentID = e.DepartmentID
GROUP BY d.DepartmentName
HAVING SUM(e.Salary) > 500000 AND COUNT(e.EmployeeID) > 10;
```  

- Please list out projects that have employees from more than one department working on them


we want people from more than one department.
we join projects, assignments, and employees, then count distinct departments per project.
```
SELECT p.ProjectName
FROM Projects p
JOIN ProjectAssignments pa ON p.ProjectID = pa.ProjectID
JOIN Employees e ON pa.EmployeeID = e.EmployeeID
GROUP BY p.ProjectID, p.ProjectName
HAVING COUNT(e.DepartmentID) > 1;
```


we need to get the name of the employee who earns the 3rd highest salary.
first sort salaries, skip top 2, and pick the next one.  

```
SELECT Name, Salary
FROM Employees
WHERE Salary = (
SELECT DISTINCT Salary
FROM Employees
ORDER BY Salary DESC
LIMIT 1 OFFSET 2
);
```