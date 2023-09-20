import sqlite3 
from sqlite3 import Error




# Connect db and create cursor
def conn_db():
	# Connect to database
	return sqlite3.connect('customer.db')
def create_cursor(conn):
	# Create a cursor
	return conn.cursor()

# Commit and close the connection with database
def commit(conn):
	# Commit our command
	conn.commit()
def close(conn):
	# Close our connection
	conn.close()

# Create a Table
def create_table():
	conn = conn_db()
	c = conn.cursor()
	c.execute("CREATE TABLE IF NOT EXISTS customers (first_name TEXT,last_name TEXT,email TEXT)")
	print("Table is created successfully!\n")
	commit(conn)
	close(conn)

# Drop Table
def drop_table():
	conn = conn_db()
	c = conn.cursor()
	confirmation = input("\nConfirm to Delete Table? (Enter y or n): \n")
	if confirmation == 'y':
		c.execute("Drop TABLE customers")
		commit(conn)
		close(conn)
	else:
		commit(conn)
		close(conn)

def __repr__(count): 
    return count

# To Display the Records in the Table
def display_records():
	conn = conn_db()
	c = create_cursor(conn)
	try:
		c.execute("SELECT rowid, * FROM customers")
		items = c.fetchall()
		lenght = len(items)
		print("\nHere the Records: \n")
		if lenght > 0:
			for item in items:
				print("Row ID: " + str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
			print()
			commit(conn)
			close(conn)
		else: 
			print("\nNo Records in the Database\n")
			confirmation = input("Would you like to Create a Record? (Enter y or n): \n")
			if confirmation == 'y':
				add_one_record()
			else:
				print("Record is Not Created")				
				commit(conn)
				close(conn)
	except Error as e:
		print("No Table Exists\n")
		confirmation = input("Would you like to Create a new Table into the Database? (Enter y or n): \n")
		if confirmation == 'y':
			create_table()
			commit(conn)
			close(conn)
		else:
			commit(conn)
			close(conn)

	

# Insert One record into the table
def add_one_record():
	conn = conn_db()
	c = conn.cursor()
	first_name = input("\nEnter your First Name: \n")
	last_name = input("Enter your Last Name: \n")
	email = input("Enter your Email Address: \n")
	confirmation = input("Confirm to create this Record? (Enter y or n) \n")
	if confirmation == "y":
		c.execute("INSERT INTO customers VALUES (?,?,?)", (first_name, last_name, email))
		commit(conn)
		display_records()
		close(conn)
	else:
		print("Record Not Created")
		commit(conn)
		close(conn)
		return None

	
# Delete Record in the table.
def delete_record():
	conn = conn_db()
	c = conn.cursor()
	print("""Please Enter the number, according to the below list, to Find and Delete the Record: 
	1. Row ID
	2. First Name
	3. Last Name
	4. Email
	5. Exit
		""")
	num = input()
	# Find Record by Row ID, and Delete Record.
	if num == '1':
		row_id = input("\nEnter the Row ID: \n")
		items = c.execute("SELECT rowid , * FROM customers WHERE rowid = ?", (row_id))
		print("\nHere the Search Results: \n")
		for item in items:
			print("Row ID: "+ str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
		confirmation = input("\nConfirm to delete this Record? (Enter y or n) \n")
		if confirmation == "y":
			c.execute("DELETE FROM customers WHERE rowid = (?)", (row_id))
			commit(conn)
			close(conn)
		else:
			print("Record is Not Deleted")
			commit(conn)
			close(conn)
			return 0
	# Find Record by First Name, and Delete Record.
	elif num == '2':
		count = 0
		first_name = input("\nEnter the First Name: \n")
		items = c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE '%{}%'".format(first_name))
		print("\nHere the Search Results: \n")
		for item in items:
			count = count + 1
			print("Row ID: "+ str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
		if count>0:
			row_id = input("\nEnter the Row ID that you want to delete: \n")
			confirmation = input("Confirm to delete this Record? (Enter y or n) \n")
			if confirmation == "y":
				c.execute("DELETE FROM customers WHERE rowid = (?)", (row_id))
				commit(conn)
				close(conn)
			else:
				print("Record is Not Deleted")
				commit(conn)
				close(conn)
				return None
		else:
			print("\nNo Records Found\n")
			commit(conn)
			close(conn)
	# Find Record by Last Name, and Delete Record.
	elif num == '3':
		flag = False
		last_name = input("\nEnter the Last Name: \n")
		items = c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%{}%'".format(last_name))
		print("\nHere the Search Results: \n")
		for item in items:
			flag = True
			print("Row ID: "+ str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
		if flag == True:
			row_id = input("\nEnter the Row ID that you want to delete: \n")
			confirmation = input("Confirm to delete this Record? (Enter y or n):n \n")
			if confirmation == "y":
				c.execute("DELETE FROM customers WHERE rowid = (?)", (row_id))
				commit(conn)
				close(conn)
			else:
				print("Record is Not Deleted")		
				commit(conn)
				close(conn)
				return None
		else:
			print("\nNo Records Found\n")
			commit(conn)
			close(conn)
	# Find Record by Email, and Delete Record.
	elif num == '4':
		flag = False
		email = input("\nEnter the Email: \n")
		items = c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%{}%'".format(email))
		print("\nHere the Search Results: \n")
		for item in items:
			flag = True
			print("Row ID: "+ str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
		if flag == True:
			row_id = input("\nEnter the Row ID that you want to delete: \n")
			confirmation = input("Confirm to delete this Record? (Enter y or n): \n")
			if confirmation == "y":
				c.execute("DELETE FROM customers WHERE rowid = (?)", (row_id))
				commit(conn)
				close(conn)
			else:
				print("Record is Not Deleted")
				commit(conn)
				close(conn)
				return None
		else:
			print("\nNo Records Found\n")
			commit(conn)
			close(conn)
	else:
		commit(conn)
		close(conn)
		return None


# Update Record
def update_record():
	conn = conn_db()
	c = conn.cursor()
	print("""Select Below option to Update: (Enter the number)
	1. First Name
	2. Last Name
	3. Email
	4. Exit
		""")
	num = input()
	# Find Record by First Name, and Update First Name.
	if num == '1':
		flag = False
		first_name = input("\nEnter your First Name to Search in Records: \n")
		c.execute("SELECT rowid, * FROM customers WHERE first_name LIKE '%{}%'".format(first_name))
		items = c.fetchall()
		print("\nHere the Search Results: \n")
		for item in items:
			flag = True
			print("Row ID: "+ str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
		print()
		
		if flag == True:
			row_id = input("\nEnter the Row ID of your First Name:\n")
			change_name = input("Enter the First Name to be Changed: \n")
			confirmation = input("Confirm to Update this First Name? (Enter y or n): \n")
			if confirmation == 'y':
				c.execute("UPDATE customers SET first_name = (?) WHERE rowid = (?)", (change_name, row_id))
				commit(conn)
				display_records()
				close(conn)
			else:
				print("First Name is Not Updated")				
				commit(conn)
				close(conn)
				return None
		else:
			print("\nNo Records Found\n")
			commit(conn)
			close(conn)
	# Find Record by Last Name, and Update Last Name.
	elif num == '2':
		flag = False
		last_name = input("\nEnter your Last Name to Search in Records: \n")
		c.execute("SELECT rowid, * FROM customers WHERE last_name LIKE '%{}%'".format(last_name))
		items = c.fetchall()
		print("\nHere the Search Results: \n")
		for item in items:
			flag = True
			print("Row ID: "+ str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
		print()
		if flag == True:
			row_id = input("\nEnter the Row ID of your Last Name: \n")
			change_name = input("Enter the Last Name to be Changed: \n")
			confirmation = input("Confirm to Update this Last Name? (Enter y or n): \n")
			if confirmation == 'y':
				c.execute("UPDATE customers SET last_name = (?) WHERE rowid = (?)", (change_name, row_id))
				commit(conn)
				display_records()
				close(conn)
			else:
				print("Last Name is Not Updated")
				commit(conn)
				close(conn)
				return None
		else:
			print("\nNo Records Found\n")
			commit(conn)
			close(conn)
	# Find Record by Email Name, and Update Email.
	elif num == '3':
		flag = False
		email = input("\nEnter your Email to Search in Record: \n")
		c.execute("SELECT rowid, * FROM customers WHERE email LIKE '%{}%'".format(email))
		items = c.fetchall()
		print("\nHere the Search Results: \n")
		for item in items:
			flag = True
			print("Row ID: "+ str(item[0]) + "\t" + " Name: " + item[1] + " " + item[2] + "\t" + "Email: " + item[3])
		print()
		if flag == True:
			row_id = input("\nEnter the Row ID of your Email: \n")
			change_email = input("Enter the Email to be Changed: \n")
			confirmation = input("Confirm to Update this Email? (Enter y or n): \n")
			if confirmation == 'y':
				c.execute("UPDATE customers SET email = (?) WHERE rowid = (?)", (change_email, row_id))
				commit(conn)
				display_records()
				close(conn)
			else:
				print("Email is Not Updated")
				commit(conn)
				close(conn)
				return None
		else:
			print("\nNo Records Found\n")
			commit(conn)
			close(conn)
			return None
	else:
		commit(conn)
		close(conn)
		return None




