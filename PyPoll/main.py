#Solution for PyPoll Challenge
# Import required packages
import csv
import os

file_path= os.path.join("Resources","election_data.csv")
file_to_output = os.path.join("Output", "election_data_analysis.txt")

with open(file_path, newline='') as csvfile:
    
    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    headerrow=next(csvreader)
    #print(headerrow)

    #declare the variables
    total_votes=0
    candidates = ["Khan", "Correy", "Li", "O'Tooley"]
    candidates_results = [0, 0, 0, 0]

    for row in csvreader:
        #print(row)
        total_votes += 1
        if row[2] == "Khan":
            candidates_results[0] += 1
        elif row[2] == "Correy":
            candidates_results[1] += 1
        elif row[2] == "Li":
            candidates_results[2] += 1
        elif row[2] == "O'Tooley":
            candidates_results[3] += 1
    
    
    # Vote Percentages
    khan_percent = str(round((candidates_results[0]/total_votes)*100, 0))
    correy_percent = str(round((candidates_results[1]/total_votes)*100, 0))
    li_percent = str(round((candidates_results[2]/total_votes)*100, 0))
    otooley_percent = str(round((candidates_results[3]/total_votes)*100, 0))
    
    candidate_percent = [khan_percent, correy_percent, li_percent, otooley_percent]
   
        
    for i in range(len(candidates)):

        cand_name = str(candidates[i])

        if candidate_percent[i] == max(candidate_percent):
            #print(f"Winner: {cand_name}")
            winner=cand_name
            break

    
    output=(
        f"\nElection Results\n"
        f"-----------------\n"
        f"Total votes : {total_votes}\n"
        f"{candidates[0]}: {candidate_percent[0]}00% ({candidates_results[0]})\n"
        f"{candidates[1]}: {candidate_percent[1]}00% ({candidates_results[1]})\n"
        f"{candidates[2]}: {candidate_percent[2]}00% ({candidates_results[2]})\n"
        f"{candidates[3]}: {candidate_percent[3]}00% ({candidates_results[3]})\n"
        f"-----------------\n"
        f"Winner: {winner}"

     )
    print(output)

with open(file_to_output, "w") as txt_file:
    txt_file.write(output)

        