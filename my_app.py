import crud_operation

crud_operation.create_table()
def crud():
	print("""Select a operation, to do in Database: (Enter the number)
	1. Create a Record into Database
	2. Display the Records in the Database
	3. Update the Record in the Database
	4. Delete the Record in the Database
	5. Exit	
	""")
	num = input()
	if num == '1':
		crud_operation.add_one_record()
	elif num == '2':
		crud_operation.display_records()
	elif num == '3':
		crud_operation.update_record()
	elif num == '4':
		crud_operation.delete_record()
	else:
		return None;
crud()
 
