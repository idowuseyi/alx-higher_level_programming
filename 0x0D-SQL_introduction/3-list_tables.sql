<<<<<<< HEAD
#!/usr/bin/bash

-- script that lists all the tables of a database in your MySQL server

SELECT table_name
FROM information_schema.tables
WHERE table_type='BASE TABLE'
      AND table_schema = 'hbtn_0c_0'
=======
-- a script that lists all the tables of a database in your MySQL server.
SHOW TABLES;
>>>>>>> 973f18ea498314fc507db680e5c7fa1e0184e817
