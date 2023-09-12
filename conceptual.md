### Conceptual Exercise

Answer the following questions below:

- What is PostgreSQL?
## PostgreSQL is an open source object relatioal database management system that uses and extends SQL to bw abale to safely store and scale data.

- What is the difference between SQL and PostgreSQL?
## SQL is the langauage for relational databases while PostgreSQL is the system to enchance SQL.

- In `psql`, how do you connect to a database?
## $createdb my_data_base_name.

- What is the difference between `HAVING` and `WHERE`?
## HAVING (determines which grouped results to keep) WHERE (decides which rows to use).

- What is the difference between an `INNER` and `OUTER` join?
## An INNER JOIN focuses on matching or overlapping data and combines the info and puts it in one table. While OUTER JOIN returns a set of records or rows that include an INNER JOIN would return but also includes rows which no matches is found in the other table. 

- What is the difference between a `LEFT OUTER` and `RIGHT OUTER` join?
## The way they handle data from the two tables being joined.

- What is an ORM? What do they do?
## ORM is a object relational mapping tool a software framework that simplifies the translations betweem the object-oriented programming and relational database tables.

- What are some differences between making HTTP requests using AJAX 
  and from the server side using a library like `requests`?
## The difference between AJAX and HTTP requests are the excution envireoment where the AJAX requests are made from the client's browser, while server side http requests from the server. The page reload where AJAX requests can update the webpage without reload while HTTP requests dont interact with the webpage. AJAX requests are made with javascript while HTTP can be made with any server side language. And last lastly the visibilty to the user.
- What is CSRF? What is the purpose of the CSRF token?
## CSRF is a type of security vulnerablity in web appplications. It allows an attacker to trick users into performing actions they didn't intend to perform 

- What is the purpose of `form.hidden_tag()`?
## To generate a hidden field that includes a token to protect the form against CSRF attacks.