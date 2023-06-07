import colorama
from colorama import Fore, Style
import pyfiglet
import time

# Initialize colorama
colorama.init()
# Display the message when opening the command prompt
print(Fore.YELLOW + "Thanks for downloading our Converter!")
print("This tool is very easy to use, just follow readme.txt for all the steps!")
print("If you have any questions, feel free to message me on Telegram @blugoshop\n" + Style.RESET_ALL)


# Generate the ASCII art
ascii_art = pyfiglet.figlet_format("BluGo Token Cut")
print(Fore.BLUE + ascii_art + Style.RESET_ALL)

# Open the tokens file
with open("tokens.txt", "r") as file:
    # Prompt the user to press button 1 to start
    input(Fore.CYAN + "Press button 1 to start the token cutting process." + Style.RESET_ALL)

    # Start the timer
    start_time = time.time()

    try:
        tokens = file.readlines()

        for token in tokens:
            # Remove spaces from the token
            cut_token = token.split(":")[2].strip()
            print(token)

            # Simulate cutting a token by waiting for 1 second
            time.sleep(0)

            # Display success message in green along with the token
            print(Fore.GREEN + "Success!" + Style.RESET_ALL + " Token: " + cut_token)

            # Write the cut token to the file
            open("cut-tokens.txt", "a").write(f"{cut_token}\n")

        # Calculate the elapsed time
        elapsed_time = time.time() - start_time
        print(Fore.YELLOW + f"Finished in {elapsed_time:.2f} seconds." + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + f"Error occurred: {e}" + Style.RESET_ALL)


