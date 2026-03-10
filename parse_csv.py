import csv
# We COULD use split on the delimiters of the csv file, but the csv module makes parsing these files so much easier. For example, if someone has a comma in their name, we don't want to split on that. csv module also handles new lines and other stuff for us

with open("names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file) # csv_reader is an iterator (and by extension an iterable). Each iteration returns a row of the CSV file (which can span multiple input lines).
    # print(list(csv_reader))
    # print(csv_reader)
    # This file has ['first_name', 'last_name', 'email'] as the field names. The first line in csv file is the names of the fields. We can skip it via next()
    # next(csv_reader) # Return next item from iterator and move iterator forward
    
    with open("new_names.csv", "w") as new_file:
        csv_writer = csv.writer(new_file, delimiter="-") # We can overwrite the comma as the default delimiter
        
        for line in csv_reader:
            print("line =", line)
            print(line[2]) # Just email
            
            csv_writer.writerow(line)
			# Look at the first row of new_names. csv_writer knew to put quotes around the first element "john-doe@bogusemail.com" since it already contained a -, and it does not want to confuse the - in the email for the - delimiter. It is 1 whole value and should not be split on that -. Same thing with "Smith-Robinson"
   
# What would happen if we read a file with the wrong delimiter?
with open("new_names.csv", "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter="\t")
    for line in csv_reader:
        print(line) # Each line is 1 element, instead of the expected 3
        
# We can also work with csv data using dictionary_reader and dictionary_writer
with open("names.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file) # Dictionary for each line vs. list. Easier to read
    
    with open("new_names_dict.csv", "w") as new_file:
        fieldnames = ["first_name", "last_name", "email"] # too big and we get empty fields in written csv. Too small we get ValueError: dict contains fields not in fieldnames: 'fieldname' when writing
        csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter="-")
        csv_writer.writeheader() # Write out the field names at the top

        for line in csv_reader:
            print(line) # Uses first row as the field names. So we get {'first_name': 'John', 'last_name': 'Doe', 'email': 'john-doe@bogusemail.com'} vs ['John', 'Doe', 'john-doe@bogusemail.com']. 
            print(line["email"])
            csv_writer.writerow(line)
