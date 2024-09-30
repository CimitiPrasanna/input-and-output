...
It was in the 1997-98 season that Ranchi saw the rise of the Captain Cool in the interschool trophy between DAV Jawahar Vidhya Mandir and Kendriya School. It was in that match Dhoni convinced Banerjee to be the opener and justified it with a double century.
Write a program to display the details of the match with Team name, Scores of the team and Overs played.
Input and Output Format:  
Refer sample input and output for formatting specifications.
[All text in bold corresponds to input and the rest corresponds to output]
...

def display_match_details():
    team1 = input("**Enter the name of Team 1:** ")
    team2 = input("**Enter the name of Team 2:** ")
    score1 = int(input(f"**Enter the score of {team1}:** "))
    score2 = int(input(f"**Enter the score of {team2}:** ")
    overs1 = float(input(f"**Enter the overs played by {team1}:** "))
    overs2 = float(input(f"**Enter the overs played by {team2}:** "))
    print("\n**Match Details:**")
    print(f"Team Name: {team1}")
    print(f"Score: {score1}/{overs1} overs")
    print(f"Team Name: {team2}")
    print(f"Score: {score2}/{overs2} overs")
display_match_details()
