import os,csv

with open('../sample_data/reviews.csv','a+',newline='') as csvfile:
    try:
        writer = csv.writer(csvfile, delimiter=',')
        writer.writerow(['1235', 'Nabiya', 'Data Engineering', '93'])
        print("Row written to CSV file")

        csvfile.seek(0)
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

    except Exception as e:
        print(f"An error occurred: {e}")
