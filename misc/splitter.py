import csv
import os

def split_csv(input_file, output_dir, num_files):
    os.makedirs(output_dir, exist_ok=True)
    with open(input_file, 'r', newline='') as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader) 
        num_lines = sum(1 for line in reader)
        chunk_size = (num_lines + num_files - 1) // num_files  
        
        csvfile.seek(0)  
        next(reader)  
        for i in range(num_files):
            output_file = os.path.join(output_dir, f"chunk_{i+1}.csv")
            with open(output_file, 'w', newline='') as chunk_file:
                writer = csv.writer(chunk_file)
                writer.writerow(header)  
                for j in range(chunk_size):
                    line = next(reader, None)
                    if line is None:
                        break
                    writer.writerow(line)

input_file = 'final_clean_1.csv'
output_dir = 'output_chunks'
num_files = 5  
split_csv(input_file, output_dir, num_files)